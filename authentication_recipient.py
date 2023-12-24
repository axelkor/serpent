from serpent_decode import serpent_de
from service_step import to_symbol
file_name2='file_name_2.txt'
def auto_recp(key,random):#отримує параметр ключ та випадкове значення
    decode = serpent_de(key, file_name2)
    text_final = ''
    for i in range(len(decode)):
        text_final += to_symbol(decode[i])
    print(text_final[:-len(random)])
    return text_final
