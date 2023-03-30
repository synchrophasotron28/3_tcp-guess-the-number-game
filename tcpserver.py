import socket
import threading
import random

host, port = 'localhost', 8005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print('Listen:  {}:{}'.format(host, port))


def client_connection(client_socket):
	hiddenNumber = random.randint(0,100)
	playerNumber = -5
	while (playerNumber != hiddenNumber):
		request = client_socket.recv(4096)
		str_request = request.decode('utf-8')
		playerNumber = int(str_request[6:])
		if playerNumber < hiddenNumber:
			client_socket.send('more'.encode())
		elif playerNumber > hiddenNumber:
			client_socket.send('less'.encode())
		elif playerNumber == hiddenNumber:
			client_socket.send('correct'.encode())
		else:
			print("неправильный формат числа")
			client_socket.send('Неправильный формат числа'.encode())
	client_socket.close()

while True:
	client_sock, address = server.accept()
	print('Новое подключение с {}:{}'.format(address[0], address[1]))
	client_handler = threading.Thread(
		target=client_connection,
		args=(client_sock,)
	)
	client_handler.start()