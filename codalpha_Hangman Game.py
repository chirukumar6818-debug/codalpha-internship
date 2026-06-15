import random

words=["python","computer","hangman","programming","developer"]

word=random.choice(words)

guessed_letters=[]
incorrect_guesses=0
max_attempts=6

display=["_"]*len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses<max_attempts and "_" in display:
    print("\nWord:"," ".join(display))
    print("Guessed letters:"," ".join(guessed_letters))
    print(f"Attempts remaining:{max_attempts-incorrect_guesses}")

    guess=input("Enter a letter:").lower()

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i]==guess:
                 display[i]=guess
    else:
        print("Wrong guess!")
        attempts-=1

if "_" not in display:
    print("\nCongratulations! You have guessed the word:",word)
else:
    print("\nGameOver! The word was:",word)
        
                       