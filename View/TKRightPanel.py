import time
from threading import Thread
from tkinter import *

import PIL
import numpy as np
import cv2
from IPython.terminal.pt_inputhooks import tk
from PIL import ImageTk

from SignalRStuff import SignalRStuff


class TkRightPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Right Frame and its contents
        self.frameCanvas = Label(self.frame)
        self.frameCanvas.grid(row=0, column=0, padx=10, pady=2)

        self.btnFrame = Frame(self.frame, width=200, height=50, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

        # significantly simplified button creation
        self.startBtn = Button(self.frame, text="Start", command=lambda: self.on_start())
        # using pack eliminates the need to count grid spaces
        self.startBtn.grid(row=2, column=0, padx=10, pady=2)

        self.frameLog = Text(self.frame, width=50, height=50, takefocus=0)
        self.frameLog.grid(row=3, column=0, padx=10, pady=2)
        self.signalR = SignalRStuff()

        self.show_frame()
    def on_start(self):
        self.frameLog.insert(0.0, "Start information" + "\n")
        thread = Thread(target=self.signalR.start)
        thread.start()
        #thread2 = Thread(target=self.show_frame())
        #thread2.start()
        #time.sleep(5)
        #self.show_frame()


    def show_frame(self):
        self.image = self.signalR.GetCurrentImage()
        if self.image != 0:

            imgtk = ImageTk.PhotoImage(image=self.image)
            self.frameCanvas.imgtk = imgtk
            self.frameCanvas.configure(image=imgtk)
        self.frameCanvas.after(10, self.show_frame)


