import random
from serpent_encode import serpent_en

def auto_send(key):#отримує параметром ключ для шифрування
    file=open('text.txt','r')#для копіювання тексту
    text=file.read()#початковий текст
    leng=len(text)

    file_3 = open('text_random.txt', 'w')
    random_number=generator(leng)
    file_3.write(text+random_number)#запис тексту у третій файл
    file_3.close()

    encode = serpent_en(key, 'text_random.txt')#отримання закодованого тексту
    file2 = open('file_name_2.txt', 'w')#запис закодованого тексту
    for i in range(len(encode)):
        file2.write(encode[i])
    file2.close()


    return random_number#повернення зашифрованого тексту і рандомного числа

def generator(len):
    string=''
    for i in range((len//16+1)*16-len):
        string+=str(random.randint(0,9))
    return string