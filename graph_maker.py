import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)



def get_graph_canvas(ammo, title):

    # fill arrays that define the point values for the broken line graph
    # first point at 0 meters, max damage
    distances = [0]
    damages = [ammo[0][1]]
    
    # fill other points
    for i in range(len(ammo)):
        distances.append(ammo[i][0])
        damages.append(ammo[i][1])

    # calculate high and low damage
    highest_damage = int(damages[0])
    lowest_damage = int(damages[-1])

    # end graph at last point + 20x, same damage as last point
    distances.append(distances[-1]+20)
    damages.append(lowest_damage)

    # create the broken line graph
    plt.plot(distances, damages, 'bo-')

    # defining y axis bounds, show lowest damage - 10 except if negative then zero, highest dmage +
    plt.ylim(lowest_damage-5 if lowest_damage-5 >= 0 else 0, highest_damage + 5)

    # add a title and axis labels
    plt.title(title)
    plt.xlabel('Meters')
    plt.ylabel('Damage')

    #plt.show()


