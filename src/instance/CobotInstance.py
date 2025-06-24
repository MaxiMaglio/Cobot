import time
import socket
import urx

startingPoint = [-4.6887, -1.1634, 2.1585, -1.1679, 0.0117, 0.2661]

HOST = "192.168.0.16"
PORT = 30002

class CobotInstance:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.speed = 0.5
        self.acceleration = 0.5
        self.connected = False
        self.robot = urx.Robot(HOST)

    def connect(self):
        try:
            self.socket.connect((HOST, PORT))
            self.connected = True
            print("Connected to the robot")
        except socket.error as e:
            print(f"Connection error: {e}")
            self.connected = False

    def close(self):
        if self.connected:
            self.socket.close()
            self.connected = False
            print("Disconnected from the robot")
        else:
            print("Not connected to the robot")

    def movej(self, joint_positions, sleep=0):
        if self.connected:
            command = f"movej({joint_positions}, a={self.acceleration}, v={self.speed})\n"
            self.socket.send(command.encode())
            time.sleep(sleep)
        else:
            print("Not connected to the robot")

    def movel(self, pose, sleep=0):
        if self.connected:
            command = f"movel({pose}, a={self.acceleration}, v={self.speed})\n"
            self.socket.send(command.encode())
            time.sleep(sleep)
        else:
            print("Not connected to the robot")
    
    def tilt(self, current_pose, sleep=0):
        tilt_pose = [-3.622, -1.747, 1.427, -1.451, -1.486, -0.465]
        # angle must be in radians
        if self.connected:
            # self.setSpeed(0.2)
            # self.setAcceleration(0.2)
            self.movej(tilt_pose, sleep)
            # Return to horizontal position after tilting
            self.movej(current_pose, sleep)
            # self.setSpeed(0.5)
            # self.setAcceleration(0.5)
        else:
            print("Not connected to the robot")

    def setSpeed(self, speed):
        self.speed = speed

    def setAcceleration(self, aceleration): 
        self.acceleration = aceleration

    def start(self):
        if self.connected:
            print("starting")
            self.movej(startingPoint, sleep=5)
        else:
            print("Not connected to the robot")
