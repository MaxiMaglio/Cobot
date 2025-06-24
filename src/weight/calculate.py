import serial
import time
import threading

port = '/dev/tty.usbmodem101'
baud_rate = 9600

def weight():
    def read_serial():
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"[WEIGHT] Conectado a {port} a {baud_rate} baud")
        time.sleep(3)
        ser.reset_input_buffer()

        try:
            while True:
                if ser.in_waiting:
                    message = ser.readline().decode('utf-8', errors='ignore').strip()
                    if message:
                        print(f"[WEIGHT] {message}")
        except Exception as e:
            print(f"[WEIGHT ERROR] {e}")
        finally:
            ser.close()

    # Lanzar el hilo
    thread = threading.Thread(target=read_serial, daemon=True)
    thread.start()

if __name__ == "__main__":
    weight()
    while True:
        time.sleep(1)