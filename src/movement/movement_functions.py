from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from time import sleep

origin = [-1.528, -3.123, 2.718, -4.326, -1.672, -0.339]
baseRotation = [-4.700810496007101, -3.1229621372618617, 2.717733685170309, -4.326068302194113, -1.6716540495501917, -0.3389657179461878]
pos = [-4.29382831255068, -0.6716346901706238, 1.8415020147906702, -4.070017953912252, -0.39274341264833623, -0.22160655656923467]

def handleInput(robot: CobotInstance, gripper: Robotiq_Two_Finger_Gripper, input):
    if (input == "1"):
        robot.moveTo(pos, False)
        sleep(8)
        gripper.close_gripper()
    elif (input == "q"):
        robot.moveTo(baseRotation, wait=False)
        sleep(5)
        robot.setSpeed(2)
        robot.setAcceleration(2)
        robot.moveTo(origin, wait=False)
        sleep(5)
        gripper.close_gripper()