import socket

host, port = 'localhost', 8005
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))
response = ""
myNumber = -1

print("-\nУгадай загаданное сервером число (от 0 до 100). Игра закончится, когда число будет угадано. \n-\n")

while (response != "correct"):
	myNumber=input("Введите ваше предполагаемое число от 0 до 100:\t")
	try:
		myNumber = int(myNumber)
		if myNumber >= 0 and myNumber <= 100:
			client.send(("guess "+str(myNumber)).encode())
			response = client.recv(4096).decode('utf-8')
			print(response)
		else:
			continue
	except ValueError:
		continue

