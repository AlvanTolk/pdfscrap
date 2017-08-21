#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.converter import TextConverter
#from pdfminer.converter import XMLConverter
#from pdfminer.layout import LAParams
#from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO




def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    laparams.line_margin=1.1


    print laparams
    print rsrcmgr
    device = XMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    #device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    outstring = retstr.getvalue()
    retstr.close()

    return outstring


import sys


print "running..."
#fullstring=convert_pdf_to_txt("AP30Ae0756.pdf")
#f = open("output.xml","w")
#f = open("output.txt","w")
#f.write(fullstring)
#f.close()
#print "Done!"

from pdftables.pdf_document import PDFDocument
from pdftables.pdftables import page_to_tables


filepath = "AP30Ae0756.pdf"
fileobj = open(filepath,'rb')
doc = PDFDocument.from_fileobj(fileobj)

page = doc.get_page(23)
tables = page_to_tables(page)
print tables

