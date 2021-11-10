import socket
import os
import argparse

PROTOCOLO='tcp'
ADD='127.0.0.1'
arg_parse=argparse.ArgumentParser()
arg_parse.add_argumentosment('-d', '--direccion', default=ADD)
arg_parse.add_argumentosment('-pc', '--protocolo', default=PROTOCOLO)
arg_parse.add_argumentosment('-a', '--archivo',help='path del documento/archivo')

argumentos=arg_parse.parse_args()
HOST='localhost'
PUERTO=argumentos.PUERTO
TYPE=argumentos
mensajes = []

def main():
    if argumentos.type==PROTOCOLO:
        servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        servidor=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    servidor.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    servidor.bind((HOST, PUERTO))

    print("Iniciando servidor...")
    if argumentos.type=='udp':
        data,addr=servidor.recvfrom(1024)
        print(f'UPD establecido {data.decode()}')
        servidor.sendto(TYPE.encode(), addr)
        
    if argumentos.type==PROTOCOLO:
        servidor.listen()
        socketCliente,addr=servidor.accept()
        servidor=socketCliente
        print("Nuevo usuario: {} // {}".format(addr[0], addr[1]))
        servidor.send(TYPE.encode())


    while True:
        mensaje=servidor.recv(1024)
        if mensaje:
            print("Recibimos su peticion")
            if mensaje.decode()=='exit':
                break
        if mensaje==bytes(0):
            file=os.open(argumentos.file ,os.O_RDWR|os.O_CREAT)
            for msjs in mensajes:
                os.write(file, msjs)
                os.write(file, b'\n')
            os.close(file)
            break
        else:
            mensajes.append(mensaje)
if __name__ == "__main__":
    main()