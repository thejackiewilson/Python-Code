import socket  

target_host = "www.example.com"
target_port = 8080

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
