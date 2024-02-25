#!/bin/bash

n=$1

for i in $( seq 1 $n)
do
	python2 ./run.py ./assignment_B.py
done

