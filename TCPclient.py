import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

client.connect((host, port))

outgoingMsg = input("Type something here: \n")
client.send(outgoingMsg.encode('ascii'))
response = client.recv(1024)

client.close()

print(response.decode('ascii'))