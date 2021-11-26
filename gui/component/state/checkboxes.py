from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=False)
class ConfigCheckbox:
    btn_name: str
    help_text: str
    activated: bool
    html_heading: [Optional[str]]
    ios_command: str


class CheckBoxes:
    all_configuration_objects = []

    show_interfaces_brief = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Interfaces",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Interfaces List",
            ios_command="show ip int br"))

    show_acls = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="ACL",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Access Control List",
            ios_command="show access-lists"))

    show_spanning_tree = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Spanning Tree",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Spanning Tree",
            ios_command="show spanning-tree"))

    show_protocols = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Protocols",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="IP Protocols",
            ios_command="show ip protocols"))

    show_etherchannel = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Etherchannel",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Etherchannel",
            ios_command=""))

    show_routes = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Routes",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="IP Routes",
            ios_command="show ip route"))

    show_arp = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="ARP",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="ARP",
            ios_command="show arp"))

    show_mac_table = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="MAC Table",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="MAC Table",
            ios_command="show mac-address-table"))

    show_tech_support = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Tech Support",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Tech Support Debugging Information",
            ios_command="show tech-support"))

    show_logging = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Logging",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Cisco Logging",
            ios_command="show logging"))

    show_users = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Users",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Users",
            ios_command="show users"))

    show_hardware = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Hardware",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="Hardware",
            ios_command="show clock"))

    show_system = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="System",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="System",
            ios_command="show flash"))

    show_ntp = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="NTP",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="NTP",
            ios_command="show ntp status"))

    show_cdp = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="CDP",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="CDP (Cisco Discovery Protocol)",
            ios_command="show cdp"))

    show_vlan = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="VLAN",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="VLANs",
            ios_command="show vlan-switch"))

    show_vtp = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="VTP",
            help_text="Retrieve the ...",
            activated=False,
            html_heading="VTP (Virtual Trunking Protocol)",
            ios_command="show vtp status"))

    show_dhcp = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="DHCP",
            help_text="Retrieve the DHCP...",
            activated=False,
            html_heading="DHCP Server",
            ios_command="show dhcp server"))

    show_startup_config = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Startup Configuration",
            help_text="Retrieve the startup configuration",
            activated=False,
            html_heading="Startup Configuration",
            ios_command="show start"))

    show_running_config = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Running Configuration",
            help_text="Retrieve the running configuration",
            activated=True,
            html_heading="Running Configuration",
            ios_command='show run'))

    write_config_to_startup = all_configuration_objects.append(
        ConfigCheckbox(
            btn_name="Copy run start",
            help_text="Copy the running configuration into the startup configuration",
            activated=False,
            html_heading=None,  # Doesn't render text to the output
            ios_command="write"))
