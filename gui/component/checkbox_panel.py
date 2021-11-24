import logging
from tkinter import *

from gui.component.state.checkboxes import CheckBoxes
from state_handler import ProgramConfig as PC


class Checkbox:
    boxes = []
    statusbar = None

    def __init__(self, parent, cisco_show_setting, elem_text, statusbar_text, col, row):
        self.var = BooleanVar()
        self.var.set(True if cisco_show_setting is True else False)
        self.checkbox = Checkbutton(parent, text=elem_text, var=self.var, onvalue=True, offvalue=False)
        self.checkbox.config(
            command=lambda show_setting_flag=cisco_show_setting,
                           checkbox=self.var,
                           checkbox_text=elem_text: Checkbox.toggle_program_config_elem_value(show_setting_flag,
                                                                                              checkbox, checkbox_text))
        self.checkbox.bind("<Enter>",
                           lambda event, text=statusbar_text: Checkbox.statusbar.set_statusbar_text(event, text))
        self.checkbox.bind("<Leave>", Checkbox.statusbar.clear_statusbar)
        self.checkbox.grid(column=col, row=row, sticky="w")
        Checkbox.boxes.append(self.checkbox)

    @staticmethod
    def toggle_program_config_elem_value(show_setting_flag, checkbox, checkbox_text):
        show_setting_flag = checkbox.get()
        logging.info(f"Toggle {checkbox_text}: {show_setting_flag, checkbox.get()}")

    @staticmethod
    def clear_checkboxes():
        for i in range(0, len(Checkbox.boxes)):
            Checkbox.boxes[i].deselect()


class CheckboxPanel:
    def __init__(self, config_panel, statusbar):
        Checkbox.statusbar = statusbar
        COLUMN_SIZE = 6
        grid = None
        grid1 = PanedWindow(config_panel)
        grid1.grid(column=0, row=0, sticky="ns")
        grid2 = PanedWindow(config_panel)
        grid2.grid(column=1, row=0, sticky="ns")
        grid3 = PanedWindow(config_panel)
        grid3.grid(column=2, row=0, sticky="ns")
        for idx, checkbox in enumerate(CheckBoxes.all_configuration_objects):
            if idx <= COLUMN_SIZE:
                grid = grid1
            elif idx <= COLUMN_SIZE * 2:
                grid = grid2
            elif idx <= COLUMN_SIZE * 3:
                grid = grid3
            Checkbox(grid, checkbox.activated, checkbox.btn_name, checkbox.help_text, 0, idx % (COLUMN_SIZE + 1))
