import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
import cisco_management
from program_config import *
import sys


class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''

    def __init__(self, text_area):
        self.text_area = text_area


class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''

    def write(self, str):
        self.text_area.insert(tkinter.INSERT, str)


class TkinterInitializer():
    def __init__(self):
        self.window = Tk()
        self.window.title("Cisco Debug Collector")
        self.prgcfg = ProgramConfig()
        self.config_panel = PanedWindow()
        self.hosts_panel = PanedWindow()
        self.logging_panel = PanedWindow()
        self.statusbar_panel = PanedWindow()

        self.config_panel.grid(column=0, row=0, columnspan=80, sticky="we")
        self.hosts_panel.grid(column=0, row=1)
        self.logging_panel.grid(column=1, row=1)
        self.statusbar_panel.grid(column=0, row=10, columnspan=80, sticky="we")

        self.config_checkboxes = PanedWindow(self.config_panel)
        self.config_checkboxes.grid(column=0, row=0, columnspan=80, sticky="we")

        self.config_hosts_input = PanedWindow(self.hosts_panel)
        self.config_hosts_input.pack(fill=tkinter.X, expand=1)

        self.buttons_pane = PanedWindow(self.config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        self.buttons_pane.columnconfigure(tuple(range(80)), weight=1)
        self.buttons_pane.rowconfigure(tuple(range(80)), weight=1)

        logging_output = PanedWindow(self.logging_panel)
        logging_output.pack(fill=tkinter.BOTH, expand=1)

        self.set_cfg_checkboxes()
        self.add_menu()
        self.add_statusbar()
        btn_run = Button(self.buttons_pane, text="Run Debug Collector", command=cisco_management.run)
        btn_run.grid(column=0, row=1, sticky="news")
        btn_clear = Button(self.buttons_pane, text="Clear")
        btn_clear.grid(column=1, row=1, sticky="news")
        btn_exit = Button(self.buttons_pane, text="Exit")
        btn_exit.grid(column=2, row=1, sticky="news")
        txt = scrolledtext.ScrolledText(logging_output, height=20, width=120)
        # sys.stdout = StdoutRedirector(txt) # TODO: Why this crashes?

        txt.grid(column=0, row=2, sticky="sew")

        hosts = []
        Label(self.config_hosts_input, text="IPv4/6 address list").grid(column=0, row=0)
        for i in range(0, 14):
            host = Entry(self.config_hosts_input, width=20)
            host.grid(column=0, row=i + 1, sticky="wes")
            if len(self.prgcfg.host_list) > 0:
                host.insert(0, self.prgcfg.host_list.pop())
            hosts.append(host)
        self.window.mainloop()

    def set_cfg_checkboxes(self):
        chk_dhcp = BooleanVar()
        chk_vtp = BooleanVar()
        chk_running_config = BooleanVar()
        chk_startup_config = BooleanVar()

        chk_w_dhcp = Checkbutton(self.config_checkboxes, text="DHCP", var=chk_dhcp)
        chk_w_vtp = Checkbutton(self.config_checkboxes, text="VTP", var=chk_vtp)
        chk_w_running_config = Checkbutton(self.config_checkboxes, text="Startup Config", var=chk_startup_config)
        chk_w_startup_config = Checkbutton(self.config_checkboxes, text="Running Config", var=chk_running_config)

        chk_w_dhcp.grid(column=0, row=0)
        chk_w_vtp.grid(column=1, row=0)
        chk_w_running_config.grid(column=2, row=0)
        chk_w_startup_config.grid(column=3, row=0)

    def add_menu(self):
        menubar = Menu(self.window)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="Clear Settings")
        file.add_separator()
        file.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file)

        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")
        menubar.add_cascade(label="Help", menu=help)

        self.window.config(menu=menubar)

    def add_statusbar(self):
        statusbar = Label(self.statusbar_panel, text="on the way…", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=1)
