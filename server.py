import socket
import os
import shutil

PORT = 8800
HOST = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
print(f'Socket is listening on {HOST}:{PORT}...')

while True:
    con, addr = sock.accept()
    print(f'Connected with {addr}')

    data = con.recv(1024).decode()
    print(f'Request: {data}')
    dataArray = data.split('#')
    option = dataArray[0]
    filename = dataArray[1]
    
    filePath = f'{os.path.abspath(os.getcwd())}/files_received/${filename}_folder'
    print(filePath)
    os.makedirs(filePath, exist_ok=True)

    if (dataArray[0] == 'DEPOSIT'):
        data = str.encode('Iniciando deposito')
        con.sendall(data)

        tolerancia = int(dataArray[2])
        with open(f'{filePath}/{filename}', "wb") as f:
            while True:
                fileBytes = con.recv(1024)
                if not fileBytes:    
                    break
                f.write(fileBytes)

    for i in range(tolerancia):
        shutil.copy(f'{filePath}/{filename}', f"{filePath}/{filename}_{i}")

    con.close()