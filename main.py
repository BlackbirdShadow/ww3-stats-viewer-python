import graph_maker
from tkinter import *
import json
import gun
import caliber
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image,ImageTk

def load_data(filename:str, Class) -> list:
    list = []
    with open('data/'+filename, 'r') as f:
    # Load the JSON data into a Python object
        data = json.load(f)
        for map in data:
            gun = Class(map)
            list.append(gun)
    return list

 # Define the function to be executed when the selection in the dropdown menu changes

def __launch_app():
    
    guns = load_data("gunstats.json",gun.Gun)
    calibers = load_data("calibers.json",caliber.Caliber)

    # Create object
    root = Tk()
    root.geometry( "500x800" )
    root.title('WW3 Stats Utility')

    selected_gun = StringVar(root)
    selected_gun.set("Choose a gun...")

    # Create a dropdown menu
    gun_options = [gun.fullname for gun in guns]
    dropdown_guns = OptionMenu(root, selected_gun, *gun_options)
    dropdown_guns.pack()

    gun_title_label = Label(text = "", font=("Arial", 15))
    gun_realname_label = Label(text = "", font=("Arial", 8), fg="green")
    gun_weight_label = Label(text = "", font=("Arial", 11))
    gun_firerate_label = Label(text = "", font=("Arial", 11))
    gun_caliber_label = Label(text = "", font=("Arial", 11))

    gun_title_label.pack()
    gun_realname_label.pack()
    gun_weight_label.pack()
    gun_firerate_label.pack()
    gun_caliber_label.pack(pady=1)

    selected_barrel = StringVar(root)
    selected_barrel.set("")

    dropdown_barrels = OptionMenu(root, selected_barrel, [])
    fig_canvas = Label()
    
    

    def show_gun_info(gun_selection, *args):
        # Retrieve the data for the selected table
        fig_canvas.pack_forget()
        gun = next(gun for gun in guns if gun.fullname == gun_selection.get())
        ammo = next(ammo for ammo in calibers if ammo.shortname == gun.caliber)

        gun_title_label.config(text=gun.fullname + " - " + gun.type.value)
        if(gun.fullname.lower() != gun.realname.lower()):
            gun_realname_label.config(text="Real name: " + gun.realname)
        else:
            gun_realname_label.config(text="")

        gun_weight_label.config(text="Weight: " + str(gun.weight) + " units")
        gun_firerate_label.config(text="Fire rate: " + str(gun.rof) + " (" + gun.firemode.value + ")")
        gun_caliber_label.config(text="Caliber: " + ammo.name)

        # Create a dropdown menu 
        barrel_options = ["Standard"]
        if ammo.compact:
            barrel_options.append("Compact")
        if ammo.marksman:
            barrel_options.append("Marksman")
        
        dropdown_barrels.pack(pady=10)
        menu = dropdown_barrels.children["menu"]
        menu.delete(0, "end")

        selected_barrel.set("Choose a barrel...")
        for option in barrel_options:
            menu.add_command(label=option, command=partial(show_ballistic_info, option, ammo))

        

    def show_ballistic_info(barrel_selection, ammo, *args):
        selected_barrel.set(barrel_selection)
        ammo_stats = []
        title = barrel_selection + " barrel damage"
        if barrel_selection == "Standard":
            ammo_stats = ammo.standard
        elif barrel_selection == "Compact":
            ammo_stats =  ammo.compact
        elif barrel_selection == "Marksman":
            ammo_stats = ammo.marksman
        
        
        figure = graph_maker.get_graph_figure(ammo_stats, title, "green")

        figure.savefig("figure.png", transparent=True)
        img = ImageTk.PhotoImage(Image.open("figure.png"))
        
        fig_canvas.config(image=img)
        fig_canvas.image = img
        fig_canvas.pack()
        
        


    # Call the show_table function whenever the user selects a different table from the dropdown
    selected_gun.trace('w', partial(show_gun_info, selected_gun))

    # Start the event loop
    root.mainloop()

if __name__ == '__main__':
    __launch_app()