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
    red = None
    green = None
    blue = None
    alpha = None

    pin = {}

    def __init__(self, red_pin, green_pin, blue_pin):
        self.pin = {
            'red': machine.PWM(machine.Pin(red_pin)),
            'green': machine.PWM(machine.Pin(green_pin)),
            'blue': machine.PWM(machine.Pin(blue_pin))
        }

    def set_color(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def on(self):
        self.pin['red'].freq(self.red) # или как-то так
