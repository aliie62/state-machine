import socket
from config.populate_table import create_table,empty_table, fill_table
from resources.state import StateResource


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

create_table()
empty_table()
fill_table()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.sendall(bytes('A\n','utf-8'))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            state = StateResource.move(data.decode())
            conn.sendall(bytes(state+'\n','utf-8'))