import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os

class EstonianTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Эстонский тест B1 уровня")
        self.root.geometry("1000x800")
        # Запрещаем изменение размеров окна
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.questions = [
            {
                "question": "Ma ... kodus.",
                "options": ["olen", "ole", "oli"],
                "answer": "olen"
            },
            {
                "question": "Kas sa ... kooli lähed?",
                "options": ["tule", "tulevad", "tuleb"],
                "answer": "tule"
            },
            {
                "question": "Ta ... homme tööle.",
                "options": ["ei lähe", "ei läheb", "ei mine"],
                "answer": "ei lähe"
            },
            {
                "question": "Me ... eile muuseumi.",
                "options": ["läksime", "lähete", "läheb"],
                "answer": "läksime"
            },
            {
                "question": "Nad ... homme puhkusele.",
                "options": ["lähevad", "läheb", "läksid"],
                "answer": "lähevad"
            },
            {
                "question": "Ta ... mind.",
                "options": ["aitab", "aita", "aitavad"],
                "answer": "aitab"
            },
            {
                "question": "Ma ... sind.",
                "options": ["näen", "näeb", "näete"],
                "answer": "näen"
            },
            {
                "question": "Kas te ... mind?",
                "options": ["kuulete", "kuulda", "kuulavad"],
                "answer": "kuulete"
            },
            {
                "question": "Nad ... raamatut.",
                "options": ["loevad", "loeb", "loeme"],
                "answer": "loevad"
            },
            {
                "question": "Ma ... sind homme.",
                "options": ["kohtan", "kohtub", "kohtuvad"],
                "answer": "kohtan"
            },
            {
                "question": "Ta ... uue auto.",
                "options": ["ostis", "osta", "ostan"],
                "answer": "ostis"
            },
            {
                "question": "Kas sa ... mind eile?",
                "options": ["nägid", "nägi", "näen"],
                "answer": "nägid"
            },
            {
                "question": "Me ... eile koos.",
                "options": ["olime", "oli", "oleme"],
                "answer": "olime"
            },
            {
                "question": "Ma ... sind väga.",
                "options": ["armastan", "armastab", "armastavad"],
                "answer": "armastan"
            },
            {
                "question": "Ta ... väga kiire.",
                "options": ["on", "oli", "ole"],
                "answer": "on"
            },
            {
                "question": "Kas te ... mulle?",
                "options": ["aitate", "aitab", "aita"],
                "answer": "aitate"
            },
            {
                "question": "Me ... eile kinos.",
                "options": ["käisime", "käib", "käivad"],
                "answer": "käisime"
            },
            {
                "question": "Nad ... oma kodu.",
                "options": ["armastavad", "armastan", "armastab"],
                "answer": "armastavad"
            },
            {
                "question": "Kas sa ... mind homme?",
                "options": ["kohtad", "kohtab", "kohtavad"],
                "answer": "kohtad"
            },
            {
                "question": "Ma ... eile uue sõbra.",
                "options": ["kohtasin", "kohtab", "kohtan"],
                "answer": "kohtasin"
            }
        ]

        self.listening_questions = [
            {"question": "Kus armastas Hendrik lapsena üksi käia?", "answer": "metsas"},
            {"question": "Kus hakkas Hendrik koolis käima?", "answer": "Tallinnas"},
            {"question": "Missugust puud armastab Hendrik kõige rohkem?", "answer": "tamm"},
            {"question": "Mitu korda on Hendrik kõrgkooli lõpetanud?", "answer": "2"},
            {"question": "Millise ajakirja peatoimetaja Hendrik on?", "answer": "Eesti Mets"},
            {"question": "Kes on Hendriku kõige parem reisikaaslane?", "answer": "naine"},
            {"question": "Mitu aastat tagasi kolis Hendrik maale elama?", "answer": "17"},
            {"question": "Mida teeb Hendrik praegu?", "answer": "kirjutab raamatut"}
        ]
        
        self.create_widgets()

    def create_widgets(self):
        # Frame for audio playback and listening questions
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")

        self.title_label = tk.Label(self.frame_top, text="Kuulamistesti 1. ülesanne, 1.-8. küsimus", font=("Helvetica", 16))
        self.title_label.pack()

        self.description_label = tk.Label(self.frame_top, text="Kuula lõiku ja kirjuta igale küsimusele sobiv vastus (1-3 sõna). Teksti kuula kaks korda.", bg="lightblue", font=("Helvetica", 10), padx=5, pady=5)
        self.description_label.pack(fill="x")

        self.frame_button = tk.Frame(self.root, pady=10, padx=10)
        self.frame_button.pack(fill="x")

        self.play_button = tk.Button(self.frame_button, text="Play", command=self.on_button_click1)
        self.play_button.pack()

        self.example_label = tk.Label(self.root, text="Näidis:\nKus armastas Hendrik lapsena üksi käia?\nVastus: metsas", bg="lightgreen", padx=5, pady=5, justify="left")
        self.example_label.pack(fill="x", pady=10, padx=10)

        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")

        self.answer_entries = []
        for i, question in enumerate(self.listening_questions, start=1):
            question_label = tk.Label(self.frame_questions, text=f"{i}. {question['question']}")
            question_label.pack(anchor="w")
            answer_entry = tk.Entry(self.frame_questions)
            answer_entry.pack(fill="x", pady=5)
            self.answer_entries.append(answer_entry)

        self.next_section_button = tk.Button(self.root, text="Перейти к грамматике", command=self.switch_to_grammar)
        self.next_section_button.pack(pady=20)

    def switch_to_grammar(self):
        self.is_listening_section = False
        self.frame_top.pack_forget()
        self.frame_button.pack_forget()
        self.example_label.pack_forget()
        self.frame_questions.pack_forget()
        self.next_section_button.pack_forget()

        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.option_buttons = []
        for i in range(3):
            btn = tk.Radiobutton(self.root, text="", variable=self.var, value="", font=("Arial", 14))
            btn.pack(anchor="w")
            self.option_buttons.append(btn)

        self.next_button = tk.Button(self.root, text="Следующий", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=20)

        self.display_question()

    def play_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load("audio/B1EestiKeel.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def on_button_click1(self):
        threading.Thread(target=self.play_audio).start()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            self.var.set("")
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, value=option)
                self.option_buttons[i].pack_forget()
                self.option_buttons[i].pack(anchor="w")
        else:
            self.show_result()

    def next_question(self):
        if self.is_listening_section:
            self.switch_to_grammar()
        else:
            if self.current_question < len(self.questions):
                question = self.questions[self.current_question]
                answer = self.var.get()
                self.answers.append(answer)
                if answer == question["answer"]:
                    self.score += 1

                self.current_question += 1
                if self.current_question < len(self.questions):
                    self.display_question()
                else:
                    self.show_result()

    def show_result(self):
        results_path = os.path.join(os.path.dirname(__file__), 'results.txt')
        with open(results_path, 'w', encoding='utf-8') as f:
            f.write(f'{self.score}\n')
            f.write(f'{len(self.questions)}\n')
            for answer in self.answers:
                f.write(f'{answer}\n')
            for question in self.questions:
                f.write(f'{question["answer"]}\n')

        self.root.destroy()

        subprocess.Popen(["python", "show_score.py"])

root = tk.Tk()
app = EstonianTestApp(root)
root.mainloop()
