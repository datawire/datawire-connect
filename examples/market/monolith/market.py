import sys

import json
import os
import time

from flask import Flask, render_template, url_for, request, jsonify

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
