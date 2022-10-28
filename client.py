from hashlib import new
import PyPDF2

file = open('a.pdf', 'rb')

fileReader = PyPDF2.PdfFileReader(file)

qstData = {}
text_cache = ''

questionNumber = 1
secondNumber = -1
secondNumberActive = False
active = 0

for page in fileReader.pages:
    for text in page.extract_text():

        text_cache += f'{text}'        
        
        if text == f'{questionNumber}':
            active = 1
        if active == 1:
            if text == f'{secondNumber}' and secondNumberActive:
                pass
            elif text == '.':
                active = 0
                key = questionNumber if not secondNumberActive else questionNumber*10 + secondNumber
                qstData[f'{key}']  = f'Q{questionNumber - 1}{text_cache[:-2]}'
                text_cache = ''
                if questionNumber == 9:
                    questionNumber = 1
                    secondNumberActive = True

                elif not secondNumberActive:
                    questionNumber += 1
                if secondNumberActive:
                    if secondNumber == 9:
                        secondNumber = 0
                        questionNumber += 1
                    else:
                        secondNumber += 1
key = questionNumber if not secondNumberActive else questionNumber*10 + secondNumber
qstData[f'{key}']  = f'Q{questionNumber - 1}{text_cache[:-2]}'                    

for i in qstData.values():
    print(i)   
