# Automated Hardware-Store with UR Robot

This project implements an automated hardware-store system using a Universal Robots (UR) collaborative robot (cobot). The system allows users to place orders for hardware items in Spanish, and the cobot prepares the requested order.

## Features
- **Supported Items**: The system supports the following hardware items:
    - Tuercas
    - Arandelas
    - Tornillos
- **Automated Order Preparation**: The cobot processes the input and prepares the requested items.

## How to Run
1. Ensure you have Python 3 installed on your system.
2. Ensure you have urx installed.
3. Navigate to the directory containing the `Main.py` file.
4. Run the following command in your terminal:
     ```bash
     python3 Main.py
     ```
5. Follow the on-screen instructions to input the item you want to purchase in Spanish.

## Notes
- The system is designed to work with an UR Robot, so ensure the robot is properly set up and connected before running the program.
- Input must be provided in Spanish for the system to correctly process the order.