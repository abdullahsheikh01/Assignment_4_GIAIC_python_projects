# **Project_3_Guess_the_Number_Game_Python_Project_(user)**
This is an interactive **number guessing game**, but with a twist—**the computer** will try to guess your number! The user provides feedback on whether the guess is **too low, too high, or correct**, and the computer adjusts its guesses accordingly.

## How It Works
1. The user **chooses a secret number** in their mind (between 1 and 220 by default).
2. The **computer makes a guess** and waits for user feedback.
3. The user provides feedback using:
   - `"c"` → Correct guess 🎯
   - `"l"` → A little low (computer increases guess slightly)
   - `"h"` → A little high (computer decreases guess slightly)
   - `"vl"` → Very low (computer increases guess significantly)
   - `"vh"` → Very high (computer decreases guess significantly)
4. The computer continues guessing until it finds the correct number.
5. Once correct, the game prints `"Yah! computer guessed correct number!"`.

## Features
- The **computer actively adjusts its guessing strategy** based on user feedback.
- Supports **fine-tuned and broad adjustments** for more dynamic guessing.
- Simple and fun interactive gameplay.

## Program Code Link(Google Colab):
https://colab.research.google.com/drive/1cxkAyXVfkxzUKHOzUOJZQ0wl_rHbNiCm?usp=sharing