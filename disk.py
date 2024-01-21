def hanoikuleleri(n, kaynak,hedef,yedek):
    if n==1:
        print("disk 1 taşı,kaynak:" ,kaynak,"hedef:",hedef)
        return
    hanoikuleleri(n-1,kaynak,yedek,hedef)
    print("disk",n,"taşı,kaynak:",kaynak,"hedef:",hedef)
    hanoikuleleri(n-1,yedek ,hedef,kaynak)

n=4
hanoikuleleri(n,'a','B','c')
