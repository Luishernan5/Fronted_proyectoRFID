import time
import requests
from datetime import datetime

def leer_uid():
    return input("Ingrese el UID (o 'salir' para terminar): ").strip()

def enviar_asistencia(uid):
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = requests.post("http://localhost:5000/frontRasperry/terminal_logo_tesji.html", json={"uid": uid})
        print(f"[{ahora}] Respuesta del servidor:", response.json())
    except Exception as e:
        print(f"[{ahora}] Error al enviar:", e)

print("Sistema de registro manual activo. Ctrl+C o escribir 'salir' para salir.")

try:
    while True:
        uid = leer_uid()
        
        if not uid:
            continue
            
        if uid.lower() == 'salir':
            break
            
        print(f"\nRegistrando UID:", uid)
        enviar_asistencia(uid)
        
except KeyboardInterrupt:
    print("\nPrograma interrumpido.")
finally:
    print("Sistema detenido.")