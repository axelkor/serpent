
data_return=[
        [13, 3, 11, 0, 10, 6, 5, 12, 1, 14, 4, 7, 15, 9, 8, 2],
        [5, 8, 2, 14, 15, 6, 12, 3, 11, 4, 7, 9, 1, 13, 10, 0],
        [12, 9, 15, 4, 11, 14, 1, 2, 0, 3, 6, 13, 5, 8, 10, 7],
        [0, 9, 10, 7, 11, 14, 6, 13, 3, 5, 12, 2, 4, 8, 15, 1],
        [5, 0, 8, 3, 10, 9, 7, 14, 2, 12, 11, 6, 4,15 , 13, 1],
        [8, 15, 2, 9, 4, 1, 13, 14, 11, 6, 5, 3, 7, 12, 10, 0],
        [15, 10, 1, 13, 5, 3, 6, 0, 4, 9, 14, 7, 2, 12, 8, 11],
        [3, 0, 6, 13, 9, 14, 15, 8, 5, 12, 11, 7, 10, 1, 4, 2],
    ]#s-box inverse
from main_func import s_box_func,key_block,lt_reverse
def serpent_de(key,file_name):
    file = open(file_name, "r")  # отримання стрічки для першої перестановки
    text_file = file.read()
    file.close()
    chunks = [text_file[i:i + 128] for i in range(0, len(text_file), 128)]

    #step 31 comp key+file
    list_bits_ip = key_block(chunks,key)             #key+text2
    list_bits_ip=s_box_func(list_bits_ip,data_return)   #s-box2
    list_bits_ip = key_block(list_bits_ip, key)         #key+text2

    #step 30-0
    for i in range(0,31):
        list_bits_lt=lt_reverse(list_bits_ip)#line trans
        list_sbox=s_box_func(list_bits_lt,data_return)#s-box
        list_bits_ip= key_block(list_sbox, key)  # key+text
    return list_bits_ip
