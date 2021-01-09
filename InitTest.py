import logging
import sys
import os
import base64
import io
import numpy as np
from array import array
import PIL.Image as Image
import matplotlib.pyplot as plt
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
from PIL import Image
import cv2
import time
from matplotlib import animation
from signalrcore.hub_connection_builder import HubConnectionBuilder
from signalrcore.protocol.messagepack_protocol import MessagePackHubProtocol

# Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
def print_message(x):
    print (x[1]["frame"])

    s =x[1]["frame"]
    image = stringToRGB(s)
    # reading image
    #image = cv2.imread("Path of image here")
    img = Image.fromarray(image)
    img.show()

started = False
def input_with_default(input_text, default_value):
    value = input(input_text.format(default_value))
    return default_value if value is None or value.strip() == "" else value
def Start():
    global started
    started = True
    print("connection opened and handshake received ready to send messages")

currentImage = 0
def next(x):
    #print(x["frame"])
    image = stringToRGB(x["frame"])
    # reading image
    # image = cv2.imread("Path of image here")
    global currentImage
    currentImage = Image.fromarray(image)

protocol = "https"
host = "10.61.250.103"
port = "44323"
hub = "RLHub"
server_url = f"{protocol}://{host}:{port}/{hub}"

handler = logging.StreamHandler()
#handler.setLevel(logging.DEBUG)
connection = HubConnectionBuilder() \
    .with_url(server_url, options={"verify_ssl": False}) \
    .configure_logging(logging.DEBUG, socket_trace=True, handler=handler) \
    .build()


#connection.on_open(lambda: Start)
connection.on_open(lambda: Start())
connection.on_close(lambda: print("connection closed"))
connection.on_error(lambda data: print(f"An exception was thrown closed{data.error}"))
connection.start()
while not started:
    pass
connection.stream(
    "StreamFrameInformation",
    []).subscribe({
        "next": lambda x: next(x),
        "complete": lambda x: print(x),
        "error": lambda x: print(x)
    })

def GetCurrentImage():
    return currentImage

message = None


while message != "exit()":
    i = 0

connection.stop()

sys.exit(0)


