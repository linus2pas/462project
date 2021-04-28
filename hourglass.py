import board
import busio
import adafruit_mpu6050
import time
from rpi_ws281x import *

# LED strip config:
LED_COUNT      = 85      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 25     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# MPU config
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

def strand_off(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def upright(n):
    
    def show_sand():
        for s in range(0, LED_COUNT):
            #print(s)
            if sand[s] == 1:
                strip.setPixelColor(s,Color(255,255,255))
            elif sand[s] == 0:
                strip.setPixelColor(s,Color(0,0,0))
        strip.show()
        time.sleep(0.1)

    # if n == 14 # steady state?

    if n == 13:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,1,1,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,1,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,1,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            ]
        show_sand()     
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,1,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,1,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,
            ]
        show_sand()
        time.sleep(0.5)
        
    elif n == 12:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,1,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,0,0,
            ]
        show_sand()
        time.sleep(0.5)
        
    elif n == 11:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,1,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,0,0,0,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 10:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,1,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,1,0,0,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 9:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                1,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,0,0,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 8:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,1,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,0,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,0,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 7:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,1,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,1,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,0,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 6:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,1,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,0,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 5:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 1,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,1,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        time.sleep(0.5)

    elif n == 4:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,1,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,0,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,0,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        time.sleep(0.5) 

    elif n == 3:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  1,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,1,0,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,0,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,0,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        time.sleep(0.5) 

    elif n == 2:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,1,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    1,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,1,1,0,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,1,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        time.sleep(0.5) 

    elif n == 1:
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    1,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,1,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    0,
                  0,1,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,1,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    0,
                  0,0,0,
                 0,0,0,0,
                0,0,1,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,0,1,1,1,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    0,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,1,0,0,0,
             0,0,0,1,1,1,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,
               0,0,0,0,0,0,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    0,
                  0,0,0,
                 0,0,0,0,
                0,0,0,0,0,
               0,0,0,0,0,0,
              0,0,0,0,0,0,0,
             0,0,1,1,1,1,0,0,
            1,1,1,1,1,1,1,1,1,
            ]
        show_sand()
# 
#     elif n == 0:
        
    
try:
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    
    max_count = 13 + 1 # grains of "sand" + end state
    count = max_count - 1
    
    for i in range(13):
        upright(count)
        count -= 1
    time.sleep(5)
    strand_off(strip)
        
except KeyboardInterrupt:
    strand_off(strip)