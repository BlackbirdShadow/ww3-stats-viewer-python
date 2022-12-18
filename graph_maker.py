import matplotlib.pyplot as plt

def get_graph_canvas(ammo_data, title, color):

    figure = plt.figure()   
    figure.set_figwidth(4)
    figure.set_figheight(2)
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

    # end graph at last point + 20x, same damage as last point
    distances.append(distances[-1]+20)
    damages.append(lowest_damage)

    # create the broken line graph
    plt.plot(distances, damages, 'o-', color=color)

    for i, j in zip(distances, damages):
        plt.text(i,j+0.5,str(j).format(i, j))

    # defining y axis bounds, show lowest damage - 10 except if negative then zero, highest dmage +
    plt.ylim(lowest_damage-2 if lowest_damage-2 >= 0 else 0, highest_damage + 5)

    # add a title and axis labels
    plt.title(title)
    plt.xlabel('Meters')
    plt.ylabel('Damage')
    #plt.show()
    
    return figure
    #plt.show()


