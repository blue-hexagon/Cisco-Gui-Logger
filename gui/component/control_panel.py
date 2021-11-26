from tkinter import *
from tkinter import ttk

import state_handler
from gui.component.checkbox_panel import Checkbox


class ControlButtonPanel:
    def __init__(self, config_panel):
        self.BUTTON_WIDTH = 24
        self.control_panel = PanedWindow(config_panel)
        self.control_panel.grid(column=0, row=1, columnspan=80, sticky="we")

        self.credentials_panel = PanedWindow(self.control_panel)
        self.credentials_panel.grid(column=0, row=0, sticky="w")
        self.buttons_panel = PanedWindow(self.control_panel)
        self.buttons_panel.grid(column=1, row=0, sticky="w")

        # separator = ttk.Separator(self.control_panel, orient='horizontal')
        # separator.grid(column=0,row=0, columnspan=2000,sticky="news",padx=2,pady=4)

        # TODO: Implement username and password entries so that they are saved into the "state_handler.py"
        if state_handler.ProgramConfig.default_conf.get("username") is None:
            state_handler.ProgramConfig.default_conf["username"] = StringVar()
        username_label = Label(self.credentials_panel, text="Username")
        username_label.grid(column=0, row=1, sticky="w")
        username_entry = Entry(self.credentials_panel, width=20, relief=GROOVE,
                               textvariable=state_handler.ProgramConfig.default_conf.get("username"))
        username_entry.grid(column=1, row=1, sticky="e", ipady=2, pady=1, padx=3)

        if state_handler.ProgramConfig.default_conf.get("password") is None:
            state_handler.ProgramConfig.default_conf["password"] = StringVar()
        password_label = Label(self.credentials_panel, text="Password")
        password_label.grid(column=0, row=2, sticky="w")
        password_entry = Entry(self.credentials_panel, width=20, relief=GROOVE,
                               textvariable=state_handler.ProgramConfig.default_conf.get("password"))
        password_entry.grid(column=1, row=2, sticky="e", ipady=2, pady=1, padx=3)

        btn_save_running_config = Button(self.buttons_panel, text="Save Running Configuration", width=self.BUTTON_WIDTH,
                                         relief=GROOVE)
        btn_save_running_config.grid(column=0, row=1, padx=2, sticky="ew")

        btn_reset_equipment = Button(self.buttons_panel, text="Reset Equipment", width=self.BUTTON_WIDTH, relief=GROOVE)
        btn_reset_equipment.grid(column=0, row=2, padx=2, sticky="ew")

        btn_delete_vlans = Button(self.buttons_panel, text="Delete vlan.dat", width=self.BUTTON_WIDTH,
                                  relief=GROOVE)  # TODO #, command=)
        btn_delete_vlans.grid(column=1, row=1, padx=2, sticky="ew")

        btn_undefined2 = Button(self.buttons_panel, text="Undefined", width=self.BUTTON_WIDTH,
                                relief=GROOVE)  # TODO #, command=)
        btn_undefined2.grid(column=1, row=2, padx=2, sticky="ew")

        btn_clear_checkboxes = Button(self.buttons_panel, text="Clear All Checkboxes", width=self.BUTTON_WIDTH,
                                      relief=GROOVE, command=Checkbox.clear_checkboxes)
        btn_clear_checkboxes.grid(column=2, row=1, padx=2, sticky="ew")

        btn_save_all_config = Button(self.buttons_panel, text="Save All Configuration", width=self.BUTTON_WIDTH,
                                     relief=GROOVE, command=Checkbox.clear_checkboxes)
        btn_save_all_config.grid(column=2, row=2, padx=2, sticky="ew")
