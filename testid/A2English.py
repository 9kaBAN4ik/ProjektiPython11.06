import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os


class EnglishTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English Test Level A2")
        self.root.geometry("1000x800")
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True
        self.answers = []
        self.questions = [
            {
                "question": "George is ................ than Nick.",
                "options": ["tall", "taller", "tallest"],
                "answer": "taller"
            },
            {
                "question": "What time ..... Calais tomorrow afternoon?",
                "options": ["do the ferry reach", "is the ferry reaching", "does the ferry reach"],
                "answer": "does the ferry reach"
            },
            {
                "question": "My friend ..................... lives in Australia is a nurse.",
                "options": ["who", "which", "whose"],
                "answer": "who"
            },
            {
                "question": "I like walking in the park ............. hot days.",
                "options": ["at", "on", "in"],
                "answer": "on"
            },
            {
                "question": "Centuries ago, people .......... animals for food.",
                "options": ["transported", "played", "hunted"],
                "answer": "hunted"
            },
            {
                "question": "If he ................... the lottery, he'll go on a round-the-world trip.",
                "options": ["won", "wins", "will win"],
                "answer": "wins"
            },
            {
                "question": "John has to get ... early in the morning.",
                "options": ["on", "up", "down"],
                "answer": "up"
            },
            {
                "question": "The door was locked so I ..... go inside.",
                "options": ["will be able to", "wasn't able to", "can"],
                "answer": "wasn't able to"
            },
            {
                "question": "She often ......................... to music when she does the housework.",
                "options": ["listens", "listening", "to listen"],
                "answer": "listens"
            },
            {
                "question": "We ..... at the sports centre every Wednesday afternoon.",
                "options": ["are usually meeting", "usually meet", "have usually met"],
                "answer": "usually meet"
            },
            {
                "question": "That's the man ..... son is a famous actor.",
                "options": ["who", "where", "whose"],
                "answer": "whose"
            },
            {
                "question": "......... is a dairy product.",
                "options": ["Cheese", "Meat", "Rice"],
                "answer": "Cheese"
            },
            {
                "question": "Greg .... down, opened the book and began to read.",
                "options": ["was sitting", "sat", "has been sitting"],
                "answer": "sat"
            },
            {
                "question": "Levi Strauss was the man ................. invented blue jeans.",
                "options": ["who", "whose", "which"],
                "answer": "who"
            },
            {
                "question": "You have been to Spain, ...............?",
                "options": ["have you", "you have", "haven't you"],
                "answer": "haven't you"
            },
            {
                "question": "If you study hard, you ....... your exams this time.",
                "options": ["passes", "pass", "will pass"],
                "answer": "will pass"
            },
            {
                "question": "This is the park ...... I take my dog every afternoon.",
                "options": ["what", "where", "which"],
                "answer": "where"
            },
            {
                "question": ".................. do you like playing during long winter evenings?",
                "options": ["What", "Which", "Why"],
                "answer": "What"
            },
            {
                "question": "Use this bowl. It's ..................... than the other one.",
                "options": ["big", "bigger", "biggest"],
                "answer": "bigger"
            },
            {
                "question": "They ........... to Disneyland last week.",
                "options": ["went", "had gone", "will go"],
                "answer": "went"
            }
        ]

        self.listening_questions = [
            "Brazilians don’t like eating with their friends. ❏ True ❏ False",
            "Brazilians don’t drink coffee in the evening. ❏ True ❏ False",
            "Filipinos eat with a fork and a spoon. ❏ True ❏ False",
            "Filipinos add rice into their desserts. ❏ True ❏ False",
            "Finns like drinking wine. ❏ True ❏ False"
        ]

        self.listening_answers = ["False", "False", "True", "True", "False"]

        self.create_widgets()

    def create_widgets(self):
        # Frame for audio playback and listening questions
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")

        self.title_label = tk.Label(self.frame_top, text="Listening Test 1. Task, Questions 1-5",
                                    font=("Helvetica", 16))
        self.title_label.pack()

        self.description_label = tk.Label(self.frame_top,
                                          text="Listen to the passage and mark each statement as True or False.",
                                          bg="lightblue", font=("Helvetica", 10), padx=5, pady=5)
        self.description_label.pack(fill="x")

        self.frame_button = tk.Frame(self.root, pady=10, padx=10)
        self.frame_button.pack(fill="x")

        self.play_button = tk.Button(self.frame_button, text="Play", command=self.on_button_click1)
        self.play_button.pack()

        self.example_label = tk.Label(self.root,
                                      text="Example:\nPeople in Brazil don't like eating with their friends. ❏ True ❏ False\nAnswer: False",
                                      bg="lightgreen", padx=5, pady=5, justify="left")
        self.example_label.pack(fill="x", pady=10, padx=10)

        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")

        self.answer_vars = []
        for i, question in enumerate(self.listening_questions, start=1):
            question_label = tk.Label(self.frame_questions, text=f"{i}. {question}")
            question_label.pack(anchor="w")
            answer_var = tk.StringVar(value="False")
            true_radio = tk.Radiobutton(self.frame_questions, text="True", variable=answer_var, value="True")
            false_radio = tk.Radiobutton(self.frame_questions, text="False", variable=answer_var, value="False")
            true_radio.pack(anchor="w")
            false_radio.pack(anchor="w")
            self.answer_vars.append(answer_var)

        self.next_section_button = tk.Button(self.root, text="Proceed to Grammar", command=self.switch_to_grammar)
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

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=20)

        self.display_question()

    def play_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load("audio/A2English.mp3")
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
app = EnglishTestApp(root)
root.mainloop()
