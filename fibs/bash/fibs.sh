#!/bin/bash

function fibs {
    if (( $1 <= 1 )); then
	echo "1"
    else
	echo $(( $(fibs $(($1 - 1))) + $(fibs $(($1 - 2))) ))
    fi
}

fibs $1
