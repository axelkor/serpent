from authentication_send import auto_send as a_s
from authentication_recipient import auto_recp as a_r




if __name__ == '__main__':
    file_name="text.txt"#основний текст
    file_name_with_random='text_random.txt'#файл в якому записані значення + рандомне число
    file_name2='file_name_2.txt'#в цьому файлі записаний зашифрований текст
    key='H9$%42Q-r9*sdkhd'

    random_number=a_s(key)#повертає рандомне значення
    d=a_r(key,random_number)
    x=len(random_number)#довжина добавленого рандомного значення
    first_file=open(file_name,'r')#основний текст
    third_file=open(file_name_with_random,'r')#випадковий текст
    first=first_file.read()
    third=third_file.read()
    if first==third[:-x] and first+random_number==third:#можна створити помилку замінивши рандом на інше
        print("all is right")
    elif first!=third[:-x]:
        print("текст неправильний")
    elif first+random_number==third:
        print('Випадкове число передано з помилкою')