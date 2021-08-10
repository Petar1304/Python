from PyPDF2 import PdfFileWriter, PdfFileReader

file_name = 'MathematicalMethodsInPhysicalSciences.pdf'

pages_to_keep = [i for i in range(14, 829)]
infile = PdfFileReader(file_name, 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)