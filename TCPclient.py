#AUTHOR: VIVIAN LEUNG
#OCTOBER 24, 2017
#CMPE148, PROF: ROD FATOOHI

#TESTING INSTRUCTIONS:
#!RUN THE SERVER BEFORE THE CLIENT!
#IN TERMINAL, TYPE "python TCPserver.py" FOLLOWED BY "python TCPclient.py"
#ENJOY!
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #unlike UDP, uses SOCK_STREAM 
host = socket.gethostname() #unlike UDP, puts host & port in separate variables
port = 12345

client.connect((host, port)) #unlike UDP, connects to host & port

outgoingMsg = input("Type something here: \n")
client.send(outgoingMsg.encode('ascii')) #unlike UDP, uses send(msg)

response = client.recv(1024) #same as UDP
print(response.decode('ascii')) #same

client.close() #same 

