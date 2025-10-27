import random

# Word bank
words = ['apple', 'orange', 'kiwi', 'pineapple', 'banana', 'pear', 'mango']

# Hangman ASCII art stages
hang_man = {
    0: ('     ',
        '     ',
        '     '),
    1: (' o   ',
        '     ',
        '     '),
    2: (' o   ',
        ' |   ',
        '     '),
    3: (' o   ',
        '/|   ',
        '     '),
    4: (' o   ',
        '/|\\ ',
        '     '),
    5: (' o   ',
        '/|\\ ',
        '/    '),
    6: (' o   ',
        '/|\\ ',
        '/ \\ ')
}


def display_man(wrong_answer):
    """Display the hangman based on wrong attempts"""
    for line in hang_man[wrong_answer]:
        print(line)


def display_hint(hint):
    """Display the current hint (with underscores and guessed letters)"""
    print(" ".join(hint))


def display_answer(answer):
    """Show the correct answer at the end"""
    print(f"The word was: {answer}")


def main():
    answer = random.choice(words)  # Random word from the list
    hint = ["_"] * len(answer)     # Create blanks
    guessed = set()
    wrong_guesses = 0
    max_wrong = 6

    print("🎯 Welcome to Hangman! 🎯")

    # Game loop
    while wrong_guesses < max_wrong and "_" in hint:
        display_man(wrong_guesses)
        display_hint(hint)
        print(f"Guessed letters: {', '.join(sorted(guessed))}")
        
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single letter.")
            continue

        if guess in guessed:
            print("⚠️ You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in answer:
            print("✅ Good guess!")
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1

    # End game
    display_man(wrong_guesses)
    if "_" not in hint:
        print("🎉 You win!")
        display_hint(hint)
    else:
        print("💀 Game over!")
        display_answer(answer)


if __name__ == "__main__":
    main()
