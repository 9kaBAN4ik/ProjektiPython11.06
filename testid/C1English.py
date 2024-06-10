import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os

class EnglishTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Английский тест B1 уровня")
        self.root.geometry("1150x700")
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.audio_played = False  # Переменная для отслеживания состояния воспроизведения аудио
        self.questions = [
            {
                "question": "When the director went to China on business his … took over all his duties.",
                "options": ["officer", "deputy", "caretaker"],
                "answer": "deputy"
            },
            {
                "question": "She saw the plane crash when its engines … .",
                "options": ["failed", "struck", "held"],
                "answer": "failed"
            },
            {
                "question": "You are going to come to the meeting, …?",
                "options": ["will you", "do you", "aren’t you"],
                "answer": "aren’t you"
            },
            {
                "question": "You will not finish that project by tomorrow unless you … some help.",
                "options": ["get", "would get", "will get"],
                "answer": "get"
            },
            {
                "question": "It’s difficult to pay my bills when prices keep … .",
                "options": ["rising", "gaining", "raising"],
                "answer": "rising"
            },
            {
                "question": "After the death of her father, she was brought … by her uncle.",
                "options": ["round", "about", "up"],
                "answer": "up"
            },
            {
                "question": "Why did the police suspect you? It doesn’t make … to me.",
                "options": ["right", "sense", "truth"],
                "answer": "sense"
            },
            {
                "question": "When they heard that their children had crossed the road without looking, they told them they … do it again.",
                "options": ["mustn’t", "needn’t", "didn’t need to"],
                "answer": "mustn’t"
            },
            {
                "question": "He went to Germany hoping to find a teaching … .",
                "options": ["work", "occupation", "post"],
                "answer": "post"
            },
            {
                "question": "I can’t … what they are doing; it’s way too dark down there.",
                "options": ["look into", "make out", "see through"],
                "answer": "make out"
            },
            {
                "question": "This country has … good transport.",
                "options": ["the", "a", "very"],
                "answer": "a"
            },
            {
                "question": "I’d like you to meet a very good friend of …, Dave.",
                "options": ["me", "my", "mine"],
                "answer": "mine"
            },
            {
                "question": "We travelled to Australia by the most … route.",
                "options": ["direct", "unique", "easy"],
                "answer": "direct"
            },
            {
                "question": "This film is based … a novel.",
                "options": ["of", "on", "in"],
                "answer": "on"
            },
            {
                "question": "I should be grateful … any advice you can give regarding this situation.",
                "options": ["for", "about", "with"],
                "answer": "for"
            },
            {
                "question": "I was shocked … her indifference!",
                "options": ["on", "with", "at"],
                "answer": "at"
            },
            {
                "question": "The manager has just gone on her … leave. She gets three weeks’ holiday a year.",
                "options": ["regular", "annual", "regular"],
                "answer": "annual"
            },
            {
                "question": "He have … this minute left for the city centre.",
                "options": ["ever", "already", "just"],
                "answer": "just"
            },
            {
                "question": "To my …, a pandemic is more dangerous than nuclear arms.",
                "options": ["mind", "view", "disbelief"],
                "answer": "mind"
            },
            {
                "question": "They are always … with each other about investments.",
                "options": ["shouting", "arguing", "annoying"],
                "answer": "arguing"
            },
            {
                "question": "I took that faulty laptop back to the shop where I’d bought it and asked the … if they would change it for me.",
                "options": ["clerk", "official", "assistant"],
                "answer": "assistant"
            },
            {
                "question": "I … to the cinema last night. I’m so tired now.",
                "options": ["had not to go", "shouldn’t have gone", "haven’t had to go"],
                "answer": "shouldn’t have gone"
            },
            {
                "question": "You will spend at least one year working in this company … you can find out how things operate here.",
                "options": ["so that", "so as to", "because"],
                "answer": "so that"
            },
            {
                "question": "I can … with most things but I cannot stand lies.",
                "options": ["put aside", "put up", "put off"],
                "answer": "put up"
            },
            {
                "question": "I think she is … her time looking for a job here.",
                "options": ["losing", "wasting", "missing"],
                "answer": "wasting"
            }
        ]

        self.listening_questions = [
            {"question": "Charles thinks a surprise party is … (a chance to relax, too much of a shock, a different way to celebrate)", "answer": "too much of a shock"},
            {"question": "Marco and Dora agree that … (a 40th birthday is more special than other birthdays, ageing is a bad thing, both of the above are true)", "answer": "a 40th birthday is more special than other birthdays"},
            {"question": "Charles sees himself as someone who … (prefers to be in the background, likes to be the centre of attention, organises nice things for other people)", "answer": "prefers to be in the background"},
            {"question": "Describe Marco's feelings about his child's ninth birthday party. (he is not looking forward to it., he is looking forward to it, it is a sensitive topic for him.)", "answer": "he is not looking forward to it"},
            {"question": "Why can't he organise a trip to the cinema for the ninth birthday party? (Children prefer to go rock-climbing., Another child has had a cinema party recently., it is not a good idea to repeat parties from the year before.)", "answer": "It's not a good idea to repeat parties from the year before"},
            {"question": "Charles stopped celebrating birthdays because … (he thinks they're not suitable for adults, it became hard to find people to celebrate with, it is less fun when you cant play kids games)", "answer": "it became hard to find people to celebrate with"}
        ]

        self.create_widgets()

    def create_widgets(self):
        # Frame for audio playback and listening questions
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")

        self.title_label = tk.Label(self.frame_top, text="Listening 1-6 questions", font=("Helvetica", 16))
        self.title_label.pack()

        self.description_label = tk.Label(self.frame_top, text="Listen to the listening passage and write a suitable answer to each question. Listen to the text once.", bg="lightblue", font=("Helvetica", 10), padx=5, pady=5)
        self.description_label.pack(fill="x")

        self.frame_button = tk.Frame(self.root, pady=10, padx=10)
        self.frame_button.pack(fill="x")

        self.play_button = tk.Button(self.frame_button, text="Play", command=self.on_button_click1)
        self.play_button.pack()

        self.example_label = tk.Label(self.root, text="Example:\nWhat was cleaned in different ports today?\nAnswer: seabed", bg="lightgreen", padx=5, pady=5, justify="left")
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
            # Stop audio playback if it's playing
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            self.frame_top.pack_forget()
            self.frame_button.pack_forget()
            self.example_label.pack_forget()
            self.frame_questions.pack_forget()
            self.next_section_button.pack_forget()

            self.is_listening_section = False

            self.title_label.config(text="Грамматика B1 уровня")
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
            threading.Thread(target=self.play_audio, args=("audio/C1English.mp3",)).start()
        else:
            messagebox.showinfo("Info", "You can only play the audio once.")

    def play_audio(self, filename):
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.grammar_question_label.config(text=question["question"])
            self.var.set("")
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, value=option)
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
app = EnglishTestApp(root)
root.mainloop()
