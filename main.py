from authentication_send import auto_send as a_s
from authentication_recipient import auto_recp as a_r
from tkinter import *

from tkinter import Tk, Frame, Label

window = Tk()
window['bg'] = '#ffffff'
window.title('Автентифікація')
window.geometry('450x300')
window.resizable(width=False, height=False)

frame = Frame(window, bg='grey')
frame.place(relheight=1, relwidth=1)

label1 = Label(frame, text="Сторона А").grid(row=0, column=0,sticky="ew")
label2 = Label(frame, text="Сторона B").grid(row=0, column=1, sticky="ew")
label3 = Label(frame, text="Текст автентифікації",bg='grey').grid(row=1, column=0,sticky="ew")
entry1=Entry(frame).grid(row=2, column=0,sticky="ew")#Введення тексту А
label4 = Label(frame, text="Рандомне значення",bg='grey').grid(row=3, column=0,sticky="ew")
entry2=Entry(frame).grid(row=4, column=0,sticky="ew")#Рандомне число
button1=Button(frame,text='Заповнення всіх комірок',bg='grey').grid(row=5, column=0,sticky="ew")
button1=Button(frame,text='Розшифрування значень',bg='grey').grid(row=5, column=1,sticky="ew")
label5 = Label(frame, text="Розшифрований текст",bg='grey').grid(row=1, column=1,sticky="ew")
label6 = Label(frame, text="Отримане значення",bg='grey').grid(row=3, column=1,sticky="ew")
entry3=Entry(frame).grid(row=2, column=1,sticky="ew")#Введення тексту А
entry4=Entry(frame).grid(row=4, column=1,sticky="ew")#Рандомне число


label7 = Label(frame, text="Автентифікація").grid(row=6,column=0,columnspan=2,sticky='ew')#Цей віджет буде в кінці кінців



frame.grid_columnconfigure(0,minsize=225)
frame.grid_columnconfigure(1,minsize=225)

window.mainloop()

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