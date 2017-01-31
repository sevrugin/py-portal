import machine

RGBPin = {
    'blue': {'red': 5, 'green': 4, 'blue': 0},
    'yellow': {'red': 14, 'green': 12, 'blue': 13}
}

PIRPin = {'blue': 2, 'yellow': 15}

light = machine.ADC()


# Проверка пир-датчиков на движение и включение нужного леда при необходимости
def check():
    return


class Led:
    FREQ = 100

    red = 0
    green = 0
    blue = 0
    alpha = 100

    pin = {}

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

    def __minmax(self, value: int, minval: int, maxval: int):
        if value > maxval:
            return maxval
        if value < minval:
            return minval
        return value
