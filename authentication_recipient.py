from serpent_decode import serpent_de
from service_step import to_symbol
file_name2='file_name_2.txt'
def auto_recp(key):#отримує параметр ключ та випадкове значення
    decode = serpent_de(key, file_name2)
    text_final = ''
    for i in range(len(decode)):
        text_final += to_symbol(decode[i])
    return text_final
