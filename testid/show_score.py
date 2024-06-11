import csv
import tkinter as tk
from tkinter import messagebox, ttk
import os

def display_csv(user_answers, correct_answers):
    # Kuvab tulemused CSV-vormingus
    top = tk.Toplevel()
    top.title("Tulemused CSV-vormingus")
    
    tree = ttk.Treeview(top)
    tree["columns"] = ("user_answer", "correct_answer")
    tree.column("#0", width=120, minwidth=25)
    tree.column("user_answer", width=120, minwidth=25)
    tree.column("correct_answer", width=120, minwidth=25)
    
    tree.heading("#0", text="Küsimus", anchor=tk.W) # määrab selle standardveeru pealkirja
    tree.heading("user_answer", text="Sinu vastus", anchor=tk.W)
    tree.heading("correct_answer", text="Õige vastus", anchor=tk.W)
    
    for i, (user_answer, correct_answer) in enumerate(zip(user_answers, correct_answers)): #zip on funktsioon, mis võtab mitu itereeritavat objekti (nt loendid) ja ühendab nende elemendid korteežiks
        question_id = f"Küsimus {i+1}"
        tree.insert("", "end", text=question_id, values=(user_answer, correct_answer))
    
    tree.pack(side="top", fill="both", expand=True)

    for child in tree.get_children():
        item = tree.item(child)
        user_answer = item['values'][0]
        correct_answer = item['values'][1]
        if user_answer == correct_answer:
            tree.tag_configure('correct', background='lightgreen')
            tree.item(child, tags=('correct',))
        else:
            tree.tag_configure('incorrect', background='lightcoral')
            tree.item(child, tags=('incorrect',))

def show_score(score, total_questions, user_answers, correct_answers):
    # Kuvab tulemused
    root = tk.Tk()
    root.title("Testi tulemused")

    msg = f"Palju õnne, olete testi läbinud!\nTe saite {score} punkti {total_questions} punktist."
    lbl = tk.Label(root, text=msg, font=("Helvetica", 16))
    lbl.pack(pady=10)

    btn_show_csv = tk.Button(root, text="Kuva CSV-vormingus", command=lambda: display_csv(user_answers, correct_answers))
    btn_show_csv.pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()

def read_results():
    # Loe tulemused failist
    with open('results.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        score = int(lines[0].strip())
        total_questions = int(lines[1].strip())
        user_answers = [line.strip() for line in lines[2:2+total_questions]]
        correct_answers = [line.strip() for line in lines[2+total_questions:]]
    return score, total_questions, user_answers, correct_answers


if os.path.exists('results.txt'):
    score, total_questions, user_answers, correct_answers = read_results()
    show_score(score, total_questions, user_answers, correct_answers)
else:
    print("Faili results.txt ei leitud.")
