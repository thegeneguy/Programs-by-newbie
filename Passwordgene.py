import random

alps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num='0987654321'
salps= alps.lower()
spcl = "!@#$%^&*-+\/|?><:;`~_.,"
r = input("Pwd length:")
r1=int(r.split(',')[0])
r2=int(r.split(',')[1])

name = input("what is your name?")
caps = int(input("include caps:"))
nums = int(input("include num:"))
spe = input("except special:")

simpwd= salps

if caps:
    simpwd+=alps
# print(simpwd)

if nums:
    simpwd+=num
# print(simpwd)

for i in spe:
    spcl=spcl.replace(i,'')

simpwd+=spcl
print()

for j in range(10):
    pwd=''
    for i in range(random.randint(r1,r2)):
        pwd += random.choice(simpwd)
    m = random.randint(0,r2-len(name))
    pwd = pwd[:m]+name+pwd[m+len(name):]
        # print(pwd)
    print(pwd,len(pwd))
