import codecs
import sys

def fopen(path):
    try:
        file = codecs.open(path,"r","utf-8")
        return file
    except FileNotFoundError:
        print("Dosya bulunamadi")
        sys.exit()

file = fopen("merge.txt")
words = file.read()
file.close()

file = fopen("merge1.txt")
oku = file.read()
file.close()

words = words + " " + oku
print(words)

file = codecs.open("merged.txt","w","utf-8")
file.write(words)