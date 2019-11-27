import PyPDF2

arquivo = r'/home/joaby/Área de Trabalho/Curso Python pro.pdf'

lerpdf = PyPDF2.PdfFileReader(arquivo)
pagina = lerpdf.getPage(0)
conteúdo = pagina.extractText()

print(conteúdo)
