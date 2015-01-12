import yaml

class Yaml(object):
    def __init__(self, file_location):
        stream = file(file_location)
        self.data = yaml.load(stream)
    
    def __getattr__(self, name):
        return self.data[name]
    