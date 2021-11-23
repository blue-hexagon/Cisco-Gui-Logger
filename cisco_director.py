from os.path import basename

from netmiko import *
import os
import sys
import logging
from datetime import date
from datetime import datetime
from zipfile import ZipFile

from state_handler import ProgramConfig


class DeviceManager:
    def __init__(self):
        self.output_base_dir = 'cdr_output'
        self.current_date_dir = os.path.join(self.output_base_dir, date.today().strftime("%b-%d-%Y"))

        if ProgramConfig.logger_output_stream_is_file():
            logging.basicConfig(filename='cdr.log', format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.INFO)
        else:
            logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.INFO)

        try:
            os.mkdir(self.output_base_dir)
            logging.info(f'Created base directory for program output: {self.output_base_dir}')
        except FileExistsError:
            logging.info(f'Base directory for program output ({self.output_base_dir}) already created - continuing.')

        try:
            os.mkdir(self.current_date_dir)
        except FileExistsError:
            logging.info("Directory already created for current day - continuing.")

    def run_single(self):
        for host in ProgramConfig.host_list:
            print(host.get())

    def run(self):
        current_time_dir = os.path.join(self.current_date_dir, datetime.now().strftime("HMS_%H_%M_%S"))
        debug_files_exists = False
        try:
            os.mkdir(current_time_dir)
        except FileExistsError:
            logging.error("Directories already exists for current date and time - this should not happen!")
            sys.exit(0)
        if len(ProgramConfig.host_list) > 0:
            if ProgramConfig.erase_equipment:
                for host in range(0, len(ProgramConfig.host_list)):
                    # TODO
                    connection = ConnectHandler(**ProgramConfig.default_conf, host=ProgramConfig.host_list[host])
                    connection.send_command("erase running-config")
                    # TODO
            else:
                for host in range(0, len(ProgramConfig.host_list)):
                    if len(ProgramConfig.host_list[host].get()) > 1:
                        debug_files_exists = True
                        output = ''
                        connection = ConnectHandler(
                            **ProgramConfig.default_conf,
                            host=ProgramConfig.host_list[host].get()
                        )
                        hostname = connection.find_prompt()[:-1]
                        logging.info(f"Connected to {hostname}")
                        output_filename = os.path.join(current_time_dir, hostname)
                        for config_object in ProgramConfig.all_configuration_objects:
                            output += str(config_object.text_divider)
                            output += connection.send_command(config_object.ios_command)
                        if len(output) > 1:
                            self.write_device_info_to_file(hostname, output, output_filename)
                        else:
                            logging.warning("No output returned. Did you toggle all debug flags off?")
                        connection.disconnect()
                if debug_files_exists:
                    self.zip_files(current_time_dir)
        else:
            logging.error("No hosts specified.")

    @staticmethod
    def write_device_info_to_file(hostname, output, output_filename):
        logging.info(f'Writing output to file {hostname}')
        try:
            f = open(output_filename, 'w')
            f.write(output)
            f.close()
        except IOError:
            logging.error(f"Failed writing output to: {output_filename}")

    @staticmethod
    def zip_files(current_time_dir):
        file_paths = []
        zip_dir = current_time_dir
        for root, directories, files in os.walk(zip_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        with ZipFile(os.path.join(current_time_dir, 'files.zip'), 'w') as zip_file:
            for file in file_paths:
                logging.info(f"Adding {file} to the zip archive.")
                zip_file.write(file, arcname=basename(file) + '.txt')
