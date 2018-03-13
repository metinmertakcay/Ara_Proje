import codecs
import sys
import re

lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
}

#Bu fonksiyon noktalama işaretlerini kaldırmamızı sağlar.
def controlWord(word):
    if not(word.islower()):
        word = word.translate(lower_map).lower()
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

def threeGram(word):
    n_gram = []
    tup = tuple(word)
    i = 0
    while((i + 3) < len(tup)):
        word = "".join(tup[i:(i+3)])
        n_gram.append(word)
        i = i + 1
    return n_gram

def compareWords(question,answers):

    i = 0
    j = 0
    k = 0
    sayacA = 0
    sayacB = 0
    sayacC = 0
    sayacD = 0
    sayacE = 0
    soru = 1

    while i < len(question):
        #if(i % 8 == 0):
        #    print(question[i])
        if (i % 8 == 3): #question listesinin her 4.elamanında A şıkkının metni var
            j = 0
            while j < len(question[i]): # A şıkkının ilk kelimesinden başlanarak tüm kelimeler karşılaştırılıyor
                k = 0
                while k < len(question[i - 2]): # Paragrag A şıkkının 2 indis altındadır.
                    if question[i][j] == question[i - 2][k]: # Paragraftaki kelimeler ile şıktaki kelimeler karşılaştırılıyor
                        sayacA = sayacA + 1 # eğer aynı ise sayacA arttıtılıyor
                    k = k + 1
                j = j + 1
            maks = sayacA / len(question[i]) * 100 # tüm kelimeler karşılaştırılınca aynı olan kelime sayısı maks'a atılıyor
            cevap = "A"  # cevap A şıkkı oluyor

        if (i % 8 == 4): #question listesinin her 5.elamanında B şıkkının metni var
            j = 0
            while j < len(question[i]):
                k = 0
                while k < len(question[i - 3]):
                    if question[i][j] == question[i - 3][k]:
                        sayacB = sayacB + 1
                    k = k + 1
                j = j + 1
            sayacB = sayacB / len(question[i]) * 100
            if (maks < sayacB): # eğer sayacB maks'tan büyükse artık doğru cevap B şıkkı oluyor değilse doğru cevap A şıkkı kalıyor
                maks = sayacB
                cevap = "B"

        if (i % 8 == 5): #question listesinin her 6.elamanında C şıkkının metni var
            j = 0
            while j < len(question[i]):
                k = 0
                while k < len(question[i - 4]):
                    if question[i][j] == question[i - 4][k]:
                        sayacC = sayacC + 1
                    k = k + 1
                j = j + 1
            sayacC = sayacC / len(question[i]) * 100
            if (maks < sayacC): # eğer sayacC maks'tan büyükse artık doğru cevap C şıkkı oluyor
                maks = sayacC
                cevap = "C"

        if (i % 8 == 6): #question listesinin her 7.elamanında D şıkkının metni var
            j = 0
            while j < len(question[i]):
                k = 0
                while k < len(question[i - 5]):
                    if question[i][j] == question[i - 5][k]:
                        sayacD = sayacD + 1
                    k = k + 1
                j = j + 1
            sayacD = sayacD / len(question[i]) * 100
            if (maks < sayacD): # eğer sayacD maks'tan büyükse artık doğru cevap D şıkkı oluyor
                maks = sayacD
                cevap = "D"

        if (i % 8 == 7): #question listesinin her 8.elamanında E şıkkının metni var
            j = 0
            while j < len(question[i]):
                k = 0
                while k < len(question[i - 6]):
                    if question[i][j] == question[i - 6][k]:
                        sayacE = sayacE + 1
                    k = k + 1
                j = j + 1
            sayacE = sayacE / len(question[i]) * 100
            if (maks < sayacE): # eğer sayacE maks'tan büyükse artık doğru cevap E şıkkı oluyor
                maks = sayacE
                cevap = "E"

            answers.append(soru) # 8 satır sonunda bir sorunun hem paragrafı hem de şıkları bitmiş oluyor
            answers.append(cevap) # bundan sonra yeni soruya geçildiği için değerler yenileniyor
            sayacA = 0
            sayacB = 0
            sayacC = 0
            sayacD = 0
            sayacE = 0
            maks = 0
            soru = soru + 1 # Kaçıncı soruda olunduğunu tutuyor
        i = i + 1

#Bu fonksiyon soruların çözülme oranlarını bulmak için oluşturulmuştur
def percent(answers, cevaplar):
    i = 0
    sayac = 0
    while (i < len(answers)):
        if (i % 2 == 1):
            if (answers[i] == cevaplar[i]):
                sayac = sayac + 1
        i = i + 1
    return sayac

def reorderCevaplarListesi(cevaplarListesi):
    i = 0
    while (i < len(cevaplarListesi)):
        # İlk okunan değer soruNo'dur.
        if (i % 2 == 0):
            # Soru olduğunu gösteren ayraç çıkartılıyor.
            cevaplarListesi[i] = int(re.sub(r"[)]", "", cevaplarListesi[i]))
        else:
            # Alt satıra geçme karakteri kaldırılıyor.
            cevaplarListesi[i] = cevaplarListesi[i].replace("\n", "").replace("\r", "")
        i = i + 1
    return cevaplarListesi

def reorderWords(question):
    i = 0
    while (i < len(question)):
        # Listenin ilk elemanı soru numarasını gösterir.
        if (i % 8 != 0):
            liste = question[i]
            j = 0
            # Bütün liste gezilerek 6 dan uzun olan kelimeler parçalanıyor.
            while (j < len(liste)):
                liste[j] = deleteMoreThanSixCharacter(liste[j])
                j = j + 1
            question[i] = liste
        i = i + 1
    return question

#Bu kısımda sorular adındaki dosyadan sorular okunur. Soru txt bulunamıyorsa program sonlanır.
try:
    file = codecs.open("sorular.txt","r","utf-8-sig")
except FileNotFoundError:
    print("Dosya bulunamadi.")
    sys.exit()

#Dosyadan bütün satırlar okunuyor ve boşluklara göre ayırma işlemi gerçekleştiriliyor.
sorularText = file.read()
sorularListesi = sorularText.split(" ")
question = []
buffer = []

#Bu kısım verilen sorunun istenen formata dönüştürülerek saklanması için oluşturulmuştur.
j = 0
i = 0
while (i < len(sorularListesi)):
    sorularListesi[i] = controlWord(sorularListesi[i]) + " "
    if(checkNewlineCharacter(sorularListesi[i])):
        sorularListesi[i] = sorularListesi[i].replace("\n","").replace("\r","")
        buffer.append(sorularListesi[i])
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
        buffer.append(sorularListesi[i])
    i = i + 1

file.close()

#Cevaplar adı altında bulunan dosya okunur. Her bir sorunun cevabı elde edilir.
#Dosyanın var olup olmadığı kontrol ediliyor ve dosya yoksa program sonlandırılıyor.
try:
    file = codecs.open("cevaplar.txt","r","utf8")
except FileNotFoundError:
    print("Dosya bulunamadi")
    sys.exit()

#Dosyada bulunan bütün satırlar okunuyor.
cevaplarText = file.read()
#Dosya boşluklara göre ayırma işlemi gerçekleştiriliyor.
cevaplarListesi = cevaplarText.split(" ")
#Başta bulunan boşluk karakteri siliniyor.
cevaplarListesi.remove("")
#Bütün text geziliyor. Cevaplar soruNo - cevaplar şeklinde saklanıyor.
cevaplarListesi = reorderCevaplarListesi(cevaplarListesi)
#Açılmış olan dosya kapatılıyor.
file.close()

answers = []
#Kelime bazında soru metni ile cevaplar arasında kelime bazında karşılaştırma işlemi gerçekleştiriliyor.
compareWords(question,answers)
print("Sözcükler Bazında Yapılan Karşılaştırmada Doğru Oranı : %", percent(answers,cevaplarListesi)*100/500)


# Bu bölüm bütün kelimeleri kontrol edilir. Eğer kelime 6 dan büyük ise parçalanarak boyutu 6'ya çekilir.
question = reorderWords(question)

answers2 = []
compareWords(question,answers2)
print("6 Harflik Sözcükler Bazında Yapılan Karşılaştırmada Doğru Oranı : %", percent(answers2,cevaplarListesi)*100/500)

#Bu kısımda sorular adındaki dosyadan sorular okunur. Soru txt bulunamıyorsa program sonlanır.
try:
    file = codecs.open("sorular.txt","r","utf-8-sig")
except FileNotFoundError:
    print("Dosya bulunamadi.")
    sys.exit()

#Dosyadan bütün satırlar okunuyor ve boşluklara göre ayırma işlemi gerçekleştiriliyor.
sorularTextText = file.read()
sorularListesi = sorularTextText.split(" ")
question = []
buffer = []

#Bu kısım verilen sorunun istenen formata dönüştürülerek saklanması için oluşturulmuştur.
j = 0
i = 0
while (i < len(sorularListesi)):
    sorularListesi[i] = controlWord(sorularListesi[i]) + " "
    if(checkNewlineCharacter(sorularListesi[i])):
        sorularListesi[i] = sorularListesi[i].replace("\n","").replace("\r","")
        buffer.append(sorularListesi[i])
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
        buffer.append(sorularListesi[i])
    i = i + 1

file.close()

answers3 = []
compareWords(question,answers3)
print("3-Gram Bazında Yapılan Karşılaştırmada Doğru Oranı : % ", percent(answers3,cevaplarListesi)*100/500)