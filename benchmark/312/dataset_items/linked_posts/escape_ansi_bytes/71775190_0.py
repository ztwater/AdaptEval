#! /usr/bin/env python3

import pyte # terminal emulator: render terminal output to visible characters

pyte_screen = pyte.Screen(80, 24)
pyte_stream = pyte.ByteStream(pyte_screen)

bytes_ = b''.join([
  b'$ cowsay hello\r\n', b'\x1b[?2004l', b'\r', b' _______\r\n',
  b'< hello >\r\n', b' -------\r\n', b'        \\   ^__^\r\n',
  b'         \\  (oo)\\_______\r\n', b'            (__)\\       )\\/\\\r\n',
  b'                ||----w |\r\n', b'                ||     ||\r\n',
  b'\x1b]0;user@laptop1:/tmp\x1b\\', b'\x1b]7;file://laptop1/tmp\x1b\\', b'\x1b[?2004h$ ',
])
pyte_stream.feed(bytes_)

# pyte_screen.display always has 80x24 characters, padded with whitespace
# -> use rstrip to remove trailing whitespace from all lines
text = ("".join([line.rstrip() + "\n" for line in pyte_screen.display])).strip() + "\n"
print("text", text)

print("cursor", pyte_screen.cursor.y, pyte_screen.cursor.x)
print("title", pyte_screen.title)
