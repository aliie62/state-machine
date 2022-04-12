import time
import socket
import re
import graphviz
import string
import signal
import sys

HOST = "127.0.0.1"
PORT = 65432  # The port used by the server


def save_sm(transitions):
    dot = graphviz.Digraph(comment='The state machine')
    for letter in string.ascii_uppercase:
        dot.node(letter)
    dot.edges(transitions)
    dot.render('The_state_machine')

def main():
    print('\n',"Press contrl+c at any time to stop the pragram and save the discovered graph.",'\n')
    transitions=[]

    def sigint_handler(signal, frame):
        print('\n','The discovered graph will be saved shortly')
        print('The application will be closed in 3 seconds...')
        save_sm(list(set(transitions)))
        time.sleep(3)
        sys.exit(0)
    signal.signal(signal.SIGINT, sigint_handler)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        response = s.recv(1024).decode()

        start = ''
        end = ''

        while True:
            print(f"Server: {response}")
            node = re.sub('\n','',response).strip()
            if len(node)==1:
                if not start:
                    start = node
                else:
                    transitions.append(start+node)
                    start = node  
                
            option = input("Client: ")
            s.sendall(bytes(option+'\n','utf-8'))
            response = s.recv(1024).decode()

  

if __name__=='__main__':
    main()