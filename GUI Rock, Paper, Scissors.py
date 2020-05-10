import tkinter as tk
from tkinter import ttk
import random
import pandas as pd
import os.path

'''Popup box for game results'''
def popup_box(user, comp, label3_text):
    choice = ["Rock", "Paper", "Scissors"]
    popup = tk.Tk()
    popup.wm_title("Results")
    popup.geometry("150x150")
    
    label1 = ttk.Label(popup, text = "User: "+choice[user-1]).pack(side = "top", fill = "x", pady = 10)
    
    label2 = ttk.Label(popup, text = "Computer: "+choice[comp-1]).pack(side = "top", fill = "x", pady = 10)
    
    label3 = ttk.Label(popup, text = label3_text).pack(side = "top", fill = "x", pady = 10)
    
    B1 = ttk.Button(popup, text = "Ok", command = popup.destroy).pack()

    user_array.append(user), comp_array.append(comp), final_results.append(label3_text)
    
    popup.mainloop()

'''Winner is selected'''
def select_winner(user, comp):
    difference = user-comp
    if difference == 0:
        draws_num_text.set(draws_num_text.get() + 1)
        return "Drawn"
    elif difference in (-2,1):
        user_wins_text.set(user_wins_text.get() + 1)
        return "You Win!"
    else:
        comp_wins_text.set(comp_wins_text.get() + 1)
        return "Computer Wins!"

'''When user choice is selected, computer selection is also made''' 
def button_selected(user_action):
    comp_selection = random.choice([1, 2, 3])
    popup_box(user_action, comp_selection, select_winner(user_action, comp_selection))


def on_closing():
    data = {"User": user_array,
        "Computer": comp_array,
        "Result": final_results}
    df = pd.DataFrame({"User": user_array, "Computer": comp_array, "Final Results": final_results})
    
    if os.path.exists("/Users/jawahar/Desktop/Programming/GUI RPS.xlsx") == False:
        df.to_excel('/Users/jawahar/Desktop/Programming/GUI RPS.xlsx')
    else:
        df1 = pd.read_excel("/Users/jawahar/Desktop/Programming/GUI RPS.xlsx")
        df1 = df1.drop(columns = ["Unnamed: 0"])
        newdf = df.append(df1, ignore_index=True)
        newdf.to_excel('/Users/jawahar/Desktop/Programming/GUI RPS.xlsx')
    root.destroy()


'''The main GUI frame is initialised'''
def main():
    global root, comp_wins_text, user_wins_text, draws_num_text, user_array, comp_array, final_results

    user_array, comp_array, final_results = [], [], []
    
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    comp_wins_text, user_wins_text, draws_num_text = tk.IntVar(), tk.IntVar(), tk.IntVar()

    computer_label = tk.Label(root, text = "Computer").pack(side="left")
    computer_wins_label = tk.Label(root, textvariable = comp_wins_text, fg = "red").pack(side="left")

    user_label = tk.Label(root, text = "You").pack(side="left")
    user_wins_label = tk.Label(root, textvariable = user_wins_text, fg = "green").pack(side="left")
    
    rock_button = tk.Button(root, text = "Rock", fg = "red", command = lambda: button_selected(1)).pack(side = "left", padx = 10, pady = 10)
    
    paper_button = tk.Button(root, text = "Paper", fg = "red", command = lambda: button_selected(2)).pack(side = "left", padx = 10, pady = 10)

    scissors_button = tk.Button(root, text = "Scissors", fg = "red", command = lambda: button_selected(3)).pack(side = "left", padx = 10, pady = 10)

    draws_label = tk.Label(root, text = "Draws").pack(side="left")
    draws_update_label = tk.Label(root, textvariable = draws_num_text, fg = "blue").pack(side="left")

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == '__main__':
    main()
