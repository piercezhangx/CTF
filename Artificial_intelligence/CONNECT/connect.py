#!/usr/bin/env python

import socket
import pdb

def get_ip_status(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,port))
    server.settimeout(5)
    #pdb.set_trace()
    server.send("HELLO\n")
    data = server.recv(4096)
    #data = data.replace("\r\n", "\n")
    #print('{0} port {1} is open'.format(ip, port))
    print(data)
    server.send("GET_DATA_SIZE\n")
    #data = server.recv(3113421)
    data = server.recv(1024)
    print data

    server.send("GET_DATA_SIZE\n")
    #data = server.recv(3113421)
    data = server.recv(1024)
    print data
    server.close()

if __name__ == '__main__':
    host = '10.97.163.102'
    port = 9999
    get_ip_status(host,port)
