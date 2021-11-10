import sys
import socket
import argparse

PROTOCOLO='tcp'
ADD='127.0.0.1'
arg_parse=argparse.ArgumentParser()
arg_parse.add_argumentosment('-d','--direccion', default=ADD)
arg_parse.add_argumentosment('-pc','--protocolo', default=PROTOCOLO)
arg_parse.add_argumentosment('-p','--puerto', default=5050)


argumentos=arg_parse.parse_args()
HEADER=1024
PUERTO =argumentos.PUERTO
HOST=argumentos.address

def main():
    if argumentos.type=='udp':
        cliente=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if argumentos.type=='tcp':
        cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if argumentos.type=='tcp':
        cliente.connect((HOST, PUERTO))
        reciv=cliente.recv(HEADER)
        
    if argumentos.type.upper()=='udp':
        print("Nueva conexion via udp")
        msj="Mensaje del server"
        cliente.sendto(msj.encode(), (HOST, PUERTO))
        reciv=cliente.recv(HEADER)
        
    for i in sys.stdin:
        if argumentos.type.upper()=='tcp':
            cliente.send(i.strip().encode())
        else:
            cliente.sendto(i.strip().encode(), (HOST, PUERTO))
        if i.strip()=='exit':
            cliente.close()
    cliente.sendto(''.encode(), (HOST, PUERTO))
    print("Cliente conectado",reciv.decode())
    cliente.close()
if __name__ == "__main__":
    main()