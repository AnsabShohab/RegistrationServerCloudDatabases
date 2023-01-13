#!/usr/bin/env python3
from queue import Empty
import socket 
from threading import Thread 
from socketserver import ThreadingMixIn 
import logging
import threading
import time
import os
from datetime import datetime

# Multithreaded Python server : TCP Server Socket Thread Pool
logging.basicConfig(filename='registration-server-data/server_log.log', level=logging.DEBUG)

class ClientThread(Thread): 
 
    def __init__(self, conn, ip,port): 
        Thread.__init__(self)
        self.conn = conn
        self.ip = ip 
        self.port = port
        self.lock = synchronization_lock
        logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " [+] New server socket thread started for " + ip + ":" + str(port)) 
 
    def run(self): 
        data = self.conn.recv(BUFFER_SIZE)
        if(len(data) > 1024):
            message = "Your message was greater than 1024 bytes."
            encoded_message = message.encode('utf8')
            self.conn.send(encoded_message)
            return
        else:
            try:
                decoded_data = data.decode('utf8')
            except:
                logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) +  " Socket thread for "+str(self.ip)+":"+str(self.port)+ " The sent message wasn't properly encoded with utf-8")
                message = "Your message wasn't properly encoded with utf-8"
                encoded_message = message.encode('utf8')
                self.conn.send(encoded_message)
                return
            if(len(decoded_data)<100):        
                logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " Data received by the Server")
                decoded_data = decoded_data.strip()
                student_registered= False
                if os.path.isfile('registration-server-data/data_file.txt'):
                    data_file = open("registration-server-data/data_file.txt", "r")
                    for registered_student in data_file:
                        if registered_student.strip() == decoded_data:
                            logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) +  " Socket thread for "+str(self.ip)+":"+str(self.port)+ " Student already registered.")
                            message = "You are already registered."
                            encoded_message = message.encode('utf8')
                            self.conn.send(encoded_message)
                            student_registered = True
                            break
                    data_file.close()
                if not student_registered:
                    self.lock.acquire()
                    try:
                        logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) +  " Socket thread for "+str(self.ip)+":"+str(self.port)+ " acquiring the lock for the data file")
                        data_file = open("registration-server-data/data_file.txt", "a")
                        data_to_write = decoded_data + "\n"
                        data_file.write(data_to_write)
                        data_file.close()
                        #time.sleep(10)
                    except:
                        logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) +  " Socket thread for "+str(self.ip)+":"+str(self.port)+ " Exception in writing to data_file.txt")
                        return
                    finally:
                        logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " Socket thread for "+str(self.ip)+":"+str(self.port)+ " realeasing the lock for the data file")
                        self.lock.release()
                    message = decoded_data
                    encoded_message = message.encode('utf8')
                    self.conn.send(encoded_message)
                return
            else:
                logging.info( str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) +  " Socket thread for "+str(self.ip)+":"+str(self.port)+ " The registration number or email that sent had unsually large number number of characters")
                message = "The registration number or email that you sent has unsually large number number of characters."
                encoded_message = message.encode('utf8')
                self.conn.send(encoded_message)
                return


TCP_IP = '0.0.0.0' 
TCP_PORT = 52923 
BUFFER_SIZE = 2048  


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = []
synchronization_lock = threading.Lock()
 
while True: 
    tcpServer.listen() 
    logging.info(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " Multithreaded Python server : Waiting for connections from TCP clients...") 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(conn, ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 

