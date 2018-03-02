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

#Bu fonksiyon parametre olarak gelen kelimenin 6'dan uzun olup olmadığı kontrol edilir ve uzun ise ilk 6 karakteri alınır.
def deleteMoreThanSixCharacter(word):
    if(len(word) <= 6):
        return word
    else:
        convertedWord = tuple(word)
        return "".join(convertedWord[:6])

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
            question.append(buffer)
            j = j + 2
        elif(j % 8 == 2):
            question.append(buffer)
            j = j + 1
        elif(j % 8 == 3)or(j % 8 == 4)or(j % 8 == 5)or(j % 8 == 6)or(j % 8 == 7):
            del buffer[0]
            question.append(buffer)
            j = j + 1
        buffer = []
    else:
        buffer.append(text[i])
    i = i + 1

print(question)
file.close()

#Cevaplar adı altında bulunan dosya okunur. Her bir sorunun cevabı elde edilir.
#Dosyanın var olup olmadığı kontrol ediliyor ve dosya yoksa program sonlandırılıyor.
try:
    file = codecs.open("cevaplar.txt","r","utf8")
except FileNotFoundError:
    print("Dosya bulunamadi")
    sys.exit()

#Dosyada bulunan bütün satırlar okunuyor.
readText = file.read()
#Dosya boşluklara göre ayırma işlemi gerçekleştiriliyor.
text = readText.split(" ")
#Başta bulunan boşluk karakteri siliniyor.
text.remove("")

#Bütün text geziliyor. Cevaplar soruNo - cevaplar şeklinde saklanıyor.
i = 0
while (i < len(text)):
    #İlk okunan değer soruNo'dur.
    if(i % 2 == 0):
        #Soru olduğunu gösteren ayraç çıkartılıyor.
        text[i] = re.sub(r"[)]","",text[i])
    else:
        #Alt satıra geçme karakteri kaldırılıyor.
        text[i] = text[i].replace("\n", "").replace("\r", "")
    i = i + 1

print(text)
#Açılmış olan dosya kapatılıyor.
file.close()

#Bu bölüm bütün kelimeleri kontrol edilir. Eğer kelime 6 dan büyük ise parçalanarak boyutu 6'ya çekilir.
i = 0
while(i < len(question)):
    #Listenin ilk elemanı soru numarasını gösterir.
    if(i % 8 != 0):
        liste = question[i]
        j = 0
        #Bütün liste gezilerek 6 dan uzun olan kelimeler parçalanıyor.
        while(j < len(liste)):
            liste[j] = deleteMoreThanSixCharacter(liste[j])
            j = j + 1
        question[i] = liste
    i = i + 1

#Düzeltilmiş olan liste ekrana basılıyor.
print(question)