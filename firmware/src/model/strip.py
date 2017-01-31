import machine


class Strip: # Класс RGB-ленты
    FREQ = 100 # частота мерцания ленты

    # цвета ленты
    red = 0
    green = 0
    blue = 0
    alpha = 100

    pin = {}
    status = 0 # Статус включенности ленты

    def __init__(self, red_pin: int, green_pin: int, blue_pin: int):
        self.pin = {
            'red': machine.PWM(machine.Pin(red_pin), self.FREQ, 0),
            'green': machine.PWM(machine.Pin(green_pin), self.FREQ, 0),
            'blue': machine.PWM(machine.Pin(blue_pin), self.FREQ, 0)
        }

    def set_color(self, red: int, green: int, blue: int):
        self.red = self.__minmax(red, 0, 255)
        self.green = self.__minmax(green, 0, 255)
        self.blue = self.__minmax(blue, 0, 255)

    def set_alpha(self, alpha: int):
        self.alpha = self.__minmax(alpha, 0, 100)

    def on(self, alpha: int = None):
        if alpha is not None:
            self.set_alpha(alpha)

        self.pin['red'].freq(int(self.red * self.alpha / 100))
        self.pin['green'].freq(int(self.green * self.alpha / 100))
        self.pin['blue'].freq(int(self.blue * self.alpha / 100))
        self.status = 1

    def off(self):
        self.on(0)
        self.status = 0

    def get_status(self):
        return self.status

    @staticmethod
    def __minmax(value: int, minval: int, maxval: int):
        if value > maxval:
            return maxval
        if value < minval:
            return minval
        return value
