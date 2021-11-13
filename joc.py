from random import *
a=randrange(1000)
k=7
while a:
    b=int(input("Ghicește numărul: "))
    if b==a:
        print('Ai ghicit numărul!')
        break;
    print('\nMai mare' if (int(b)<a) else '\nMai mic')
    k-=1
    if k>1:
        print('\nMai ai '+str(k)+' vieți\n')
    elif k==1:
            print('\nMai ai o viață!')
    if k==0:
        print("Ai pierdut! Numărul căutat era "+str(a))
        break;
