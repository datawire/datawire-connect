#!python

import sys

import json

from ratings import *

# Start by finding the root directory of our script...
scriptDir = os.path.dirname(os.path.realpath(__file__))

# ...from which we can determine the root of the Market example...
rootDir = os.path.abspath(os.path.join(scriptDir, ".."))

# ...from which we can locate our resources.
resourceDir = os.path.join(rootDir, "resources")

# Utility function for setting up paths within the resource directory.
def resPath(path):
  """ Return a path to something in the resource directory. """
  return os.path.join(resourceDir, path)

#### The Ratings microservice itself
class RatingsService (object):
  """ The Ratings microservice itself. """
  def __init__(self, ratings):
    self.ratings = ratings

  def get (self, thingID):
    """ Get the rating for a given Thing. """
    rating = Rating()

    rating.thingID = thingID
    rating.rating = self.ratings[thingID]

    print("GET %s => %s" % (rating.thingID, rating.rating))

    rating.finish(None)

    return rating

#### MAINLINE

# Start by loading up the ratings data we'll use.
Ratings = json.load(open(resPath("ratings.json"), "r"))

# Next up, get our port number...
port = 8001

if len(sys.argv) > 1:
  port = int(sys.argv[1])

print("listening on port %d" % port)

url = "http://127.0.0.1:%d/ratings" % port

# ...and fire up the ratings service.
srv = RatingsServer(RatingsService(Ratings))
srv.serveHTTP(url)
