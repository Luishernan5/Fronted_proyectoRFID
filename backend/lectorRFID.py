import serial
import time
import requests
from datetime import datetime

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

def leer_uid():
    data = ser.read(14)
    uid = data[1:11].decode('utf-8', errors='ignore')
    return uid

def enviar_asistencia(uid):
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = requests.post("http://localhost:5000/asistencias", json={"uid": uid})
        print(response.json())
    except Exception as e:
        print("Error al enviar:", e)

print("Lector EM4100 activo. Ctrl+C para salir.")

try:
    while True:
        uid = leer_uid()
        if uid:
            print("UID leído:", uid)
            enviar_asistencia(uid)
            time.sleep(2)
except KeyboardInterrupt:
    print("\nLector detenido.")