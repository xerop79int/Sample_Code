import socket
import random			

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
ip = '127.0.0.1'
port = 12345			
s.bind((ip, port))		
s.listen()	
print ("socket is listening")		

while True:

	# Establish connection with client.
	client, addr = s.accept()	
	print ('Got connection from', addr )

	# send a thank you message to the client. encoding to send byte type.
	I = client.recv(1024).decode()

	N = random.randint(1, 10)
	
	client.send(str(N).encode())

	message = ""

	for i in range(1, N + 1 ):
		message += str(int(I) * i) + ", " 

	message += str(0) + "."

	if (client.recv(1024).decode() == message):
		print("\nCorrect!!")
	else:
		print("\nIncorrect!!")

	client.close()

	# Breaking once connection closed
	break
