from os.path import basename

from netmiko import *
import os
import sys
import logging
from datetime import date
from datetime import datetime
from zipfile import ZipFile

from cisco_manager.program_config import ProgramConfig


class DeviceManager:
    def __init__(self):

        self.output_base_dir = '../cdr_output'
        if ProgramConfig.logger_output_stream_is_file():
            logging.basicConfig(filename='../cdr.log', format='%(asctime)s/%(levelname)s/%(message)s', level=logging.INFO)
        else:
            logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    def run(self):
        current_date_dir = os.path.join(self.output_base_dir, date.today().strftime("%b-%d-%Y"))
        current_time_dir = os.path.join(current_date_dir, datetime.now().strftime("HMS_%H_%M_%S"))

        try:
            os.mkdir(self.output_base_dir)
            logging.info(f'Created base directory for program output: {self.output_base_dir}')
        except FileExistsError:
            logging.info(f'Base directory for program output ({self.output_base_dir}) already exists. Continuing.')

        try:
            os.mkdir(current_date_dir)
        except FileExistsError:
            logging.info("Directory already created for current day. Continuing.")
        try:
            os.mkdir(current_time_dir)
        except FileExistsError:
            logging.error("Directories already exists for current date and time - error!")
            sys.exit(0)
        if ProgramConfig.erase_equipment:
            for host in range(0, len(ProgramConfig.host_list)):
                # TODO
                connection = ConnectHandler(**ProgramConfig.default_conf, host=ProgramConfig.host_list.pop())
                connection.send_command("erase running-config")
                # TODO
        else:
            for host in range(0, len(ProgramConfig.host_list)):
                output = ''
                connection = ConnectHandler(**ProgramConfig.default_conf, host=ProgramConfig.host_list.pop())
                hostname = connection.find_prompt()[:-1]
                logging.info(f"Connected to {hostname}")
                output_filename = os.path.join(current_time_dir, hostname)
                if ProgramConfig.write_config_to_startup:
                    logging.info('Saving running-config into startup-config')
                    connection.send_command('write')
                if ProgramConfig.show_running_config:
                    output += "*** Gathering Running Configuration File Data ***\n"
                    output += connection.send_command('show run', use_textfsm=True)
                if ProgramConfig.show_vtp:
                    output += "\n\n*** VTP Configuration ***\n"
                    output += connection.send_command('show vtp status')
                if ProgramConfig.show_vlan:
                    output += "\n\n*** Data from flash:vlan.dat ***\n"
                    output += connection.send_command('show vlan-switch')
                if ProgramConfig.show_interfaces_brief:
                    output += "\n\n*** Interfaces Configuration ***\n"
                    output += connection.send_command('show ipv6 int br')
                if ProgramConfig.show_dhcp:
                    output += "\n\n*** DHCP Configuration ***\n"
                    output += connection.send_command('show ip dhcp pool')
                    output += connection.send_command('show ip dhcp binding')
                    output += connection.send_command('show ip dhcp server statistics')
                if len(output) > 1:
                    self.write_device_info_to_file(hostname, output, output_filename)
                else:
                    logging.warning("No output returned. Did you toggle all debug flags off?")
                connection.disconnect()

            self.zip_files(current_time_dir)

    @staticmethod
    def write_device_info_to_file(hostname, output, output_filename):
        logging.info(f'Writing output to file {hostname}')
        try:
            f = open(output_filename, 'w')
            f.write(output)
            f.close()
        except IOError:
            logging.warning(f"Failed writing output to: {output_filename}")

    @staticmethod
    def zip_files(current_time_dir):
        file_paths = []
        zip_dir = current_time_dir
        for root, directories, files in os.walk(zip_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        for file_name in file_paths:
            print(file_name)
        with ZipFile(os.path.join(current_time_dir, 'files.zip'), 'w') as zip_file:
            for file in file_paths:
                zip_file.write(file, arcname=basename(file) + '.txt')
