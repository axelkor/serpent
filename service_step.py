def to_number(text):#string bits to num for s-box
    ###Опис функції
    ###В цій функції отримується текстове позначення і повертається звичайне число 101=5
    a = 1
    sum = 0
    for i in range(len(text), 0, -1):
        if text[i-1] == "0":
            a *= 2
            continue
        else:
          sum += a
          a *= 2
    return sum
def to_bits(text):#to bits
    ###Опис функції

    ###У цій функцїі приймається на вхід число(як текст)"15" і повертається бітова стрічка яка розширена до 8 бітів
    str=''
    for char in text:
        str+=bin(ord(char))[2:].rjust(8, '0')
    return str
def to_symbol(str):#to symbol
    ###на вхід подається стрічка бітів і на вихід повертається символьне позначення через перетворення аскі


    chunks = [str[i:i + 8] for i in range(0, len(str), 8)]
    text=''
    for i in range(len(chunks)):
        x=int(chunks[i],2)
        text+=chr(x)
    return text
def slide(a,key):#зсув файлу а на кеу розрядів
    return a[key:]+a[:key]
def slide_reverse(a,key):#зсув файлу а на кеу розрядів
    return a[-key:]+a[:-key]
def xor(a,b):#виконання конкатенації
    s=''
    for j in range(len(a)):
        x = a[j]
        d = b[j]
        if x == d:
            s += '0'
        else:
            s += '1'
    return s
def slide_0(a,key):
    return a[key:]+'0'*key