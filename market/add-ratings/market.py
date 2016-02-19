import sys

import json
import os
import time

from flask import Flask, render_template, url_for, request, jsonify

# Import the interface to our ratings service
from ratings import *

# Start by finding the root directory of our script...
scriptDir = os.path.dirname(os.path.realpath(__file__))

# ...from which we can determine the root of the Market example...
rootDir = os.path.abspath(os.path.join(scriptDir, ".."))

# ...from which we can locate our resources.
resourceDir = os.path.join(rootDir, "resources")
templateDir = os.path.join(resourceDir, "templates")
staticDir = os.path.join(resourceDir, "static")

# Utility function for setting up paths within the resource directory.
def resPath(path):
  """ Return a path to something in the resource directory. """
  return os.path.join(resourceDir, path)

# OK, load up the set of Things we'll show!
Things = json.load(open(resPath("things.json"), "r"))

# Next, set up an empty shopping cart...
cartItems = []

# ...get the Ratings microservice going...
ratings = RatingsClient("ratings")
ratings.setResolver(RatingsResolver())

# ...and get Flask running, using the correct directories.
app = Flask("Market", template_folder=templateDir, static_folder=staticDir)

def cartCost():
  totalCost = 0
  for thingID in cartItems:
    totalCost += Things[thingID]['price']
  return totalCost

def checkout():
  global cartItems
  del cartItems[:]
  return renderIndex("Succesfully checked out your items!")

# Try to get ratings for our Things.
def checkRatings(things):
  """
  Use the Ratings service to get ratings for all of our Things. We launch one request
  per item, asynchronously, then block checkRatings until all the requests have 
  finished, successfully or otherwise.

  If we successfully get a rating for a given Thing, we update that Thing's rating. If
  we don't successfully get a rating, we don't touch any existing rating for that Thing,
  which means that once we get a rating, we'll cache it so that we can show something
  to the user even if all the ratings services are down.
  """

  # A Wireable is a thing that can be slung around over the wire. They are inherently
  # asynchronous; once you get one, you _must_ make sure that it's fully resolved
  # before trying to use it.
  #
  # Here, we're going to ask for many ratings, and save all the Wireables we get from
  # that. Then we'll wait for all of them to finish.

  wireables = []

  # We use os.times to track elapsed time in a high-resolution, monotonically 
  # increasing way.
  start = os.times()[4]

  for thingID in things:
    print("ASK for %s" % thingID)      

    # ratings.get() returns an inherently-asynchronous Wireable. Don't forget that.
    wireables.append(ratings.get(thingID))

  # OK, we have a Wireable for each Thing we've asked for. Wait for all of them to
  # be finished.
  #
  # This way look odd for two reasons:
  #
  # 1. Calling .await() on a Wireable won't actually wait if the Wireable is already
  #    resolved, so it actually is totally safe to call .await() sequentially.  The
  #    actual waiting happens in parallel -- by the time the first Wireable is ready,
  #    they're likely to all be ready, in which case the other Wireables will return
  #    instantly from .await().
  #
  # 2. Yes, this is a list comprehension for which the result is ignored. That is, 
  #    amazingly enough, legal in Python.

  [ wireable.await(1.0) for wireable in wireables ]

  # All done, so now's the time to do our elapsed-time calculation.

  end = os.times()[4]
  elapsed = (end - start) * 1000

  print("WAITED %dms" % elapsed)

  # OK. What'd we get?
  for wireable in wireables:
    # If all of our services are down, and we literally have no one to talk to, we'll
    # get None for our wireable. In that case, we can just skip all the work: the 
    # error has already been logged and there's really nothing else we can do.

    if wireable:
      # OK, we have a real Wireable. We don't yet know if it's a success or an error.
      #
      # If it's an error, .getError() will return error text, and we _may_ have a
      # thingID (it depends on the class of the error, and where exactly it happened).
      # 
      # If it's not an error, .getError() will return None and we'll definitely have
      # a thingID.
      #
      # So. Start by grabbing the thingID and .getError(), in ways that are safe in all
      # cases.

      thingID = getattr(wireable, "thingID", None)
      errString = wireable.getError()

      if errString:
        # Error. Oh well. Report it...
        print("BAD %s: %s" % (thingID, errString))

        # ...and we're done.
      else:
        # Success! Figure out the rating and save it.
        #
        # XXX We sholud be sending the ratings over the wire as floats, but, uh, that
        # doesn't work yet.
        rating = float(wireable.rating) / 10
        things[thingID]["rating"] = rating

        print("GOT %s: %s" % (thingID, rating))

def renderIndex(cartMessage):
  # When rendering, start by checking our ratings.
  checkRatings(Things)

  return render_template('index.html',
                         allThingIDs=sorted(Things.keys()),
                         Things=Things,
                         cartItems=sorted(cartItems),
                         cartMessage=cartMessage,
                         totalCost=cartCost(),
                         numItems=len(cartItems))

@app.route('/', methods = ['GET', 'POST'])
def index():
  global cartItems
  if request.method == 'GET':
    sendJSON = request.args.get('json', False)

    if sendJSON:
      return jsonify({ "thingIDs": sorted(Things.keys()) })
    else:
      return renderIndex("")
  elif request.method == 'POST':
    if 'checkout' in request.form:
      return checkout()
    elif 'addCart' in request.form:
      for thingID in Things:
        if thingID in request.form:
          cartMessage = "Item could not be added."
          if (cartItems.count(thingID) == 0):
            cartItems.append(thingID)
            cartMessage = "Item added successfully!"
          return renderIndex(cartMessage)
    elif 'removeCart' in request.form:
      for thingID in cartItems:
        if thingID in request.form:
          cartItems.remove(thingID)
          return renderIndex("Item removed successfully!")

@app.route('/thing/<thingID>', methods = [ 'GET' ])
def thing(thingID=None):
  if (request.method == 'GET'):
    # You always get JSON when looking up a particular Thing. This is mostly
    # here for tests.

    if (thingID is None) or (not thingID in Things):
      return ('no such Thing: %s' % thingID, 404)
  
    return jsonify(Things[thingID])

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

if __name__ == '__main__':
  app.run(debug=True)
