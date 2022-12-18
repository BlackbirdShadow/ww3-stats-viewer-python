import json
from enum import Enum

class Gun:
    def __init__(self, data):
        self.shortname = data['shortname']
        self.type = GunTypes[data['type']]
        self.firemode = Firemodes[data['firemode']]
        self.weight = data['weight']
        self.rof = data['rof']
        self.caliber = data['caliber']
        self.fullname = data['fullname']
        self.realname = data['realname']
        self.desc = data['desc'] if data['desc'] is not None else ''


class GunTypes(Enum):
    SHOTGUN = "Shotgun"
    PISTOL = "Pistol"
    SMG = "Submachine Gun"
    AR = "Assault Rifle"
    BR = "Battle Rifle"
    LMG = "Light Machinegun"
    SNIPER = "Sniper"
    ATTACHMENT = "Attachment"

class Firemodes(Enum):
    BOLT = "Pump/Bolt"
    SEMI = "Semi-auto"
    BURST = "Burst"
    AUTO = "Full-auto"