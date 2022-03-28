import tabula

file = '/home/petar/Documents/pdf_csv/smerovi.pdf'
csv = '/home/petar/Documents/pdf_csv/smerovi.csv'

tabula.convert_into(file, csv, output_format='csv', pages='all')