import sys

import json
import time

from Queue import Queue
from threading import Thread

from flask import Flask, render_template, url_for, request, jsonify
from ratings import *

# Start by loading up our set of Things...
Things = json.load(open("things.json", "r"))

# ...an empty shopping cart...
cartItems = []

# ...and the queue for updates to Things from our microservices.
updaterQueue = Queue()

# Once all that's done, we can start our updater thread.
#
# This is here solely because we're talking to our microservices asynchronously,
# and multiple simultaneous updates into an dictionary of dictionaries is not
# necessarily safe without locking.

def updater(queue, things):
  """ Watch the given queue for updates to the given set of things. """
  print("Updater thread started")

  while True:
    mod = queue.get()

    if 'thingID' not in mod:
      print("updater: no thingID in %s" % mod)
      continue

    if 'cmd' not in mod:
      print("updater: no cmd in %s" % mod)
      continue

    if 'key' not in mod:
      print("updater: no key in %s" % mod)
      continue

    thingID = mod['thingID']
    cmd = mod['cmd']
    key = mod['key']

    if thingID not in things:
      print("updater: bad thingID %s in %s" % (thingID, mod))
      continue

    if cmd == 'set':
      if 'value' not in mod:
        print("updater: set: no value for in %s" % mod)
        continue

      value = mod['value']

      # For now, 'key' is flat. We can extend it later if need be.
      print("updater: set %s.%s = %s" % (thingID, key, value))

      things[thingID][key] = value
    elif cmd == 'del':
      # For now, 'key' is flat. We can extend it later if need be.
      print("updater: del %s.%s" % (thingID, key))

      del(things[thingID][key])

updaterThread = Thread(target=updater, args=[ updaterQueue, Things ])
updaterThread.start()

# Once the updater thread is running, we can start trying to query for
# ratings.
#
# We do this very asynchronously: we start the RPC and use a 
# ratingFutureListener to catch the response.

class ratingFutureListener (object):
  def __init__(self, thingID, queue):
    self.thingID = thingID
    self.queue = queue

  def onFuture(self, future):
    errString = future.getError()

    if errString:
      print("BAD %s: %s" % (self.thingID, errString))
    else:
      thingID = future.thingID

      # We can't pass floats back correctly for some weird reason, so
      # we cheat.

      rating = float(future.rating) / 10

      print("GET %s: %s" % (thingID, rating))

      self.queue.put(dict(
        cmd='set',
        thingID=thingID,
        key='rating',
        value=rating
      ))

def ratingsWatcher(queue, things):
  print("Ratings watcher started")

  ratings = RatingsClient("ratings", MyHub())
  ratings.setTimeout(1000)

  while True:
    for thingID in things:
      print("ASK for %s" % thingID)      
      futureRating = ratings.get(thingID)
      futureRating.onFinished(ratingFutureListener(thingID, queue))

    # Once that's done, sleep for ten seconds or so.
    time.sleep(10)

ratingsWatcherThread = Thread(target=ratingsWatcher, args=[ updaterQueue, Things ])
ratingsWatcherThread.start()

app = Flask("Market")

def cartCost():
  totalCost = 0
  for thingID in cartItems:
    totalCost += Things[thingID]['price']
  return totalCost

def checkout():
  global cartItems
  del cartItems[:]
  return renderIndex("Succesfully checked out your items!")


def renderIndex(cartMessage):
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

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

if __name__ == '__main__':
  app.run(debug=True)
