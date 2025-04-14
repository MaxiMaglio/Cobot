from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from movement.movement_functions import handleInput
from time import sleep

def main():
    robot = CobotInstance()
    robot.connect()
    gripper = Robotiq_Two_Finger_Gripper(robot.robot)
    gripper.open_gripper()
    sleep(2)
    robot.setSpeed(2)
    robot.setAcceleration(2)
    robot.start()
    robot.setSpeed(0.5)
    robot.setAcceleration(0.5)
    
    while True:
        user_input = input("Enter the item you want to order between tuercas, tornillos, arandelas (Enter q to exit): ")
        handleInput(robot, gripper, user_input)
        if (user_input == "q"):
            break

    robot.close()

if __name__ == "__main__":
    main()