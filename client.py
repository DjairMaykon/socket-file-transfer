import socket
import os

PORT = 8080
HOST = 'localhost'

def depositFile(filename, tolerancia):
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print('Connection Established.')
    
    sock.send(f'DEPOSIT#{filename}#{tolerancia}'.encode())
    response = sock.recv(1024).decode()
    print(f'Response: {response}\n')

    with open(filename, "rb") as readFile:
          while True:
              fileBytes = readFile.read(1024)
              if not fileBytes:
                break
              sock.sendall(fileBytes)

    print('File has been send successfully.')

    sock.close()
    print('Connection Closed.')

def listServerFiles():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print('Connection Established.')
    
    sock.send(f'LIST'.encode())
    response = sock.recv(1024).decode()

    sock.close()
    print('Connection Closed.')

    return response.split(',')

def restoreFile(filename):
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print('Connection Established.')
    
    sock.send(f'RESTORE#{filename}'.encode())
    response = sock.recv(1024).decode()
    print(f'Response: {response}\n')

    filesRestoredPath = f'{os.path.abspath(os.getcwd())}/files_restored'
    os.makedirs(filesRestoredPath, exist_ok=True)

    with open(f'{filesRestoredPath}/{filename}', "wb") as f:
        while True:
            fileBytes = sock.recv(1024)
            if not fileBytes:    
                break
            f.write(fileBytes)

    print('File has been restored successfully.')

    sock.close()
    print('Connection Closed.')
