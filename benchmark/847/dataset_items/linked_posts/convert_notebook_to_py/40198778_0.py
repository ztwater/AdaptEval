for i in *.ipynb **/*.ipynb; do 
    echo "$i"
    jupyter nbconvert  "$i" "$i"
done
