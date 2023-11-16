# client and server is connected thru ip address and port.
# run server first.

import socket as sk
import random as rnd

# localhost, server connection.
host = 'localhost'
port = str(input('Port: '))
if(len(port) == 0):
    print('default: 12345')
    port = 12345

# Establish connection, waits for client to connect.
server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server_socket.bind((host,int(port)))
server_socket.listen(5)
print(f'Server listening on port {port}...')

while True:
    auth = False
    # First phase: Authentication
    
    client_socket, client_address = server_socket.accept()
    
    print('Awaiting authentication details from {}:{}'.format(client_address[0], client_address[1]))
    
    account = {'name':['ren','ken'],'password': [1234,4321]}
    
    # assumes client gives username and password
    acc_data = client_socket.recv(1024)
    if not acc_data:
        break
    acc_data_decoded = acc_data.decode()
    
    x = str(acc_data_decoded)
    try:
        x = x.split()
        print(f'\nUsername input received: {x[0]}\nPassword input received: {x[1]}')
    except:
        print('error input')
        
    
    # checking phase here ---
    for name,password in zip(account['name'],account['password']):
        if(x[0] == name and int(x[1]) == password):
            print('\nClient verified, now connected.\n')
            
            response = 'Authenticated, Welcome to Guessing Game!'
            client_socket.send(response.encode())
            auth = True
            break
            
    if(auth == False):
        """ response = 'Authentication Failure'
        client_socket.send(response.encode()) """
        print('\nAuth Failed. Client denied.\n')
    else:
    
    # Second phase: guess game
    
        print('Guess Game initiated')
        while True:
            # print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
            data = client_socket.recv(1024) #bit by bit
            if not data:
                break
            client_input = str(data.decode())
            print(client_input)
            
            server_response = 'Now Guess! -> (1 to 100)'
            client_socket.send(server_response.encode())
            
            rnd_num = rnd.randrange(1,101) # 1 to 10
            print(f'target number: {rnd_num}')
            while True:
                
                data = client_socket.recv(1024) #bit by bit
                if not data:
                    break
                client_input = int(data.decode())
                
                print(f'user attempt: {client_input}')
                
                if(client_input > rnd_num):
                    server_response = "-- Lower --"
                    client_socket.send(server_response.encode())
                elif(client_input < rnd_num):
                    server_response = '-- Higher --'
                    client_socket.send(server_response.encode())
                elif(client_input == rnd_num):
                    server_response = "Correct! You is winner!!!!"
                    client_socket.send(server_response.encode())
                    break
                    
                
            break # temporary
    
    client_socket.close()
    
    

client_socket.close()