from serpent_encode import serpent_en
from serpent_decode import serpent_de
from service_step import to_symbol






if __name__ == '__main__':
    file_name="text.txt"
    file_name2='file_name_2.txt'

    key='H9$%42Q-r9*sdkhd'

    encode=serpent_en(key,file_name)
    file2=open('file_name_2.txt', 'w')
    for i in range(len(encode)):
        file2.write(encode[i])
    file2.close()

    decode=serpent_de(key,file_name2)
    text_final=''
    for i in range(len(decode)):
        text_final+=to_symbol(decode[i])
    print(text_final)