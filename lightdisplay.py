from adafruit_circuitplayground import cp
import time

class LightDisplay:

    def __init__(self, brightness):
        self.pixels_off_state = [0, 0, 0]
        self.pixel_amount = len(cp.pixels)
        cp.pixels.brightness = brightness
        cp.pixels.autowrite = False

    def half_pattern(self, colour):
        pixel_top = self.pixel_amount - 1
        pixel_bottom = 0

        for pixel in range(pixel_bottom, (self.pixel_amount/2)):
            cp.pixels[pixel_bottom] = colour
            cp.pixels[pixel_top] = colour
            cp.pixels.show()
            time.sleep(0.5)
            pixel_bottom += 1
            pixel_top -= 1

        cp.pixels.fill(self.pixels_off_state)
        cp.pixels.show()

    def light(self, side, colour):
        if side == 0:
            for pixel in range(1, 4):
                cp.pixels[pixel] = colour
        elif side == 1:
            for pixel in range(6, 9):
                cp.pixels[pixel] = colour
        elif side == 2:
            for pixel in [4, 5]:
                cp.pixels[pixel] = colour
        elif side == 3:
            for pixel in [0, 9]:
                cp.pixels[pixel] = colour

    def random_light(self, colour, sec_interval):
        import random

        for i in range(5):
            pixel_list = []

            while len(pixel_list) < 5:
                random_number = random.randint(0, 9)
                if random_number not in pixel_list:
                    pixel_list.append(random_number)

            for item in pixel_list:
                cp.pixels[item] = colour
            cp.pixels.show()

            time.sleep(sec_interval)

            cp.pixels.fill(self.pixels_off_state)
            cp.pixels.show()

            time.sleep(sec_interval)

        cp.pixels.fill(self.pixels_off_state)
        cp.pixels.show()

    def snake(self, snake_size, colour, interval):
        snake_start = -1
        if snake_size < 2 or snake_size > self.pixel_amount/2:
            print("Invalid entry for Snake Size!!")
            return

        while snake_start + snake_size != self.pixel_amount:
            snake_start += 1
            for pixel in range(snake_start, snake_start + snake_size):
                cp.pixels[pixel] = colour
                off_light = snake_start - 1
                cp.pixels[off_light] = self.pixels_off_state
            cp.pixels.show()
            time.sleep(interval)
            if snake_start + snake_size == self.pixel_amount:
                cp.pixels.fill(self.pixels_off_state)
                cp.pixels.show()
                time.sleep(1)
                break
