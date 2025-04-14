from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from time import sleep

origin = [-1.528, -3.123, 2.718, -4.326, -1.672, -0.339]
baseRotation = [-4.700810496007101, -3.1229621372618617, 2.717733685170309, -4.326068302194113, -1.6716540495501917, -0.3389657179461878]
tuercas = [-4.281659428273336, -0.6886347693255921, 1.899863068257467, -4.173770566979879, -0.4969385305987757, -0.25207502046693975]
tuercas_pullback_pose = [0.43721, -0.37752, -0.27135, 2.480, -2.280, 2.302]
tornillos = []
tornillos_pullback_pose = []
arandelas = []
arandelas_pullback_pose = []
balance_pose = []

def handleInput(robot: CobotInstance, gripper: Robotiq_Two_Finger_Gripper, input):
    if (input == "tuercas"):
        robot.movej(tuercas, sleep=8) # change this to movel with the correct pose
        gripper.close_gripper()
        sleep(5)
        robot.setSpeed(0.01)
        robot.setAcceleration(0.01)
        robot.movel(tuercas_pullback_pose, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        robot.movel(balance_pose, sleep=8)
        robot.tilt(balance_pose, 0.5, sleep=8)
        robot.movel(tuercas_pullback_pose, sleep=5)
        robot.setSpeed(0.01)
        robot.setAcceleration(0.01)
        robot.movel(tuercas, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        gripper.open_gripper()
        sleep(5)
    elif (input == "tornillos"):
        robot.movel(tornillos, sleep=8)
        gripper.close_gripper()
        sleep(5)
        robot.setSpeed(0.01)
        robot.setAcceleration(0.01)
        robot.movel(tornillos_pullback_pose, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        robot.movel(balance_pose, sleep=8)
        robot.tilt(balance_pose, 0.5, sleep=8)
        robot.movel(tornillos_pullback_pose, sleep=5)
        robot.setSpeed(0.01)
        robot.setAcceleration(0.01)
        robot.movel(tornillos, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        gripper.open_gripper()
        sleep(5)
    elif (input == "arandelas"):
        robot.movel(arandelas, sleep=8)
        gripper.close_gripper()
        sleep(5)
        robot.setSpeed(0.01)
        robot.setAcceleration(0.01)
        robot.movel(arandelas_pullback_pose, sleep=8)
        robot.setSpeed(0.5)
        robot.setAcceleration(0.5)
        robot.movel(balance_pose, sleep=8)
        robot.tilt(balance_pose, 0.5, sleep=8)
        robot.movel(arandelas_pullback_pose, sleep=5)
        robot.setSpeed(0.01)
        robot.setAcceleration(0.01)
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