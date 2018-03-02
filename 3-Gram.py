import codecs
import sys
import re

#Bu fonksiyon noktalama işaretlerini kaldırmamızı sağlar.
def controlWord(word):
    if not(word.islower()):
        word = word.lower()
    if (word.find('.')) or (word.find(',')) or (word.find('!')) or (word.find('?')) or (word.find(':')) or (word.find(';')) or (word.find('-')) or (word.find('(')) or (word.find(')')) or (word.find("'")):
        return re.sub(r"[-'(.,!?:;)]", '', word)
    if (word.find('"'))or(word.find('"')):
        return re.sub(r'[""]','',word)
    else:
        return word

#Bu fonksiyon alt satıra geçme karakteri olup olmadığı kontrol edilir.
def checkNewlineCharacter(word):
    tup = tuple(word)
    i = 0
    while i < len(tup):
        if tup[i] == "\n":
            return True
        i = i + 1
    return False

#Bu fonksiyon var olan texti 3'er 3'er ngramlara parçalama işlemini gerçekleştirir.
def threeGram(word):
    n_gram = []
    tup = tuple(word)
    i = 0
    while((i + 3) < len(tup)):
        word = "".join(tup[i:(i+3)])
        n_gram.append(word)
        i = i + 1
    return n_gram

#Bu kısımda sorular adındaki dosyadan sorular okunur. Soru txt bulunamıyorsa program sonlanır.
try:
    file = codecs.open("sorular.txt","r","utf8")
except FileNotFoundError:
    print("Dosya bulunamadi.")
    sys.exit()

#Dosyadan bütün satırlar okunuyor ve boşluklara göre ayırma işlemi gerçekleştiriliyor.
readText = file.read()
text = readText.split(" ")
question = []
buffer = []

#Bu kısım verilen sorunun istenen formata dönüştürülerek saklanması için oluşturulmuştur.
j = 0
i = 0
while (i < len(text)):
    text[i] = controlWord(text[i]) + " "
    if(checkNewlineCharacter(text[i])):
        text[i] = text[i].replace("\n","").replace("\r","")
        buffer.append(text[i])
        if(j % 8 == 0):
            question.append(buffer[0])
            del buffer[0]
            question.append(threeGram("".join(buffer)))
            j = j + 2
        elif(j % 8 == 2):
            question.append(buffer)
            j = j + 1
        elif(j % 8 == 3)or(j % 8 == 4)or(j % 8 == 5)or(j % 8 == 6)or(j % 8 == 7):
            del buffer[0]
            question.append(threeGram("".join(buffer)))
            j = j + 1
        buffer = []
    else:
        buffer.append(text[i])
    i = i + 1

print(question)
file.close()