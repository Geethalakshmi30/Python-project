def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'please input your lucky number in the window between 1 and {x}:'))
        if guess < random_number:
            print("sorry you got keyed the wrong no.Too low")
        elif guess > random_number:
            print("sorry you got keyed the wrong no.Too low")

    print(f' yay!! congragulation you won! you guess the correct {random_number}:')
guess(30)
