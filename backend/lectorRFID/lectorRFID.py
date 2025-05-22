#Este es el codigo del lector del RFID que usa como protocolo el EM4001/4100 
#Que simula entradas por teclado.
from datetime import datetime

def obtencionFecha():
    #Esta funcion obtendra la fehca y hora actual
    fecha=datetime.now()
    print(fecha)
    return fecha

def lecturaTarjeta():
    #Funcion para leer los datos que lanza el teclado el lector
    tarjeta=input("Acerca la tarjeta-->")
    print(tarjeta)
    return tarjeta

#   Iniciación del bucle
contador=0
while True:    
    lecturaTarjeta()
    obtencionFecha()
    contador+=1
    if contador >= 50:
        break 

