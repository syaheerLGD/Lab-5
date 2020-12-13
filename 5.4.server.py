import socket
import os
import tqdm


pemisah = "<SEPERATOR>"
bufferSize = 4096


s = socket.socket()
print("Socket successfully created")


port = 8080


s.bind(("", port))
print("socket binded to " + str(port))


s.listen(5)
print("socket is listening")


c, addr = s.accept() #accept connection if there is any
print("Got connection from " + str(addr))


received = c.recv(bufferSize).decode()
filename, filesize = received.split(pemisah)

filename = os.path.basename(filename)
filesize = int(filesize)


progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
	for _ in progress:
		bytes_read = c.recv(bufferSize)
		if not bytes_read:
			break

		f.write(bytes_read)

		progress.update(len(bytes_read))

c.close()
