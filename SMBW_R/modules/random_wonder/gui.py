import itertools
import tkinter as tk
import json
from tkinter import messagebox

morph_checkboxes = []
effect_checkboxes = []


def morphs_update_checkboxes_with_json():
    with open("SMBW_R/modules/random_wonder/morph_config.json", "r") as json_file:
        data = json.load(json_file)
        for label_text, checkbox_var in morph_checkboxes:
            enabled = checkbox_var.get()
            data[label_text]["enabled"] = enabled

    with open("SMBW_R/modules/random_wonder/morph_config.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    messagebox.showinfo("Morphs Selected", "Morphs are selected successfuly")


def effects_update_checkboxes_with_json():
    with open("SMBW_R/modules/random_wonder/effect_config.json", "r") as json_file:
        data = json.load(json_file)
        for label_text, checkbox_var in effect_checkboxes:
            enabled = checkbox_var.get()
            data[label_text]["enabled"] = enabled

    with open("SMBW_R/modules/random_wonder/effect_config.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    messagebox.showinfo("Effects Selected", "Effects are selected successfuly")


class custom_morph_gui:
    def custom_morph_list_configurator():
        custom_morph_list = tk.Tk()

        with open("SMBW_R/modules/random_wonder/morph_config.json", "r") as json_file:
            data = json.load(json_file)

        custom_morph_list.title("Custom Morphs Selector")

        custom_morph_list_frame = tk.Frame(custom_morph_list)
        custom_morph_list_frame.pack()

        rows, cols = 1, 8

        json_keys = list(data.keys())

        for row, col in itertools.product(range(rows), range(cols)):
            index = row * cols + col
            if index < len(json_keys):
                label_text = json_keys[index]
                checkbox_var = tk.BooleanVar(value=data[label_text]["enabled"])
                checkbox = tk.Checkbutton(
                    custom_morph_list_frame, text=label_text, variable=checkbox_var
                )
                checkbox.grid(row=row, column=col, padx=5, pady=5)
                morph_checkboxes.append((label_text, checkbox_var))

        update_button = tk.Button(
            custom_morph_list,
            text="Set Custom Morphs",
            command=lambda: {
                morphs_update_checkboxes_with_json(),
                custom_morph_list.destroy(),
            },
        )
        update_button.pack()

        custom_morph_list.mainloop()


class custom_effect_gui:
    def custom_effect_list_configurator():
        custom_effect_list = tk.Tk()

        with open("SMBW_R/modules/random_wonder/effect_config.json", "r") as json_file:
            data = json.load(json_file)

        custom_effect_list.title("Custom Effects Selector")

        custom_effect_list_frame = tk.Frame(custom_effect_list)
        custom_effect_list_frame.pack()

        rows, cols = 1, 8

        json_keys = list(data.keys())

        for row, col in itertools.product(range(rows), range(cols)):
            index = row * cols + col
            if index < len(json_keys):
                label_text = json_keys[index]
                checkbox_var = tk.BooleanVar(value=data[label_text]["enabled"])
                checkbox = tk.Checkbutton(
                    custom_effect_list_frame, text=label_text, variable=checkbox_var
                )
                checkbox.grid(row=row, column=col, padx=5, pady=5)
                effect_checkboxes.append((label_text, checkbox_var))

        update_button = tk.Button(
            custom_effect_list,
            text="Set Custom Effect",
            command=lambda: {
                effects_update_checkboxes_with_json(),
                custom_effect_list.destroy(),
            },
        )
        update_button.pack()

        custom_effect_list.mainloop()
