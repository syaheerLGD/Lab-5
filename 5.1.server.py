import socket


s = socket.socket()
print("Berjaya buat soket")


port = 8888

s.bind(("", port))
print("Berjaya bind soket di port " + str(port))


s.listen(5)
print("Soket sedang menunggu client!")


while True:

	c, addr = s.accept()
	print("Dapat capaian dari " + str(addr))


	c.send(b'Terima Kasih!')
	buffer = c.recv(1024)
	print(buffer)

c.close()
