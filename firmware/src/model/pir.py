from machine import Pin
import utime


class Pir: # Чтение данных с PIR-датчика
    pir = None

    last_time = None # Время
    __callback = None

    def __init__(self, gpio):
        self.pir = Pin(gpio, Pin.IN)
        self.pir.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.__trigger)

    def value(self):
        return self.pir.value()

    def set_callback(self, callback: callable):
        self.__callback = callback

    @staticmethod
    def __trigger(pin):
        pass
    #     if self.value():
    #         self.last_time = utime.time()
    #     else:
    #         self.last_time = None
    #
    #     if hasattr(self.__callback, '__call__'):
    #         self.__callback(self)
