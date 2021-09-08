import board
import busio
import adafruit_mpu6050
from time import sleep, perf_counter
from rpi_ws281x import *
import time

# LED strip config:
LED_COUNT      = 85      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 25      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# MPU config
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# animation borrowed from default LED strip test program
def colorWipe(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
#         time.sleep(wait_ms / 1000.0)

try:
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    while True:
        a = mpu.acceleration
        a_y = a[1] # when standing upright, gravity works in the y direction
        # gravity accelerates downward at ~9.81 m/s^2
        #print(a_y)
        if (a_y > 7.0):
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
        if (a_y < -7.0):
            colorWipe(strip, Color(0, 0, 255))  # Blue wipe

            
except KeyboardInterrupt:
    colorWipe(strip, Color(0, 0, 0), 10)
