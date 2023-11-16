# note to self, client must response to receive server response, 1:1

import socket as sk

client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

print("-- Client Terminal --")

# Attempt connection to a server first.
print('\n- (Leave blank for default) -')
host = str(input('Host: '))
port = str(input('Port: '))

if(len(host) == 0):
    print('default: localhost')
    host = 'localhost'
if(len(port) == 0):
    print('default: 12345')
    port = 12345
print('\nConnecting...')
client_socket.connect((host,int(port)))
print('Connected!\n')

# Attempt authentication to the server.

username = str(input('Username: ')).lower()
password = str(input('Password: ')).lower()

# encode client response
client_response = username + ' ' + password
client_socket.send(client_response.encode())

# decode server response
server_response = client_socket.recv(1024)
server_response_decoded = str(server_response.decode())

# if auth fails, repeat the input.
if(server_response_decoded == 'Authenticated, Welcome to Guessing Game!'):
    print(f'\n-- {server_response_decoded} --')
    
    client_response = 'client is on standby'
    client_socket.send(client_response.encode())
    
    server_response = client_socket.recv(1024)
    server_response_decoded = server_response.decode()
    print(f'\nServer: {server_response_decoded} ')
else:
    print('Auth failed!')
    exit()


# Assume connected, able to communicate with target server.
while True:
    client_input = input('Response to Server: ')
    
    # Encode client input and send to server
    message = f'{client_input}'
    client_socket.send(message.encode())

    server_response = client_socket.recv(1024)
    
    # Decode the server response and print
    server_response_decoded = server_response.decode()
    print(f'\nServer: {server_response_decoded} ')
    
    if(server_response_decoded == 'Correct! You is winner!!!!'):
        print('Game Exiting')
        break
    # client_socket.close()
    
client_socket.close()
