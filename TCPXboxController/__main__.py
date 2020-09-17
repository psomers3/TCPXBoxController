from TCPXboxController import TCPXboxController
import argparse

parser = argparse.ArgumentParser(description='Connect to an Xbox 360 controller and forward the signals on a TCP port')
parser.add_argument('-D', '--dev_num', type=int, help='device number corresponding to desired controller', default=0)
parser.add_argument('-S', '--send_port', type=int, help='TCP port to send the signals to. Default=63636', default=63636)
parser.add_argument('-R', '--receive_port', type=int, help='TCP port to receive vibration commands. Default=63637', default=63637)
parser.add_argument('-I', '--ip_addr', type=str, help='ip address to use for TCP communication. Default=\'localhost\'', default='localhost')

if __name__ == '__main__':
    args = parser.parse_args()
    controller = TCPXboxController(dev_num=args.dev_num,
                                   send_socket_port=args.send_port,
                                   rec_socket_port=args.receive_port,
                                   socket_ip=args.ip_addr)
    controller.start_sockets()
    input("Press enter to shutdown.")
    controller.stop_sockets()
    print("Sockets successfully shutdown.")
