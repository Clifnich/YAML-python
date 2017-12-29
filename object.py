import sys
import ruamel.yaml

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


yaml = ruamel.yaml.YAML()
yaml.register_class(User)
yaml.dump([User('Anthon', 19)], sys.stdout)
