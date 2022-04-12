import socket
import re
import graphviz
import string

HOST = "20.211.33.233"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
transitions=[]

def save_sm(transitions):
    dot = graphviz.Digraph(comment='The state machine')
    for letter in string.ascii_uppercase:
        dot.node(letter)
    dot.edges(transitions)
    dot.render('The_state_machine')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    response = s.recv(1024).decode()

    start = ''
    end = ''

    while True: 
        print(f"Server: {response}")
        node = re.sub('\n','',response).strip()
        if node != 'Z':
            if not start:
                start = node
            else:
                transitions.append(start+node)
                start = node              
        else:
            transitions.append(start+node)
            transitions.append(('ZA'))
            save_sm(list(set(transitions)))
            break
        
        option = input("Client: ")
        s.sendall(bytes(option+'\n','utf-8'))
        response = s.recv(1024).decode()
        

