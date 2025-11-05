# 7-bit and 8-bit C1 ANSI sequences
ansi_escape_8bit = re.compile(
    br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])'
)
result = ansi_escape_8bit.sub(b'', somebytesvalue)
