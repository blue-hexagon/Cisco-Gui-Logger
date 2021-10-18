import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from tkinter import Menu
import cisco_management
import tk_gui_element
from program_config import *
import sys

from tk_gui_element.statusbar import Statusbar
from tk_gui_element.config_panel import ConfigPanel


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

        self.config_panel = LabelFrame(text="", padx=4, pady=4)
        self.hosts_panel = LabelFrame(text="IPv4/6 Hosts", padx=4, pady=4)
        self.logging_panel = LabelFrame(text="IO Direction", padx=4, pady=4)
        self.statusbar_panel = PanedWindow()

        self.config_panel.grid(column=0, row=0, columnspan=80, sticky="we", padx=4, pady=4)
        self.hosts_panel.grid(column=0, row=1, padx=4, pady=4)
        self.logging_panel.grid(column=1, row=1, padx=4, pady=4, sticky="news")
        self.statusbar_panel.grid(column=0, row=10, columnspan=80, sticky="we")
        self.statusbar = Statusbar(self.statusbar_panel)
        self.configuration_panel = ConfigPanel(self.config_panel,self.statusbar)
        self.add_menu()

        self.create_control_buttons()

        output_textbox = scrolledtext.ScrolledText(self.logging_panel, width=120, relief=GROOVE)
        output_textbox.grid(column=0, row=0, sticky="news")
        input_textbox = Entry(self.logging_panel, width=120, relief=GROOVE)
        input_textbox.grid(column=0, row=1, ipady=4, sticky="we")
        # sys.stdout = StdoutRedirector(output_textbox) # TODO: Why this crashes?
        # sys.stderr = StdoutRedirector(output_textbox) # TODO: Why this crashes?

        self.create_hosts_entry_panel_content()
        self.window.mainloop()

    def create_hosts_entry_panel_content(self):
        hosts = []
        length = 13
        for i in range(0, length):
            host = Entry(self.hosts_panel, width=20, relief=GROOVE)
            host.grid(column=0, row=i + 1, ipady=3, pady=1, padx=3)
            btn = Button(self.hosts_panel, text="Run", relief=GROOVE)
            btn.grid(column=1, row=i + 1, pady=1)
            if len(self.prgcfg.host_list) > 0:
                host.insert(0, self.prgcfg.host_list.pop())
            hosts.append(host)
        btn_run = Button(self.hosts_panel, text="Run on All", relief=GROOVE, command=cisco_management.run)
        btn_run.grid(column=0, columnspan=10, row=length + 1, ipady=1, pady=2, sticky="we")
        btn = Button(self.hosts_panel, relief=GROOVE, text="Clear Hosts")
        btn.grid(column=0, columnspan=10, row=length + 2, ipady=1, pady=2, sticky="we")

    def create_control_buttons(self):
        self.buttons_pane = PanedWindow(self.config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        # self.buttons_pane.columnconfigure(tuple(range(80)), weight=1)
        # self.buttons_pane.rowconfigure(tuple(range(80)), weight=1)

        btn_clear_checkboxes = Button(self.buttons_pane, text="Clear All Checkboxes", relief=GROOVE)
        btn_clear_checkboxes.grid(column=1, row=1, padx=2, sticky="news")
        btn_reset_equipment = Button(self.buttons_pane, text="Reset Equipment", relief=GROOVE)
        btn_reset_equipment.grid(column=2, row=1, padx=2, sticky="e")

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


