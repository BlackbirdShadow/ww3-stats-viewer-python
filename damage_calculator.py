from scipy.interpolate import interp1d
import numpy as np

def calculate_damage(ammo_data: list, distance:int, region:str) -> int:
    
    distances, damages = zip(*ammo_data)

    raw_damage = 0

    if distance <= distances[0]:
        raw_damage = damages[0]
    elif distance >= distances[-1]:
        raw_damage = damages[-1]
    else:
        function = interp1d(distances, damages, kind='linear')
        raw_damage = function(distance)

    if region == "Head":
        raw_damage = raw_damage*2
    elif region == "Legs":
        raw_damage = raw_damage*0.67
    elif region == "Feet":
        raw_damage = raw_damage*0.57

    damage = int(np.round(raw_damage))

    return damage