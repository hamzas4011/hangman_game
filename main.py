import random

def play_game():
    fruits = ["apple", "mango", "banana", "grape", "orange", "kiwi", "melon", "peach"]
    word = random.choice(fruits)
    guessed = ["_"] * len(word)
    attempts = 4
    guessed[0] = word[0]

    hangman_pics = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    print("🎮 Welcome to Fruits Hangman! 🍎🍌🍇")
    print(f"Hint: The first letter is '{word[0]}'")
    print(hangman_pics[0])

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter (or type 'quit' to exit): ").lower()

        if guess == "quit":
            print("👋 Exiting game...")
            return

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("Wrong guess!")

        print(hangman_pics[min(4 - attempts, 4)])

    if "_" not in guessed:
        print("\n🎉 You win! The word was:", word)
    else:
        print("\n💀 Game over! The word was:", word)

while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
