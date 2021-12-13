import picamera

print ("Ready Guys.")
with picamera.PiCamera() as Camera:
     camera.start_preview()
     camera.resolution = (1280, 720)
     camera.capture("/home/pi/Desktop/project/")
     camera.stop_preview()
     print("Take picture Olready")
