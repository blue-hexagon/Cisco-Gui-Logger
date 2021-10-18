import tkinter
from tkinter import *


class Checkbox():
    def __init__(self, parent, statusbar, text, statusbar_text, col, row):
        self.var = BooleanVar()
        self.elem = Checkbutton(parent, text=text, var=self.var)
        self.elem.bind("<Enter>", lambda event, text=statusbar_text: statusbar.set_statusbar_text(event, text))
        self.elem.bind("<Leave>", statusbar.clear_statusbar)
        self.elem.grid(column=col, row=row, sticky="w")


class ConfigPanel:
    def __init__(self, config_panel, statusbar):
        self.config_checkboxes1 = PanedWindow(config_panel)
        self.config_checkboxes1.grid(column=0, row=0, sticky="ns")
        self.config_checkboxes2 = PanedWindow(config_panel)
        self.config_checkboxes2.grid(column=1, row=0, sticky="ns")
        self.config_checkboxes3 = PanedWindow(config_panel)
        self.config_checkboxes3.grid(column=2, row=0, sticky="ns")
        self.config_checkboxes4 = PanedWindow(config_panel)
        self.config_checkboxes4.grid(column=3, row=0, sticky="ns")
        self.config_checkboxes5 = PanedWindow(config_panel)
        self.config_checkboxes5.grid(column=4, row=0, sticky="ns")

        running_config = Checkbox(self.config_checkboxes1, statusbar, "Running Configuration", "Show running configuration", 0, 0)
        startup_config = Checkbox(self.config_checkboxes1, statusbar, "Startup Configuration", "Show startup configuration", 0, 1)
        system = Checkbox(self.config_checkboxes1, statusbar, "System", "", 0, 2)
        hardware = Checkbox(self.config_checkboxes1, statusbar, "Hardware", "", 0, 3)
        users = Checkbox(self.config_checkboxes1, statusbar, "Users", "", 0, 4)
        logging = Checkbox(self.config_checkboxes1, statusbar, "Logging", "", 0, 5)
        tech_support = Checkbox(self.config_checkboxes1, statusbar, "Tech Support", "", 0, 6)

        mac_address_table = Checkbox(self.config_checkboxes2, statusbar, "Mac Table", "", 0, 0)
        arp = Checkbox(self.config_checkboxes2, statusbar, "ARP", "", 0, 1)
        interfaces = Checkbox(self.config_checkboxes2, statusbar, "Interfaces", "", 0, 2)
        routes = Checkbox(self.config_checkboxes2, statusbar, "Routes", "", 0, 3)
        protocols = Checkbox(self.config_checkboxes2, statusbar, "Protocols", "", 0, 4)
        spannign_tree = Checkbox(self.config_checkboxes2, statusbar, "Spanning Tree", "", 0, 5)
        access_control_lists = Checkbox(self.config_checkboxes2, statusbar, "ACLs", "", 0, 6)

        dhcp = Checkbox(self.config_checkboxes3, statusbar, "DHCP", "", 0, 0)
        vtp = Checkbox(self.config_checkboxes3, statusbar, "VTP", "", 0, 1)
        vlan = Checkbox(self.config_checkboxes3, statusbar, "VLAN", "", 0, 2)
        etherchannel = Checkbox(self.config_checkboxes3, statusbar, "Etherchannel", "", 0, 3)
        cdp = Checkbox(self.config_checkboxes3, statusbar, "CDP", "", 0, 4)
        ntp = Checkbox(self.config_checkboxes3, statusbar, "NTP", "", 0, 5)
        ntp = Checkbox(self.config_checkboxes3, statusbar, "NTP", "", 0, 5)
