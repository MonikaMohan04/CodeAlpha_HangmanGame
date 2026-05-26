# ============================================================
#  CodeAlpha_HangmanGame
#  Task 1 — Text-Based Hangman Game
#  Author  : Monika M
#  Intern  : CodeAlpha Python Programming Internship
# ============================================================

# ── Imports ─────────────────────────────────────────────────
import random   # to pick a random word from the list

# ── Predefined Word List (5 words as per task scope) ────────
WORDS = ["python", "hangman", "coding", "laptop", "terminal"]

# ── Hangman ASCII Visuals ────────────────────────────────────
# A list of 7 strings — one for each stage (0 wrong → 6 wrong).
# Printed directly in the console every turn.

HANGMAN = [
    # 0 wrong guesses — empty gallows
    """
   +---+
   |   |
       |
       |
       |
       |
=========
    """,
    # 1 wrong guess — head
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========
    """,
    # 2 wrong guesses — head + body
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
    """,
    # 3 wrong guesses — head + body + left arm
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
    """,
    # 4 wrong guesses — head + body + both arms
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
    """,
    # 5 wrong guesses — head + body + both arms + left leg
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
    """,
    # 6 wrong guesses — full hangman — GAME OVER
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
    """,
]

# Maximum number of wrong guesses allowed
MAX_WRONG = 6


# ── Functions ────────────────────────────────────────────────

def choose_word():
    """Randomly pick and return one word from WORDS."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """
    Return the word with only guessed letters revealed.
    Unguessed letters are shown as '_'.

    Example: word='python', guessed={'p','y'} → 'p y _ _ _ _'
    """
    return "  ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def display_status(wrong_count, word, guessed_letters, wrong_letters):
    """
    Print the full game state for the current turn:
      - Hangman drawing
      - Masked word
      - Wrong guesses so far
      - Lives remaining
    """
    # Print the hangman picture matching number of wrong guesses
    print(HANGMAN[wrong_count])

    # Print the word with blanks
    print("  Word  :  " + display_word(word, guessed_letters))

    # Print wrong guesses as a neat list
    wrong_str = "  ".join(sorted(wrong_letters)) if wrong_letters else "none yet"
    print(f"\n  Wrong guesses ({wrong_count}/{MAX_WRONG}) : {wrong_str}")
    print(f"  Lives remaining              : {MAX_WRONG - wrong_count}")
    print("\n  " + "-" * 40)


def get_guess(guessed_letters):
    """
    Ask the player for a single letter.
    Keep asking until a valid, new letter is entered.
    """
    while True:
        guess = input("\n  Enter a letter : ").strip().lower()

        if len(guess) != 1:
            print("  ⚠  Please enter exactly ONE letter.")
        elif not guess.isalpha():
            print("  ⚠  Only letters are allowed.")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess   # valid new letter — return it


def play_game():
    """
    Run one full round of Hangman.
    Returns True if the player wants to play again, False to quit.
    """
    # ── Setup ─────────────────────────────────────────────────
    word             = choose_word()
    guessed_letters  = set()   # all letters guessed (correct + wrong)
    wrong_letters    = set()   # only the wrong ones
    wrong_count      = 0

    print("\n  A new word has been chosen. Start guessing!\n")

    # ── Game Loop ──────────────────────────────────────────────
    while wrong_count < MAX_WRONG:

        # Show current state
        display_status(wrong_count, word, guessed_letters, wrong_letters)

        # Check win condition — every letter in word has been guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\n  🎉  YOU WON!  The word was: '{word.upper()}'  🎉\n")
            break

        # Get a valid guess from the player
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print(f"\n  ✔  '{guess}' is in the word!")
        else:
            wrong_letters.add(guess)
            wrong_count += 1
            print(f"\n  ✘  '{guess}' is NOT in the word.")

    else:
        # Loop ended without winning — player lost
        print(HANGMAN[MAX_WRONG])
        print(f"  💀  GAME OVER!  The word was: '{word.upper()}'\n")

    # ── Play Again? ────────────────────────────────────────────
    print("  " + "-" * 40)
    again = input("\n  Play again? (yes / no) : ").strip().lower()
    return again in ("yes", "y")


# ── Main ─────────────────────────────────────────────────────

def main():
    """Entry point — show welcome message then loop rounds."""

    print("""
  ╔══════════════════════════════════════════╗
  ║       🎮   Hangman Game  🎮             ║
  ║         CodeAlpha Python Internship       ║
  ╚══════════════════════════════════════════╝

  Guess the hidden word — one letter at a time.
  You have 6 chances before the hangman is complete!
    """)

    # Keep playing rounds until the player says no
    while True:
        keep_playing = play_game()
        if not keep_playing:
            print("\n  👋  Thanks for playing! Keep coding! 🐍\n")
            break


# ── Run ───────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
