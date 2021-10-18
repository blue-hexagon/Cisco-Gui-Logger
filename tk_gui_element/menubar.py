from tkinter import messagebox, Menu


class Menubar():
    def __init__(self,root):
        def show_help():
            messagebox.showinfo("About", "This program was developed by Manjana\n\nhttps://github.com/blue-hexagon")

        menubar = Menu(root)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New")
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save as")
        file.add_separator()
        file.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file)

        help = Menu(menubar, tearoff=0)
        help.add_command(label="About", command=show_help)
        menubar.add_cascade(label="Help", menu=help)

        root.config(menu=menubar)