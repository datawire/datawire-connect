#!python

import sys
import os

from ratings import *

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

print("Trying for camera")

start = os.times()[4]

f = ratings.get("camera")
f.onFinished(ratingsListener(start))
