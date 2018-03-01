#!/usr/bin/env bash

a=(a b c d e)
for((i=0; i<${#a[@]}; i++))
do 
    echo "OUT: ${a[i]}"
    sleep 1
    echo "ERR: $i" >&2
    sleep 1
done
