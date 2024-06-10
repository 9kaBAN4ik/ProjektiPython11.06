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
                "question": "I __________ on redecorating the house for the last few days and I'm still not finished. (WORK)",
                "options": ["have been working", "was working", "worked"],
                "answer": "have been working"
            },
            {
                "question": "She _________________________ his phone number, so she can't call him. (FORGET)",
                "options": ["forgot", "has forgotten", "was forgetting"],
                "answer": "has forgotten"
            },
            {
                "question": "It _________________________ all day. It seems as if it will never stop. (RAIN)",
                "options": ["rained", "has been raining", "was raining"],
                "answer": "has been raining"
            },
            {
                "question": "I _________________________ a lot of work this morning, and it's only nine. (DO)",
                "options": ["have done", "did", "was doing"],
                "answer": "have done"
            },
            {
                "question": "She ____________________________ the tasks her teacher provided her with. (JUST FINISH)",
                "options": ["just finished", "has just finished", "was just finishing"],
                "answer": "has just finished"
            },
            {
                "question": "We ____________________________ for our exams since October. I hope we're well prepared for them. (STUDY)",
                "options": ["studied", "have been studying", "were studying"],
                "answer": "have been studying"
            },
            {
                "question": "You look so tired. What's happened? – I ____________________________ after the children the whole morning. They're really a nuisance. (LOOK)",
                "options": ["looked", "have been looking", "was looking"],
                "answer": "have been looking"
            },
            {
                "question": "We _________________________ this film before, so there's no need to watch it again. (SEE)",
                "options": ["saw", "have seen", "were seeing"],
                "answer": "have seen"
            },
            {
                "question": "I ____________________________ for you all morning. - Where _________________________? (WAIT, YOU BE)",
                "options": ["have been waiting, have you been", "waited, were you", "was waiting, are you"],
                "answer": "have been waiting, have you been"
            },
            {
                "question": "Mike _________________________ an airplane before, but I think he won't be able to manage such a large one. (FLY)",
                "options": ["flew", "has flown", "was flying"],
                "answer": "has flown"
            },
            {
                "question": "I _________________________ up my mind not to accept the job offer. (MAKE)",
                "options": ["made", "have made", "was making"],
                "answer": "have made"
            },
            {
                "question": "I ______________________ to India twice and each time it was a remarkable experience. (BE)",
                "options": ["was", "have been", "were"],
                "answer": "have been"
            },
            {
                "question": "Jack _________________________ his driving test twice. He should be better prepared. (FAIL)",
                "options": ["failed", "has failed", "was failing"],
                "answer": "has failed"
            },
            {
                "question": "I ___________________________ to a party since Christmas. I really think I should socialize more. (NOT BE)",
                "options": ["haven't been", "wasn't", "were not"],
                "answer": "haven't been"
            },
            {
                "question": "People _________________________ all morning about slow internet services. (COMPLAIN)",
                "options": ["complained", "have been complaining", "were complaining"],
                "answer": "have been complaining"
            },
            {
                "question": "My brother _________________________ for this company for the last forty years and _________________________ any trouble. (WORK, NEVER CAUSE)",
                "options": ["has been working, has never caused", "worked, never caused", "was working, didn't cause"],
                "answer": "has been working, has never caused"
            },
            {
                "question": "Someone _________________________ my computer. The battery is dead. (USE)",
                "options": ["used", "has been using", "was using"],
                "answer": "has been using"
            },
            {
                "question": "Why __________________________ your monthly fee yet? You're always late. (YOU NOT PAY)",
                "options": ["haven't you paid", "didn't you pay", "weren't you paying"],
                "answer": "haven't you paid"
            },
            {
                "question": "He _________________________ golf with us since he moved here. (PLAY)",
                "options": ["played", "has played", "was playing"],
                "answer": "has played"
            },
            {
                "question": "My mother _________________________ the bus, so she won't be here on time. (MISS)",
                "options": ["missed", "has missed", "was missing"],
                "answer": "has missed"
            },
            {
                "question": "I _________________________ three letters so far this morning, and I'm tired already. (TYPE)",
                "options": ["typed", "have typed", "was typing"],
                "answer": "have typed"
            },
            {
                "question": "The baby _________________________. That's why her eyes are so red. (CRY)",
                "options": ["cried", "has been crying", "was crying"],
                "answer": "has been crying"
            },
            {
                "question": "I am really excited about going to the new restaurant because I _________________________ Indian food before. (NEVER EAT)",
                "options": ["never ate", "have never eaten", "was never eating"],
                "answer": "have never eaten"
            },
            {
                "question": "We _________________________ through the accounts since Monday, but we _________________________ any irregularities yet. (LOOK, NOT FIND)",
                "options": ["have been looking, haven't found", "looked, didn't find", "were looking, weren't finding"],
                "answer": "have been looking, haven't found"
            },
            {
                "question": "My cousin _________________________ this house since the end of the war. (OWN)",
                "options": ["owned", "has owned", "was owning"],
                "answer": "has owned"
            }
        ]

        self.listening_questions = [
            {"question": "How often does the woman watch the show? (always, sometimes, we dont know)", "answer": "always"},
            {"question": "How has the woman's opinion of the show changed over time? (it is become more positive, it is become less positive, it hasnt changed)", "answer": "it is become less positive"},
            {"question": "What does the man think of the story? (it is very well written, too many characters died, he cant remember much about it)", "answer": "it is very well written"},
            {"question": "What is the one negative thing about the show for the man? (they spent too much money on the special effects, the episodes were too short, there were not enough episodes)", "answer": "there were not enough episodes"},
            {"question": "Why does the man think the writers have fewer ideas for stories now? (because they are saving their ideas to make a hollywood film, because they are not copying the books, because they are copying the books)", "answer": "because they are not copying the books"},
            {"question": "Why does the woman like Cersei? (the character does unpredictable things, the character learns from her mistakes, she is a very intelligent character)", "answer": "the character does unpredictable things"}
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
            threading.Thread(target=self.play_audio, args=("audio/B1English.mp3",)).start()
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
