import socket
# import cv2
import time
import threading


class Tello:
    # Send and receive command
    TELLO_IP = "192.168.10.1"
    CMD_UDP_PORT = 8889
    STATES_UDP_PORT = 8890

    SPEED = 100

    # Video
    VIDEO_IP_UDP = "0.0.0.0"
    VIDEO_UDP_PORT = 11111

    def __init__(self, drone_ip=TELLO_IP):
        self.address = (drone_ip, Tello.CMD_UDP_PORT)
        self.cmd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cmd_socket.bind(("", Tello.CMD_UDP_PORT))
        self._running = True
        self.video_on = False
        self._ready = False
        self.is_flying = False

        self.connect()
        self.set_speed()

        """Separate Threads for listening to UDP Ports"""
        # Thread 1 for receiving response command
        response_recv_thread = threading.Thread(target=self.recv_response)
        response_recv_thread.daemon = True
        response_recv_thread.start()

        # Thread 2 constantly receiving telemetry_states
        state_recv_thread = threading.Thread(target=self.udp_states_recv)
        state_recv_thread.daemon = True
        state_recv_thread.start()

        # self.battery()

    def connect(self):
        """Enter in SDK mode"""
        self.send_command("command")
        time.sleep(1)

    def send_command(self, command):
        command_enc = command.encode(encoding="utf-8")
        self.cmd_socket.sendto(command_enc, self.address)
        print(f"Command: {command}.")  # print command

    def set_speed(self):
        self.send_command(f"speed {str(Tello.SPEED)}")

    def recv_response(self):
        while self._running:
            try:
                msg, _ = self.cmd_socket.recvfrom(1024)
                print(f"Response: {msg.decode(encoding='utf-8')}")
            except Exception as err:
                print(err)

    def udp_states_recv(self):
        state_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        state_socket.bind(("", Tello.STATES_UDP_PORT))
        while self._running:
            try:
                data, address = state_socket.recvfrom(1024)
                data = data.decode(encoding='utf-8')

                print(f"States: {data.split(';')}")
                time.sleep(2)

            except Exception as err:
                print(err)

    """ALL THE COMMANDS"""
    def takeoff(self):
        """Drone automatically take off"""
        self.send_command("takeoff")
        time.sleep(1)
        self.is_flying = True

    def land(self):
        """Drone will automatically land"""
        self.send_command("land")
        time.sleep(3)
        self.is_flying = False

    def disconnect(self):
        self.land()
        time.sleep(3)
        self._running = False
        self.is_flying = False
        # self.cmd_socket.close()

    def move_left(self, x: int):
        self.send_command(f"left {str(x)}")
        # time.sleep(0.5)

    def move_right(self, x: int):
        self.send_command(f"right {str(x)}")
        # time.sleep(0.5)

    def move_up(self, x: int):
        self.send_command(f"up {str(x)}")
        # time.sleep(0.5)

    def move_down(self, x: int):
        self.send_command(f"down {str(x)}")
        # time.sleep(0.5)

    def move_forward(self, x: int):
        self.send_command(f"forward {str(x)}")
        # time.sleep(0.5)

    def move_back(self, x: int):
        self.send_command(f"back {str(x)}")
        # time.sleep(0.5)

    def turn_right(self, x: int):
        self.send_command(f"cw {str(x)}")
        # time.sleep(0.5)

    def turn_left(self, x: int):
        self.send_command(f"ccw {str(x)}")
        # time.sleep(0.5)

    """Flips only when battery above 70%?"""
    def flip(self, direction: str):
        """direction could be: l, r, f, b"""
        self.send_command(f"flip {direction}")
        # time.sleep(0.5)

    """Read commands: temperature, battery, etc"""
    def temp(self):
        """Gets drone temperature"""
        self.send_command("temp?")

    def battery(self):
        """Gets drone battery %"""
        self.send_command("battery?")


class VideoTello(Tello):
    pass


""" TESTING """
# tello = Tello()
# time.sleep(10)
