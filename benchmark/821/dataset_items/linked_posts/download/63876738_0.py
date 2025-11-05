from subprocess import call
url = ""
call(["curl", {url}, '--output', "song.mp3"])
