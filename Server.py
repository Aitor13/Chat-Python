# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:54:19 2020

@author: Aitor
"""

import socket
from threading import Thread


class Servidor():
    def __init__(self):
        self.clientes = []
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.bind( (socket.gethostname(),9081) )
        self.conn.listen(10)
        print('Servidor a la escucha...')
        
        # Creación de los hilos, en este caso dos, uno para la escucha de conexiones y otro para la escucha de recepción de avisos 
        Hilo_conexion = Thread(target = self.conexion, daemon=True)
        Hilo_conexion.start()
        Hilo_proceso = Thread(target = self.proceso_recepcion, daemon = True)
        Hilo_proceso.start() 
        
        while True:
            msg = input('orden: ')
            if msg == 'salir':
                self.conn.close()
                break
            else:
                pass
                          
        
    def conexion(self):
        while True:
            try:
                socketcliente, direccion = self.conn.accept() 
                socketcliente.setblocking(False) # Para poder enviar dos mensajes seguidos desde el mismo cliente, sino se bloquea el socket
                self.clientes.append(socketcliente)
                print('Ha llegado una solicitud desde ', direccion)
            except:
                pass
            
            
    def proceso_recepcion(self):
        while True:
               if len(self.clientes) > 0:
                   for c in self.clientes:
                       try:
                           mensaje = c.recv(1000)
                           tupla_mensaje = mensaje.decode('utf-8').split(';')
                           nombre = tupla_mensaje[0]
                           msg = tupla_mensaje[1]
                           self.envio_msg(f'{nombre}: {msg}'.encode('utf-8'), c)
                       except:
                           pass

            
    def envio_msg(self, mensaje, cliente):
        for c in self.clientes:
            try:
                c.send(mensaje)
            except:
                pass
         

if __name__ == '__main__':
    Servidor()

    




