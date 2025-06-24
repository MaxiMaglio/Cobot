import tkinter as tk
import threading
import time
import serial
from instance.CobotInstance import CobotInstance
from movement.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from movement.movement_functions import handleInputAux
from time import sleep

selected_item = None  # Variable global para el ítem seleccionado

# --- Simulated robot initialization ---
def initialize_robot():
    print("Initializing robot arm...")
    gripper.open_gripper()
    sleep(2)
    robot.setSpeed(2)
    robot.setAcceleration(2)
    robot.start()
    robot.setSpeed(0.5)
    robot.setAcceleration(0.5)
    time.sleep(1)
    print("Robot arm initialized.")

# --- Enviar comando a la balanza ---
def enviar_volcado(item):
    port = '/dev/ttyACM0'
    baud_rate = 9600
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)
        if item in ["clavos", "tornillos"]:
            print("Enviando VOLCAR2 a la balanza")
            ser.write(b'VOLCAR2\n')
        elif item in ["tuercas", "arandelas"]:
            print("Enviando VOLCAR1 a la balanza")
            ser.write(b'VOLCAR1\n')
        else:
            print("Item no reconocido, no se envía comando.")
        ser.close()
    except Exception as e:
        print(f"[ERROR enviando a balanza] {e}")

def on_item_selected(item):
    global selected_item
    selected_item = item
    print(f"Ítem seleccionado: {item}")
    # Si quieres que el robot actúe al seleccionar, descomenta la siguiente línea:
    # threading.Thread(target=handleInputAux, args=(robot, gripper, item)).start()

def on_volcar():
    global selected_item
    if selected_item is None:
        print("No se seleccionó ningún ítem, usando 'tuercas' por defecto.")
        selected_item = "tuercas"
    port = '/dev/ttyACM0'
    baud_rate = 9600
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)
        if selected_item in ["clavos", "arandelas"]:
            print("Enviando VOLCAR1 a la balanza")
            ser.write(b'VOLCAR1\n')
        elif selected_item in ["tuercas", "tornillos"]:
            print("Enviando VOLCAR2 a la balanza")
            ser.write(b'VOLCAR2\n')
        else:
            print("Item no reconocido, no se envía comando.")
        ser.close()
    except Exception as e:
        print(f"[ERROR enviando a balanza] {e}")

# --- Robot Setup ---
robot = CobotInstance()
robot.connect()
gripper = Robotiq_Two_Finger_Gripper(robot.robot)
initialize_robot()

# --- Tkinter UI ---
root = tk.Tk()
root.title("Robot Arm Controller")

# --- Main content ---
content_frame = tk.Frame(root)
content_frame.pack(expand=True)

# --- Button box ---
button_names = ['arandelas', 'clavos', 'tornillos', 'tuercas']
buttons = []

for name in button_names:
    btn = tk.Button(
        root,
        text=name,
        width=20,
        height=2,
        font=('Helvetica', 14),
        command=lambda n=name: on_item_selected(n)
    )
    btn.pack(pady=10)
    buttons.append(btn)

# --- Botón VOLCAR ---
volcar_button = tk.Button(
    root,
    text="VOLCAR",
    width=20,
    height=2,
    font=('Helvetica', 14, 'bold'),
    bg="#F1C40F",
    command=on_volcar
)
volcar_button.pack(pady=10)

# --- Footer or exit button ---
exit_button = tk.Button(root, text="Salir", command=root.destroy, bg="#E74C3C", fg="white", font=("Helvetica", 12))
exit_button.pack(pady=20, side='bottom')

# --- Start redirect ---
def redirect_after_start():
    pass  # Aquí podrías poner lógica para redirigir o inicializar algo tras el arranque

root.after(1000, redirect_after_start)
root.mainloop()