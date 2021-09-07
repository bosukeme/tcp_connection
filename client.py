import socket 
from time import sleep

host = socket.gethostbyname(socket.gethostname()) #socket.gethostname() 

port = 5050
BUFFER_SIZE = 2000 
# MESSAGE = input("tcpClientA: Enter message/ Enter exit:") 
# MESSAGE = MESSAGE + f" from {host}"
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

# while MESSAGE != 'exit':

#     tcpClientA.send(MESSAGE.encode())    
#     data = tcpClientA.recv(BUFFER_SIZE)
#     print(" Client received data:", data)
#     MESSAGE = input("tcpClient: Enter message to continue/ Enter exit:")

# tcpClientA.close() 


while True:
    MESSAGE = "heartbeat"
    tcpClientA.send(MESSAGE.encode())    
    data = tcpClientA.recv(BUFFER_SIZE)
    print(" Client received data:", data)
    sleep(15)


