# Ganga Project - CERN-HSF - GSoC 2019

As part of the Ganga Project assignment for Google Summer of Code 2019, the codes and instructions have been put to execute the mentioned tasks in the [given file](https://drive.google.com/open?id=0BznbTbqEGKGyc3ZPME9TYTlpR3IydEM2NGFnenMtX1Nwazc0).

## Required Modules

1) [ganga](https://ganga.readthedocs.io/en/latest/)
2) [pdfminer](https://pypi.org/project/pdfminer/)
3) [PyPDF2](https://pypi.org/project/PyPDF2/)
4) [Jupyter](https://jupyter.org/)
5) [memory-profiler](https://pypi.org/pypi/memory_profiler/)

Since there was a Task Statement and Memory Management Statement, both have been discussed seperately in detail below.

## Task

First task was to execute a simple __Hello World___ job in the Ganga Shell whose output can be found here: [Ganga_Hello_World.ipynb](https://github.com/radonys/Ganga-Assignment/blob/master/Task/Ganga_Hello_World.ipynb). The Jupyter Notebook can be opened in the Colab Notebook whose link is available at the top of the notebook.

In the next task, the [given PDF file](https://github.com/radonys/Ganga-Assignment/blob/master/Task/CERN.pdf) needs to be seperated into individual pages. Next, the Ganga ```Job``` should count the number of ```the``` in the given PDF file. The count of individual pages should be performed using ```subjobs```. Finally, a ```merge``` needs to be written which takes the count from each subjob and adds up the values and writes it in a file.

In this regard, two helper modules/functions: [execute.sh](https://github.com/radonys/Ganga-Assignment/blob/master/Task/execute.sh) and [adder.py](https://github.com/radonys/Ganga-Assignment/blob/master/Task/adder.py) are written and explained below:

1) [execute.sh](https://github.com/radonys/Ganga-Assignment/blob/master/Task/execute.sh)

This file contains __bash__ commands which convert the individual PDF pages into text file and count the number of ```the``` existing in the file.

2) [adder.py](https://github.com/radonys/Ganga-Assignment/blob/master/Task/adder.py)

This file contains a __CustomMerger__ function which adds up all the counts and writes it in a output file.

The [Ganga_File_Split.ipynb](https://github.com/radonys/Ganga-Assignment/blob/master/Task/Ganga_File_Split.ipynb) notebook contains the commands and code for: 

1) Install and Import needed modules
2) Getting the required files
3) Split the PDF file to PDF pages
4) Commands to execute in the Ganga Shell

___Note___: I tried placing the code in a single Python file but while execution the __merger__ failed due to the job being in __submitted__ mode. Even after adding _time-delay_ nothing worked. Hence, commands need to be put manually in the Ganga Shell.

The file ___stdout___ in the current directory will contain the needed sum.

## Memory Management

For Memory Management, 4 tasks were given, out of which 3 were performed with all the requirements fulfilled. Please find the description of the performed experiments below:

1) There are two folders: [Deep Copy](https://github.com/radonys/Ganga-Assignment/tree/master/Memory-Management/Deep-Copy) and [Shallow Copy](https://github.com/radonys/Ganga-Assignment/tree/master/Memory-Management/Deep-Copy).
2) In Deep Copy folder, there are two python files:
    a) [deepcopy_delay-1.py](https://github.com/radonys/Ganga-Assignment/blob/master/Memory-Management/Deep-Copy/deepcopy_delay-1.py) executes the first task of performing deep copy of previous simple objects and monitors the memory usage.
    b) [deep-release_reference-2.py](https://github.com/radonys/Ganga-Assignment/blob/master/Memory-Management/Deep-Copy/deep-release_reference-2.py) executes the second task of releasing the reference of created objects one by one and observe the memory usage.
3) In Shallow Copy folder, there is one python file:
    - [shallow-release_reference-3.py](https://github.com/radonys/Ganga-Assignment/blob/master/Memory-Management/Shallow-Copy/shallow-release_reference-3.py) executes the same tasks as in the deep-copy case but using __shallow__ copy.

### Note

I checked for implementing the algorithm for using shallow-copy to mimic deep-copy (as described by Ulrik sir's in the email). I got an idea as well which is described below:

___Shallow Copy creates a new object and has only references from original object for the sub-objects within it. This can be shown below. To use shallow-copy and make it mimic like deep-copy, we have to make shallow-copies of the available sub-objects as well.___

## Results

1) Deep-Copy of Objects

![deep-copy-1](https://github.com/radonys/Ganga-Assignment/blob/master/Memory-Management/Deep-Copy/memory-usage-1.png "Deep Copy (Task 1) Memory Management")

2) Release Reference - Deep Copy

![deep-copy-2](https://github.com/radonys/Ganga-Assignment/blob/master/Memory-Management/Deep-Copy/memory-usage-2.png "Release Reference (Task 2) Memory Management")

3) Shallow Copy

![shallow-copy-3](https://github.com/radonys/Ganga-Assignment/blob/master/Memory-Management/Shallow-Copy/memory-usage-3.png "Shallow Copy (Task 3) Memory Management")