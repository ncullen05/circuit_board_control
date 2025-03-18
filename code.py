from adafruit_circuitplayground import cp
import time

from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay

light_display = LightDisplay(0.5)
sensor_light_display = SensorLightDisplay(0.5)

while True:
    light_display.half_pattern([0, 255, 100])
    time.sleep(1)
    #light_display.light(0, [0, 255, 100])
    #time.sleep(1)
    #light_display.random_light([0, 100, 255], 1)
    #time.sleep(1)
    #light_display.snake(3, [0, 100, 255], 0.5)
    #time.sleep(1)
    #sensor_light_display.light([cp.acceleration[0], cp.acceleration[1]], [0, 100, 255])
    #sensor_light_display.control_feedback_y(cp.acceleration[1])# Write your code here :-)
