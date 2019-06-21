#!/usr/bin/env sh

rm -r logs
mkdir logs
> log.txt
# for i in {$(1)..$(2)..$(3)}
for ((i = $1; i <= $2; i += $3));
do
    STRING="logs/"$i".txt" 
    bin/thor --amount $i ws://localhost:9000/ws > $STRING
done

python vis.py