import time

from lsm6ds3 import LSM6DS3

lsm = LSM6DS3()

while True:
    ax, ay, az, gx, gy, gz = lsm.get_readings()
    print("Accelerometer\nX:{}, Y:{}, Z:{}\nGyro\nX:{}, Y:{}, Z{}\n\n ".format(ax, ay, az, gx, gy, gz))
    time.sleep(1.0)
