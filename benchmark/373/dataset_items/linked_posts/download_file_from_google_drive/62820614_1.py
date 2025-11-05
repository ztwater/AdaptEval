set cookieFile="cookie.txt"
set confirmFile="confirm.txt"
   
REM downlaod cooky and message with request for confirmation
wget --quiet --save-cookies "%cookieFile%" --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=%fileid%" -O "%confirmFile%"
   
REM extract confirmation key from message saved in confirm file and keep in variable resVar
jrepl ".*confirm=([0-9A-Za-z_]+).*" "$1" /F "%confirmFile%" /A /rtn resVar
   
REM when jrepl writes to variable, it adds carriage return (CR) (0x0D) and a line feed (LF) (0x0A), so remove these two last characters
set confirmKey=%resVar:~0,-2%
   
REM download the file using cookie and confirmation key
wget --load-cookies "%cookieFile%" -O "%filename%" "https://docs.google.com/uc?export=download&id=%fileid%&confirm=%confirmKey%"
   
REM clear temporary files 
del %cookieFile%
del %confirmFile%
