import socket
import tqdm
import os


pemisah = "<SEPERATOR>"
bufferSize = 4096 #send 4096 bytes each time step

filename = "ClientProfile.txt" #the name of file we want to send from the same directory
filesize = os.path.getsize(filename)
#/home/maribelajar/ITT440/Lab-5/ClientProfile.txt

port = 8080


s = socket.socket()

s.connect(('192.168.0.200', port))


s.send(f"{filename}{pemisah}{filesize}".encode()) #send the filename and filesize


progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit = "B", unit_scale = True, unit_divisor = 1024)
with open(filename, "rb") as f:
        for _ in progress:
                bytes_read = f.read(bufferSize) #read the bytes from the file
                if not bytes_read:
                        break #file transmiting is done

                s.sendall(bytes_read)

                progress.update(len(bytes_read))


s.close()
