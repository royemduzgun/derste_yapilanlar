def ortlamaAl(*sayi):
    print("gönderilen veri/dizi:",sayi)
    print("gönderilen parametre sayısı:",len(sayi))
    toplam=0
    for x in sayi:
        toplam+=x
    return toplam /len(sayi)

print("ortalama:",ortalamaAl(10,20,30,)
