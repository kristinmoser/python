'''
cs1122
username: km3322
name: Kristin Moser
this was not for python class.
this was for my intro to compsci class.
it sets up a server at port 50000

'''

import socket 

host = '' 
port = 50000 
bl = 5 
size = 1024 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((host,port)) 
sock.listen(bl) 
while 1: 
    client, address = s.accept() 
    data = client.recv(size) 
    if data: 
        client.send(data) 
    client.close()
