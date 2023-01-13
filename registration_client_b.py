#!/usr/bin/env python3
# Python TCP Client B
import socket
import os

host = 'clouddatabases.msrg.in.tum.de'#socket.gethostname() 
port = 5551
# host = '0.0.0.0'#socket.gethostname() 
# port = 52923
BUFFER_SIZE = 1024 
message = "03694122\r\n"
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))


encoded_message = message.encode('utf8')
# size = 1024
# message_bytes = bytes(size)
# message_bytes = os.urandom(1000)
# print(str(len(message_bytes)))
# tcpClientB.send(message_bytes)
tcpClientB.send(encoded_message)     
data = tcpClientB.recv(BUFFER_SIZE)
decoded_data = data.decode('utf8')
print("Client received data:" + decoded_data)

tcpClientB.close() 