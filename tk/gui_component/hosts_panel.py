from tkinter import *



class HostPanel():
    def __init__(self, panel, program_config,cisco_manager):
        self.hosts = []
        length = 13
        for i in range(0, length):
            host = Entry(panel, width=20, relief=GROOVE)
            host.grid(column=0, row=i + 1, ipady=3, pady=1, padx=3)
            btn = Button(panel, text="Run", relief=GROOVE)
            btn.grid(column=1, row=i + 1, pady=1)
            if len(program_config.host_list) > 0:
                host.insert(0, program_config.host_list.pop())
            self.hosts.append(host)
        btn_run = Button(panel, text="Run on All", relief=GROOVE, command=cisco_manager.run)
        btn_run.grid(column=0, columnspan=10, row=length + 1, ipady=1, pady=2, sticky="we")
        btn = Button(panel, relief=GROOVE, text="Clear Hosts", command=self.clear_host_list)
        btn.grid(column=0, columnspan=10, row=length + 2, ipady=1, pady=2, sticky="we")

    def clear_host_list(self):
        for i in range(0, len(self.hosts)):
            self.hosts[i].delete(0, END)

    def get_host_list(self):
        return self.hosts
