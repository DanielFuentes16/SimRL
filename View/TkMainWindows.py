from tkinter import Tk, Frame

from View.TKRightPanel import TkRightPanel
from View.TkLeftPanel import TkLeftPanel


class TkMainWindow:

    def __init__(self):
        self.root = Tk()  # Makes the window
        self.root.wm_title("RL Viper")  # Makes the title that will appear in the top left
        self.root.config(background="#FFFFFF")

        self.leftFrame = Frame(self.root, width=500, height=300)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)

        self.rightFrame = Frame(self.root, width=500, height=300)
        self.rightFrame.grid(row=0, column=1, padx=10, pady=2)

        self.leftPanel = TkLeftPanel(self.root, self.leftFrame)
        self.rightPanel = TkRightPanel(self.root, self.rightFrame)

    def start(self):
        self.root.mainloop()  # start monitoring and updating the GUI
