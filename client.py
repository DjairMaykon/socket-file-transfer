import socket

PORT = 8082
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
