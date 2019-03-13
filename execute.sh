#!/bin/bash

execute()
{
	pdf2txt.py $1 > output.txt
	echo $(tr -s ' ' '\n' < output.txt | grep the | wc -l)
}

execute $1
