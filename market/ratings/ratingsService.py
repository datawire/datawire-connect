#!python

import sys

import json

import argparse
from ratings import *

parser = argparse.ArgumentParser(description='Ratings Microservice')

parser.add_argument('--instance', metavar='INSTANCE', type=int,
                    help='Listen on port 8000 + INSTANCE (--instance 1 => listen on port 8001)')
parser.add_argument('--port', metavar='PORT', type=int,
                    help='Listen on PORT (defaults to 8001)')
parser.add_argument('--count', metavar='COUNT', type=int,
                    help='Listen on COUNT ports starting with 8001 (--count 2 => 8001, 8002)')

######## RATINGS MICROSERVICE
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

######## MAINLINE

# Parse arguments first off...
args = parser.parse_args()

# ...then, from our arguments, work out where to listen.

ports = [ 8001 ]

if args.count:
  ports = [ 8000 + i for i in range(1, args.count+1) ]
elif args.instance:
  ports = [ 8000 + args.instance ]
elif args.port:
  ports = [ args.port ]

# Next up, find the root directory of our script...
scriptDir = os.path.dirname(os.path.realpath(__file__))

# ...from which we can determine the root of the Market example...
rootDir = os.path.abspath(os.path.join(scriptDir, ".."))

# ...from which we can locate our resources...
resourceDir = os.path.join(rootDir, "resources")

# ...from which we can locate our ratings info.
ratingsPath = os.path.join(resourceDir, "ratings.json")

# OK. Load up the ratings data we'll use...
ratings = json.load(open(ratingsPath, "r"))

# ...and fire up listener(s).

for port in ports:
  print("listening on port %d" % port)

  url = "http://127.0.0.1:%d/ratings" % port

  # ...and fire up the ratings service.
  srv = RatingsServer(RatingsService(ratings))
  srv.serveHTTP(url)
