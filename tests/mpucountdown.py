import board
import busio
import adafruit_mpu6050
from time import sleep, perf_counter

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
max_count = 13
count = max_count

while True:
    print(count)
    a = mpu.acceleration
    a_y = a[1] # upright: gravity in y direction (~9.81m/s^2)
    a_x = a[0] # horizontal acceleration
    #print(a_y)
    #print(a_x)
    if (a_y > 6.0 and count < max_count):
        if (a_x > 3.0):
            print("tilt right")
        elif (a_x < -3.0):
            print("tilt left")
        else:
            print("centered")
        count += 1
    elif (a_y < -6.0 and count > 0):
        if (a_x > 3.0):
            print("tilt right")
        elif (a_x < -3.0):
            print("tilt left")
        else:
            print("centered")
        count -= 1
    else:
        if (a_x > 3.0):
            print("tilt right")
        elif (a_x < -3.0):
            print("tilt left")
        else:
            print("centered")
    sleep(1)
    