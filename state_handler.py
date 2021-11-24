from dataclasses import dataclass
from tkinter import StringVar
from typing import List, Optional
from enum import Enum, auto


@dataclass(frozen=False)
class ConfigCheckbox:
    btn_name: str
    help_text: str
    activated: bool
    text_divider: [Optional[str]]
    ios_command: str


class ProgramConfig:
    log_to_file = False  # Toggle flag - logs to stdout if not to file.
    erase_equipment = False  # TODO : Make the user type in a diceware password or something...
    all_configuration_objects = []

    write_config_to_startup = ConfigCheckbox(btn_name="Copy run start",
                                             help_text="Copy the running configuration into the startup configuration",
                                             activated=False,
                                             text_divider=None,  # Doesn't render text to the output
                                             ios_command="write")
    all_configuration_objects.append(write_config_to_startup)

    show_running_config = ConfigCheckbox(btn_name="Running Configuration",
                                         help_text="Retrieve the running configuration",
                                         activated=True,
                                         text_divider="\n\n*** Gathering Running Configuration File Data ***\n",
                                         ios_command='show run')
    all_configuration_objects.append(show_running_config)
    show_startup_config = ConfigCheckbox(btn_name="Startup Configuration",
                                         help_text="Retrieve the startup configuration",
                                         activated=False,
                                         text_divider="",
                                         ios_command="show start")
    all_configuration_objects.append(show_startup_config)
    show_dhcp = ConfigCheckbox(btn_name="DHCP",
                               help_text="Retrieve the DHCP...",
                               activated=False,
                               text_divider="",
                               ios_command="show dhcp server")
    all_configuration_objects.append(show_dhcp)
    show_vtp = ConfigCheckbox(btn_name="VTP",
                              help_text="Retrieve the ...",
                              activated=False,
                              text_divider="",
                              ios_command="show vtp status")
    all_configuration_objects.append(show_vtp)
    show_vlan = ConfigCheckbox(btn_name="VLAN",
                               help_text="Retrieve the ...",
                               activated=False,
                               text_divider="",
                               ios_command="show vlan-switch")
    all_configuration_objects.append(show_vlan)
    show_cdp = ConfigCheckbox(btn_name="CDP",
                              help_text="Retrieve the ...",
                              activated=False,
                              text_divider="",
                              ios_command="show cdp")
    all_configuration_objects.append(show_cdp)
    show_ntp = ConfigCheckbox(btn_name="NTP",
                              help_text="Retrieve the ...",
                              activated=False,
                              text_divider="",
                              ios_command="show ntp status")
    all_configuration_objects.append(show_ntp)
    show_system = ConfigCheckbox(btn_name="System",
                                 help_text="Retrieve the ...",
                                 activated=False,
                                 text_divider="",
                                 ios_command="show flash")
    all_configuration_objects.append(show_system)
    show_hardware = ConfigCheckbox(btn_name="Hardware",
                                   help_text="Retrieve the ...",
                                   activated=False,
                                   text_divider="",
                                   ios_command="show clock")
    all_configuration_objects.append(show_hardware)
    show_users = ConfigCheckbox(btn_name="Users",
                                help_text="Retrieve the ...",
                                activated=False,
                                text_divider="",
                                ios_command="show users")
    all_configuration_objects.append(show_users)
    show_logging = ConfigCheckbox(btn_name="Logging",
                                  help_text="Retrieve the ...",
                                  activated=False,
                                  text_divider="",
                                  ios_command="show logging")
    all_configuration_objects.append(show_logging)
    show_tech_support = ConfigCheckbox(btn_name="Tech Support",
                                       help_text="Retrieve the ...",
                                       activated=False,
                                       text_divider="",
                                       ios_command="show tech-support")
    all_configuration_objects.append(show_tech_support)
    show_mac_table = ConfigCheckbox(btn_name="MAC Table",
                                    help_text="Retrieve the ...",
                                    activated=False,
                                    text_divider="",
                                    ios_command="show mac-address-table")
    all_configuration_objects.append(show_mac_table)
    show_arp = ConfigCheckbox(btn_name="ARP",
                              help_text="Retrieve the ...",
                              activated=False,
                              text_divider="",
                              ios_command="show arp")
    all_configuration_objects.append(show_arp)
    show_routes = ConfigCheckbox(btn_name="Routes",
                                 help_text="Retrieve the ...",
                                 activated=False,
                                 text_divider="",
                                 ios_command="show ip route")
    all_configuration_objects.append(show_routes)
    show_etherchannel = ConfigCheckbox(btn_name="Etherchannel",
                                       help_text="Retrieve the ...",
                                       activated=False,
                                       text_divider="",
                                       ios_command="")
    all_configuration_objects.append(show_etherchannel)
    show_protocols = ConfigCheckbox(btn_name="Protocols",
                                    help_text="Retrieve the ...",
                                    activated=False,
                                    text_divider="",
                                    ios_command="show ip protocols")
    all_configuration_objects.append(show_protocols)
    show_spanning_tree = ConfigCheckbox(btn_name="Spanning Tree",
                                        help_text="Retrieve the ...",
                                        activated=False,
                                        text_divider="",
                                        ios_command="show spanning-tree")
    all_configuration_objects.append(show_spanning_tree)
    show_acls = ConfigCheckbox(btn_name="ACL",
                               help_text="Retrieve the ...",
                               activated=False,
                               text_divider="",
                               ios_command="show access-lists")
    all_configuration_objects.append(show_acls)
    show_interfaces_brief = ConfigCheckbox(btn_name="Interfaces",
                                           help_text="Retrieve the ...",
                                           activated=False,
                                           text_divider="",
                                           ios_command="show ip int br")
    all_configuration_objects.append(show_interfaces_brief)
    default_conf = {
        'device_type': 'cisco_ios',
        'username': None,
        'password': None,
        'port': 22,
        # 'secret': 'secret',  # optional, defaults to ''
    }

    host_list = []

    @classmethod
    def logger_output_stream_is_file(cls):
        return cls.log_to_file
