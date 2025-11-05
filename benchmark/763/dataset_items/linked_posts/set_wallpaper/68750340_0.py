function wallpaper() {
    wallpaper_script="tell application \"Finder\" to set desktop picture to POSIX file \"$HOME/$1\""
    osascript -e $wallpaper_script 
}
