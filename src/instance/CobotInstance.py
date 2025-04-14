import time
import socket
import urx

startingPoint = [-4.700810496007101, -3.1229621372618617, 2.717733685170309, -4.326068302194113, -1.6716540495501917, -0.3389657179461878]

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
    
    def tilt(self, current_pose, angle, sleep=0):
        # angle must be in radians
        if self.connected:
            current_pose[3] += angle
            self.movel(current_pose, sleep)
            # Return to horizontal position after tilting
            current_pose[3] -= angle
            self.movel(current_pose, sleep)
        else:
            print("Not connected to the robot")

    def setSpeed(self, speed):
        self.speed = speed

    def setAcceleration(self, aceleration): 
        self.acceleration = aceleration

    def start(self):
        if self.connected:
            self.movej(startingPoint, sleep=5)
        else:
            print("Not connected to the robot")
