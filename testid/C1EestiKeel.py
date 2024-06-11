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
        self.root.geometry("1150x700")
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.audio_played = False  # Переменная для отслеживания состояния воспроизведения аудио
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
            {"question": "Kellele on mõeldud riigimetsamajanduskeskuse (RMK) üritused?", "answer": "peredele"},
            {"question": "Mis rändlindu loendati linnuvaatlusel kõige rohkem?", "answer": "metsvinti"},
            {"question": "Millele on Eesti Energia otsustanud üle minna?", "answer": "uutele arvestitele"},
            {"question": "Mida tuleks lisaks kontrollimisele küteseadmetega teha?", "answer": "puhastada"},
            {"question": "Kus küsitletud inimesed kõige rohkem internetti kasutavad?", "answer": "kodus"},
            {"question": "Kui kaua kestis näitus, kus vaatajarekord saavutati?", "answer": "neli nädalat"},
            {"question": "Mis loodusnähtus tekitas Küprose pealinnas pahandusi?", "answer": "tornaado"}
        ]
        
        self.create_widgets()

    def create_widgets(self):
        #Ülemise raami loomine ja päise paigutamine:
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")
        
        self.title_label = tk.Label(self.frame_top, text="Kuulamine 1-7 küsimused", font=("Helvetica", 16))
        self.title_label.pack()

        self.description_label = tk.Label(self.frame_top, text="Kuulake kuulamist ja kirjutage igale küsimusele sobiv vastus. Kuulake tekst üks kord.", bg="lightblue", font=("Helvetica", 10), padx=5, pady=5)
        self.description_label.pack(fill="x")
        
        self.frame_button = tk.Frame(self.root, pady=10, padx=10)
        self.frame_button.pack(fill="x")

        self.play_button = tk.Button(self.frame_button, text="Play", command=self.on_button_click1)
        self.play_button.pack()

        self.example_label = tk.Label(self.root, text="Näide:\nMida täna erinevates sadamates puhastati?\nVastus: merepõhi", bg="lightgreen", padx=5, pady=5, justify="left")
        self.example_label.pack(fill="x", pady=10, padx=10)
        #Looge küsimuste raam ja asetage küsimuste ja vastuste kastid
        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")
        #Muutuja self.answer_entries lähtestatakse sisestusväljade salvestamiseks tühja loendina
        self.answer_entries = []
        for i, question in enumerate(self.listening_questions, start=1): #loob sildi tekstiga, mis sisaldab küsimuse i numbrit ja küsimuse enda teksti
            question_label = tk.Label(self.frame_questions, text=f"{i}. {question['question']}")
            question_label.pack(anchor="w")

            entry = tk.Entry(self.frame_questions, width=100) #sisestusväljale
            entry.pack(anchor="w", pady=5) #vasakpoolne joondus
            self.answer_entries.append(entry)

        self.next_section_button = tk.Button(self.root, text="Next", command=self.next_question) 
        self.next_section_button.pack(pady=10)

    def switch_to_grammar(self):
        if self.is_listening_section:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            self.frame_top.pack_forget()
            self.frame_button.pack_forget()
            self.example_label.pack_forget()
            self.frame_questions.pack_forget()
            self.next_section_button.pack_forget()

            self.is_listening_section = False

            self.title_label.config(text="Грамматика C1 уровня")
            self.title_label.pack(fill="x")

            self.frame_grammar = tk.Frame(self.root, pady=10, padx=10)
            self.frame_grammar.pack(fill="x")

            self.grammar_question_label = tk.Label(self.frame_grammar, text="", font=("Helvetica", 14), wraplength=600)
            self.grammar_question_label.pack(pady=20)

            self.var = tk.StringVar() # salvestab kasutaja valitud vastusevaliku
            self.option_buttons = []
            for i in range(3):
                btn = tk.Radiobutton(self.frame_grammar, text="", font=("Helvetica", 12), variable=self.var, value="")
                btn.pack(anchor="w")
                self.option_buttons.append(btn)

            self.next_question_button = tk.Button(self.root, text="Järgmine küsimus", command=self.next_question)
            self.next_question_button.pack(pady=10)

            self.display_question()

    def on_button_click1(self):
        if not self.audio_played:
            self.audio_played = True
            threading.Thread(target=self.play_audio, args=("audio/C1EestiKeel.mp3",)).start()
        else:
            messagebox.showinfo("Info", "Saate heli esitada ainult üks kord.")

    def play_audio(self, filename):
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.grammar_question_label.config(text=question["question"])
            self.var.set("")
            
            # Eemaldage valitud eelmised nupud
            for btn in self.option_buttons:
                btn.destroy()
            
            # Looge uusi nuppe
            self.option_buttons = []
            for i, option in enumerate(question["options"]):
                btn = tk.Radiobutton(self.frame_grammar, text=option, font=("Helvetica", 12), variable=self.var, value=option)
                btn.pack(anchor="w")
                self.option_buttons.append(btn)
        else:
            self.show_result()

    def next_question(self):
        if self.is_listening_section:
            # Enne vahetamist hinnake kuulamisvastused
            self.grade_listening_answers()
            self.is_listening_section = False  # Määra muutuja väärtuseks False
            self.switch_to_grammar()  # Lülituge grammatikaküsimustele
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

    def grade_listening_answers(self):
        for i, entry in enumerate(self.answer_entries):
            answer = entry.get().strip().lower()
            self.answers.append(answer)
            if answer == self.listening_questions[i]["answer"]:
                self.score += 1
            self.switch_to_grammar()

    def show_result(self):
        results_path = os.path.join(os.path.dirname(__file__), 'results.txt')
        with open(results_path, 'w', encoding='utf-8') as f:
            f.write(f'{self.score}\n')
            f.write(f'{len(self.listening_questions) + len(self.questions)}\n')
            
            # Записываем ответы пользователя
            for answer in self.answers[:len(self.listening_questions)]:
                f.write(f'{answer}\n')
            for answer in self.answers[len(self.listening_questions):]:
                f.write(f'{answer}\n')
            
            # Записываем правильные ответы
            for question in self.listening_questions:
                f.write(f'{question["answer"]}\n')
            for question in self.questions:
                f.write(f'{question["answer"]}\n')

        self.root.destroy()
        subprocess.Popen(["python", "show_score.py"])


root = tk.Tk()
app = EstonianTestApp(root)
root.mainloop()

