mystery_word = 'bread'
mystery_word = mystery_word.lower()
attempt = 0
status = ''
print('How To Play:\n| A | = the letter is in the correct position \n| A   = the letter is in the word, but not here \n  a   = the letter is not in the word')

for i in range(5):
    user_guess = input('Enter a five letter word: ')
    if user_guess == mystery_word:
        status = 'solved'
        break
    else:
        for i in range(5):
            if user_guess[i] == mystery_word[i]:
                print('| ' + user_guess[i].upper() + ' |')
            elif user_guess[i] != mystery_word[i] and user_guess[i] in mystery_word:
                print('| ' + user_guess[i].upper() + '  ')
            else:
                print('  ' + user_guess[i] + '  ')
        attempt = attempt + 1
if status != 'solved':
    print('Sorry you ran out of guesses. The word was ' + mystery_word.upper())
else:
    print('Correct! The mystery word was '+ mystery_word.upper())