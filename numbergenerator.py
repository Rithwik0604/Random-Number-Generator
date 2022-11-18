import random
import time

def pirntlist(l):
    for i in l:
        print(i)
def repeatq():
    while True:
        a= input("do you want to repeat the program?:[y/n] ")
        print()
        print()
        if a=='y':
            print('==============================')
            print()
            print()
            loop=True
            return loop
        elif a=='n':
            print('Bye!')
            time.sleep(0.7)
            return False
        else:
            print('Invaid option. Try again.')
            print()
            continue

loop=True
while loop:
    l=[]
    print()
    print()
    while True:
        try:
            q1 = int(input("how many numbers do you want to generate? : "))
            if q1<0:
                print()
                print('Has to be 0 or more.')
                print()
                continue
            break
        except Exception:
            print()
            print('Not an integer. Try again')
            print()
    print()
    print()

    while True:
        while True:
            try:
                q2 = int(input("Enter the lower limit: "))
                print()
                print('-----')
                break
            except Exception:
                print()
                print('Not an integer. Try again')
                print()
        print()

        while True:
            try:
                q3 = int(input("Enter the upper limit: "))
                print()
                print('-----')
                break
            except Exception:
                print()
                print('Not an integer. Try again')
                print()
        print()
        if q2>q3:
            print('lower limit cannot be greater than upper limit.')
            print()
            continue
        else:
            break
    print()
    print()

    

    for i in range(q1):
        a=random.randint(q2,q3)
        l.append(a)
    pirntlist(l)
    print()
    loop=repeatq()
