import os
import time
while True:
  os.system("termux-wake-lock && termux-telephony-deviceinfo && termux-camera-info")
  time.sleep(60)
