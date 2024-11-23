import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Beautiful Tic-Tac-Toe")

# Game variables
player1_name = "Player 1"
player2_name = "Player 2"
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
scores = {player1_name: 0, player2_name: 0, "Draws": 0}

# Function to check for a winner
def check_winner():
    global board
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return board[row][0], [(row, 0), (row, 1), (row, 2)]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col], [(0, col), (1, col), (2, col)]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2], [(0, 2), (1, 1), (2, 0)]
    return None, []

# Function to handle cell click
def handle_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled", bg="#383838" if current_player == "X" else "#ff9800")
        winner, winning_combo = check_winner()
        if winner:
            highlight_winner(winning_combo)
            winner_name = player1_name if winner == "X" else player2_name
            scores[winner_name] += 1
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            update_scoreboard()
            reset_board()
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            scores["Draws"] += 1
            messagebox.showinfo("Game Over", "It's a draw!")
            update_scoreboard()
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            update_status()

# Function to highlight the winning combination
def highlight_winner(combo):
    for row, col in combo:
        buttons[row][col].config(bg="lightgreen")

# Function to reset the board for a new game
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state="normal", bg="#505050")
    update_status()

# Function to reset scores and start fresh
def reset_scores():
    global scores
    scores = {player1_name: 0, player2_name: 0, "Draws": 0}
    update_scoreboard()
    reset_board()

# Function to update the scoreboard
def update_scoreboard():
    score_label.config(
        text=f"{player1_name} (X): {scores[player1_name]} | {player2_name} (O): {scores[player2_name]} | Draws: {scores['Draws']}",
        fg="#ffffff"
    )

# Function to update the status bar
def update_status():
    status_label.config(text=f"{player1_name if current_player == 'X' else player2_name}'s turn ({current_player})", fg="#ffffff")

# Function to set player names
def set_player_names():
    global player1_name, player2_name
    player1_name = player1_entry.get() or "Player 1"
    player2_name = player2_entry.get() or "Player 2"
    update_scoreboard()
    update_status()

# UI Setup
# Player Name Input
name_frame = tk.Frame(root, bg="#212121", padx=15, pady=15)
name_frame.pack(pady=20)

tk.Label(name_frame, text="Player 1 (X):", font=("Arial", 16), bg="#212121", fg="#81c784").grid(row=0, column=0)
player1_entry = tk.Entry(name_frame, font=("Arial", 14), width=20, bg="#424242", fg="#81c784")
player1_entry.grid(row=0, column=1)

tk.Label(name_frame, text="Player 2 (O):", font=("Arial", 16), bg="#212121", fg="#ffb74d").grid(row=1, column=0)
player2_entry = tk.Entry(name_frame, font=("Arial", 14), width=20, bg="#424242", fg="#ffb74d")
player2_entry.grid(row=1, column=1)

tk.Button(name_frame, text="Set Names", font=("Arial", 12), bg="#2e7d32", fg="white", command=set_player_names).grid(row=2, column=0, columnspan=2, pady=10)

# Scoreboard
score_label = tk.Label(root, text="", font=("Arial", 16), bg="#212121", fg="#ffffff")
score_label.pack(pady=10)

# Status Bar
status_label = tk.Label(root, text="", font=("Arial", 14), bg="#212121", fg="#ffffff")
status_label.pack()

# Game Board
buttons_frame = tk.Frame(root, bg="#212121")
buttons_frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(buttons_frame, text="", font=("Arial", 32), width=5, height=2, relief="flat",
                           bg="#616161", fg="white", activebackground="#424242", 
                           command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        buttons[row][col] = button

# Control Buttons
control_frame = tk.Frame(root, bg="#212121")
control_frame.pack(pady=10)

tk.Button(control_frame, text="Restart Game", font=("Arial", 14), bg="#0288d1", fg="white", command=reset_board).pack(side="left", padx=15)
tk.Button(control_frame, text="Reset Scores", font=("Arial", 14), bg="#d32f2f", fg="white", command=reset_scores).pack(side="left", padx=15)

# Initialize
update_scoreboard()
update_status()

# Run the application
root.config(bg="#212121")
root.mainloop()