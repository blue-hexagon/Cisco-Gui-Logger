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
from tk_gui_element.config_panel import ConfigPanel, Checkbox
from tk_gui_element.hosts_panel import HostPanel
from tk_gui_element.menubar import Menubar


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
        self.root = Tk()
        self.root.title("Cisco Debug Collector")
        self.program_config = ProgramConfig()

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
        self.menubar = Menubar(self.root)
        self.hosts_panel = HostPanel(self.hosts_panel,self.program_config)


        self.create_control_buttons()
        output_textbox = scrolledtext.ScrolledText(self.logging_panel, width=120, relief=GROOVE)
        output_textbox.grid(column=0, row=0, sticky="news")
        input_textbox = Entry(self.logging_panel, width=120, relief=GROOVE)
        input_textbox.grid(column=0, row=1, ipady=4,pady=4, sticky="news")
        # sys.stdout = StdoutRedirector(output_textbox) # TODO: Why this crashes?
        # sys.stderr = StdoutRedirector(output_textbox) # TODO: Why this crashes?

        self.root.mainloop()



    def create_control_buttons(self):
        self.buttons_pane = PanedWindow(self.config_panel)
        self.buttons_pane.grid(column=0, row=1, columnspan=80, sticky="we")
        btn_clear_checkboxes = Button(self.buttons_pane, text="Clear All Checkboxes", relief=GROOVE,command=Checkbox.clear_checkboxes)
        btn_clear_checkboxes.grid(column=1, row=1, padx=2, sticky="news")
        # btn_reset_equipment = Button(self.buttons_pane, text="Reset Equipment", relief=GROOVE)
        # btn_reset_equipment.grid(column=2, row=1, padx=2, sticky="e")




