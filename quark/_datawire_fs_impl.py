import os

import quark

__all__ = """_datawire_fs""".split(' ')

class _datawire_fs (object):
    @classmethod
    def userHomeDir(klass):
        return os.path.expanduser('~')

    @classmethod
    def fileContents(klass, path):
        try:
            inputFile = open(path, "r")
            return inputFile.read()
        except Exception as e:
            runtime = quark.concurrent.Context.runtime()
            runtime.fail("failure reading %s: %s" % (path, e))
