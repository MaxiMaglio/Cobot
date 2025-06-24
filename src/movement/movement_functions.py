from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from time import sleep
from ArmPositions import ArmPositions
from movement.constants import *


instances = {
    'tuercas': ArmPositions(tuercas, tuercas_pullback_pose),
    'tornillos': ArmPositions(tornillos, tornillos_pullback_pose),
    'clavos': ArmPositions(clavos, clavos_pullback_pose),
    'arandelas': ArmPositions(arandelas, arandelas_pullback_pose)
}


def tiltItems(robot):
    robot.movel(go_up_pose, sleep=8)
    robot.movel(go_back_pose, sleep=8)
    robot.setSpeed(0.1)
    robot.setAcceleration(0.1)
    robot.movel(tilt_pose, sleep=8)    
    robot.setSpeed(0.2)
    robot.setAcceleration(0.2)
    robot.movel(go_back_pose, sleep=8)
    robot.movel(go_up_pose, sleep=8)


def handleInputAux(robot: CobotInstance, gripper: Robotiq_Two_Finger_Gripper, input: str):
    instance = instances[input]
    robot.movej(instance.initial_position(), sleep=6)
    gripper.close_gripper()
    sleep(2)
    robot.setSpeed(0.05)
    robot.setAcceleration(0.05)
    robot.movel(instance.pullback_position(), sleep=5)
    robot.setSpeed(0.2)
    robot.setAcceleration(0.2)
    tiltItems(robot)
    robot.movel(instance.pullback_position(), sleep=5)
    robot.setSpeed(0.03)
    robot.setAcceleration(0.03)
    robot.movel(instance.initial_position(), sleep=8)
    gripper.open_gripper()
    robot.setSpeed(0.5)
    robot.setAcceleration(0.5)
    sleep(2)