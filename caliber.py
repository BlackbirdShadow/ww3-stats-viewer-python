import json

class Caliber:
    def __init__(self, data):
          self.shortname = data['shortname']
          self.name = data['name']
          self.pellets = data['pellets']
          self.compact = data['compact'] if 'compact' in data else []
          self.standard = data['standard']
          self.marksman = data['marksman']  if 'marksman' in data else []