import service_step as sst
from service_step import slide,slide_0,xor
def lt(slist):#параметром отримуємо список по 128 біт і виконуємо LT крок
    lt_final=[]
    for j in range(len(slist)):###кількість стрічок по 128 біт
        arrays = [slist[j][i:i+32] for i in range(0, len(slist[j]), 32)]#отримали 4 елементи по 32 біта
        a,b,c,d=arrays
        #step 1
        a=slide(a,13)
        c=slide(c,3)
        #step 2
        b=xor(b,a)
        d=xor(d,c)
        #step 3
        b=xor(b,c)
        #step 4
        time=slide_0(a,3)
        d=xor(d,time)
        #step 5
        b=slide(b,1)
        d=slide(d,7)
        #step 6
        a=xor(a,b)
        c=xor(c,d)
        #step 7
        a=xor(a,d)
        #step 8
        a=slide(a,5)
        time=slide_0(b,7)
        c=xor(c,time)
        c=slide(c,22)
        s=a+b+c+d
        lt_final.append(s)
    return lt_final
def key_block(list_bits,key):#key step

    ###Один з підкроків який можна пояснити злиттям ключа і списку бітів
    list_key = []  # масив прогнатих ключ+текст
    key_bit = sst.to_bits(key)
    for i in range(len(list_bits)):
        s = ''
        for j in range(len(list_bits[i])):
            x= str((int(list_bits[i][j]) and not int(key_bit[j])) or (not int(list_bits[i][j]) and int(key_bit[j])))
            if x==1 or x==True:
                s+='1'
            else:
                s+='0'
        list_key.append(s)

    return list_key  # before s-box-list,list 128 bit chunks

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
def s_box_func(list_key):

    ### розбиття стрічки бітів по 128 біт на стрічки по 32 які в наступному розбиваються на 8 по 4 біта,числа 4
    # біт перетворюються на їх чисельне представлення 1111=15 і індекс перестановки зміщується відповідно до порядку роботи
    # наприклад перше виконання S0 число яке отримали 1101=13 тобто число в масив [0][13] отримали 7

    sbox_list=[]
    for i in range(len(list_key)):#кількість 128 бітних чанків
        sbox = ''
        for j in range(4):#4 слова по 32 біти
            massive_word=list_key[i][j*32:(j+1)*32]#масив слів
            index_for_data=0
            for k in range(4):
                massive_byte=massive_word[k*8:(k+1)*8]

                first_part=massive_byte[0:4]#отримання перших чотирьох бітів байту
                second_part=massive_byte[4:]#отримання других чотирьох бітів байту

                first_num=sst.to_number(first_part)#перетворення в число
                second_num=sst.to_number(second_part)

                first_sbox=data[index_for_data][first_num]#отримання після с-боксу чисел
                second_sbox=data[index_for_data+1][second_num]

                sbox+=bin(first_sbox)[2:].rjust(4,'0')+bin(second_sbox)[2:].rjust(4,'0')
                index_for_data+=2
        sbox_list.append(sbox)
    return sbox_list