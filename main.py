import random


words = ["python", "developer", "hangman", "terminal", "github", "programming"]


word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

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
       |   |
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
      /    |
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

print("🎮 Welcome to Hangman! 🎮")
print(hangman_pics[0])

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

    print(hangman_pics[6 - attempts])

# Check win/lose conditions
if "_" not in guessed:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n💀 Game over! The word was:", word)
