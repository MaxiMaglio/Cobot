from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from movement.movement_functions import handleInput
from time import sleep

pos = [-4.282105747853414, -0.6960337919047852, 1.9044182936297815, -4.208718200723165, -0.49647504488100225, -0.18647653261293584]
origin = [-1.528, -3.123, 2.718, -4.326, -1.672, -0.339]
def main():
    robot = CobotInstance("192.168.0.16")
    gripper = Robotiq_Two_Finger_Gripper(robot.robot)
    gripper.open_gripper()
    sleep(3)
    robot.setSpeed(2)
    robot.setAcceleration(2)
    robot.start()
    robot.setSpeed(0.5)
    robot.setAcceleration(0.5)

    while True:
        user_input = input("Enter 1 to move to position, o to go back to origin (Enter q to exit): ")
        handleInput(robot, gripper, user_input)
        if (user_input == "q"):
            break
    # print(robot.getInfo())

    robot.close()

if __name__ == "__main__":
    main()