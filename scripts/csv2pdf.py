#! /usr/bin/env python

###############################################################################
#
#  Created:    29.10.2021
#  Authors:    Xiaoxia CHEN
#              
###############################################################################
import csv

with open('info/CCCC_en.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
	
from fpdf import FPDF     
pdf = FPDF()
pdf.add_page()
page_width = pdf.w - 2 * pdf.l_margin
		
pdf.set_font('Times','B',14.0) 
pdf.cell(page_width, 0.0, 'CCCC List', align='C')
pdf.ln(10)

pdf.set_font('Courier', '', 12)
	
col_width = page_width/3
	
pdf.ln(1)
	
th = pdf.font_size
	
for row in reader:
        #print(row)
    pdf.cell(col_width, th, str(row[0]), border=1)
    pdf.cell(col_width, th, row[1], border=1)
    pdf.cell(col_width, th, row[2], border=1)
    pdf.ln(th)
		
pdf.ln(10)

pdf.set_font('Times','',10.0) 
pdf.cell(page_width, 0.0, '- end of report -', align='C')
	
pdf.output('CCCC_en.pdf', 'F')
