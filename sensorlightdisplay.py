from adafruit_circuitplayground import cp

class SensorLightDisplay:

    def __init__(self, brightness):
        self.pixels_off_state = [0, 0, 0]
        self.pixel_amount = len(cp.pixels)
        cp.pixels.brightness = brightness
        cp.pixels.autowrite = False

    def light(self, acceleration, colour):
        x = acceleration[0]
        y = acceleration[1]

        if x < -3 and x < y:
            for pixel in range(6, 9):
                cp.pixels[pixel] = colour
            cp.pixels.show()
        elif x > 3 and x > y:
            for pixel in range(1, 4):
                cp.pixels[pixel] = colour
            cp.pixels.show()
        elif y > 3 and y > x:
            for pixel in [4, 5]:
                cp.pixels[pixel] = colour
            cp.pixels.show()
        elif y < -3 and y < x:
            for pixel in [0, 9]:
                cp.pixels[pixel] = colour
            cp.pixels.show()
        else:
            cp.pixels.fill(self.pixels_off_state)
            cp.pixels.show()

    def control_feedback_y(self, acceleration_y):
        y = acceleration_y
        acceleration_peak = 9.81

        if y < 0:
            flipped_y = y * -1
        else:
            flipped_y = y

        if flipped_y < acceleration_peak:
            x = (flipped_y/acceleration_peak)
            colour = 255 * x
            cp.pixels.fill([0, 0, colour])
            cp.pixels.show()
