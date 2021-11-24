import logging
from tkinter import *
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


class ConfigPanel:
    def __init__(self, config_panel, statusbar):
        Checkbox.statusbar = statusbar

        grid1 = PanedWindow(config_panel)
        grid1.grid(column=0, row=0, sticky="ns")
        grid2 = PanedWindow(config_panel)
        grid2.grid(column=1, row=0, sticky="ns")
        grid3 = PanedWindow(config_panel)
        grid3.grid(column=2, row=0, sticky="ns")

        Checkbox(grid1, PC.show_running_config.activated, PC.show_running_config.btn_name,PC.show_running_config.help_text, 0, 0)
        Checkbox(grid1, PC.show_startup_config.activated, PC.show_startup_config.btn_name,PC.show_startup_config.help_text, 0, 1)
        Checkbox(grid1, PC.show_system.activated, PC.show_system.btn_name, PC.show_system.help_text, 0, 2)
        Checkbox(grid1, PC.show_hardware.activated, PC.show_hardware.btn_name, PC.show_hardware.help_text, 0, 3)
        Checkbox(grid1, PC.show_users.activated, PC.show_users.btn_name, PC.show_users.help_text, 0, 4)
        Checkbox(grid1, PC.show_logging.activated, PC.show_logging.btn_name, PC.show_logging.help_text, 0, 5)
        Checkbox(grid1, PC.show_tech_support.activated, PC.show_tech_support.btn_name,PC.show_tech_support.help_text, 0, 6)

        Checkbox(grid2, PC.show_mac_table.activated, PC.show_mac_table.btn_name, PC.show_mac_table.help_text, 0,0)
        Checkbox(grid2, PC.show_arp.activated, PC.show_arp.btn_name, PC.show_arp.help_text, 0, 1)
        Checkbox(grid2, PC.show_interfaces_brief.activated, PC.show_interfaces_brief.btn_name,PC.show_interfaces_brief.help_text, 0, 2)
        Checkbox(grid2, PC.show_routes.activated, PC.show_routes.btn_name, PC.show_routes.help_text, 0, 3)
        Checkbox(grid2, PC.show_protocols.activated, PC.show_protocols.btn_name, PC.show_protocols.help_text, 0,4)
        Checkbox(grid2, PC.show_spanning_tree.activated, PC.show_spanning_tree.btn_name,PC.show_spanning_tree.help_text, 0, 5)
        Checkbox(grid2, PC.show_acls.activated, PC.show_acls.btn_name, PC.show_acls.help_text, 0, 6)

        Checkbox(grid3, PC.show_dhcp.activated, PC.show_dhcp.btn_name, PC.show_dhcp.help_text, 0, 0)
        Checkbox(grid3, PC.show_vtp.activated, PC.show_vtp.btn_name, PC.show_vtp.help_text, 0, 1)
        Checkbox(grid3, PC.show_vlan.activated, PC.show_vlan.btn_name, PC.show_vlan.help_text, 0, 2)
        Checkbox(grid3, PC.show_etherchannel.activated, PC.show_etherchannel.btn_name, PC.show_etherchannel.help_text, 0, 3)
        Checkbox(grid3, PC.show_cdp.activated, PC.show_cdp.btn_name, PC.show_cdp.help_text, 0, 4)
        Checkbox(grid3, PC.show_ntp.activated, PC.show_ntp.btn_name, PC.show_ntp.help_text, 0, 5)

        # = Checkbox(self.config_checkboxes4, "", "", 0, 0)
