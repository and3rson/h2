from os.path import expanduser, join, isfile, isdir
from os import mkdir
import json

_instances = dict()


class DB(object):
    CONF_DIR = join(expanduser('~'), '.h2')

    @classmethod
    def get(cls, name):
        global _instances
        if name not in _instances:
            _instances[name] = DB(name)
        return _instances[name]

    def __init__(self, name):
        if not isdir(DB.CONF_DIR):
            mkdir(DB.CONF_DIR)
        self.path = join(DB.CONF_DIR, name + '.db')
        if isfile(self.path):
            f = open(self.path, 'r')
            data = f.read()
            f.close()
            self.data = json.loads(data)
        else:
            self.data = dict()

    def __del__(self):
        f = open(self.path, 'w')
        f.write(json.dumps(self.data))
        f.close()
