import service_step as sst
from service_step import slide,slide_0,xor,slide_reverse
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
            x=list_bits[i][j]
            d=key_bit[j]
            if x==d:
                s+='0'
            else:
                s+='1'
        list_key.append(s)

    return list_key  # before s-box-list,list 128 bit chunks

def s_box_func(list_key,data):

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

def lt_reverse(slist):#параметром отримуємо список по 128 біт і виконуємо LT крок
    lt_final=[]
    for j in range(len(slist)):###кількість стрічок по 128 біт
        arrays = [slist[j][i:i+32] for i in range(0, len(slist[j]), 32)]#отримали 4 елементи по 32 біта
        a,b,c,d=arrays
        #step 1
        c = slide_reverse(c, 22)#змінена функція
        time = slide_0(b, 7)
        c=xor(c,time)
        c=xor(c,d)


        #step 2
        a=slide_reverse(a,5)
        a=xor(a,d)
        a=xor(a,b)

        #step 3
        time=slide_0(a,3)#для ксору над Д6
        b=slide_reverse(b,1)
        b=xor(b,c)
        b=xor(b,a)
        a=slide_reverse(a,13)

        #step 4
        d=slide_reverse(d,7)
        d=xor(d,time)
        d=xor(d,c)
        c=slide_reverse(c,3)

        s=a+b+c+d
        lt_final.append(s)
    return lt_final
