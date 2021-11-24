from tkinter import *

import state_handler
from gui.component.checkbox_panel import Checkbox


class ControlButtonPanel:
    def __init__(self, config_panel):
        self.buttons_pane = PanedWindow(config_panel)
        self.buttons_pane2 = PanedWindow(config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        btn_clear_checkboxes = Button(self.buttons_pane, text="Clear All Checkboxes", relief=GROOVE,
                                      command=Checkbox.clear_checkboxes)
        btn_clear_checkboxes.grid(column=2, row=1, padx=2, sticky="w")

        btn_reset_equipment = Button(self.buttons_pane, text="Reset Equipment", relief=GROOVE)
        btn_reset_equipment.grid(column=3, row=1, padx=2, sticky="e")

        btn_save_running_config = Button(self.buttons_pane, text="Save Running Configuration", relief=GROOVE)
        btn_save_running_config.grid(column=4, row=1, padx=2, sticky="e")

        # TODO: Implement username and password entries so that they are saved into the "state_handler.py"
        if state_handler.ProgramConfig.default_conf.get("username") is None:
            state_handler.ProgramConfig.default_conf["username"] = StringVar()
        username_label = Label(self.buttons_pane, text="Username")
        username_label.grid(column=0, row=1, sticky="w")
        username_entry = Entry(self.buttons_pane, width=20, relief=GROOVE,
                               textvariable=state_handler.ProgramConfig.default_conf.get("username"))
        username_entry.grid(column=1, row=1, sticky="e", ipady=2, pady=1, padx=3)

        if state_handler.ProgramConfig.default_conf.get("password") is None:
            state_handler.ProgramConfig.default_conf["password"] = StringVar()
        password_label = Label(self.buttons_pane, text="Password")
        password_label.grid(column=0, row=2, sticky="w")
        password_entry = Entry(self.buttons_pane, width=20, relief=GROOVE,
                               textvariable=state_handler.ProgramConfig.default_conf.get("password"))
        password_entry.grid(column=1, row=2, sticky="e", ipady=2, pady=1, padx=3)
