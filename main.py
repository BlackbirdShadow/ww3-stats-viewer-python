import graph_maker
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import json
from gun import Gun
from caliber import Caliber


def load_data(filename:str, Class) -> list:
    list = []
    with open('data/'+filename, 'r') as f:
    # Load the JSON data into a Python object
        data = json.load(f)
        for map in data:
            gun = Class(map)
            list.append(gun)
    return list


def __launch_app():

    guns = load_data("gunstats.json",Gun)
    calibers = load_data("calibers.json",Caliber)


if __name__ == '__main__':
    __launch_app()
