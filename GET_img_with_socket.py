import socket, time

HOST = 'data.pr4e.org'
PORT = 80
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((HOST, PORT))
mysocket.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
  data = mysocket.recv(5120)
  if len(data) < 1: break
  time.sleep(0.25)
  count = count + len(data)
  print(len(data), count)
  picture = picture + data

mysocket.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print("Header length", pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()