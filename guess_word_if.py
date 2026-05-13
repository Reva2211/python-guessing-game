secret_word = input("enter the secret word:")
guess=input("Enter your guess: ")
guess_count=0
guess_limit=3

while guess != secret_word and guess_limit>guess_count:
    guess_count+=1
    if guess_count<=1:
       print("you still have a chance and you are using your limit")
    guess=input("Guess the word:")
    if guess == secret_word:
            print("Correct!")
            print(f"you have used your limit {guess_count} out of {guess_limit}")
    else:
            print("Wrong!")
            if guess_limit>guess_count:
              print("you have a chance of ",guess_limit-guess_count)
            else:
                print("out of limit")

if secret_word == guess:
    print("You guessed the right word")
    if guess_count==0:
        print("congrats!you did not used your limit")
else:
    print("you have not guessed the right word and you are out of limit")
