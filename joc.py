from random import *
print("Ghiceste numarul: ")
a=randrange(10000)
while a:
    b=int(input())
    if b==a:
        print("Ai ghicit numarul!")
        break;
    print("Mai mare" if (int(b)<a) else "Mai mic")
