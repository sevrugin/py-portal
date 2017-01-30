from pynode.http.request import Request
from pynode.http.controller import Controller
from pynode.http.response import Response


class PortalController(Controller):
    def __init__(self):
        self.add('/', self.main, ['GET'])

    def main(self, request: Request):
        view = self.view('test.html')

        return Response(view)
