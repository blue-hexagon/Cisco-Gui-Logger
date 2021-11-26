from dataclasses import dataclass
from typing import Optional

class ProgramConfig:
    HOSTS_AMOUNT = 13
    host_list = []
    log_to_file = False  # Toggle flag: logs to stdout if not to file.
    erase_equipment = False  # TODO : Make the user type in a diceware password or something

    default_conf = {
        'device_type': 'cisco_ios',
        'username': None,
        'password': None,
        'port': 22,
        # 'secret': 'secret',  # optional, defaults to ''
    }

    @classmethod
    def logger_output_stream_is_file(cls):
        return cls.log_to_file
