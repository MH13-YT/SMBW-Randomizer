import itertools
import tkinter as tk
import json
from tkinter import messagebox

enemy_checkboxes = []
effect_checkboxes = []


def enemy_update_checkboxes_with_json():
    with open("SMBW_R/modules/random_enemy/enemy_config.json", "r") as json_file:
        data = json.load(json_file)
        for label_text, checkbox_var in enemy_checkboxes:
            enabled = checkbox_var.get()
            data[label_text]["enabled"] = enabled

    with open("SMBW_R/modules/random_enemy/enemy_config.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    messagebox.showinfo("enemys Selected", "enemys are selected successfuly")


class custom_enemy_gui:
    def custom_enemy_list_configurator():
        custom_enemy_list = tk.Tk()

        with open("SMBW_R/modules/random_enemy/enemy_config.json", "r") as json_file:
            data = json.load(json_file)

        custom_enemy_list.title("Custom enemy Selector")

        custom_enemy_list_frame = tk.Frame(custom_enemy_list)
        custom_enemy_list_frame.pack()

        rows, cols = 11, 6

        json_keys = list(data.keys())

        for row, col in itertools.product(range(rows), range(cols)):
            index = row * cols + col
            if index < len(json_keys):
                label_text = json_keys[index]
                checkbox_var = tk.BooleanVar(value=data[label_text]["enabled"])
                checkbox = tk.Checkbutton(
                    custom_enemy_list_frame, text=label_text, variable=checkbox_var
                )
                checkbox.grid(row=row, column=col, padx=5, pady=5)
                enemy_checkboxes.append((label_text, checkbox_var))

        update_button = tk.Button(
            custom_enemy_list,
            text="Set Custom enemy",
            command=lambda: {
                enemy_update_checkboxes_with_json(),
                custom_enemy_list.destroy(),
            },
        )
        update_button.pack()

        custom_enemy_list.mainloop()
