meyve=input("hangi meyveyi istiyorsun?")

if meyve==("muz"):
    kilo=int(input("kaçkilo muz istiyorsun?"))
    print(kilo*5,"tl ücret ödeyeceksiniz.")

elif meyve==("elma"):
    renk=input("hangi renk elma istiyorsun?")
    if renk==("kırmızı"):
        kilo=int(input("kaç kilo kırmızı elma istiyorsun?"))
    elif renk==("sarı"):
        kilo=int(input("kaç kilo sarı elma istiyorsun?"))
    elif renk==("yeşil"):
        kilo=int(input("kaç kilo yeşil elma istiyorsun?"))
    else:
        print("sadece sarı,kırmızı yada yeşil renk elma var.")


    print(kilo*4,"tl ücret ödüyeceksiniz.")


elif meyve==("üzüm"):
    renk=input("hangi renk üzüm istiyorsun?")
    if renk==("mor"):
        kilo=int(input("kaç kilo mor üzüm istiyorsun?"))
        print(kilo*6,"tl ücret ödeyeceksiniz.")
    elif renk==("yeşil"):
        kilo=int(input("kaç kilo yeşil üzüm istiyorsun?"))
        print(kilo*6.5,"tl ücret ödeyeceksiniz.")
    else:
        print(" sadece mor yada yeşil üzüm var.")

else:
    print("manavda sadece  muz, elma ve üzüm var.")
        
