import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import subprocess
import os

class EnglishTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Английский тест B2 уровня")
        self.root.geometry("1150x700")
        self.score = 0
        self.current_question = 0
        self.is_listening_section = True  # Переменная для отслеживания текущей секции
        self.answers = []
        self.audio_played = False  # Переменная для отслеживания состояния воспроизведения аудио
        self.questions = [
            {
                "question": "to be excellent __________ something",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "at"
            },
            {
                "question": "he is experienced __________ writing emails",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "in"
            },
            {
                "question": "ashamed __________ having failed",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "of"
            },
            {
                "question": "concentrate __________ something important",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "on"
            },
            {
                "question": "an answer __________ the question",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "to"
            },
            {
                "question": "proud __________ his son",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "of"
            },
            {
                "question": "famous __________ breath-taking sights",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "for"
            },
            {
                "question": "supply the customers __________ the right products",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "with"
            },
            {
                "question": "succeed __________ making a lot of money",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "in"
            },
            {
                "question": "similar __________ mine",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "to"
            },
            {
                "question": "respected __________ being an honest politician",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "for"
            },
            {
                "question": "deal __________ the problem later",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "with"
            },
            {
                "question": "keen __________ going to the cinema",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "on"
            },
            {
                "question": "sorry __________ having done something wrong",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "for"
            },
            {
                "question": "provide her __________ everything she needs",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "with"
            },
            {
                "question": "responsible __________ employing new workers",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "for"
            },
            {
                "question": "an expert __________ astronomy",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "in"
            },
            {
                "question": "fond __________ romantic films",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "of"
            },
            {
                "question": "congratulate him __________ his success",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "on"
            },
            {
                "question": "interested __________ pursuing a career",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "in"
            },
            {
                "question": "capable __________ getting to the top",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "of"
            },
            {
                "question": "to take pride __________ what you do",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "in"
            },
            {
                "question": "to be short __________ money",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "of"
            },
            {
                "question": "praise her __________ doing such a good job",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "for"
            },
            {
                "question": "cooperate __________ the competitor",
                "options": ["at", "for", "in", "of", "on", "to", "with"],
                "answer": "with"
            }
        ]

        self.listening_questions = [
            {"question": "Anna ...  (did not start the company but manages it now, started the company and manages it now, started the company but does not manage it any more)", "answer": "started the company and manages it now"},
            {"question": "The app ...  (is for parents to learn from, is for students to learn from, is for students who want to find a tutor)", "answer": "is for students who want to find a tutor"},
            {"question": "Many parents ...  (dont have the time or knowledge to help with their childrens homework, think that schools should help with their childrens homework, dont want to help with their childrens homework)", "answer": "dont have the time or knowledge to help with their childrens homework"},
            {"question": "The app ...  (has student exercises on it, is only for people in remote areas, offers live online support from tutors)", "answer": "offers live online support from tutors"},
            {"question": "On the app, tutors who live in remote areas ...  (often charge lower rates, often charge higher rates, dont like to work too much)", "answer": "often charge lower rates"},
            {"question": "The app ...  (is new and not many people know about it, is already popular, is not very successful)", "answer": "is already popular"}
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
            threading.Thread(target=self.play_audio, args=("audio/B2English.mp3",)).start()
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
app = EnglishTestApp(root)
root.mainloop()
