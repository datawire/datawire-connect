#!python

import sys
import os

from ratings import *
# import builtin

# urls = [ "http://127.0.0.1:%d/ratings" % port for port in [ 8001 ] ]

class ratingsListener (object):
  def __init__(self, start):
    self.start = start

  def onFuture(self, future):
    end = os.times()[4]
    elapsed = (end - start) * 1000

    print("in onFuture after %dms, rating %s is %s" % 
          (elapsed, future.thingID, future.rating))

ratings = RatingsClient("ratings", MyHub())
ratings.setTimeout(5000)

print("Grabbing 100 ratings")

start = os.times()[4]

futures = [ ratings.get(str(i)) for i in range(100) ]

first = futures[98].rating
print("Before waiting, rating 98 was %s" % first)

futures[98].onFinished(ratingsListener(start))

resolutions = [ future.await(1000) for future in futures ]

end = os.times()[4]
elapsed = (end - start) * 1000

print("After waiting %dms, rating 98 is %s" % (elapsed, futures[98].rating))

for i in range(100):
  future = futures[i]

  if future.getError():
    print("%d: failed! %s" % (i, future.getError()))
  elif (future.thingID != i) or (future.rating != (i % 5)):
    print("%3d: wrong! %s, %s" % (i, future.thingID, future.rating))
