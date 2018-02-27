import codecs
import sys
import re

def controlWord(word):
    if (word.find('.')) or (word.find(',')) or (word.find('!')) or (word.find('?')) or (word.find(':')) or (word.find(';')) or (word.find('-')) or (word.find('(')) or (word.find(')')) or (word.find("'")):
        return re.sub(r"[-'(.,!?:;)]", '', word)
    else:
        return word

try:
    file = codecs.open("file.txt","r","utf8")
except FileNotFoundError:
    print("Dosya bulunamadi.")
    sys.exit()

oku = file.read()
liste_ = oku.split(" ")

i = 0
while (i < len(liste_)):
    liste_[i] = controlWord(liste_[i]) + " "
    i = i + 1

metin = ''.join(liste_)
print(metin)
file.close()