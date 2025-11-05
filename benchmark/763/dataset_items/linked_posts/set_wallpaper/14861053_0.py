#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/opt/local/bin
size=1440
dest="/usr/local/share/backgrounds/wallpaperEAA.jpg"
read -r baseurl < <(lynx -nonumbers -listonly -dump 'http://www.eaa.org/en/eaa/aviation-education-and-resources/airplane-desktop-wallpaper' | grep $size) &&
wget -q "$baseurl" -O "$dest"
killall Dock
