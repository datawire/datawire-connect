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
