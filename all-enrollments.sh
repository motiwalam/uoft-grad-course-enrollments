#!/bin/sh

cat "$1" | while read line; do 
	echo "doing $line" 1>&2
	./acorn.sh "$UTORID" "$PASSWORD" $line
done | jq -s | sed 's/: ",/",/g' | sed 's/ ",/",/g'

