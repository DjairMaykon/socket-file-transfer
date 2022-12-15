import socket
import os
import shutil

PORT = 8082
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
    
    filesReceivedPath = f'{os.path.abspath(os.getcwd())}/files_received'
    os.makedirs(filesReceivedPath, exist_ok=True)

    if option == 'DEPOSIT':
        filename = dataArray[1]
        filePath = f'{filesReceivedPath}/{filename}_folder'
        os.makedirs(filePath, exist_ok=True)

        data = str.encode('Iniciando deposito')
        con.sendall(data)

        with open(f'{filePath}/{filename}', "wb") as f:
            while True:
                fileBytes = con.recv(1024)
                if not fileBytes:    
                    break
                f.write(fileBytes)

        tolerancia = int(dataArray[2])
        for i in range(tolerancia):
            shutil.copy(f'{filePath}/{filename}', f"{filePath}/{filename}_{i}")
    elif option == 'LIST':
        filesReceivedDirList = []
        for f in os.scandir(filesReceivedPath):
            if f.is_dir():
                filesReceivedDirList.append(f.name.split('_folder')[0])
        print(','.join(filesReceivedDirList).encode())
        con.send(','.join(filesReceivedDirList).encode())

    con.close()