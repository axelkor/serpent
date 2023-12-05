import service_step as sst
import main_func as mf
def serpent_en(key,file_name):
    file = open(file_name, "r")#отримання стрічки для першої перестановки
    text_file = file.read()
    file.close()
    text_bits=sst.to_bits(text_file)#стрічка бітів

    chunks = [text_bits[i:i + 128] for i in range(0, len(text_bits), 128)]#розбиття по 16 байтів(128біт)
    list_bits_ip=[]#final
    print(chunks)
###початкова перестановка
    for i in range(len(chunks)):#виконання початкової перестановки
        one_of_chunks=list(chunks[i])
        for j in range(len(chunks[i])):
            one_of_chunks[j]=chunks[i][(j+32)%128]

        list_bits_ip.append("".join(one_of_chunks))#отримали масив з елементами по 128б для подальших перестановок
    print(list_bits_ip)
###злиття ключа з блоками виконується кожний з 31 кроки
    xj=list_bits_ip#це початок і кінець всіх функцій
    for i in range(0,31):
        print(i)
        list_key=mf.key_block(xj,key)#ключ
        s_box=mf.s_box_func(list_key)#отримали після с-боксу значення
        xj=mf.lt(s_box)
    list_key=mf.key_block(xj,key)#ключ
    s_box=mf.s_box_func(list_key)
    xj=mf.key_block(s_box,key)
    return xj
if __name__ == '__main__':
    file_name="text.txt"
    key='H9$%42Q-r9*sdkhd'
    x=serpent_en(key,file_name)
    final=''
    for i in range(len(x)):
        s=sst.to_symbol(x[i])
        final+=s

    print(final)