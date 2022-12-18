import json

class Gun:
    def __init__(self, data):
        self.gun_shortname = data['shortname']
        self.gun_class = data['class']
        self.fire_type = data['fire_type']
        self.weight = data['weight']
        self.rof = data['rof']
        self.caliber = data['caliber']
        self.gun_fullname = data['gun_fullname']
        self.gun_realname = data['gun_realname']
        self.desc = data['desc'] if data['desc'] is not None else ''
