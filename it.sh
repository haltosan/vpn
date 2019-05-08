#!/bin/bash

file="config"
while IFS=: read -r f1 f2 f3 f4 f5
do
        # display fields using f1, f2,..,f7
        printf 'First: %s, Second: %s, Third: %s, Fourth: %s, Fifth: %s\n' "$f1" "$f2" "$f3" "$f4" "$f5"
done <"$file"
