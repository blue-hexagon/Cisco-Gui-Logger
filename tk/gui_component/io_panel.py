import tkinter
from tkinter import *
from tkinter import scrolledtext

class IORedirector(object):
    # A general class for redirecting I/O to this Text widget.

    def __init__(self, text_area):
        self.text_area = text_area


class StdoutRedirector(IORedirector):
    # A class for redirecting stdout to this Text widget.

    def write(self, string):
        self.text_area.insert(tkinter.INSERT, string)

class IOPanel:
    def __init__(self, logging_panel):
        output_textbox = scrolledtext.ScrolledText(logging_panel, width=120, relief=GROOVE)
        output_textbox.grid(column=0, row=0, sticky="news")
        input_textbox = Entry(logging_panel, width=120, relief=GROOVE)
        input_textbox.grid(column=0, row=1, ipady=4, pady=4, sticky="news")
        # sys.stdout = StdoutRedirector(output_textbox) # TODO: Why this crashes?
        # sys.stderr = StdoutRedirector(output_textbox) # TODO: Why this crashes?
