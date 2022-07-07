import socket
import sys
Target_IP = "127.0.0.1"
Port = 12345
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
I = int(input("Enter a Positive Integer:"))

if I <= 0:
	
	print("You haven't Enter the Positve number Please enter correct number")
	exit(1)

else:
	
	clientSocket.connect((Target_IP, Port))

	clientSocket.send(str(I).encode())

	N = clientSocket.recv(1024).decode()

	message = ""

	for i in range(1, int(N) + 1 ):
		message += str(I * i) + ", " 

	message += str(0) + "."

	clientSocket.send(message.encode())
	
	clientSocket.close()