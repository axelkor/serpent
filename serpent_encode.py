import service_step as sst
import main_func as mf

data = [
        [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 2, 7, 0, 9, 12],
        [15, 12, 2, 7, 9, 0, 5, 10, 1, 11, 14, 8, 6, 13, 3, 4],
        [8, 6, 7, 9, 3, 12, 10, 15, 13, 1, 14, 4, 0, 11, 5, 2],
        [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14],
        [1, 15, 8, 3, 12, 0, 11, 6, 2, 5, 4, 10, 9, 14, 7, 13],
        [15, 5, 2, 11, 4, 10, 9, 12, 0, 3, 14, 8, 13, 6, 7, 1],
        [7, 2, 12, 5, 8, 4, 6, 11, 14, 9, 1, 15, 13, 3, 10, 0],
        [1, 13, 15, 0, 14, 8, 2, 11, 7, 4, 12, 10, 9, 3, 5, 6],
    ]#s-box
def serpent_en(key,file_name):
    file = open(file_name, "r")#отримання стрічки для першої перестановки
    text_file = file.read()
    file.close()
    text_bits=sst.to_bits(text_file)#стрічка бітів

    chunks = [text_bits[i:i + 128] for i in range(0, len(text_bits), 128)]#розбиття по 16 байтів(128біт)
    list_bits_ip=chunks




###злиття ключа з блоками виконується кожний з 31 кроки
    xj=list_bits_ip#це початок і кінець всіх функцій
    for i in range(0,31):
        list_key=mf.key_block(xj,key)#ключ
        s_box=mf.s_box_func(list_key,data)#отримали після с-боксу значення
        xj=mf.lt(s_box)



    list_key=mf.key_block(xj,key)#ключ
    s_box=mf.s_box_func(list_key,data)#s-box
    xj=mf.key_block(s_box,key)#key
    return xj


