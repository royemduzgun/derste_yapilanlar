def topla(x,y):
    return x+y
def cıkar(x,y):
    return x-y
def carp(x,y):
    return x*y
def böl(x,y):
    return x/y

print("lütfen yapmak istediginiz işlemi seçin.")
print("1.toplama")
print("2.çıkarma")
print("3.çarpma")
print("4.bölme")

secim=input("seçiminiz(1/2/3/4:")

sayi1=float(input("ilk sayıyı girin:"))
sayi2=float(input("ikinci sayıyı girin:"))

if secim=='1':
    print(sayi1,"+",sayi2,"=",topla(sayi1,sayi2))
    
elif secim=='2':
    print(sayi1,"-",sayi2,"=",cıkar(sayi1,sayi2))
    
elif secim=='3':
    print(sayi1,"*",sayi2,"=",carp(sayi1,sayi2))

elif secim=='4':
    if saayi2==0:
        print("bir sayi sıfıra bölünemez.")
    else:
        (sayi1,"/",sayi2,"=",böl(sayi1,sayi2))
        
else:
    print("islem gecersiz.")
