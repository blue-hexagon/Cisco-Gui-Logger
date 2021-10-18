from tk_gui_element import config_panel


class ProgramConfig:
    def __init__(self):
        self.LOG_TO_FILE = False  # Toggle flag - logs to stdout if not to file.
        self.WRITE_CONFIG_TO_STARTUP = False
        self.SHOW_RUNNING_CONFIG = True
        self.SHOW_DHCP = False
        self.SHOW_VTP = False
        self.SHOW_VLAN = False
        self.SHOW_INTERFACES_BRIEF = False
        self.ERASE_EQUIPMENT = False # WARNING : Make the user type in a diceware password or something...


        self.running_config = config_panel.ConfigPanel.running_config

        self.default_conf = {
            'device_type': 'cisco_ios',
            'username': 'admin',
            'password': 'admin',
            'port': 22,
            # 'secret': 'secret',  # optional, defaults to ''
        }

        self.host_list = [
            '2001:db8:12:2::1',
            '2001:db8:12:2::2',
            '2001:db8:12:2::3'
        ]

    def logger_output_stream_is_file(self):
        return self.LOG_TO_FILE
