import picamera
from time import sleep

with picamera.Picamera() as camera:
     camera.start_recording("Video_Group1.h264")
     sleep(5)
     camera.stop_recording()
