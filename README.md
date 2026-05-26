# 🎮 CodeAlpha_HangmanGame


---

## 📌 Project Description

**CodeAlpha_HangmanGame** is a classic word-guessing game that runs entirely in the terminal. A random word is chosen from a list of 5 predefined words. The player guesses one letter at a time — the hangman drawing grows with each wrong guess. Guess the full word before 6 mistakes to win!

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎨 ASCII Hangman Visual | 7-stage drawing printed to console each turn |
| 🔤 5 Predefined Words | python, hangman, coding, laptop, terminal |
| 🔁 Play Again Loop | Replay as many rounds as you like |
| ✅ Input Validation | Rejects non-letters, multi-char input, repeated guesses |
| 💡 Live Status | Wrong guesses, lives remaining, masked word — updated every turn |

---

## 🗂️ Folder Structure

```
CodeAlpha_HangmanGame/
│
├── main.py            # Complete game source code
├── README.md          # Project documentation
└── requirements.txt   # No external dependencies needed
```

---

## 🛠️ Technologies & Key Concepts

| Concept | Where Used |
|---|---|
| `random` | `random.choice()` to pick a word |
| `while` loop | Game loop, play-again loop, input validation loop |
| `if-else` | Correct/wrong guess checking, win/lose logic |
| Strings | `.lower()`, `.strip()`, `.join()`, `.isalpha()` |
| Lists | `WORDS` word bank, `HANGMAN` stage list |
| Sets | Efficient tracking of guessed and wrong letters |
| Functions | `choose_word()`, `display_word()`, `get_guess()`, `play_game()` |

---

## 🚀 How to Run

```bash
# Navigate into the folder
cd CodeAlpha_HangmanGame

# Run the game
python main.py
```

> Use `python3 main.py` on Linux/Mac if needed. No installs required — pure Python 3 standard library.

---

## 🖥️ Sample Console Output

```
  ╔══════════════════════════════════════════╗
  ║       🎮   Hangman Game  🎮             ║
  ║         CodeAlpha Python Internship       ║
  ╚══════════════════════════════════════════╝

  A new word has been chosen. Start guessing!

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========

  Word  :  _ _ _ _ _ _

  Wrong guesses (5/6) : a  e  i  t  z
  Lives remaining     : 1

  ----------------------------------------

  Enter a letter : p

  ✔  'p' is in the word!

  ...

  🎉  YOU WON!  The word was: 'PYTHON'  🎉
```

---

## 👩‍💻 Author

Monika M
---

## 📄 License

Open-source — free to use for educational purposes.
