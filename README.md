# Tic-Tac-Toe Application

This is a **Tic-Tac-Toe** game built using Python's `tkinter` library. It allows two players to compete in a simple, visually appealing game, with features like score tracking, player name customization, and restart/reset functionality.

---

## Features

1. **Interactive Gameplay**:
   - Players take turns to place their markers (`X` or `O`) on a 3x3 grid.
   - The game announces a winner or a draw after each match.

2. **Player Customization**:
   - Players can enter their names for personalized gameplay.

3. **Scoreboard**:
   - Tracks the scores of both players and the number of draws.

4. **Controls**:
   - Restart the current game without resetting scores.
   - Reset scores and start fresh.

5. **Dynamic UI**:
   - Highlight winning combinations.
   - Adaptive buttons and status bar reflecting the current state.

---

## Installation

Follow these steps to install and run the application:

1. **Clone or Download the Repository**:
   - Clone the repository using:
     ```bash
     git clone https://github.com/your-username/tic-tac-toe.git
     ```
   - Alternatively, download the ZIP file and extract it.

2. **Install Python**:
   - Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Verify `tkinter`**:
   - `tkinter` is pre-installed with Python in most distributions. Verify its availability by running:
     ```bash
     python -m tkinter
     ```
   - If a blank window opens, `tkinter` is properly installed.

4. **Run the Script**:
   - Navigate to the directory containing the script:
     ```bash
     cd tic-tac-toe
     ```
   - Run the application:
     ```bash
     python tic_tac_toe.py
     ```

---

## How to Use

1. **Run the Program**:
   - Execute the script in any Python environment that supports the `tkinter` library.

2. **Set Player Names**:
   - Input player names in the provided fields and click **Set Names**.

3. **Play the Game**:
   - Players take turns clicking on the grid cells.
   - The game will automatically check for a winner or a draw after each move.

4. **Restart/Reset**:
   - Use the **Restart Game** button to start a new game while keeping the current scores.
   - Use the **Reset Scores** button to clear the scoreboard and start over.

---

## Dependencies

- Python 3.x
- `tkinter` (pre-installed with Python in most distributions)

---

## File Structure

The application is self-contained in a single Python script. No additional files or dependencies are required.

---

## Code Walkthrough

### Main Components

1. **Game Logic**:
   - The `board` is a 2D list representing the grid.
   - The `check_winner()` function checks for winning conditions or a draw.

2. **UI Elements**:
   - Buttons represent the grid cells.
   - Labels and entries allow player interaction and display game status.

3. **Control Functions**:
   - `handle_click(row, col)`: Handles player actions and updates the UI.
   - `reset_board()`: Resets the game board for a new round.
   - `reset_scores()`: Clears all scores.

4. **Dynamic Updates**:
   - `update_scoreboard()` and `update_status()` dynamically reflect the game's current state.

---

## Customization

You can modify the following:
- **Color Theme**: Change the button, label, or background colors to fit your style.
- **Winning Message**: Update the messages in the `messagebox.showinfo()` calls.
- **Grid Size**: Extend functionality for larger grid sizes.

---

## License

Feel free to use and modify the code for personal or educational purposes. Contributions and suggestions are welcome!
