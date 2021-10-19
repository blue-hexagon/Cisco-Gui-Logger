from tkinter import messagebox, Menu


class Menubar:
    def __init__(self, root):
        def show_help():
            messagebox.showinfo("About", "This program was developed by Manjana\n\nhttps://github.com/blue-hexagon")

        menubar = Menu(root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=show_help)
        menubar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=menubar)
