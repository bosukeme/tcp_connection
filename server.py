import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER ="" #socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((SERVER, PORT))

def handle(conn, addr):
    print(f"New Connection::::::: {addr} connected. ")

    connnected = True
    while connnected:
        msg = conn.recv(2048)#.decode(FORMAT)

        if msg == "exit":
            connnected = False
        print(f"{addr} == {msg}")
        conn.send("Message received".encode(FORMAT))
    conn.close()


def start():
    s.listen()
    print(f"server is listening on {SERVER}")
    while True:
        conn, addr = s.accept()

        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()
        print(f"Active threads {threading.activeCount() -1}")



print(f"server is starting...")
start()
