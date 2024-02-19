import threading
import socket

alias = input('choose an alias>>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1',59000))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)    
        except:
            print('Error')
            client.close()
            break

def send_file():
    while True:
        filename = input('Input filename you need to send:') 
        try:
            
            fi = open(filename, 'r')
            data = fi.read() 
            if not data: 
                break
            while data: 
                client.send(str(data).encode()) 
                data = fi.read() 
            fi.close()
        except IOError:
            print('Entered filename is invalid')

def client_send():
    while True:
        message = f'{alias}:{input("")}'
        if message == '1':
            send_file()
        else:
            client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target = client_receive)
receive_thread.start()
send_thread = threading.Thread(target = client_send)
send_thread.start()