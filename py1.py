import random

secret = random.randint(1,10)
temp = input('guess what i am thinking about')
try:
    guess = int(temp)
except ValueError:
    print('invalid number')
    guess = secret

while guess != secret:
    temp = input('your answer is wrong, try again:')
    guess = int(temp)


if guess == 8:
    print('u r right')
    print('haha')
else:
    print('wrong choice')

print('game is over')
