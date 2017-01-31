import sys

if sys.platform != 'linux':
    from pynode import wifi
    wifi.init()

# Init portal service
from src.service import portal
from src.model.strip import Strip
from src.model.pir import Pir
from src.model.luminosity import Luminosity

portal.init(Strip(5, 4, 0), Strip(14, 12, 13), Pir(2), Pir(15), Luminosity(0))

# Init timers
from pynode import interval

interval.add('portal.check', portal.check, 100) # проверяем датчики каждые 100 мс
interval.add('wifi.check', wifi.check, 10000) # проверяем wi-fi каждые 10 с
interval.start() # начинаем работу таймеров

# start HTTP-server
from pynode.http.server import Server
from src.controller.controller import PortalController

server = Server(PortalController())
server.start()
