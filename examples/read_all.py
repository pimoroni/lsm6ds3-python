import time

from lsm6ds3 import LSM6DS3

lsm = LSM6DS3()

while True:
    ax, ay, az, gx, gy, gz = lsm.get_readings()
    print(f"Accelerometer\nX:{ax}, Y:{ay}, Z:{az}\nGyro\nX:{gx}, Y:{gy}, Z{gz}\n\n ")
    time.sleep(1.0)
