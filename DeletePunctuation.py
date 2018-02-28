import codecs
import sys
import re

def controlWord(word):
    if not(word.islower()):
        word = word.lower()
    if (word.find('.')) or (word.find(',')) or (word.find('!')) or (word.find('?')) or (word.find(':')) or (word.find(';')) or (word.find('-')) or (word.find('(')) or (word.find(')')) or (word.find("'")):
        return re.sub(r"[-'(.,!?:;)]", '', word)
    else:
        return word

def checkNewlineCharacter(word):
    tup = tuple(word)

    i = 0
    while i < len(tup):
        if tup[i] == "\n":
            return True
        i = i + 1
    return False

try:
    file = codecs.open("file1.txt","r","utf8")
except FileNotFoundError:
    print("Dosya bulunamadi.")
    sys.exit()

readText = file.read()
text = readText.split(" ")
question = []
buffer = []

j = 0
i = 0
while (i < len(text)):
    text[i] = controlWord(text[i]) + " "
    if(checkNewlineCharacter(text[i])):
        text[i] = text[i].replace("\n","").replace("\r","")
        buffer.append(text[i])
        if(j % 7 == 0):
            question.append(buffer[0])
            del buffer[0]
            question.append(buffer)
        elif(j % 7 == 2)or(j % 7 == 3)or(j % 7 == 4)or(j % 7 == 5)or(j % 7 == 6):
            del buffer[0]
            question.append(buffer)
        j = j + 1
        buffer = []
    else:
        buffer.append(text[i])
    i = i + 1

print(question)
file.close()