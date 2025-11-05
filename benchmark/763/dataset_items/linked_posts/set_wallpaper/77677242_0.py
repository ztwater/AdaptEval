SCRIPT = """/usr/bin/osascript<<END
tell application "System Events"
tell every desktop
 set picture to "%s"
end tell
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)
