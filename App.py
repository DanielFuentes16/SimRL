import cv2
from PIL import Image
from threading import Thread
from time import sleep

import time
from SignalRStuff import SignalRStuff
import tkinter
from View.TkMainWindows import *

def show_webcam(signalR):

    while True:

        img = signalR.GetCurrentImage()

        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    myWindow = TkMainWindow()
    myWindow.start()

    #signalR = SignalRStuff()
    #thread2 = Thread(target=signalR.start)
    #thread2.start()
    ##thread = Thread(target= show_webcam, args=(signalR,))
    ##thread.start()
    #show_webcam(signalR)





if __name__ == '__main__':
    main()

