from dataclasses import dataclass
from typing import List
from enum import Enum, auto


@dataclass(frozen=False)
class ConfigCheckbox:
    btn_name: str
    help_text: str
    activated: bool


class ProgramConfig:
    log_to_file = False  # Toggle flag - logs to stdout if not to file.
    erase_equipment = False  # TODO : Make the user type in a diceware password or something...

    write_config_to_startup = ConfigCheckbox(btn_name="Copy run start", help_text="Copy the running configuration into the startup configuration", activated=True)
    show_running_config = ConfigCheckbox(btn_name="Running Configuration", help_text="Retrieve the running configuration", activated=False)
    show_startup_config = ConfigCheckbox(btn_name="Startup Configuration", help_text="Retrieve the startup configuration", activated=False)
    show_dhcp = ConfigCheckbox(btn_name="DHCP", help_text="Retrieve the DHCP...", activated=True)
    show_vtp = ConfigCheckbox(btn_name="VTP", help_text="Retrieve the ...", activated=False)
    show_vlan = ConfigCheckbox(btn_name="VLAN", help_text="Retrieve the ...", activated=False)
    show_cdp = ConfigCheckbox(btn_name="CDP", help_text="Retrieve the ...", activated=False)
    show_ntp = ConfigCheckbox(btn_name="NTP", help_text="Retrieve the ...", activated=False)
    show_system = ConfigCheckbox(btn_name="System", help_text="Retrieve the ...", activated=False)
    show_hardware = ConfigCheckbox(btn_name="Hardware", help_text="Retrieve the ...", activated=False)
    show_users = ConfigCheckbox(btn_name="Users", help_text="Retrieve the ...", activated=False)
    show_logging = ConfigCheckbox(btn_name="Logging", help_text="Retrieve the ...", activated=False)
    show_tech_support = ConfigCheckbox(btn_name="Tech Support", help_text="Retrieve the ...", activated=False)
    show_mac_table = ConfigCheckbox(btn_name="MAC Table", help_text="Retrieve the ...", activated=False)
    show_arp = ConfigCheckbox(btn_name="ARP", help_text="Retrieve the ...", activated=False)
    show_routes = ConfigCheckbox(btn_name="Routes", help_text="Retrieve the ...", activated=False)
    show_etherchannel = ConfigCheckbox(btn_name="Etherchannel", help_text="Retrieve the ...", activated=False)
    show_protocols = ConfigCheckbox(btn_name="Protocols", help_text="Retrieve the ...", activated=False)
    show_spanning_tree = ConfigCheckbox(btn_name="Spanning Tree", help_text="Retrieve the ...", activated=False)
    show_acls = ConfigCheckbox(btn_name="ACL", help_text="Retrieve the ...", activated=False)
    show_interfaces_brief = ConfigCheckbox(btn_name="Interfaces", help_text="Retrieve the ...", activated=False)

    default_conf = {
        'device_type': 'cisco_ios',
        'username': 'admin',
        'password': 'admin',
        'port': 22,
        # 'secret': 'secret',  # optional, defaults to ''
    }

    host_list = [
        '2001:db8:12:2::1',
        '2001:db8:12:2::2',
        '2001:db8:12:2::3'
    ]

    @classmethod
    def logger_output_stream_is_file(cls):
        return cls.log_to_file
