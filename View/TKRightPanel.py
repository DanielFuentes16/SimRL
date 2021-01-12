import time
from threading import Thread
from tkinter import *

import PIL
import numpy as np
import cv2
from IPython.terminal.pt_inputhooks import tk
from PIL import ImageTk
from PIL import Image

from SignalRStuff import SignalRStuff


class TkRightPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Right Frame and its contents
        im = Image.new('RGB', (60, 30), color = 'red')
        im.save('pil_red.png')
        self.image = ImageTk.PhotoImage(im)

        self.frameCanvas = Label(self.frame, image = self.image)
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
            self.frameLog.delete('1.0', END)
            imgtk = ImageTk.PhotoImage(image=self.image)
            #self.frameCanvas.imgtk = imgtk
            self.frameCanvas.configure(image=imgtk)
            self.frameCanvas.image = imgtk
            #self.frameCanvas.configure(image=imgtk)
            self.frameLog.insert(0.0, self.signalR.currentId+"\n")
            self.frameLog.insert(0.0, self.signalR.currentModel+"\n")
            count = 0
            for position in self.signalR.currentPositions:
                count += 1
                self.frameLog.insert(0.0, str(position)+"\n")

            self.frameLog.insert(0.0, self.signalR.currentId+"\n")

        self.frameCanvas.after(50, self.show_frame)


