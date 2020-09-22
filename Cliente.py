# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:54:34 2020

@author: Aitor
"""

import socket
from threading import Thread


class Cliente():
    def __init__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((socket.gethostname(), 9081))
        
        hilo_escucha = Thread(target = self.escucha, daemon = True)
        hilo_escucha.start()
        
        while True:
            msg = input('Mensaje: ')
            if msg == 'salir':
                self.conn.close()
                break
            else:
                self.envio_mensaje(msg)

        
    def escucha(self):
        while True:
            try:
                mensaje = self.conn.recv(1000).decode('utf-8')
                if mensaje:
                    print(mensaje)
            except:
                pass
    
    def envio_mensaje(self, mensaje):
        self.conn.send(bytes(mensaje.encode('utf-8')))
         
    

if __name__ == '__main__':
    Cliente()