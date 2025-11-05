# p3 code
def safePath (url):
    return ''.join(map(lambda ch: chr(ch) if ch in safePath.chars else '%%%02x' % ch, url.encode('utf-8')))
safePath.chars = set(map(lambda x: ord(x), '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-_ .'))
