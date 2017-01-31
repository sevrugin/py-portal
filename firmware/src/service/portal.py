import utime
from ..model.strip import Strip
from ..model.pir import Pir
from ..model.luminosity import Luminosity


class Portal:
    __blueStrip = None
    __yellowStrip = None
    __bluePir = None
    __yellowPir = None
    __luminosity = None

    LIGHT_TIME = 60 # Strip light time
    MIN_LUMINOSITY = 0 # Min luminosity for system on

    # PIR last motion time
    __blueMotionTime = None
    __yellowMotionTime = None

    def __init__(self, blueStrip: Strip, yellowStrip: Strip, bluePir: Pir, yellowPir: Pir, luminosity: Luminosity):
        self.__blueStrip = blueStrip
        self.__yellowStrip = yellowStrip
        self.__bluePir = bluePir
        self.__yellowPir = yellowPir
        self.__luminosity = luminosity

        # Как только меняется значение на движении сразу делаем проверку
        self.__bluePir.set_callback(self.check)
        self.__yellowPir.set_callback(self.check)

    def info(self):
        print('luminosity: ', self.__luminosity.value())
        print('bluePir: ', self.__bluePir.value())
        print('yellowPir: ', self.__yellowPir.value())
        print('blueStrip: ', self.__blueStrip.status)
        print('yellowStrip: ', self.__yellowStrip.status)

    def check(self): # Check PIR-sensor
        # print('Start check...')
        can_light = True
        if self.__luminosity is not None and self.__luminosity.value() < self.MIN_LUMINOSITY:
            can_light = False
        # print('can_light: ', can_light)
        # print(' # Blue strip')
        self.__check_strip(self.__bluePir, self.__blueStrip, can_light)
        # print(' #Yellow strip:')
        self.__check_strip(self.__yellowPir, self.__yellowStrip, can_light)

        return


    @staticmethod
    def __check_strip(pir, strip, can_light: bool):
        if isinstance(pir, Pir) and isinstance(strip, Strip):
            # print('pir.value: ', pir.value())
            if pir.value(): # motion
                if not can_light or strip.get_status():
                    return
                strip.on()
                # print('strip.on')
            else: # no motion
                if strip.get_status():
                    strip.off()
                    # print('strip.off')
        return
