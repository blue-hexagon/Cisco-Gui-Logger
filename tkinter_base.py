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

        self.config_checkboxes1 = PanedWindow(self.config_panel)
        self.config_checkboxes1.grid(column=0, row=0, sticky="nw")
        self.config_checkboxes2 = PanedWindow(self.config_panel)
        self.config_checkboxes2.grid(column=1, row=0, sticky="nw")
        self.config_checkboxes3 = PanedWindow(self.config_panel)
        self.config_checkboxes3.grid(column=2, row=0, sticky="nw")

        self.config_hosts_input = PanedWindow(self.hosts_panel)
        self.config_hosts_input.pack(fill=tkinter.X, expand=1)

        self.buttons_pane = PanedWindow(self.config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        # self.buttons_pane.columnconfigure(tuple(range(80)), weight=1)
        # self.buttons_pane.rowconfigure(tuple(range(80)), weight=1)

        logging_output = PanedWindow(self.logging_panel)
        logging_output.pack(fill=tkinter.BOTH, expand=1)

        self.set_cfg_checkboxes()
        self.add_menu()
        self.add_statusbar()
        btn_run = Button(self.buttons_pane, text="Run Debug Collector", command=cisco_management.run,width=18)
        btn_run.grid(column=0, row=1, sticky="w")
        btn_clear = Button(self.buttons_pane, text="Clear",width=18)
        btn_clear.grid(column=1, row=1, sticky="w")
        btn_exit = Button(self.buttons_pane, text="Nuke This Sh!t",width=18)
        btn_exit.grid(column=2, row=1, sticky="e")
        btn_exit = Button(self.buttons_pane, text="Exit",width=18)
        btn_exit.grid(column=3, row=1, sticky="e")
        txt = scrolledtext.ScrolledText(logging_output, height=20, width=120)
        # sys.stdout = StdoutRedirector(txt) # TODO: Why this crashes?

        txt.grid(column=0, row=2, sticky="sew")

        hosts = []
        Label(self.config_hosts_input, text="IPv4/6 Host List").grid(column=0, row=0)
        for i in range(0, 14):
            host = Entry(self.config_hosts_input, width=20,relief=GROOVE)
            host.grid(column=0, row=i + 1, sticky="wes")
            if len(self.prgcfg.host_list) > 0:
                host.insert(0, self.prgcfg.host_list.pop())
            hosts.append(host)
            btn_apply_to_this_ip = Button(self.config_hosts_input, text="Run Cfg",relief=GROOVE)
            btn_apply_to_this_ip.grid(column=1, row=i+1, sticky="w")
        self.window.mainloop()

    def set_cfg_checkboxes(self):
        chk_running_config = BooleanVar()
        chk_startup_config = BooleanVar()
        chk_dhcp = BooleanVar()
        chk_vtp = BooleanVar()
        chk_vlan = BooleanVar()


        chk_w_running_config = Checkbutton(self.config_checkboxes1, text="Startup Config", var=chk_startup_config)
        chk_w_startup_config = Checkbutton(self.config_checkboxes1, text="Running Config", var=chk_running_config)

        chk_w_dhcp = Checkbutton(self.config_checkboxes2, text="DHCP", var=chk_dhcp)
        chk_w_vtp = Checkbutton(self.config_checkboxes2, text="VTP", var=chk_vtp)
        chk_w_vlan = Checkbutton(self.config_checkboxes2, text="VLAN", var=chk_vlan)

        chk_w_running_config.grid(column=0, row=0, sticky="nw")
        chk_w_startup_config.grid(column=0, row=1, sticky="nw")
        chk_w_dhcp.grid(column=0, row=0, sticky="nw")
        chk_w_vtp.grid(column=0, row=1, sticky="nw")
        chk_w_vlan.grid(column=0, row=2, sticky="nw")


    def add_menu(self):
        def about_messagebox():
            messagebox.showinfo('About', 'Developed by @Manjana\nGithub: Blue-Hexagon')
        menubar = Menu(self.window)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="Clear Settings")
        file.add_separator()
        file.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file)

        help = Menu(menubar, tearoff=0)
        help.add_command(label="About",command=about_messagebox)
        menubar.add_cascade(label="Help", menu=help)

        self.window.config(menu=menubar)



    def add_statusbar(self):
        statusbar = Label(self.statusbar_panel, text="on the way…", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=1)
