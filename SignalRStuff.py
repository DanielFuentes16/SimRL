import logging
import base64
import io
import numpy as np

from PIL import Image
import cv2
from signalrcore.hub_connection_builder import HubConnectionBuilder


class SignalRStuff:
    def __init__(self):
      protocol = "https"
      host = "10.61.250.103"
      port = "44323"
      hub = "RLHub"
      server_url = f"{protocol}://{host}:{port}/{hub}"
      handler = logging.StreamHandler()
      # handler.setLevel(logging.DEBUG)
      self.currentImage = 0
      self.started = False;
      self.connection = HubConnectionBuilder() \
          .with_url(server_url, options={"verify_ssl": False}) \
          .configure_logging(logging.DEBUG, socket_trace=True, handler=handler) \
          .build()
      self.connection.on_open(lambda: self.on_connect())
      self.connection.on_close(lambda: print("connection closed"))
      self.connection.on_error(lambda data: print(f"An exception was thrown closed{data.error}"))

    def start(self):
        self.connection.start()
        while not self.started:
            pass
        self.connection.stream(
          "StreamFrameInformation",
          []).subscribe({
          "next": lambda x: self.next(x),
          "complete": lambda x: print(x),
          "error": lambda x: print(x)
        })
        message = None

        while message != "exit()":
          pass

        self.connection.stop()

    def stringToRGB(self, base64_string):
        imgdata = base64.b64decode(str(base64_string))
        image = Image.open(io.BytesIO(imgdata))
        return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    def on_connect(self):

        self.started = True
        print("connection opened and handshake received ready to send messages")

    def next(self, x):
        #print(x["frame"])
        image = self.stringToRGB(x["frame"])
        # reading image
        # image = cv2.imread("Path of image here")
        #Image.fromarray(image)
        self.currentImage = Image.fromarray(image)

    def GetCurrentImage(self):
        return self.currentImage

