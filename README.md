# 🇺🇸 U.S. States Game

An interactive U.S. States guessing game built using **Python Turtle** and **Pandas**.  
Type state names to label them on the U.S. map. If you exit early, the program generates a CSV file containing the states you missed so you can learn them later.

---

## ✨ Features

- 🗺️ Displays a blank U.S. map using Turtle graphics
- ⌨️ User inputs state names through a popup text box
- ✅ Correct guesses are written at the correct location on the map
- 📊 Uses Pandas to read state coordinates from `50_states.csv`
- 🚪 Type `Exit` anytime to generate a CSV of unguessed states

---

## 🧠 How It Works

- The program reads all state names + coordinates from `50_states.csv`
- Each time you guess a correct state, it gets added to `guessed_states`
- A turtle writes the state name on the map at its `(x, y)` position
- If you type **Exit**, it saves all unguessed states to:

`failed_to_guess.csv`

---

## 📁 Project Structure
```
us-states-turtle-game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── failed_to_guess.csv # generated after typing "Exit"
├── .gitignore
└── README.md
```
---
## Gameplay

<img width="2560" height="1310" alt="Screenshot (183)" src="https://github.com/user-attachments/assets/155f84ce-88a8-4c95-8694-d7974773f89f" />

---
## ⚙️ Requirements

- Python 3.7 or +
- pandas

Install pandas using:

```bash
pip install pandas
```
---

## ▶️ How to Run

**Clone the repository:**

`https://github.com/sudinkatuwal7/us_states_quiz.git`

`cd us-states-turtle-game`


**Run the program:**
```
python main.py
```

---

## 🎮 Controls / Gameplay

Enter a state name in the input box

Correct answers will appear on the map

To give up and learn the missed states:

**Type:**
```
Exit
```
---

## 📝 Output File

If you exit before guessing all 50 states, the program generates:
```
failed_to_guess.csv
```
This file contains the states you missed, so you can practice them later.

---

## 🚀 Future Improvements

- Keep asking until all 50 are guessed

- Prevent duplicate guesses

- Show incorrect guess feedback

- Add timer or scoring system

---

## 🎉 Enjoy the Game!

`Have fun exploring the U.S. map, test your geography skills, and keep on learning!`
