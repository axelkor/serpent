import random
from serpent_encode import serpent_en

def auto_send(key,random_number):#отримує параметром ключ для шифрування

    file=open('text.txt','r')#для копіювання тексту
    text=file.read()#початковий текст

    file_3 = open('text_random.txt', 'w')
    file_3.write(text+random_number)#запис тексту у третій файл
    file_3.close()

    encode = serpent_en(key, 'text_random.txt')#отримання закодованого тексту
    file2 = open('file_name_2.txt', 'w')#запис закодованого тексту
    for i in range(len(encode)):
        file2.write(encode[i])


def generator(len):
    string=''
    for i in range((len//16+1)*16-len):
        string+=str(random.randint(0,9))
    return string