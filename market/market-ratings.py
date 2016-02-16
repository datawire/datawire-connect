import sys

import json
import os
import time

from flask import Flask, render_template, url_for, request, jsonify
from ratings import *

# Start by loading up our set of Things...
Things = json.load(open("things.json", "r"))

# ...an empty shopping cart...
cartItems = []

ratings = RatingsClient("ratings", MyHub())

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

def checkRatings(things):
  wireables = []

  start = os.times()[4]

  for thingID in things:
    print("ASK for %s" % thingID)      
    wireables.append(ratings.get(thingID))

  [ wireable.await(1000) for wireable in wireables ]

  end = os.times()[4]
  elapsed = (end - start) * 1000

  print("WAITED %dms" % elapsed)

  for wireable in wireables:
    if wireable:
      thingID = wireable.thingID
      errString = wireable.getError()

      if errString:
        print("BAD %s: %s" % (thingID, errString))
      else:
        rating = float(wireable.rating) / 10
        things[thingID]["rating"] = rating

        print("GOT %s: %s" % (thingID, rating))

def renderIndex(cartMessage):
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

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

if __name__ == '__main__':
  app.run(debug=True)
