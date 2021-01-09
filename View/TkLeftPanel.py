from tkinter import *


class TkLeftPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Left Frame and its contents

        Label(self.frame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)