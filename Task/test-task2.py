from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import time
import keyboard

filepath = os.popen('pwd').read()
filepath = filepath.split('\n')
filepath = filepath[0] + '/'
arguments = []

inputpdf = PdfFileReader(open("CERN.pdf", "rb"))

for i in range(inputpdf.numPages):
    
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("page%s.pdf" % str(i+1), "wb") as outputStream:
        output.write(outputStream)

    temp = []
    temp_path = filepath + "page" + str(i+1) + ".pdf"
    temp.append(temp_path)
    arguments.append(temp)
    
print(arguments)

addmerge = CustomMerger()
addmerge.files = ['stdout']
addmerge.module = File(filepath + 'adder.py')
addmerge.ignorefailed = True
addmerge.overwrite = False

s = ArgSplitter(args=arguments)
j = Job(splitter=s)
j.application.exe = File(filepath + 'execute.sh')
j.merger = addmerge
j.submit()