import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os

class EstonianTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Эстонский тест C1 уровня")
        self.root.geometry("1000x800")
        # Запрещаем изменение размеров окна
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.questions = [
            {
                "question": "Ma olen veendunud, et ... on oluline osa kultuurist.",
                "options": ["muusika", "muusikast", "muusikale"],
                "answer": "muusika"
            },
            {
                "question": "Kas sa tead, kelle ... see raamat on?",
                "options": ["raamat", "raamatule", "raamatust"],
                "answer": "raamat"
            },
            {
                "question": "Ta rääkis mulle loo, mis oli ... kuulnud.",
                "options": ["kogemata", "kogemisel", "kogemata saanud"],
                "answer": "kogemata saanud"
            },
            {
                "question": "Ma olen kindel, et ta oli selleks ajaks juba ... läinud.",
                "options": ["kodust", "kodus", "kodu"],
                "answer": "kodust"
            },
            {
                "question": "Mul on raske mõista, miks ta sellise ... tegi.",
                "options": ["otsus", "otsust", "otsuses"],
                "answer": "otsuse"
            },
            {
                "question": "Ta väitis, et on seda ... teinud.",
                "options": ["mitmeid kordi", "mitmeid korda", "mitmeid korra"],
                "answer": "mitmeid kordi"
            },
            {
                "question": "Kas sa oled kunagi ... olnud?",
                "options": ["välismaal", "välismaale", "välismaalase"],
                "answer": "välismaal"
            },
            {
                "question": "Mulle ei meeldi, kuidas ta minuga ...",
                "options": ["käitub", "käituma", "käitunud"],
                "answer": "käitub"
            },
            {
                "question": "Tema ... on alati väga huvitavad.",
                "options": ["jutu", "jutud", "jutt"],
                "answer": "jutud"
            },
            {
                "question": "Ma ei suuda keskenduda, kui ümberringi on palju ...",
                "options": ["müra", "mürad", "müraga"],
                "answer": "müra"
            },
            {
                "question": "Ta sõitis ... mõtlematult.",
                "options": ["autoga", "autost", "autole"],
                "answer": "autoga"
            },
            {
                "question": "Miks sa temaga nii halvasti ...?",
                "options": ["käitud", "käituma", "käitusid"],
                "answer": "käitusid"
            },
            {
                "question": "Ma olen alati tahtnud ... rääkida.",
                "options": ["prantsuse keelt", "prantsuse keeles", "prantsuse keel"],
                "answer": "prantsuse keelt"
            },
            {
                "question": "See on kõige raskem ... , mida ma olen kunagi lahendanud.",
                "options": ["ülesanne", "ülesande", "ülesannet"],
                "answer": "ülesanne"
            },
            {
                "question": "Ma ei suuda unustada, kuidas ta mind ...",
                "options": ["abistas", "abistama", "abistanud"],
                "answer": "abistas"
            },
            {
                "question": "Ma olen kindel, et see oli ... õige otsus.",
                "options": ["tema", "temast", "tema poolt"],
                "answer": "tema poolt"
            },
            {
                "question": "Kas sa tead, kus asub ...?",
                "options": ["muuseum", "muuseumile", "muuseumi"],
                "answer": "muuseum"
            },
            {
                "question": "Mul on vaja sinult ...",
                "options": ["abi", "abistama", "abist"],
                "answer": "abi"
            },
            {
                "question": "Me peame selle probleemiga ... tegelema.",
                "options": ["kohe", "kohelt", "kohegi"],
                "answer": "kohe"
            },
            {
                "question": "Ta on ... inimene, keda ma tean.",
                "options": ["targem", "targema", "tarkem"],
                "answer": "targem"
            },
            {
                "question": "Ma olen kindel, et ta on selle ... juba teinud.",
                "options": ["ülesande", "ülesandega", "ülesannet"],
                "answer": "ülesande"
            },
            {
                "question": "Ta ... mulle, et ta tuleb hiljem.",
                "options": ["ütles", "ütlema", "ütleks"],
                "answer": "ütles"
            },
            {
                "question": "Kas sa oled ... käinud?",
                "options": ["Tallinnas", "Tallinna", "Tallinn"],
                "answer": "Tallinnas"
            },
            {
                "question": "Mulle meeldib lugeda ... raamatuid.",
                "options": ["ajaloolised", "ajalooliste", "ajaloolisi"],
                "answer": "ajaloolisi"
            },
            {
                "question": "Ta on juba ... kaks korda külastanud.",
                "options": ["Eestit", "Eestis", "Eestisse"],
                "answer": "Eestit"
            },
            {
                "question": "Kas sa ... mulle oma plaanidest?",
                "options": ["rääkiksid", "räägiksid", "räägiks"],
                "answer": "rääkiksid"
            },
            {
                "question": "Ma olen kindel, et see oli tema ... otsus.",
                "options": ["parim", "parem", "parema"],
                "answer": "parim"
            },
            {
                "question": "Ma pean minema arsti juurde, sest ma ei tunne end ...",
                "options": ["hästi", "heasti", "hästi"],
                "answer": "hästi"
            },
            {
                "question": "Ta on minu ... rääkinud.",
                "options": ["ema", "emast", "emale"],
                "answer": "emast"
            },
            {
                "question": "Mul on vaja ... poodi minna.",
                "options": ["kohe", "kohta", "kohelt"],
                "answer": "kohe"
            }
        ]

        self.listening_questions = [
            "Kellele on mõeldud riigimetsamajanduskeskuse (RMK) üritused?",
            "Mis rändlindu loendati linnuvaatlusel kõige rohkem?",
            "Millele on Eesti Energia otsustanud üle minna?",
            "Mida tuleks lisaks kontrollimisele küteseadmetega teha?",
            "Kus küsitletud inimesed kõige rohkem internetti kasutavad?",
            "Kui kaua kestis näitus, kus vaatajarekord saavutati?",
            "Mis loodusnähtus tekitas Küprose pealinnas pahandusi?"
        ]
        
        self.create_widgets()

    def create_widgets(self):
        # Frame for audio playback and listening questions
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")

        self.title_label = tk.Label(self.frame_top, text="Kuulamistesti 1. ülesanne, 1.-7. küsimus", font=("Helvetica", 16))
        self.title_label.pack()

        self.description_label = tk.Label(self.frame_top, text="Kuula lõiku uudistesaatesat ja kirjuta igale küsimusele sobiv vastus (1-3 sõna). Teksti kuula kaks korda.", bg="lightblue", font=("Helvetica", 10), padx=5, pady=5)
        self.description_label.pack(fill="x")

        self.frame_button = tk.Frame(self.root, pady=10, padx=10)
        self.frame_button.pack(fill="x")

        self.play_button = tk.Button(self.frame_button, text="Play", command=self.on_button_click1)
        self.play_button.pack()

        self.example_label = tk.Label(self.root, text="Näidis:\nMille puhastus täna erinevates sadamates käis?\nVastus: merepõhja", bg="lightgreen", padx=5, pady=5, justify="left")
        self.example_label.pack(fill="x", pady=10, padx=10)

        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")

        self.answer_entries = []
        for i, question in enumerate(self.listening_questions, start=1):
            question_label = tk.Label(self.frame_questions, text=f"{i}. {question}")
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
        pygame.mixer.music.load("audio/C1EestiKeel.mp3")
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
