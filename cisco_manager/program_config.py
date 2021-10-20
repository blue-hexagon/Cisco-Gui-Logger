class ProgramConfig:
    log_to_file = False  # Toggle flag - logs to stdout if not to file.
    write_config_to_startup = False
    show_running_config = True
    show_startup_config = True
    show_dhcp = False
    show_vtp = False
    show_vlan = False
    show_cdp = False
    show_ntp = True
    show_system = True
    show_hardware = False
    show_users = False
    show_logging = False
    show_tech_support = False
    show_mac_table = False
    show_arp = False
    show_routes = False
    show_etherchannel = False
    show_protocols = False
    show_spanning_tree = False
    show_acls = False
    show_interfaces_brief = False
    erase_equipment = False  # TODO : Make the user type in a diceware password or something...

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
