#simple guessing game

import random 

numguesses = 0

print('Hello, Please enter your name: ')
playername = str(input())

number = random.randint(1,20)
print('Well, '+ playername + ', pick a number between 1 and 20')

for numguesses in range(6) :
    print('take a guess')
    guess = int(input())

    if guess =/= number:
        print('incorrect')

    if guess == number:
        break

if guess == number:
    numguesses = str(numguesses+1)
    priint(f'correct, good job. it took you {numguesses}')

if guess != number:
    number = str(number)
    print(f'no, the number was {number}')
