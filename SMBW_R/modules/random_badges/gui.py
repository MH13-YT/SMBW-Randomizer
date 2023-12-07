import itertools
import tkinter as tk
import json
from tkinter import messagebox

checkboxes = []


def update_checkboxes_with_json():
    with open("SMBW_R/modules/random_badges/config.json", "r") as json_file:
        data = json.load(json_file)
        for label_text, checkbox_var in checkboxes:
            enabled = checkbox_var.get()
            data[label_text]["enabled"] = enabled

    with open("SMBW_R/modules/random_badges/config.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    messagebox.showinfo(
        "Badges Sélectionné", "Les Badges ont été sélectionné avec succés."
    )


class custom_badges_gui:
    def custom_badge_list_configurator():
        custom_badge_list = tk.Tk()

        with open("SMBW_R/modules/random_badges/config.json", "r") as json_file:
            data = json.load(json_file)

        custom_badge_list.title("Custom Badges Selector")

        custom_badge_list_frame = tk.Frame(custom_badge_list)
        custom_badge_list_frame.pack()

        rows, cols = 3, 8

        json_keys = list(data.keys())

        for row, col in itertools.product(range(rows), range(cols)):
            index = row * cols + col
            if index < len(json_keys):
                label_text = json_keys[index]
                checkbox_var = tk.BooleanVar(value=data[label_text]["enabled"])
                checkbox = tk.Checkbutton(
                    custom_badge_list_frame, text=label_text, variable=checkbox_var
                )
                checkbox.grid(row=row, column=col, padx=5, pady=5)
                checkboxes.append((label_text, checkbox_var))

        update_button = tk.Button(
            custom_badge_list,
            text="Set Custom Badges",
            command=lambda: {
                update_checkboxes_with_json(),
                custom_badge_list.destroy(),
            },
        )
        update_button.pack()

        custom_badge_list.mainloop()
