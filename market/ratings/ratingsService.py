#!python

import sys

import json

from ratings import *
# import builtin

class RatingsService (object):
  def __init__(self, ratings):
    self.ratings = ratings

  """ Implement the Ratings service. """
  def get (self, thingID):
    rating = Rating()

    rating.thingID = thingID
    rating.rating = self.ratings[thingID]

    print("GET %s => %s" % (rating.thingID, rating.rating))

    rating.finish(None)

    return rating

port = 8001

if len(sys.argv) > 1:
  port = int(sys.argv[1])

print("listening on port %d" % port)

url = "http://127.0.0.1:%d/ratings" % port

# Start by loading up our ratings...
Ratings = json.load(open("ratings.json", "r"))

srv = RatingsServer(RatingsService(Ratings))
srv.serveHTTP(url)
