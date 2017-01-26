import machine

RGBPin = {
    'blue': {'red': 1, 'green': 2, 'blue': 3},
    'yellow': {'red': 1, 'green': 2, 'blue': 3}
}

PIRPin = {'blue': 1, 'yellow': 2}

light = machine.ADC()


# Проверка пир-датчиков на движение и включение нужного леда при необходимости
def check():
    return


class Led:
    red = None
    green = None
    blue = None
    alpha = None

    pin = {}

    def __init__(self, red_pin, green_pin, blue_pin):
        self.pin = {
            'red': machine.PWM(red_pin),
            'green': machine.PWM(green_pin),
            'blue': machine.PWM(blue_pin)
        }

    def set_color(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def on(self):
        self.pin['red'].freq(self.red) # или как-то так
