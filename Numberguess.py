import random

a=0
b=100
num = input(f"Guess a number {a} to {b}:")
guess = str(random.randint(a,b))
while 1:
    if num==guess:
        print("Congrats")
        break

    elif num=='!':
        if guess=='0':
            gen=random.randint(a+2,b-1)
            num=input("Hint: Falls between {} to {}:".format(a,gen))
            b=gen
        elif guess=='10':
            gen=random.randint(a+2,b-2)
            num=input("Hint: Falls between {} to {}:".format(gen,b))
            a=gen
        else:
            guess=int(guess)
            if a==guess and b==guess:
                num=input("last hint provided, try again:")
                continue
            l=random.randint(a+1,guess)
            h=random.randint(guess,b-1)
            num=input("Hint: Falls between {} to {}:".format(l,h))
            a=l
            b=h
    else:
        num=input("try again:")
