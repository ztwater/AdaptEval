#!/bin/bash

name=`curl $1 |  grep -w \"name\" | sed 's/.*"name" content="//' | 
sed 's/".*//'`
id=`echo $1 | sed 's#.*/d/##; s#/view.*##'`
curl -L https://drive.google.com/uc?id=$id > $name
# or
# wget -O $name https://drive.google.com/uc?id=$id
