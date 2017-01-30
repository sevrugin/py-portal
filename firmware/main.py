import sys

if sys.platform != 'linux':
    from pynode import wifi
    wifi.init()

# Init timers
from pynode import interval
# from src.service import portal
# interval.add('portal.check', portal.check, 100) # проверяем датчики каждые 100 мс
#interval.add('wifi.check', wifi.check, 10000) # проверяем wi-fi каждые 10 с
#interval.start() # начинаем работу таймеров

# start HTTP-server
from pynode.http.server import Server
from src.controller.controller import PortalController

server = Server(PortalController())
server.start()
