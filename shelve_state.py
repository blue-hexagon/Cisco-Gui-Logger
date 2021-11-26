import logging
import shelve
import state_handler
from gui.component.state.checkboxes import CheckBoxes
hosts = []
FILENAME = "state.dat"
FILENAME_VAR = FILENAME[:-4]


def init_shelve():
    d = shelve.open(FILENAME, writeback=True)
    logging.info("Initializing shelve for hosts, selected checkboxes and credentials")
    for i in (0, state_handler.ProgramConfig.host_list-1):
        d["host" + str(i)] = hosts[i]
    for i in (0, len(CheckBoxes.all_configuration_objects)):  # state_handler.ConfigCheckbox):
        d["checkbox_state" + str(i)] = CheckBoxes.all_configuration_objects[i]
    d["username"] = state_handler.ProgramConfig.default_conf.get("username")
    d["password"] = state_handler.ProgramConfig.default_conf.get("password")

    d.close()
    load_all_hosts()


def load_all_hosts():
    d = shelve.open(FILENAME)
    hosts.clear()
    for i in range(0, 5):
        try:
            hosts.append(d["host" + str(i)])
        except KeyError:
            logging.error(f"KeyError - failed to get host: host{str(i)}")
    try:
        state_handler.ProgramConfig.default_conf["username"] = d["username"]
        state_handler.ProgramConfig.default_conf["password"] = d["password"]
    except KeyError:
        logging.error(f"KeyError - failed to get username")
        logging.error(f"KeyError - failed to get password")
    d.close()


def update_single_host(id,host_address):
    with shelve.open(FILENAME, writeback=True) as d:
        d[f'host{str(id)}'] = host_address


def update_all_hosts():
    for idx in enumerate(hosts):
        with shelve.open(FILENAME, writeback=True) as d:
            d[str(idx[0])][1] = host_address
        hosts[idx[0]][1] = host_address
        load_all_hosts()
        break
