numara=int(input("bir sayı giriniz."))
if numara>100:
    print("100'den fazla dönemem")
elif numara<=100:
    for sayı in range(1,numara,1):
        print(sayı)

else:
    print("hatalı işlem")
    
  
