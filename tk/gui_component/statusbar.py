import logging
import tkinter
from tkinter import *


class Statusbar:
    def __init__(self, statusbar_panel):
        # self.statusvar = StringVar()
        self.statusbar = Label(statusbar_panel, text="", bd=1,
                               relief=tkinter.SUNKEN, anchor=tkinter.W)
        self.statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=1)

    def set_statusbar_text(self, event, text):
        logging.info(f"{event}")
        self.statusbar.configure(text=text)

    def clear_statusbar(self, event):
        logging.info(f"{event}")
        self.statusbar.configure(text="")
