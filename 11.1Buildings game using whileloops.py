ans_num = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:

    guess_box = int(input('Guess : '))
    guess_count += 1

    if guess_box == ans_num:
        print('You win!')
        break

else:
    print('You failed')
