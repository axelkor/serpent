from authentication_send import *
from authentication_recipient import auto_recp as a_r
from serpent_encode import serpent_en
from service_step import *
from tkinter import *


window = Tk()
window['bg'] = '#ffffff'
window.title('Автентифікація')
window.geometry('450x300')
window.resizable(width=False, height=False)
key = 'H9$%42Q-r9*sdkhd'
frame = Frame(window, bg='grey')
frame.place(relheight=1, relwidth=1)

random_number=None
def comparassion():#Зробити порівняння двох введених даних
    if len(entry6_var.get())!=16:
        label7.config(text="Ключ на стороні В не дорівнює 128 бітам", bg="red")
        return
    d=a_r(entry6_var.get())#отримане значення на стороні В
    text_from_entry_1=entry_var.get()
    random_number=entry2_var.get()
    x=len(random_number)
    if text_from_entry_1+random_number==d:#можна створити помилку замінивши рандом на інше
        label7.config(text="Автентифікація пройдена",bg="green")
    if text_from_entry_1!=d[:-x]:
        label7.config(text="Текст з помилкою",bg='red')
    if random_number!=d[-x:]:
        label7.config(text="Випадкове число з помилкою",bg="red")
    if text_from_entry_1!=d[:-x] and random_number!=d[-x:]:
        label7.config(text="Помилка ключа/текст+випадкове число", bg="red")
def add_cells():
    global random_number
    file = open('text.txt', 'r')  # для копіювання тексту
    text = file.read()  # початковий текст
    leng = len(text)
    random_number = generator(leng)

    auto_send(key,random_number)  # повертає рандомне значення
    file_name = "text.txt"  # основний текст
    file = open(file_name, "r")  # отримання стрічки для першої перестановки
    text_file = file.read()
    file.close()

    entry_var.set(text_file)
    entry2_var.set(random_number)
    entry5_var.set(key)
    entry6_var.set(key)

def recip_b():
    global random_number
    if len(entry_var.get())==0:
        label7.config(text="Заповніть текст", bg="red")
        return
    if len(entry5_var.get())!=16:
        label7.config(text="Ключ має мати довжину 16 байт", bg="red")
        return


    file_name = "text.txt"  # основний текст
    file = open(file_name, "w") #файл для запису тексту
    text_from_entr=entry_var.get() #текст з ентрі
    key_from_entr=entry5_var.get() #ключ з ентрі


    # string = ''#генерування випадкового числа
    # for i in range((len(text_from_entr) // 16 + 1) * 16 - len(text_from_entr)):#вираховування рандому
    #     string += str(random.randint(0, 9))
    #
    # entry2_var.set(string)#вставка випадкового в той х

    file.write(text_from_entr)
    file.close()
    if random_number!=entry2_var.get():
        random_number=entry2_var.get()
    auto_send(key_from_entr, random_number)


    file=open('file_name_2.txt','r')
    text=file.read()

    text_final=to_symbol(text)
    entry3_var.set(text_final)

    # text_file = file.read()
    # file.close()
    # time_variable = entry_var.get()
    #
    # if text_file!=time_variable or random_number!=entry2_var.get():
    #     file_name2 = "text_random.txt"
    #     file2 = open(file_name2, "w")
    #     file2.write(time_variable+entry2_var.get())
    #     file2.close()
    #
    #     encode = serpent_en(key, 'text_random.txt')  # отримання закодованого тексту
    #     file4 = open('file_name_2.txt', 'w')  # запис закодованого тексту
    #     for i in range(len(encode)):
    #         file4.write(encode[i])
    #     file4.close()
    #
    #
    # d=a_r(key)
    # x = len(entry2_var.get())  # довжина добавленого рандомного значення
    # entry3_var.set(d[:-x])
    # entry4_var.set(d[-x:])
    #
    # if text_file==d[:-x] and text_file+random_number==d:#можна створити помилку замінивши рандом на інше
    #     label7.config(text="Автентифікація пройдена",bg="green")
    # if text_file!=d[:-x]:
    #     label7.config(text="Текст з помилкою",bg='red')
    # if random_number!=d[-x:]:
    #     label7.config(text="Випадкове число з помилкою",bg="red")
    # if text_file!=d[:-x] and random_number!=d[-x:]:
    #     label7.config(text="Помилка в тобі", bg="red")
    #

entry_var=StringVar()
entry2_var=StringVar()#випадкове число
entry3_var=StringVar()
entry4_var=StringVar()
entry5_var=StringVar()
entry6_var=StringVar()#Ключ на стороні В


label1 = Label(frame, text="Сторона А").grid(row=0, column=0,sticky="ew")
label2 = Label(frame, text="Сторона B").grid(row=0, column=1, sticky="ew")
label3 = Label(frame, text="Ідентифікатор сторони В",bg='grey').grid(row=1, column=0,sticky="ew")
entry1=Entry(frame,textvariable=entry_var).grid(row=2, column=0,sticky="ew")#Введення тексту А
label4 = Label(frame, text="Випадкове значення",bg='grey').grid(row=3, column=0,columnspan=2,sticky="ew")
entry2=Entry(frame,textvariable=entry2_var).grid(row=4, column=0,columnspan=2,sticky="ew")#Рандомне число
label8=Label(frame, text="Ключ",bg='grey')
label7 = Label(frame, text="Автентифікація")
label7.grid(row=9,column=0,columnspan=2,sticky='ew')#Цей віджет буде в кінці кінців
button1=Button(frame,text='Автоматичне заповнення',bg='grey',command=add_cells)

label8.grid(row=5,column=0,columnspan=2,sticky='ew')
entry5 = Entry(frame,textvariable=entry5_var)
entry5.grid(row=6, column=0,  sticky="ew")  # Ключ А

entry6 = Entry(frame,textvariable=entry6_var)
entry6.grid(row=6, column=1,  sticky="ew")  # Ключ В

button1.grid(row=7, column=0,sticky="ew")#Заповнення комірок автоматична
button2=Button(frame, text='Передача даних стороні В', bg='grey', command=recip_b)
button2.grid(row=7, column=1,sticky="ew")#Перевірка правильності

button3=Button(frame, text='Порівняння', bg='grey', command=comparassion)
button3.grid(row=8, column=0,columnspan=2,sticky="ew")#Перевірка правильності

label5 = Label(frame, text="Зашифрований ідентифікатор",bg='grey').grid(row=1, column=1,sticky="ew")
#label6 = Label(frame, text="Зашифроване випадкове число",bg='grey').grid(row=3, column=1,sticky="ew")

entry3=Entry(frame,textvariable=entry3_var).grid(row=2, column=1,sticky="ew")#Виведення тексту розшифрованого
#entry4=Entry(frame,textvariable=entry4_var).grid(row=4, column=1,sticky="ew")#Рандомне число_після шифрування





frame.grid_columnconfigure(0,minsize=225)
frame.grid_columnconfigure(1,minsize=225)

window.mainloop()

if __name__ == '__main__':
    file_name="text.txt"#основний текст
    file_name_with_random='text_random.txt'#файл в якому записані значення + рандомне число
    file_name2='file_name_2.txt'#в цьому файлі записаний зашифрований текст



    # x=len(random_number)#довжина добавленого рандомного значення
    # first_file=open(file_name,'r')#основний текст
    # third_file=open(file_name_with_random,'r')#випадковий текст
    #
    # first=first_file.read()
    # third=third_file.read()
    # if first==third[:-x] and first+random_number==third:#можна створити помилку замінивши рандом на інше
    #     print("all is right")
    # elif first!=third[:-x]:
    #     print("текст неправильний")
    # elif first+random_number==third:
    #     print('Випадкове число передано з помилкою')