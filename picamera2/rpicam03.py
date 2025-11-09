from picamera2 import Picamera2, Preview

import time
import datetime

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
now = datetime.datetime.now()
picam2.capture_file('%s.jpg'% now)
