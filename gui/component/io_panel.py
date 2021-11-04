import tkinter
from tkinter import *
from tkinter import scrolledtext
import sys


class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll

    def flush(self):
        pass


class IOPanel:
    def __init__(self, logging_panel):
        output_textbox = scrolledtext.ScrolledText(logging_panel, width=120, relief=GROOVE)
        output_textbox.grid(column=0, row=0, sticky="news")
        input_textbox = Entry(logging_panel, width=120, relief=GROOVE)
        input_textbox.grid(column=0, row=1, ipady=4, pady=4, sticky="news")
        sys.stdout = Redirect(output_textbox)  # TODO: Why this crashes?

        # sys.stderr = StdoutRedirector(output_textbox) # TODO: Why this crashes?
