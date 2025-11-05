import socket
sock = socket.socket()
sock.bind(('', 0))
sock.getsockname()[1]
