import random

guessesTaken = 0
print('Enter your name here: ')
myName = input()
number = random.randint(1, 10)
print(myName + ', guess the noumbers between 1 to 10')
while guessesTaken < 6:
    print("Ready? Go!")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Nope, too low.')

    if guess > number:
        print('Nah, too high.')

    if guess == number:
        break

    if guess == number:
         guessesTaken = str(guessesTaken)
print('Correct, ' + myName + '! You guessed my number in ' + guessesTaken + ' I think if you guessed correct, it means you are not from Hiiumaa!')

if guess != number:
        number = str(number)
        print('Okay, i see you are from Hiiumaa. Let me help you. My noumber was' + number)