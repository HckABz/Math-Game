import time 
import random

print('\nWelcome to my Game PEEEPS!!! Choose your Path\n')
print("1.Guessing Game")
print("2.Multipling Game")
print("3.Exit")

option=int(input('Enter number here:'))

if option==1:
    print('Guess the rigth number 1 through 5 and you get a token remember answer is randomly generated')
    print('-'*92)
    while True:
        number = input('Enter number: ')
        numberz = int(number)
        rnd=(random.randrange(1,5))

        print('checking status.........')
        time.sleep(1)

        if (numberz == rnd):
            print("YOU GOT IT HERE IS YOUR TOKEN #89819082")
            break
        elif (numberz != rnd):
            print('Nope try again')
        else:
            print("Invalid answer numbers only")

if option==2:
    while True:
        print("Welcome to the Multipling Game!!!")
        nm1=(random.randrange(1,5))
        nm2=(random.randrange(1,100))
        ans=int(input("Whats {} x {} :".format(nm1,nm2)))
        if (ans == nm1*nm2):
            print("You got it right CONGRATULATIONS")
            break
        elif ans != nm1*nm2:
            print ("No try again")
if option==3:
    print ("Have a nice day :)")
    quit()











    