# import sys
# import os

import json

from flask import Flask, render_template, url_for, request, jsonify

Things = json.load(open("things.json", "r"))
cartItems = []

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
                             Things=Things, cartItems=sorted(cartItems), cartMessage=cartMessage, totalCost=cartCost(), numItems=len(cartItems))

@app.route('/')
def index():
  global cartItems
  if request.method == 'GET':
    sendJSON = request.args.get('json', False)

    if sendJSON:
      return jsonify({ "thingIDs": sorted(Things.keys()) })
    else:
      return renderIndex("")
  elif request.method == 'POST' and 'checkout' in request.form:
    return checkout()

@app.route('/thing/<thingID>', methods = ['GET','POST'])
def thing(thingID=None):
  if (request.method == 'GET'):
    sendJSON = request.args.get('json', False)

    if (thingID is None) or (not thingID in Things):
      if sendJSON:
        return ('no such Thing: %s' % thingID, 404)
      else:
        return(render_template('noSuchThing.html', thingID=thingID), 404)
  
    if sendJSON:
      return jsonify(Things[thingID])
    else:
      return render_template('thing.html', thingID=thingID, thingInfo=Things[thingID])
  elif (request.method == 'POST' and 'addcart' in request.form):
    cartMessage = "Item could not be added."
    global totalCost
    if (cartItems.count(thingID) == 0 and (thingID in Things)):
      cartItems.append(thingID)
      cartMessage = "Item added successfully!"
    return renderIndex(cartMessage)
  elif request.method == 'POST' and 'checkout' in request.form:
    return checkout()

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

if __name__ == '__main__':
  app.run(debug=True)

