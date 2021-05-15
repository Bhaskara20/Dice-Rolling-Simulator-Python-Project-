import random
import sys

print("=======================================================\n\n")
print("        SELAMAT DATANG DI SIMULASI KOCOK DADU\n\n")
print("=======================================================")


decide=input("Apa yang akan anda lakukan? >>")

while decide=="roll":
    num=random.randint(1,6)

    if num==1:
        print("|==========|")
        print("|          |")
        print("|    0     |")
        print("|          |")
        print("|==========|")
    elif num==2:
        print("|==========|")
        print("|  0       |")
        print("|          |")
        print("|       0  |")
        print("|==========|")
    elif num==3:
        print("|==========|")
        print("|          |")
        print("|  0 0 0   |")
        print("|          |")
        print("|==========|")
    elif num==4:
        print("|==========|")
        print("|  0    0  |")
        print("|          |")
        print("|  0    0  |")
        print("|==========|")
    elif num==5:
        print("|==========|")
        print("|  0   0   |")
        print("|    0     |")
        print("|  0   0   |")
        print("|==========|")
    elif num==6:
        print("|==========|")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|==========|")
    
    decide=input("Apa langkah selanjutnya? >> ")


if decide=="stop":
    sys.exit()