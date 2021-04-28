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
    a_y = a[1] # when standing upright, gravity works in the y direction
    # gravity accelerates downward at ~9.81 m/s^2
    #print(a_y)
    if (a_y > 9.0 and count < max_count):
        count += 1
    if (a_y < -9.0 and count > 0):
        count -= 1
    sleep(1)
    