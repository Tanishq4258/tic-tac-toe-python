import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            ask_play_again()
            break

def check_tie():
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        ask_play_again()
        root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        buttons[index]["fg"] = "blue" if current_player == "X" else "red"
        check_winner()
        check_tie()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

def ask_play_again():
    play_again = messagebox.askyesno("Tic-Tac-Toe", "Do you want to play again?")
    if play_again:
        root.destroy()  
        start_new_game()
    else:
        root.quit()  

def start_new_game():
    global root, buttons, current_player, winner, label
    root = tk.Tk() 
    root.title("Tic-Tac-Toe")
    root.config(bg="lightblue")

    buttons = [tk.Button(root, text="", font=("normal",25), width=6, height=2, command=lambda i=index: button_click(i)) for index in range(9)]
    for i, button in enumerate(buttons):
        button.grid(row=i //3, column=i %3, padx=5, pady=5)

    current_player = "X"
    winner = False
    label = tk.Label(root, text=f"Player {current_player}'s turn", font = ("Helvetica", 16, "bold"), fg = "darkblue", bg="lightblue", pady=10)
    label.grid(row=3, column=0, columnspan=3)

    root.mainloop()

start_new_game()