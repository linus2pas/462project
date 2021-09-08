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

def wheel(pos): # borrowed from rpi_ws281x package test
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def strand_off(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def countup(n):
    countdown(14 - n, False)

def countdown(n, isUpright=True):
    def show_sand():
        if isUpright == False: sand.reverse()
        for s in range(0, LED_COUNT):
            #print(s)
            if sand[s]== 1:
                strip.setPixelColor(s,wheel(s+63))
            elif sand[s] == 0:
                strip.setPixelColor(s,Color(0,0,0))
        strip.show()
        time.sleep(0.1)

    if n == 14:
        sand = [
            1,1,1,1,1,1,1,1,1,
             0,0,1,1,1,1,0,0,
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
             0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            ]
        show_sand()
        sand = [
            0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,
              1,1,1,1,1,1,1,
               1,1,1,1,1,1,
                0,0,0,0,0,
                 0,0,0,0,
                  0,0,0,
                    0,
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
        time.sleep(0.7)

    elif n == 13:
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

    elif n == 0: # equilibrium state
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
        
    
try:
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    
    max_count = 13 + 1 # grains of "sand" + 1 for end state
    count = max_count - 1
    
#     count+=1
#     for i in range(14):
#         countdown(count)
#         count -= 1
#     time.sleep(3)
#     for i in range(14):
#         countup(count)
#         count += 1
#     time.sleep(3)
#     strand_off(strip)

    while True:
        a = mpu.acceleration
        a_y = a[1] # when standing upright, gravity works in the y direction
        # gravity accelerates downward at ~9.81 m/and count > 0s^2
        #print(a_y)
        #print(count)
        if (a_y > 7.0 and count < max_count):
            countup(count)
            count += 1
        if (a_y < -7.0 and count > 0):
            countdown(count)
            count -= 1
    
except KeyboardInterrupt:
    strand_off(strip)