from graph_maker import get_graph_figure
from damage_calculator import calculate_damage
from tkinter import *
import json
import gun
import caliber
from functools import partial
from PIL import Image,ImageTk
import math

current_ammo_config = []
current_gun = None

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
    
    def quitting():
        root.quit()
        root.destroy()

    guns = load_data("gunstats.json",gun.Gun)
    calibers = load_data("calibers.json",caliber.Caliber)

    # Create object
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", quitting)
    root.geometry( "550x720" )
    root.title('WW3 Stats Utility')

    selected_gun = StringVar(root)
    selected_gun.set("Choose a gun...")

    # Create a dropdown menu
    gun_options = [gun.fullname for gun in guns]
    dropdown_guns = OptionMenu(root, selected_gun, *gun_options)
    dropdown_guns.config(width=20)
    dropdown_guns.grid(row = 0, column = 0, columnspan = 4, rowspan = 1, padx = 190, pady = 5)

    gun_title_label = Label(text = "Select a gun", font=("Arial", 15))
    gun_realname_label = Label(text = "", font=("Arial", 8), fg="green")
    gun_weight_label = Label(text = "Weight:", font=("Arial", 11), anchor="w" )
    gun_firerate_label = Label(text = "Fire rate:", font=("Arial", 11), anchor="w")
    gun_caliber_label = Label(text = "Caliber:", font=("Arial", 11), anchor="w")

    gun_title_label.grid(row = 1, column = 0, columnspan = 4, rowspan = 1)
    gun_realname_label.grid(row = 2, column = 0, columnspan = 4, rowspan = 1)
    gun_weight_label.grid(row = 3, column = 0, columnspan = 2, rowspan = 1, sticky = W, padx = (100,0)) 
    gun_firerate_label.grid(row = 4, column = 0, columnspan = 2, rowspan = 1, sticky = W, padx = (100,0))
    gun_caliber_label.grid(row = 5, column = 0, columnspan = 2, rowspan = 1, sticky = W, padx = (100,0))

    gun_weight_text = Label(text = "", font=("Arial", 11), anchor="e")
    gun_firerate_text = Label(text = "", font=("Arial", 11), anchor="e")
    gun_caliber_text = Label(text = "", font=("Arial", 11), anchor="e")

    gun_weight_text.grid(row = 3, column = 2, columnspan = 2, rowspan = 1, sticky = E, padx = (0,100))
    gun_firerate_text.grid(row = 4, column = 2, columnspan = 2, rowspan = 1, sticky = E, padx = (0,100))
    gun_caliber_text.grid(row = 5, column = 2, columnspan = 2, rowspan = 1, sticky = E, padx = (0,100))

    fig_canvas = Label()
    

    #TTK Calculator elements init
    label_ttk_title = Label(text = "TTK Calculator (Choose a gun and barrel)", font=("Arial", 15), anchor="w")
    label_ttk_title.grid(row = 8, column = 0, columnspan = 4, rowspan = 1, pady = 3)

    # TTK inputs init
    Label(text = "Distance:", font=("Arial", 11), anchor="w").grid(row = 9, column = 0, columnspan = 1, rowspan = 1, sticky = W, padx = (90,0))
    Label(text = "Region:", font=("Arial", 11), anchor="w").grid(row = 9, column = 2, columnspan = 1, rowspan = 1, sticky = W, padx = (0,0))

    distance_input = Entry(root)
    distance_input.config(width=5)
    distance_input.grid(row = 9, column = 1, columnspan = 1, rowspan = 1,padx = (5,50))

    selected_region = StringVar(root)
    selected_region.set("Select region")

    region_dropdown = OptionMenu(root, selected_region, *["Head","Torso/Arms","Legs","Feet"])
    region_dropdown.config(width=10)
    region_dropdown.grid(row = 9, column = 3, columnspan = 1, rowspan = 1,padx = (0,90))

    # TTK texts init
    Label(text = "Damage:", font=("Arial", 11), anchor="w").grid(row = 11, column = 0, columnspan = 1, rowspan = 1, sticky = W, padx = (80,0))
    Label(text = "DPS:", font=("Arial", 11), anchor="w").grid(row = 11, column = 2, columnspan = 1, rowspan = 1, sticky = W, padx = (0,0))
    Label(text = "STK:", font=("Arial", 11), anchor="w").grid(row = 12, column = 0, columnspan = 1, rowspan = 1, sticky = W, padx = (80,0))
    Label(text = "TTK:", font=("Arial", 11), anchor="w").grid(row = 12, column = 2, columnspan = 1, rowspan = 1, sticky = W, padx = (0,0))

    
    text_ttk_dmg = Label(text = "", font=("Arial", 11), anchor="e")
    text_ttk_dmg.grid(row = 11, column = 1, columnspan = 1, rowspan = 1, sticky = E, padx = (0,10))

    text_ttk_dps = Label(text = "", font=("Arial", 11), anchor="e")
    text_ttk_dps.grid(row = 11, column = 3, columnspan = 1, rowspan = 1, sticky = E, padx = (0,80))

    text_ttk_stk = Label(text = "", font=("Arial", 11), anchor="e")
    text_ttk_stk.grid(row = 12, column = 1, columnspan = 1, rowspan = 1, sticky = E, padx = (0,10))

    text_ttk_ttk = Label(text = "", font=("Arial", 11), anchor="e")
    text_ttk_ttk.grid(row = 12, column = 3, columnspan = 1, rowspan = 1, sticky = E, padx = (0,80))

    text_pellets = Label(text = "", font=("Arial", 10))

    Label(text = "Licensed under GNU General Public License v3.0", font=("Arial italic", 9)).grid(row = 14, column = 0, columnspan = 4, rowspan = 1, pady = 5)
        

    def show_gun_info(gun_selection, *args):
        
        label_ttk_title.config(text= "TTK Calculator (Choose a barrel)") 
        text_ttk_dmg.config(text="")
        text_ttk_dps.config(text="")
        text_ttk_stk.config(text="")
        text_ttk_ttk.config(text="")
        text_pellets.grid_forget()

        global current_ammo_config
        current_ammo_config = []

        # Forget graph canvas
        fig_canvas.grid_forget()

        #Forget TTK button

        gun = next(gun for gun in guns if gun.fullname == gun_selection.get())
        ammo = next(ammo for ammo in calibers if ammo.shortname == gun.caliber)

        global current_gun
        current_gun = gun

        gun_title_label.config(text=gun.fullname + " - " + gun.type.value)
        if(gun.fullname.lower() != gun.realname.lower()):
            gun_realname_label.config(text="" + gun.realname)
        else:
            gun_realname_label.config(text="")

        str_weight = ""
        for i in range(int(gun.weight)):
            if i%4==0:
                str_weight = str_weight + " "
            str_weight = str_weight + "*"
        
        gun_weight_text.config(text= str_weight + " (" + str(gun.weight) + ")")
        gun_firerate_text.config(text="" + str(gun.rof) + " (" + gun.firemode.value + ")")
        gun_caliber_text.config(text="" + ammo.name)

        # Create a dropdown menu 
        barrel_options = ["Standard"]
        if ammo.compact:
            barrel_options.append("Compact")
        if ammo.marksman:
            barrel_options.append("Marksman")

        selected_barrel = StringVar(root)
        dropdown_barrels = OptionMenu(root, selected_barrel, *barrel_options)
        dropdown_barrels.config(width=15)
        selected_barrel.set("Standard")
        dropdown_barrels.grid(row = 6, column = 0, columnspan = 4, rowspan = 1, pady = 2)
        selected_barrel.trace('w', partial(show_ballistic_info, selected_barrel, ammo))
        show_ballistic_info(selected_barrel, ammo)

    def show_ballistic_info(barrel_selection, ammo, *args):
        
        text_ttk_dmg.config(text="")
        text_ttk_dps.config(text="")
        text_ttk_stk.config(text="")
        text_ttk_ttk.config(text="")

        global current_ammo_config
        current_ammo_config = []
        label_ttk_title.config(text= "TTK Calculator (No armor)") 

        ammo_stats = []
        title = ammo.name + " with " + barrel_selection.get() + " barrel"
        if barrel_selection.get() == "Standard":
            ammo_stats = ammo.standard
        elif barrel_selection.get() == "Compact":
            ammo_stats =  ammo.compact
        elif barrel_selection.get() == "Marksman":
            ammo_stats = ammo.marksman
        
        current_ammo_config = ammo_stats

        figure = get_graph_figure(ammo_stats, title, "green")

        figure.savefig("data/temp_figure.png", transparent=True)
        img = ImageTk.PhotoImage(Image.open("data/temp_figure.png"))
        
        fig_canvas.config(image=img)
        fig_canvas.image = img
        fig_canvas.grid(row = 7, column = 0, columnspan = 4, rowspan = 1, pady = 2)
        
        #TTK calculator elements


    def calculate_ttk():
        global current_gun

        text_ttk_dmg.config(text="")
        text_ttk_dps.config(text="")
        text_ttk_stk.config(text="")
        text_ttk_ttk.config(text="")
        
        if current_ammo_config and distance_input.get().isdigit() and selected_region.get() in ["Head","Torso/Arms","Legs","Feet"]:
            distance = int(distance_input.get())
            if distance >=0:
                damage = calculate_damage(current_ammo_config,distance, selected_region.get())

                if damage > 0:
                    ammo = next(ammo for ammo in calibers if ammo.shortname == current_gun.caliber)
                    pellets = int(ammo.pellets)
                    if pellets > 1:
                        damage = damage*pellets
                        text_pellets.config(text="Assuming all pellets hit (" + ammo.pellets + " pellets)")
                        text_pellets.grid(row = 13, column = 0, columnspan = 4, rowspan = 1)
                    
                    rps = current_gun.rof/60
                    dps = round(damage*(rps))
                    stk = math.ceil(100/damage)
                    ttk = round(((stk-1)/rps)*1000)
                    text_ttk_dmg.config(text=str(damage))
                    text_ttk_dps.config(text=str(dps))
                    text_ttk_stk.config(text=str(stk))
                    text_ttk_ttk.config(text=str(ttk) + "ms")
                else: 
                    text_ttk_dmg.config(text="0")
                    text_ttk_dps.config(text="0")
                    text_ttk_stk.config(text="N/A")
                    text_ttk_ttk.config(text="N/A")
                
            

    # Call the show_table function whenever the user selects a different table from the dropdown
    selected_gun.trace('w', partial(show_gun_info, selected_gun))

    ttk_button = Button(root, text = 'Calculate', bd = '2', command = calculate_ttk)
    ttk_button.grid(row = 10, column = 0, columnspan = 4, rowspan = 1, pady = 2)

    # Start the event loop
    root.mainloop()
    
    

if __name__ == '__main__':
    
    __launch_app()