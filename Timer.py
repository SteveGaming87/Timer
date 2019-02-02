from time import sleep
import winsound
import os

print("""**************************
Welcome To FASTIMER®
**************************""")

def Main():
    m = 0
    while True:
        try:
            countdown = int(input("How many seconds:  "))
            break
        except ValueError:
            print("ERROR, TRY AGAIN")
    original = countdown
    while countdown >= 60:
        countdown -= 60
        m += 1
    for i in range (original,0,-1):
        if m < 0:
            break
        for i in range(countdown,-2,-1):
            if i % 60 == 0:
                m-=1
            if i == 0:
                break
            os.system('cls')
            print(m," minutes and ",i," seconds")
            sleep(1)
        if m < 0:
            break
        for j in range(59,-1,-1):
            if j % 60 == 0:
                m-=1
            os.system('cls')
            print(m," minutes and ",j," seconds")
            sleep(1)
    print("TIMER FINISHED")
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

Main()

yes = ["y", "Y", "Yes", "yes"]
print(" ")
Again = input("Want to go again? [Y or N]")
if Again in yes:
    Main()
else:
    exit()
