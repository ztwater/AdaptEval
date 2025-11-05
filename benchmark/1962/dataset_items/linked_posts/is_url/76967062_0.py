import socket

def isValid(url):
    #connect to the host -- tells us if the host is actually reachable
    try:
        socket.create_connection((url, 80))
        return True
    except socket.gaierror:
        return False
    except OSError:
        return False

A socket.gaierror occurs if the url is not valid, and an OSErrors occurs when you are not connected.
