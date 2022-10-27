from hashlib import new
import PyPDF2

file = open('a.pdf', 'rb')

fileReader = PyPDF2.PdfFileReader(file)

qstData = {}
text_cache = ''

questionNumber = 1
active = 0


print(qstData.keys())


for page in fileReader.pages:
    for text in page.extract_text():

        text_cache += f'{text}'
        
        if text == f'{questionNumber}':
            active = 1
        if active == 1 and text == '.':
            active = 0
            qstData[f'{questionNumber}']  = f'{text_cache}'
            text_cache = ''
            break
    break
print(qstData['1'])
    