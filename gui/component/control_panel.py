from tkinter import *

from gui.component.config_panel import Checkbox


class ControlButtonPanel:
    def __init__(self, config_panel):
        self.buttons_pane = PanedWindow(config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        btn_clear_checkboxes = Button(self.buttons_pane, text="Clear All Checkboxes", relief=GROOVE, command=Checkbox.clear_checkboxes)
        btn_clear_checkboxes.grid(column=1, row=1, padx=2, sticky="w")

        btn_reset_equipment = Button(self.buttons_pane, text="Reset Equipment", relief=GROOVE)
        btn_reset_equipment.grid(column=2, row=1, padx=2, sticky="e")
