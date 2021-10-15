from os.path import basename

from netmiko import *
import os
import sys
import logging
from datetime import date
from datetime import datetime
from program_config import *
from zipfile import ZipFile

def run():
    prg_cfg = ProgramConfig()

    OUTPUT_DIR = './cdr_output'
    CURRENT_DATE_DIR = os.path.join(OUTPUT_DIR, date.today().strftime("%b-%d-%Y"))
    CURRENT_TIME_DIR = os.path.join(CURRENT_DATE_DIR, datetime.now().strftime("HMS_%H_%M_%S"))

    if prg_cfg.logger_output_stream_is_file():
        logging.basicConfig(filename='cdr.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    else:
        logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    try:
        os.mkdir(OUTPUT_DIR)
        logging.info(f'Created base directory for program output: {OUTPUT_DIR}')
    except FileExistsError:
        logging.info(f'Base directory for program output ({OUTPUT_DIR}) already exists. Continuing.')

    WRITE_CONFIG_TO_STARTUP = prg_cfg.WRITE_CONFIG_TO_STARTUP
    SHOW_RUNNING_CONFIG = prg_cfg.SHOW_RUNNING_CONFIG
    SHOW_DHCP = prg_cfg.SHOW_DHCP
    SHOW_VTP = prg_cfg.SHOW_VTP
    SHOW_VLAN = prg_cfg.SHOW_VLAN
    SHOW_INTERFACES_BRIEF = prg_cfg.SHOW_INTERFACES_BRIEF

    default_conf = prg_cfg.default_conf

    host_list = prg_cfg.host_list

    try:
        os.mkdir(CURRENT_DATE_DIR)
    except FileExistsError:
        logging.info("Directory already created for current day. Continuing.")
    try:
        os.mkdir(CURRENT_TIME_DIR)
    except FileExistsError:
        logging.error("Directory already exists for current time - that should not happend!")
        sys.exit(0)
    for host in range(0, len(host_list)):
        output = ''
        connection = ConnectHandler(**default_conf, host=host_list.pop())
        hostname = connection.find_prompt()[:-1]
        logging.info(f"Connected to {hostname}")
        output_filename = os.path.join(CURRENT_TIME_DIR, hostname)
        if WRITE_CONFIG_TO_STARTUP:
            print('*** Saving running-config into startup-config ***')
            connection.send_command('write')
        if SHOW_RUNNING_CONFIG:
            output += "*** Gathering Running Configuration File Data ***\n"
            output += connection.send_command('show run', use_textfsm=True)
        if SHOW_VTP:
            output += "\n\n*** VTP Configuration ***\n"
            output += connection.send_command('show vtp status')
        if SHOW_VLAN:
            output += "\n\n*** Data from flash:vlan.dat ***\n"
            output += connection.send_command('show vlan-switch')
        if SHOW_INTERFACES_BRIEF:
            output += "\n\n*** Interfaces Configuration ***\n"
            output += connection.send_command('show ipv6 int br')
        if SHOW_DHCP:
            output += "\n\n*** DHCP Configuration ***\n"
            output += connection.send_command('show ip dhcp pool')
            output += connection.send_command('show ip dhcp binding')
            output += connection.send_command('show ip dhcp server statistics')
        if len(output) > 1:
            logging.info(f'Writing output to file {hostname}')
            try:
                f = open(output_filename, 'w')
                f.write(output)
                f.close()
            except IOError:
                logging.warning(f"Failed writing output to: {output_filename}")
        else:
            logging.warning("No output returned. Did you toggle all debug flags off?")
        connection.disconnect()


    file_paths = []
    zip_dir = CURRENT_TIME_DIR
    for root, directories, files in os.walk(zip_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    for file_name in file_paths:
        print(file_name)

    with ZipFile(os.path.join(CURRENT_TIME_DIR,'files.zip'), 'w') as zip:
        for file in file_paths:
            zip.write(file,arcname=basename(file)+'.txt')
