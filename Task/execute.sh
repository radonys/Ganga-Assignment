#!/bin/bash

execute()
{
	pdf2txt.py $1 > output.txt
	echo $(egrep -ow 'the|The' output.txt | wc -l)
}

execute $1
