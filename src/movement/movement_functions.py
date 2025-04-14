from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from time import sleep

origin = [-1.528, -3.123, 2.718, -4.326, -1.672, -0.339]
baseRotation = [-4.700810496007101, -3.1229621372618617, 2.717733685170309, -4.326068302194113, -1.6716540495501917, -0.3389657179461878]
tuercas = [-4.287, -0.678, 1.881, -4.186, -0.487, -0.184]
tuercas_pullback_pose = [-4.718, -0.907, 2.393, -3.634, -0.087, -1.034]
tornillos = []
tornillos_pullback_pose = []
arandelas = []
arandelas_pullback_pose = []
aux_balance_pose = [-4.715, -1.785, 1.987, -2.325, -0.088, -1.059]
balance_pose = [-4.252, -2.185, 2.629, -3.434, -0.518, -0.176]

def tiltItems(robot):
    robot.movel(aux_balance_pose, sleep=3)
    robot.movel(balance_pose, sleep=8)
    robot.tilt(balance_pose, sleep=8)
    robot.movel(aux_balance_pose, sleep=3)

def handleInput(robot: CobotInstance, gripper: Robotiq_Two_Finger_Gripper, input):
    if (input == "tuercas"):
        robot.movej(tuercas, sleep=6)
        gripper.close_gripper()
        sleep(2)
        robot.setSpeed(0.05)
        robot.setAcceleration(0.05)
        robot.movel(tuercas_pullback_pose, sleep=5)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        tiltItems(robot)
        robot.movel(tuercas_pullback_pose, sleep=5)
        robot.setSpeed(0.03)
        robot.setAcceleration(0.03)
        robot.movel(tuercas, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        gripper.open_gripper()
        sleep(5)
    elif (input == "tornillos"):
        robot.movej(tornillos, sleep=6)
        gripper.close_gripper()
        sleep(2)
        robot.setSpeed(0.05)
        robot.setAcceleration(0.05)
        robot.movel(tornillos_pullback_pose, sleep=5)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        tiltItems(robot)
        robot.movel(tornillos_pullback_pose, sleep=5)
        robot.setSpeed(0.03)
        robot.setAcceleration(0.03)
        robot.movel(tornillos, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        gripper.open_gripper()
        sleep(5)
    elif (input == "arandelas"):
        robot.movej(arandelas, sleep=6)
        gripper.close_gripper()
        sleep(2)
        robot.setSpeed(0.05)
        robot.setAcceleration(0.05)
        robot.movel(arandelas_pullback_pose, sleep=5)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        tiltItems(robot)
        robot.movel(arandelas_pullback_pose, sleep=5)
        robot.setSpeed(0.03)
        robot.setAcceleration(0.03)
        robot.movel(arandelas, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        gripper.open_gripper()
        sleep(5)
    elif (input == "q"):
        robot.movej(baseRotation, sleep=5)
        robot.setSpeed(2)
        robot.setAcceleration(2)
        robot.movej(origin, sleep=5)
        gripper.close_gripper()
    else:
        print("Invalid input. Please enter 'tuercas', 'tornillos', 'arandelas', or 'q'.")