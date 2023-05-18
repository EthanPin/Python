import socket

host='127.000.000.000' #use your ip

port=6000

SOCC=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

SOCC.bind(("",port))

while 1:
	#clientaddr
	data, addr= SOCC.recvfrom(1024)
	data=data.decode('utf-8')
	print(data)
