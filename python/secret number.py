# Secret number (hardcoded)
secret_number = 7

# Keep asking the user until they guess correctly
while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
        break
    else:
        print("❌ Try again!")
