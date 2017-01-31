import utime
from src.model.strip import Strip
from src.model.pir import Pir
from src.model.luminosity import Luminosity

__blueStrip = None
__yellowStrip = None
__bluePir = None
__yellowPir = None
__luminocity = None

LIGHT_TIME = 60 # Strip light time
MIN_LUMINOCITY = 500 # Min luminocity for system on

# PIR last motion time
__blueMotionTime = None
__yellowMotionTime = None


def init(blueStrip: Strip, yellowStrip: Strip, bluePir: Pir, yellowPir: Pir, luminocity: Luminosity):
    __blueStrip = blueStrip
    __yellowStrip = yellowStrip
    __bluePir = bluePir
    __yellowPir = yellowPir
    __luminocity = luminocity


def check(): # Check PIR-sensor
    can_light = True
    if __luminocity is not None and __luminocity.value() < MIN_LUMINOCITY:
        can_light = False

    __check_strip(__bluePir, __blueStrip, can_light)
    __check_strip(__yellowPir, __yellowStrip, can_light)

    # Как только меняется значение на движении сразу делаем проверку
    __bluePir.set_callback(check)
    __yellowPir.set_callback(check)
    return


def __check_strip(pir, strip, can_light: bool):
    if pir is Pir and strip is Strip:
        if pir.value(): # motion
            if not can_light or strip.get_status():
                return
            strip.on()
        else: # no motion
            if strip.get_status():
                strip.off()
    return
