from PyPDF2 import PdfFileReader,PdfFileWriter
from os import listdir,path
nome = input('Inserisci il nome del file per il merge...')
writer = PdfFileWriter()
lista = listdir()
for nomeFile in lista:
    try:
        if path.isfile(nomeFile) and nomeFile.upper().endswith(".PDF"):
            readerPdf = PdfFileReader(nomeFile)
            for page in range(readerPdf.getNumPages()):
                writer.addPage(readerPdf.getPage(page))
    except(Exception) as ex:
        print(ex.args)
try:               
    pdfDestinazione = open(nome +'.pdf','wb')#w=write b=binary     
    writer.write(pdfDestinazione)
    print(f'Merge eseguito correttamente')
except(Exception) as ex:
    print(ex.args)
finally:
    pdfDestinazione.close()