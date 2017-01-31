import sys

# if sys.platform != 'linux':
#     from pynode import wifi
#     wifi.init()

# Init portal service
from src.service.portal import Portal
from src.model.strip import Strip
from src.model.pir import Pir
from src.model.luminosity import Luminosity
#
global portal
blueStrip = Strip(0, 2, 14)
blueStrip.set_color(0, 128, 255)
yellowStrip = Strip(12, 13, 15)
yellowStrip.set_color(255, 128, 0)

portal = Portal(blueStrip, yellowStrip, Pir(5), Pir(4), Luminosity(0))


# Init timers
from pynode import interval

# interval.add('portal.info', portal.info, 1000)
interval.add('portal.check', portal.check, 1000) # проверяем датчики каждые 100 мс
# interval.add('wifi.check', wifi.check, 10000) # проверяем wi-fi каждые 10 с
interval.start() # начинаем работу таймеров

# start HTTP-server
#from pynode.http.server import Server
#from src.controller.controller import PortalController

#server = Server(PortalController())
#server.start()
