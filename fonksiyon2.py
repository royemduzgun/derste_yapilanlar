def topla(*sayi):
    print(len(sayi))
    toplam=0
    for x in sayi:
        toplam +=x
       
    return toplam

print("toplam:",topla(10,20,14))

