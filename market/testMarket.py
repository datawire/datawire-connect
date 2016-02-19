import json
import requests

def thingIsSane(thingID, thing):
  if (thing['title'] and
      thing['blurb'] and
      thing['desc'] and
      thing['price'] > 0 and
      (('rating' not in thing) or
       (thing['rating'] >= 0)) and
      (thing['warnings'] is not None)):
    return True
  else:
    print("Thing %s is not sane" % thingID)
    return False

def objEqual(d1, d2):
  # This what we call a Brutal Hack.
  return json.dumps(d1, sort_keys=True) == json.dumps(d2, sort_keys=True)

class TestMarket (object):
    @classmethod
    def setup_class(klass):
      """ Run once per test class before any tests are run """
      TestMarket.Things = json.load(open("things.json", "r"))

    @classmethod
    def teardown_class(klass):
      """ Run once per test class after all tests are run """
      pass

    def setup(self):
      """ Run once before each test """
      pass

    def teardown(self):
      """ Run once after each test """
      pass

    def allThingIDs(self):
      return sorted(TestMarket.Things.keys())

    def __getitem__(self, key):
      return TestMarket.Things[key]

    def test_haveSomeThings(self):
      assert len(self.allThingIDs()) > 0

      for thingID in self.allThingIDs():
        assert thingID

        thing = self[thingID]

        assert thingIsSane(thingID, thing)

    def test_servedThingIDsMatch(self):
      r = requests.get('http://localhost:5000/?json=true')
      assert r.status_code == 200
      assert r.text

      fetched = json.loads(r.text)
      assert(objEqual({ "thingIDs": self.allThingIDs() }, fetched))

    def test_servedThingsMatch(self):
      for thingID in self.allThingIDs():
        thing = self[thingID]

        r = requests.get('http://localhost:5000/thing/%s?json=true' % thingID)
        assert r.status_code == 200
        assert r.text

        fetched = json.loads(r.text)
        assert(objEqual(thing, fetched))

    def test_nonExistentThing(self):
      r = requests.get('http://localhost:5000/thing/nonesuch_for_test?json=true')
      assert r.status_code == 404
