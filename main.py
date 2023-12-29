from authentication_send import auto_send as a_s
from authentication_recipient import auto_recp as a_r
from serpent_encode import serpent_en
from tkinter import *

def add_cells():
    global random_number
    random_number = a_s(key)  # повертає рандомне значення
    file_name = "text.txt"  # основний текст
    file = open(file_name, "r")  # отримання стрічки для першої перестановки
    text_file = file.read()
    file.close()
    entry_var.set(text_file)
    entry2_var.set(random_number)
def get_result():
    global random_number
    file_name = "text.txt"  # основний текст
    file = open(file_name, "r")  # отримання стрічки для першої перестановки
    text_file = file.read()
    file.close()
    global label7
    time_variable = entry_var.get()
    if text_file!=time_variable or random_number!=entry2_var.get():
        file_name2 = "text_random.txt"
        file2 = open(file_name2, "w")
        file2.write(time_variable+entry2_var.get())
        file2.close()

        encode = serpent_en(key, 'text_random.txt')  # отримання закодованого тексту
        file4 = open('file_name_2.txt', 'w')  # запис закодованого тексту
        for i in range(len(encode)):
            file4.write(encode[i])
        file4.close()


    d=a_r(key,random_number)
    x = len(entry2_var.get())  # довжина добавленого рандомного значення
    entry3_var.set(d[:-x])
    entry4_var.set(d[-x:])

    if text_file==d[:-x] and text_file+random_number==d:#можна створити помилку замінивши рандом на інше
        label7.config(text="Автентифікація пройдена")
    if text_file!=d[:-x]:
        label7['text']="Текст з помилкою"
    if text_file+random_number!=d:
        label7['text']="Випадкове число з помилкою"


window = Tk()
window['bg'] = '#ffffff'
window.title('Автентифікація')
window.geometry('450x300')
window.resizable(width=False, height=False)
key = 'H9$%42Q-r9*sdkhd'
frame = Frame(window, bg='grey')
frame.place(relheight=1, relwidth=1)
random_number=None
entry_var=StringVar()
entry2_var=StringVar()
entry3_var=StringVar()
entry4_var=StringVar()

label1 = Label(frame, text="Сторона А").grid(row=0, column=0,sticky="ew")
label2 = Label(frame, text="Сторона B").grid(row=0, column=1, sticky="ew")
label3 = Label(frame, text="Текст автентифікації",bg='grey').grid(row=1, column=0,sticky="ew")
entry1=Entry(frame,textvariable=entry_var).grid(row=2, column=0,sticky="ew")#Введення тексту А
label4 = Label(frame, text="Рандомне значення",bg='grey').grid(row=3, column=0,sticky="ew")
entry2=Entry(frame,textvariable=entry2_var).grid(row=4, column=0,sticky="ew")#Рандомне число
label7 = Label(frame, text="Автентифікація").grid(row=6,column=0,columnspan=2,sticky='ew')#Цей віджет буде в кінці кінців

button1=Button(frame,text='Заповнення всіх комірок',bg='grey',command=add_cells).grid(row=5, column=0,sticky="ew")
button2=Button(frame,text='Розшифрування значень',bg='grey',command=get_result).grid(row=5, column=1,sticky="ew")

label5 = Label(frame, text="Розшифрований текст",bg='grey').grid(row=1, column=1,sticky="ew")
label6 = Label(frame, text="Отримане значення",bg='grey').grid(row=3, column=1,sticky="ew")
entry3=Entry(frame,textvariable=entry3_var).grid(row=2, column=1,sticky="ew")#Виведення тексту розшифрованого
entry4=Entry(frame,textvariable=entry4_var).grid(row=4, column=1,sticky="ew")#Рандомне число_після шифрування





frame.grid_columnconfigure(0,minsize=225)
frame.grid_columnconfigure(1,minsize=225)

window.mainloop()

if __name__ == '__main__':
    file_name="text.txt"#основний текст
    file_name_with_random='text_random.txt'#файл в якому записані значення + рандомне число
    file_name2='file_name_2.txt'#в цьому файлі записаний зашифрований текст




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