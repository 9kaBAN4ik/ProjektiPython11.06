import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os

class EstonianTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Эстонский тест A2 уровня")
        self.root.geometry("1000x800")
        # Запрещаем изменение размеров окна
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.questions = [
            {
                "question": "Millal on sinu sõbra sünnipäev? - 24.06. ...",
                "options": ["24.juunil", "24.juunis", "24.juuni"],
                "answer": "24.juunil"
            },
            {
                "question": "Meie peres on kolm ...?",
                "options": ["laps", "last","lapsed"],
                "answer": "last"
            },
            {
                "question": "Mulle väga meeldib kööki ...",
                "options": ["koristada", "rääkida", "süüa"],
                "answer": "koristada"
            },
            {
                "question": "Tänan sind kirja ...",
                "options": ["eest", "taga", "juures"],
                "answer": "eest"
            },
            {
                "question": "Minu nimi ... Mari-Liis.",
                "options": ["olema", "on", "olen"],
                "answer": "on"
            },
            {
                "question": "... olen 37 aastat vana.",
                "options": ["Mul", "Mina", "Mulle"],
                "answer": "Mina"
            },
            {
                "question": "Eile ma ... haigeks.",
                "options": ["sain", "võin", "jäin"],
                "answer": "jäin"
            },
            {
                "question": "Täna oli klassis 16 ...",
                "options": ["õpilane", "õpilast", "õpilased"],
                "answer": "õpilast"
            },
            {
                "question": "Minu isa käib iga päev ...",
                "options": ["poodis", "poes", "poodi"],
                "answer": "poes"
            },
            {
                "question": "Lapsena soovis Liina saada ...",
                "options": ["kokkaks", "kokaks", "kokana"],
                "answer": "kokaks"
            },
            {
                "question": "Mis sõna ei sobi ritta?",
                "options": ["kohv", "restoran", "kohvik"],
                "answer": "kohv"
            },
            {
                "question": "Õhutemperatuur on +3°C.",
                "options": ["kolm kraadi", "kolm kraadi külma", "kolm kraadi sooja"],
                "answer": "kolm kraadi sooja"
            },
            {
                "question": "1. korrusel asub ilusalong.",
                "options": ["Esimene korrusel", "Ühel korrusel", "Esimesel korrusel"],
                "answer": "Esimesel korrusel"
            },
            {
                "question": "Õues on ... ilm.",
                "options": ["vihmane", "vihm", "vihma sajab"],
                "answer": "vihmane"
            },
            {
                "question": "Lapsed tahavad õues ...",
                "options": ["jalutama", "jalutavad", "jalutada"],
                "answer": "jalutada"
            },
            {
                "question": "Minu poja lemmikloomad on kass ... koer",
                "options": ["ja", "et", "aga"],
                "answer": "ja"
            },
            {
                "question": "Eile ma ... jälle lapsega kalal.",
                "options": ["olin", "olesin", "olen"],
                "answer": "olin"
            },
            {
                "question": "See on Tallinn-Maardu buss.",
                "options": ["Buss sõidab Talinna Maardu", "Buss sõidab Talinna Maardus", "Buss sõidab Tallinnast Maardusse."],
                "answer": "Buss sõidab Tallinnast Maardusse."
            },
            {
                "question": "Kuni 4-aastastele lastele!",
                "options": ["Sissepääs on ainult täiskasvanutele.", "Siin võivad olla väikesed lapsed.", "Lastele on keelatud."],
                "answer": "Siin võivad olla väikesed lapsed."
            },
            {
                "question": "Kas teie elate ...?",
                "options": ["Lasnamäele", "Lasnamäes", "Lasnamäel"],
                "answer": "Lasnamäel"
            },
            {
                "question": "Siin on ainult uued ...",
                "options": ["raamatut", "raamat", "raamatud"],
                "answer": "raamatud"
            },
            {
                "question": "Siia saab jätta oma mantli.",
                "options": ["riidehoid", "pank", "apteek"],
                "answer": "riidehoid"
            },
            {
                "question": "Kus ... oled sündinud?",
                "options": ["ta", "nad", "sa"],
                "answer": "sa"
            },
            {
                "question": "Olete väga oodatud minu ...",
                "options": ["juubeli", "juubelile", "juubel"],
                "answer": "juubelile"
            },
            {
                "question": "Kell on 13:45.",
                "options": ["Kell on kolmveerand kolm.", "Kell on kolmveerand kaks.", "Kell on veerand kolmteist."],
                "answer": "Kell on kolmveerand kaks."
            },
            {
                "question": "Palun istuge!",
                "options": ["Suur tänu.", "Homseni.", "Pole viga."],
                "answer": "Suur tänu."
            },
            {
                "question": "Pille ema on koolis ...",
                "options": ["õpetaja", "õpetajaks", "õpetajana"],
                "answer": "õpetaja"
            },
            {
                "question": "Toidupood töötab kella 8:00 kuni 18:00.",
                "options": ["kella kaheksa kuni kaheksateist", "kella kaheksast kuni kuueni", "kella kaheksast kuni kaheksateist"],
                "answer": "kella kaheksast kuni kuueni"
            },
            {
                "question": "Sõidame homme ... maale.",
                "options": ["rongiga", "rongis", "rong"],
                "answer": "rongiga"
            },
            {
                "question": "Hommikuti sööme tavaliselt ...",
                "options": ["puder", "puuder", "putru"],
                "answer": "putru"
            },
            {
                "question": "Me ei ... prantsuse keelt.",
                "options": ["õppima", "õpi", "õpime"],
                "answer": "õpi"
            },
            {
                "question": "... päeva on aastas?",
                "options": ["Kuidas", "Mitu", "Mis"],
                "answer": "Mitu"
            }
        ]

        self.listening_questions = [
            {"question": "Mitu tundi reis kestab?", "answer": ["4", "neli"]},
            {"question": "Mida saab restoranis süüa?", "answer": ["Pannkook", "pannkooke", "kook", "kooke"]},
            {"question": "Mida saab kohvikus näha?", "answer": ["Film", "filmi"]},
            {"question": "Mis on poes soodsa hinnaga?", "answer": ["kingad"]},
            {"question": "Mis kell algab etendus?", "answer": ["Üks", "kolmteist", "1", "13", "kell 1", "kell 13", "kell üks", "kell 13"]},
            {"question": "Mille saab osta infopunktist?", "answer": ["Foto", "fotod", "fotot"]}
        ]

        self.create_widgets()

    def create_widgets(self):
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
        pygame.mixer.music.load("audio/A2EestiKeel.mp3")  # Убедитесь, что путь к файлу правильный
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
