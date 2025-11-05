import socket

def isValid(url):
    if url.startswith("https://www.") or url.startswith("http://www."):
        try:
            socket.create_connection((url, 80))
            return True
        except socket.gaierror:
            return False
        except OSError:
            return False
    else:
        return False
