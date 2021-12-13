import picamera
from time import sleep
#setup the camera
with picamera.PiCamera() as camera:
     camera.start_recording("Video_Group1.h264")
     sleep(5)
     camera.stop_recording()
