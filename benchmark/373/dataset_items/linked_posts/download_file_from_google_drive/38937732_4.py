echo "gURL" | sed 's/[^A-Za-z0-9_-]/\n/g' | sed -rn '/.{26}/p'  
# replace non-word characters with new line,   
# print only line with more than 26 word characters 
