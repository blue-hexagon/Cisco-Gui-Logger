from distutils.dir_util import copy_tree
from os.path import basename

from netmiko import *
import os
import sys
import logging
from datetime import date
from datetime import datetime
from zipfile import ZipFile
import logging
import os
import sys

from jinja2 import *
from distutils.dir_util import copy_tree
import state_handler
from gui.component.state.checkboxes import CheckBoxes
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
                    if len(ProgramConfig.host_list[host].get()) > 1:
                        connection = ConnectHandler(**ProgramConfig.default_conf, host=ProgramConfig.host_list[host])
                        connection.send_command("erase running-config")
                        logging.warning(f"Erasing startup-config on: {host}")
            else:
                navbar = str()
                for host in range(0, len(ProgramConfig.host_list)):
                    if len(ProgramConfig.host_list[host].get()) > 1:
                        debug_files_exists = True
                        output = str()

                        connection = ConnectHandler(
                            device_type=ProgramConfig.default_conf.get("device_type"),
                            username=ProgramConfig.default_conf.get("username").get(),
                            password=ProgramConfig.default_conf.get("password").get(),
                            host=ProgramConfig.host_list[host].get()
                        )
                        hostname = connection.find_prompt()[:-1]
                        logging.info(f"Connected to {hostname}")
                        output_filename = os.path.join(current_time_dir, hostname)
                        for config_object in CheckBoxes.all_configuration_objects:
                            output += f"<h2 id='{str(config_object.btn_name).replace(' ', '-').lower()}'>{config_object.html_heading}</h2>"
                            navbar += f"<a class='btn btn-outline-secondary text-white px-3 py-1 my-1' href='#{str(config_object.btn_name).replace(' ', '-').lower()}'>{config_object.html_heading}</a>"
                            output += f"<div class='border border-light rounded'><pre><code class='language-html'>"
                            output += connection.send_command(config_object.ios_command).replace("<", "&#60").replace(
                                ">", "&#62")
                            output += "\n</code></pre></div>\n"
                        if len(output) > 1:
                            self.write_device_info_to_file(hostname, output, output_filename)
                        else:
                            logging.warning("No output returned (all checkboxes are probably unchecked)")
                        connection.disconnect()
                if debug_files_exists:
                    self.zip_files_and_render_templates(current_time_dir, navbar)
        else:
            logging.error("No hosts specified.")

    @staticmethod
    def write_device_info_to_file(hostname, output, output_filename):
        logging.info(f'Writing output to file {hostname}')
        with open(output_filename, 'w') as f:
            f.write(output)
        except IOError:
            logging.error(f"Failed writing output to: {output_filename}")

    @staticmethod
    def zip_files_and_render_templates(current_time_dir, navbar):
        file_paths = []
        zip_dir = current_time_dir

        copy_tree("web/templates/base/css", f"{current_time_dir}/css")
        copy_tree("web/templates/base/js", f"{current_time_dir}/js")

        for root, directories, files in os.walk(zip_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, 'r') as file:
                    data = file.read()
                    DeviceManager.render_template(data, navbar, filename, filepath)
                file_paths.append(filepath)
        with ZipFile(os.path.join(current_time_dir, 'files.zip'), 'w') as zip_file:
            for file in file_paths:
                logging.info(f"Adding {file} to the zip archive.")
                zip_file.write(file, arcname=basename(file) + '.txt')

    @staticmethod
    def render_template(cdc_output,navbar, hostname: str, filepath: str):
        env = Environment(loader=FileSystemLoader('web/templates/base'))
        template = env.get_template('template.html')
        output_from_parsed_template = template.render(navbar=navbar, cdc_output=cdc_output)
        with open(f"{os.path.dirname(filepath)}/{hostname.strip('-')}.html", "w+",
                  encoding="utf-8") as device_html_page:
            device_html_page.write(output_from_parsed_template)
