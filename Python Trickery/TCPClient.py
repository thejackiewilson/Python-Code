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

# This code is a simple example of how to use the Python socket module to create a client-server application. It creates a socket object, connects to the server using the hostname and port number, sends an HTTP request message, and then receives and prints out the response from the server. This code can be used as a basis for building more complex applications that involve sending and receiving data over networks.
