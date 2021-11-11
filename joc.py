from random import *
print("Ghicește numărul: ")
a=randrange(100)
k=5
while a:
    b=int(input())
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
        print("Ai pierdut!")
        break;
