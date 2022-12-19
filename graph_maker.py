import matplotlib.pyplot as plt

def get_graph_figure(ammo_data, title, color):

    figure = plt.figure(figsize=(6,4), dpi=80)
    # fill arrays that define the point values for the broken line graph
    # first point at 0 meters, max damage
    distances = [0]
    damages = [ammo_data[0][1]]
    
    # fill other points
    for i in range(len(ammo_data)):
        distances.append(ammo_data[i][0])
        damages.append(ammo_data[i][1])

    # calculate high and low damage
    highest_damage = int(damages[0])
    lowest_damage = int(damages[-1])

    # end graph at last point + 10x, same damage as last point
    distances.append(distances[-1]+10)
    damages.append(lowest_damage)

    # create the broken line graph

    plt.plot(distances, damages, '-', color=color)
    

    for i, j in zip(distances[1:len(distances)-1], damages[1:len(damages)-1]):
        plt.plot(i,j, 'D', color=color,  markersize=4)
        plt.text(i+0.1,j+0.7,str(j).format(i, j))

    # defining y axis bounds, show lowest damage - 10 except if negative then zero, highest dmage +
    plt.ylim(15 if lowest_damage >= 15 else 0, highest_damage + 3)
    plt.xlim(int(distances[0]), int(distances[-1]))

    range_interval = 5 if distances[-1]<100 else 10
    ax = plt.gca()
    ax.set_xticks([i for i in range(0, int(distances[-1]))][::range_interval], minor=True)
    ax.xaxis.grid(True, which = 'minor')
    ax.xaxis.grid(True, which = 'major')

    damage_interval = 5 if highest_damage<100 else 10
    ax.set_yticks([i for i in range(15 if lowest_damage >= 15 else 0, highest_damage + 3)][::damage_interval])
    ax.yaxis.grid(True)
    
    # add a title and axis labels
    plt.title(title)
    plt.xlabel('Distance (Meters)')
    plt.ylabel('Damage')

    return figure

