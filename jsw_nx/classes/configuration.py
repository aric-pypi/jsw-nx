from .yaml import Yaml
from .json import JSON
from ..base.set import set
from ..base.get import get


class Configuration:
    def __init__(self, **kwargs):
        self.engine = None
        self.data = None
        self.type = kwargs.get('type', 'yaml')
        self.filepath = kwargs.get('filepath', './config.yaml')
        self.init_engine()
        self.init_data()

    def init_engine(self):
        if self.type == 'yaml':
            self.engine = Yaml
        if self.type == 'json':
            self.engine = JSON

    def init_data(self):
        with open(self.filepath, 'r') as f:
            data = f.read()
            self.data = self.engine.parse(data)

    def set(self, path, value):
        set(self.data, path, value)

    def sets(self, obj):
        for k, v in obj.items():
            self.set(k, v)

    def get(self, path):
        return get(self.data, path)

    def gets(self):
        return self.data

    def save(self):
        with open(self.filepath, 'w') as f:
            f.write(self.engine.dump(self.data))

    def update(self, obj):
        self.sets(obj)
        self.save()