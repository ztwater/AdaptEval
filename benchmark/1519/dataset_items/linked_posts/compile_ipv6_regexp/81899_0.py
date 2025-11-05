import socket

def check_ipv6(n):
    try:
        socket.inet_pton(socket.AF_INET6, n)
        return True
    except socket.error:
        return False

print check_ipv6('::1') # True
print check_ipv6('foo') # False
print check_ipv6(5)     # TypeError exception
print check_ipv6(None)  # TypeError exception
