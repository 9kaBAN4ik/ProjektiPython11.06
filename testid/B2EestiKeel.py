import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os

class EstonianTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Эстонский тест B2 уровня")
        self.root.geometry("1150x925")
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.audio_played = False  # Переменная для отслеживания состояния воспроизведения аудио
        self.questions = [
            {
                "question": "Millal ... sa Tallinnasse?",
                "options": ["lähed", "läheb", "lähevad"],
                "answer": "lähed"
            },
            {
                "question": "Kus ... teie koer?",
                "options": ["on", "oli", "oleks"],
                "answer": "on"
            },
            {
                "question": "Mis ... te eile?",
                "options": ["tegid", "tegi", "tegin"],
                "answer": "tegid"
            },
            {
                "question": "Nad ... juba lahkunud.",
                "options": ["on", "oli", "oleks"],
                "answer": "on"
            },
            {
                "question": "Ma ... homme tööle.",
                "options": ["lähen", "läheb", "lähevad"],
                "answer": "lähen"
            },
            {
                "question": "Kas sa ... teda?",
                "options": ["tead", "teab", "teavad"],
                "answer": "tead"
            },
            {
                "question": "Mulle ... see film väga.",
                "options": ["meeldis", "meeldib", "meeldivad"],
                "answer": "meeldis"
            },
            {
                "question": "Me ... eile kinos.",
                "options": ["käisime", "käib", "käivad"],
                "answer": "käisime"
            },
            {
                "question": "Ma ... sind aidata.",
                "options": ["võin", "võib", "võivad"],
                "answer": "võin"
            },
            {
                "question": "Kas te ... mind kuulata?",
                "options": ["saate", "saab", "saavad"],
                "answer": "saate"
            },
            {
                "question": "Nad ... uut maja.",
                "options": ["ehitavad", "ehitab", "ehitame"],
                "answer": "ehitavad"
            },
            {
                "question": "Ta ... homme varakult.",
                "options": ["tuleb", "tulen", "tulevad"],
                "answer": "tuleb"
            },
            {
                "question": "Ma ei ... sind eile.",
                "options": ["näinud", "näinud", "nägin"],
                "answer": "näinud"
            },
            {
                "question": "Me ... eile palju tööd.",
                "options": ["tegime", "tegi", "tegin"],
                "answer": "tegime"
            },
            {
                "question": "Ma ei ... enam oodata.",
                "options": ["saa", "saa", "saab"],
                "answer": "saa"
            },
            {
                "question": "Kas sa ... mulle oma plaanidest?",
                "options": ["rääkiksid", "rääkima", "räägib"],
                "answer": "rääkiksid"
            },
            {
                "question": "Me peame ... lahenduse leidma.",
                "options": ["kohe", "kohelt", "kohegi"],
                "answer": "kohe"
            },
            {
                "question": "Ta ... alati õigel ajal.",
                "options": ["tuleb", "tulen", "tulevad"],
                "answer": "tuleb"
            },
            {
                "question": "Kas te ... sellele küsimusele vastata?",
                "options": ["suudate", "suudan", "suudavad"],
                "answer": "suudate"
            },
            {
                "question": "Ma ei ... teda.",
                "options": ["usu", "usub", "usuvad"],
                "answer": "usu"
            },
        ]

        self.listening_questions = [
            {"question": "Naine veedab oma puhkuse kindlasti koos lastega.", "answer": "vale"},
            {"question": "Naise abikaasale tähendab lastega tegelemine puhkust.", "answer": "õige"},
            {"question": "Naine võtab puhkust just selleks, et lihtsalt magada.", "answer": "vale"},
            {"question": "Tavaliselt on mehe uneaeg nii suvel kui talvel ühepikkune.", "answer": "vale"},
            {"question": "Naise meelest magab tema vestluskaaslane küllaldaselt.", "answer": "õige"},
            {"question": "Naise jaoks on oluline minna alati magama kindlal ajal.", "answer": "õige"},
            {"question": "Stressist saab vabaneda kindla mõtte või tegevuse abil.", "answer": "vale"},
            {"question": "Mees pidi välismaal puhates töiseid telefonikõnesid vastu võtma.", "answer": "vale"},
            {"question": "Rääkijad arvavad, et puhkamist peab harjutama.", "answer": "õige"},
            {"question": "Väsinud inimene peaks proovima igapäevatööst erinevaid tegevusi.", "answer": "õige"},
            {"question": "Naise meelest on tööl lõunapausi ajal heaks puhkuseks ajalehtede lugemine.", "answer": "vale"},
            {"question": "Mehe arvates tuleks keskenduda ainult ühele asjale korraga.", "answer": "õige"}
        ]
        
        self.create_widgets()

    def create_widgets(self):
        # Frame for audio playback and listening questions
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")

        self.title_label = tk.Label(self.frame_top, text="Kuulamine 1-12 küsimused", font=("Helvetica", 16))
        self.title_label.pack()

        self.description_label = tk.Label(self.frame_top, text="Kuulake kuulamist ja kirjutage igale küsimusele sobiv vastus. Kuulake tekst üks kord.", bg="lightblue", font=("Helvetica", 10), padx=5, pady=5)
        self.description_label.pack(fill="x")

        self.frame_button = tk.Frame(self.root, pady=10, padx=10)
        self.frame_button.pack(fill="x")

        self.play_button = tk.Button(self.frame_button, text="Play", command=self.on_button_click1)
        self.play_button.pack()

        self.example_label = tk.Label(self.root, text="Näide:\nMida täna erinevates sadamates puhastati?\nVastus: merepõhi", bg="lightgreen", padx=5, pady=5, justify="left")
        self.example_label.pack(fill="x", pady=10, padx=10)

        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")

        self.answer_entries = []
        for i, question in enumerate(self.listening_questions, start=1):
            question_label = tk.Label(self.frame_questions, text=f"{i}. {question['question']}")
            question_label.pack(anchor="w")

            entry = tk.Entry(self.frame_questions, width=100)
            entry.pack(anchor="w", pady=5)
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

            self.title_label.config(text="Грамматика B2 уровня")
            self.title_label.pack(fill="x")

            self.frame_grammar = tk.Frame(self.root, pady=10, padx=10)
            self.frame_grammar.pack(fill="x")

            self.grammar_question_label = tk.Label(self.frame_grammar, text="", font=("Helvetica", 14), wraplength=600)
            self.grammar_question_label.pack(pady=20)

            self.var = tk.StringVar()
            self.option_buttons = []
            for i in range(3):
                btn = tk.Radiobutton(self.frame_grammar, text="", font=("Helvetica", 12), variable=self.var, value="")
                btn.pack(anchor="w")
                self.option_buttons.append(btn)

            self.next_question_button = tk.Button(self.root, text="Next Question", command=self.next_question)
            self.next_question_button.pack(pady=10)

            self.display_question()

    def on_button_click1(self):
        if not self.audio_played:
            self.audio_played = True
            threading.Thread(target=self.play_audio, args=("audio/B2EestiKeel.mp3",)).start()
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
            
            # Удаляем предыдущие кнопки
            for btn in self.option_buttons:
                btn.destroy()
            
            # Создаем новые кнопки
            self.option_buttons = []
            for i, option in enumerate(question["options"]):
                btn = tk.Radiobutton(self.frame_grammar, text=option, font=("Helvetica", 12), variable=self.var, value=option)
                btn.pack(anchor="w")
                self.option_buttons.append(btn)
        else:
            self.show_result()

    def next_question(self):
        if self.is_listening_section:
            # Grade listening answers before switching
            self.grade_listening_answers()
            self.is_listening_section = False  # Установка переменной в False
            self.switch_to_grammar()  # Переключение на грамматические вопросы
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
