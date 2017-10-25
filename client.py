import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345



outgoingMsg = input("Type something here: \n")
client.send(outgoingMsg.encode('ascii'), (host, port))

response, address = client.recv(1024)

client.close()

print(response.decode('ascii'))