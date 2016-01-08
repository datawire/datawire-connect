# import sys
# import os

import json

from flask import Flask, render_template, url_for, request, jsonify

Things = json.load(open("things.json", "r"))
cartItems = []
totalCost = 0

app = Flask("Market")

@app.route('/')
def index():
  sendJSON = request.args.get('json', False)

  if sendJSON:
    return jsonify({ "thingIDs": sorted(Things.keys()) })
  else:
    return render_template('index.html', 
                           allThingIDs=sorted(Things.keys()),
                           Things=Things)

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
  elif (request.method == 'POST'):
    cartMessage = "Item could not be added."
    global totalCost
    if (cartItems.count(thingID) == 0 and (thingID in Things)):
      cartItems.append(thingID)
      cartMessage = "Item added successfully!"
      totalCost += Things[thingID]['price']
    return render_template('cart.html', cartItems=cartItems, cartMessage=cartMessage, Things=Things, totalCost=totalCost)
  else:
    pass


@app.route('/cart/')
def cart():
  global totalCost
  return render_template('cart.html', cartItems=cartItems, cartMessage="", Things=Things, totalCost=totalCost)

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

if __name__ == '__main__':
  app.run(debug=True)

