import PyPDF2
from summarizer import *
#create file object variable
#opening method will be rb
def pdftotext(file):
    pdffileobj=open(file,'rb')
    
    #create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfReader(pdffileobj)
    
    #This will store the number of pages of this pdf file
    x=len(pdfreader.pages)

    val=''
    #create a variable that will select the selected number of pages
    for i in range (x):

        pageobj=pdfreader.pages[i]
    
    #(x+1) because python indentation starts with 0.
    #create text variable which will store all text datafrom pdf file
        text=pageobj.extract_text()

        val+=text
    val2 = " ".join(val.split())
    return val2

