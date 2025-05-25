import json
import tkinter as tk
from tkinter import ttk  # Needed for Combobox and Spinbox

# Load JSON UI definition
with open("gui.json", "r") as file:
    ui_config = json.load(file)

root = tk.Tk()
root.title(ui_config["title"])
#root.iconbitmap("your_icon.ico")
root.geometry(ui_config["geometry"])

frm = tk.LabelFrame(root)#, text=ui_config["title"])
frm.grid(row=0,column=0,sticky="nsew", padx=10, pady=10)


# Menu to toggle frame visibility
menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="Show Frame", command=lambda: toggle_frame("Show"))
submenu.add_command(label="Hide Frame", command=lambda: toggle_frame("Hide"))

def toggle_frame(selection):
    """Show or hide LabelFrame based on menu selection"""
    if selection == "Show":
        frm.grid(row=0,column=0,sticky="nsew", padx=10, pady=10)
    else:
        frm.grid_remove()  # Hide the frame

widgets = {}

# Variables for dynamic widget bindings
var_dict = {}

# Function to handle button click
def submit_action():
    print(f"Name: {widgets['name_field'].get()}")
    print(f"Gender: {var_dict['gender'].get()}")
    print(f"Skills: {'Python' if widgets['skill_python'].get() else ''} {'JavaScript' if widgets['skill_js'].get() else ''}")
    print(f"Experience: {widgets['exp_years'].get()}")
    print(f"Country: {widgets['country'].get()}")

# Loop through JSON-defined widgets and create UI elements dynamically
for widget in ui_config["widgets"]:
    widget_type = widget["type"]
    param = widget.get("param", {})  # Extract widget parameters
    layout = widget.get("layout", {})  # Extract layout settings
    name = widget.get("name")  # Name for reference
    group = widget.get("group")  # Group variable name for Radiobuttons

    # Create widgets dynamically
    if widget_type == "Label":
        tk.Label(frm, **param).grid(**layout)
    elif widget_type == "Entry":
        entry = tk.Entry(frm, **param)
        entry.grid(**layout)
        widgets[name] = entry
    elif widget_type == "Button":
        tk.Button(frm, **param, command=submit_action).grid(**layout)
    elif widget_type == "Checkbutton":
        var = tk.IntVar()  # Variable for checkbox state
        widgets[name] = var
        tk.Checkbutton(frm, **param, variable=var).grid(**layout)
    elif widget_type == "Radiobutton":
        if group not in var_dict:
            var_dict[group] = tk.StringVar()  # Shared variable for group
        tk.Radiobutton(frm, **param, variable=var_dict[group]).grid(**layout)
    elif widget_type == "Spinbox":
        spin = ttk.Spinbox(frm, **param)
        spin.grid(**layout)
        widgets[name] = spin
    elif widget_type == "Combobox":
        combo = ttk.Combobox(frm, **param)
        combo.grid(**layout)
        widgets[name] = combo

root.mainloop()
