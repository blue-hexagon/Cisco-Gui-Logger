import tkinter
from tkinter import *
from tkinter import ttk, messagebox
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

    def write(self, stri):
        self.text_area.insert(tkinter.INSERT, stri)


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

        self.config_hosts_input = PanedWindow(self.hosts_panel)
        self.config_hosts_input.pack(fill=tkinter.X, expand=1)

        logging_output = PanedWindow(self.logging_panel)
        logging_output.pack(fill=tkinter.BOTH, expand=1)

        self.create_config_checkboxes()
        self.add_menu()
        self.add_statusbar()
        self.create_control_buttons()

        output_textbox = scrolledtext.ScrolledText(logging_output, width=120,relief=GROOVE)
        output_textbox.grid(column=0, row=0, sticky="news")
        input_textbox = Entry(logging_output, width=120, relief=GROOVE)
        input_textbox.grid(column=0, row=1, ipady=4, sticky="news")
        # sys.stdout = StdoutRedirector(output_textbox) # TODO: Why this crashes?
        # sys.stderr = StdoutRedirector(output_textbox) # TODO: Why this crashes?

        self.create_hosts_entry_panel_content()
        self.window.mainloop()

    def create_hosts_entry_panel_content(self):
        hosts = []
        Label(self.config_hosts_input, text="IPv4/6 address list").grid(column=0, row=0)
        for i in range(0, 14):
            host = Entry(self.config_hosts_input, width=20, relief=GROOVE)
            host.grid(column=0, row=i + 1, ipady=3, pady=1, padx=3)
            btn = Button(self.config_hosts_input, text="Run", relief=GROOVE)
            btn.grid(column=1, row=i + 1, pady=1)
            if len(self.prgcfg.host_list) > 0:
                host.insert(0, self.prgcfg.host_list.pop())
            hosts.append(host)
        btn_run = Button(self.config_hosts_input, text="Run on All", relief=GROOVE, command=cisco_management.run)
        btn_run.grid(column=0, columnspan=10, row=15, ipady=1, pady=2, sticky="we")
        btn = Button(self.config_hosts_input, relief=GROOVE, text="Clear Hosts")
        btn.grid(column=0, columnspan=10, row=16, ipady=1, pady=2, sticky="we")

    def create_control_buttons(self):
        self.buttons_pane = PanedWindow(self.config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        # self.buttons_pane.columnconfigure(tuple(range(80)), weight=1)
        # self.buttons_pane.rowconfigure(tuple(range(80)), weight=1)

        btn_clear_checkboxes = Button(self.buttons_pane, text="Clear All Checkboxes",relief=GROOVE)
        btn_clear_checkboxes.grid(column=1, row=1, padx=2, sticky="news")
        btn_reset_equipment = Button(self.buttons_pane, text="Reset Equipment",relief=GROOVE)
        btn_reset_equipment.grid(column=2, row=1, padx=2, sticky="news")

    def create_config_checkboxes(self):
        self.config_checkboxes1 = PanedWindow(self.config_panel)
        self.config_checkboxes1.grid(column=0, row=0, sticky="ns")
        self.config_checkboxes2 = PanedWindow(self.config_panel)
        self.config_checkboxes2.grid(column=1, row=0, sticky="ns")

        chk_running_config = BooleanVar()
        chk_startup_config = BooleanVar()
        chk_system = BooleanVar()

        chk_dhcp = BooleanVar()
        chk_vtp = BooleanVar()
        chk_vlan = BooleanVar()
        chk_etherchannel = BooleanVar()

        chk_w_running_config = Checkbutton(self.config_checkboxes1, text="Startup Config", var=chk_startup_config)
        chk_w_startup_config = Checkbutton(self.config_checkboxes1, text="Running Config", var=chk_running_config)
        chk_w_system = Checkbutton(self.config_checkboxes1, text="System", var=chk_system)

        chk_w_dhcp = Checkbutton(self.config_checkboxes2, text="DHCP", var=chk_dhcp)
        chk_w_vtp = Checkbutton(self.config_checkboxes2, text="VTP", var=chk_vtp)
        chk_w_vlan = Checkbutton(self.config_checkboxes2, text="VLAN", var=chk_vlan)
        chk_w_etherchannel = Checkbutton(self.config_checkboxes2, text="Etherchannel", var=chk_etherchannel)

        chk_w_running_config.grid(column=0, row=0, sticky="w")
        chk_w_startup_config.grid(column=0, row=1, sticky="w")
        chk_w_system.grid(column=0, row=2, sticky="w")

        chk_w_dhcp.grid(column=0, row=0, sticky="w")
        chk_w_vtp.grid(column=0, row=1, sticky="w")
        chk_w_vlan.grid(column=0, row=2, sticky="w")
        chk_w_etherchannel.grid(column=0, row=3, sticky="w")

    def add_menu(self):
        def show_help():
            messagebox.showinfo("About", "This program was developed by Manjana\n\nhttps://github.com/blue-hexagon")

        menubar = Menu(self.window)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New")
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save as")
        file.add_separator()
        file.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file)

        help = Menu(menubar, tearoff=0)
        help.add_command(label="About", command=show_help)
        menubar.add_cascade(label="Help", menu=help)

        self.window.config(menu=menubar)

    def add_statusbar(self):
        statusbar = Label(self.statusbar_panel, text="on the way…", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=1)
