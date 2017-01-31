from machine import ADC


class Luminosity: # Уровень освещенности с фоторезистора
    adc = None

    def __init__(self, gpio: int = 0):
        self.adc = ADC(gpio)

    def value(self):
        return self.adc.read()
