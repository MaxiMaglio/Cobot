import urx
from time import sleep

startingPoint = [-4.700810496007101, -3.1229621372618617, 2.717733685170309, -4.326068302194113, -1.6716540495501917, -0.3389657179461878]

class CobotInstance:
    def __init__(self, ip):
        self.robot = urx.Robot(ip)
        self.speed = 0.5
        self.acceleration = 0.5

    def setSpeed(self, speed: float):
        self.speed = speed

    def setAcceleration(self, acceleration: float):
        self.acceleration = acceleration

    def moveTo(self, pos, wait):
        self.robot.movej(pos, acc=self.acceleration, vel=self.speed, wait=wait)
    
    def start(self):
        self.moveTo(startingPoint, False)

    def close(self):
        self.robot.close()

    def getInfo(self):
        return self.robot.getj()