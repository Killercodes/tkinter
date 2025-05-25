import yaml
import tkinter as tk
from tkinter import ttk

# Load YAML UI definition
with open("gui.yaml", "r") as file:
    ui_config = yaml.safe_load(file)

root = tk.Tk()
root.title(ui_config["title"])
root.geometry(ui_config["geometry"])

widgets = {}
var_dict = {}

# Function to handle button click
def submit_action():
    print(f"Name: {widgets['name_field'].get()}")
    print(f"Email: {widgets['email_field'].get()}")
    print(f"Experience: {widgets['exp_years'].get()}")

# Loop through YAML-defined frames and create labeled sections
for frame_data in ui_config["frames"]:
    frame = tk.LabelFrame(root, **frame_data["param"])  # Create LabelFrame
    frame.grid(**frame_data["layout"])  # Apply layout

    # Create widgets inside the labeled frame
    for widget in frame_data["widgets"]:
        widget_type = widget["type"]
        param = widget.get("param", {})
        layout = widget.get("layout", {})
        name = widget.get("name")

        # Create widgets dynamically inside the frame
        if widget_type == "Label":
            tk.Label(frame, **param).grid(**layout)
        elif widget_type == "Entry":
            entry = tk.Entry(frame, **param)
            entry.grid(**layout)
            widgets[name] = entry
        elif widget_type == "Button":
            tk.Button(frame, **param, command=submit_action).grid(**layout)
        elif widget_type == "Spinbox":
            spin = ttk.Spinbox(frame, **param)
            spin.grid(**layout)
            widgets[name] = spin

root.mainloop()
