import picamera

print ("Ready Guys.")
with picamera.PiCamera() as camera:
     camera.start_preview()
     camera.resolution = (1280, 720)
     camera.capture("/home/pi/Desktop/group-1")
     camera.stop_preview()
     print("Take picture Olready")
