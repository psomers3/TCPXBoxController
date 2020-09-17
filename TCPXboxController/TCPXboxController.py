from DataSocket import TCPReceiveSocket, TCPSendSocket, JSON
from xinput import XInputJoystick
import sys
from operator import attrgetter


class TCPXboxController(object):
    def __init__(self, dev_num=0, send_socket_port=63636, rec_socket_port=63637, socket_ip="localhost"):
        self.send_socket = TCPSendSocket(tcp_port=send_socket_port, tcp_ip=socket_ip, send_type=JSON)
        self.rec_socket = TCPReceiveSocket(tcp_port=rec_socket_port, tcp_ip=socket_ip, handler_function=self.on_receive)

        joysticks = XInputJoystick.enumerate_devices()
        device_numbers = list(map(attrgetter('device_number'), joysticks))

        print('found %d devices: %s' % (len(joysticks), device_numbers))

        if not joysticks:
            sys.exit(0)

        self.joystick = joysticks[dev_num]
        print('using %d' % self.joystick.device_number)

        @self.joystick.event
        def on_button(button, pressed):
            self.send_socket.send_data([button, pressed])

        @self.joystick.event
        def on_axis(axis, value):
            self.send_socket.send_data([axis, value])

    def on_receive(self, data):
        ''' Do something here to activate the vibrations '''
        pass

    def start_sockets(self):
        self.send_socket.start()
        self.rec_socket.start()

    def stop_sockets(self):
        self.send_socket.stop()
        self.rec_socket.stop()
