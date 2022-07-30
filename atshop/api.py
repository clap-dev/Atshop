import json
import websocket
from threading import Thread, Event

from .endpoints import *

class Opcode:
    PING            = 'ping'
    RESULT          = 'result'
    CONNECTED       = 'connected'

class Server():
    '''
    This class is our middleman between us and atshop,
    and it handles everything related to websockets.
    '''

    def __init__(self):
        self._id = 0
        self._login = False

        self._connected = Event()
        self._response = Event()
        self._response_data = None

        self._websocket = self.create_websocket()

        self.run()

    def create_websocket(self):
        return websocket.WebSocketApp(
            url=ROOT,
            on_open=lambda ws: self.on_open(ws),
            on_message=lambda ws, msg: self.on_message(ws, msg),
            on_error=lambda ws, msg: self.on_error(ws, msg),
            on_close=lambda ws, close_code, close_msg: self.on_close(ws, close_code, close_msg)
        )

    def on_open(self, ws):
        self.send(
            {
                'msg': 'connect',
                'version': '1',
                'support': [
                    '1',
                    'pre2',
                    'pre1'
                ]
            }
        )

    def on_close(self, ws, close_code, close_msg):
        self.connected = False

    def on_error(self, ws, error):
        raise Exception(error)

    def on_message(self, ws, message):
        data = json.loads(message)
        op = data.get('msg')

        if op == Opcode.RESULT and self._login:
            if data.get('error'):
                raise Exception(
                    data['error']['reason']
                )

            else:
                self._login = False

        elif op == Opcode.PING:
            self.send(
                {
                    'msg': 'pong'
                }
            )
            # Heartbeat

        elif op == Opcode.CONNECTED:
            self._connected.set()

        elif op == Opcode.RESULT and self._id >= 11:
            self._response_data = data
            self._response.set()

        self._id += 1

    def send(self, payload):
        self._websocket.send(
            json.dumps(payload)
        )

        self._id += 1

    def run(self):
        Thread(
            target=self._websocket.run_forever,
            kwargs={
                'ping_interval': 10,
                'ping_timeout': 5
            },
            # daemon=True
        ).start()

        self._connected.wait()

        # Waiting for the websocket to connect to atshop
        # if we do not include this, our code will begin
        # executing before we want to. The result of this is
        # websocket._exceptions.WebSocketConnectionClosedException

class Client(Server):
    '''
    This will be how users interact
    with our server class, mainly through
    the use of our "request" function.
    '''

    def login(self, token):
        self.send(
            {
                'msg': 'method',
                'id': str(self._id),
                'method': 'login',
                'params': [
                    {
                        'resume': token
                    }
                ]
            }
        )

        self._id += 1
        self._login = True

    def request(self, **kwargs):
        method = kwargs['method']
        method_args = METHODS.get(method)

        if all(
            arg in kwargs
            for arg in method_args
        ):
            del kwargs['method']

            self.send(
                {
                    'msg': 'method',
                    'id': str(self._id),
                    'method': method,
                    'params': [
                        *kwargs.values()
                    ]
                }
            )

            self._response.wait()
            self._response.clear()

            return self._response_data
