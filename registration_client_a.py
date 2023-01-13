#!/usr/bin/env python3

# Python TCP Client A
import socket 
import os

host = 'clouddatabases.msrg.in.tum.de'#socket.gethostname() 
port = 5551
# host = '0.0.0.0'#socket.gethostname() 
# port = 52923
BUFFER_SIZE = 1024
message = "ga53wuz@tum.de"
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))


encoded_message = message.encode('utf8')
size = 1024
message_bytes = bytes(size)
# message_bytes = os.urandom(1000)
# tcpClientA.send(message_bytes)
tcpClientA.send(encoded_message)  
data = tcpClientA.recv(BUFFER_SIZE)
decoded_data = data.decode('utf8')
print( "Client2 received data:"+ decoded_data)


tcpClientA.close() 