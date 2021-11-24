from tkinter import *

import state_handler


class HostPanel:
    def __init__(self, panel, program_config, cisco_manager, hosts_length):
        self.hosts = []
        self.string_vars = []
        for i in range(0, hosts_length):
            state_handler.ProgramConfig.host_list.append(StringVar())
            #print(i,state_handler.ProgramConfig.host_list[i],state_handler.ProgramConfig.host_list)
            host = Entry(panel, width=20, relief=GROOVE, textvariable=state_handler.ProgramConfig.host_list[i])
            host.grid(column=0, row=i + 1, ipady=3, pady=1, padx=3)
            btn = Button(panel, text="Run", relief=GROOVE, command=cisco_manager.run_single)
            btn.grid(column=1, row=i + 1, pady=1)
            # if len(program_config.host_list) > 0:
            #     host.insert(0, program_config.host_list[i].get())
            self.hosts.append(host)

        btn_run = Button(panel, text="Run on All", relief=GROOVE, command=cisco_manager.run)
        btn_run.grid(column=0, columnspan=10, row=hosts_length + 1, ipady=1, pady=2, sticky="we")
        btn = Button(panel, relief=GROOVE, text="Clear Hosts", command=self.clear_host_list)
        btn.grid(column=0, columnspan=10, row=hosts_length + 2, ipady=1, pady=2, sticky="we")

        # separator = ttk.Separator(panel, orient='vertical')
        # separator.grid(column=2,row=0,rowspan=hosts_length+1,sticky="news",padx=6)

    def clear_host_list(self):
        for i in range(0, len(self.hosts)):
            self.hosts[i].delete(0, END)

    def get_host_list(self):
        return self.hosts
    def test(self):
        print(self.string_vars[0].get())
    def update_host_entry(self):
        print("hello")
