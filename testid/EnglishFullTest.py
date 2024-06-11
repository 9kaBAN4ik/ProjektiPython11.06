import tkinter as tk
import os
import subprocess

class EnglishTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Английский тест A2-С1 уровня")
        self.root.geometry("1000x800")
        # Запрещаем изменение размеров окна
        self.score = 0
        self.current_question = 0
        self.answers = []
        self.questions = [
            {
        "question": "The workday _______ at eight o'clock.",
        "options": ["starts", "begin", "begins"],
        "answer": "starts"
    },
    {
        "question": "What did he mean by that?",
        "options": ["keeping in mind", "keeping in mind", "keeping in mind"],
        "answer": "keeping in mind"
    },
    {
        "question": "Your subscription _______ soon.",
        "options": ["expires", "slows", "drives"],
        "answer": "expires"
    },
    {
        "question": "The next gathering is _______ two years.",
        "options": ["from behind", "after", "after"],
        "answer": "after"
    },
    {
        "question": "I _______ my handbag on the bus.",
        "options": ["remembered", "dreamed", "forgot"],
        "answer": "forgot"
    },
    {
        "question": "The contract must be confirmed _______.",
        "options": ["with a title", "with a transcript", "with a signature"],
        "answer": "with a signature"
    },
    {
        "question": "Please a cup of black _______.",
        "options": ["coffee", "coffee", "coffee"],
        "answer": "coffee"
    },
    {
        "question": "The weather was cold and there was a strong _______ wind.",
        "options": ["sudden", "strong", "severe"],
        "answer": "strong"
    },
    {
        "question": "A: Have you already filed your tax return? B: _______.",
        "options": ["Not yet.", "Not anymore.", "Why not?"],
        "answer": "Not yet."
    },
    {
        "question": "A: _______ do you go to the gym? B: Once a week.",
        "options": ["How much", "How often", "How long"],
        "answer": "How often"
    },
    {
        "question": "During the summer, I got to know people well _______.",
        "options": ["by working", "by working", "by working"],
        "answer": "by working"
    },
    {
        "question": "Orange is an _______ fruit.",
        "options": ["emerging", "emerging", "emerging"],
        "answer": "emerging"
    },
    {
        "question": "I didn't order coffee, _______ tea!",
        "options": ["but", "but", "but"],
        "answer": "but"
    },
    {
        "question": "A: How often do you have to go on business trips? B: _______.",
        "options": ["From time to time.", "More or less.", "Maybe."],
        "answer": "From time to time."
    },
    {
        "question": "Where are you _______ from?",
        "options": ["coming", "are", "getting"],
        "answer": "are"
    },
    {
        "question": "I don't like this idea _______.",
        "options": ["to me", "to me", "to me"],
        "answer": "to me"
    },
    {
        "question": "A: Would you open the window? B: _______.",
        "options": ["No, thanks. Not now.", "Yes, if you are so kind.", "Yes, right away."],
        "answer": "Yes, right away."
    },
    {
        "question": "A: I'm having trouble with the toaster I bought from you. B: _______.",
        "options": ["No problem!", "Not my problem!", "What's the problem?"],
        "answer": "What's the problem?"
    },
    {
        "question": "A: Hello, my name is Mari. B: _______.",
        "options": ["Nice to meet you!", "Congratulations!", "Have a nice day!"],
        "answer": "Nice to meet you!"
    },
    {
        "question": "A: Could you lend me 20 euros? B: _______.",
        "options": ["Unfortunately, I don't have cash.", "I'll pay you back on payday.", "Too bad!"],
        "answer": "Unfortunately, I don't have cash."
    },
    {
        "question": "A: Achoo! B: _______",
        "options": ["Bless you!", "Thank you!", "Cheers!"],
        "answer": "Cheers!"
    },
    {
        "question": "In the event of an _______ call 112.",
        "options": ["occasion", "attack", "accident"],
        "answer": "accident"
    },
    {
        "question": "The hairdresser works _______ salon.",
        "options": ["in the salon", "in the post office", "in the restaurant"],
        "answer": "in the salon"
    },
    {
        "question": "These books resemble each other in _______.",
        "options": ["over", "according to", "part"],
        "answer": "part"
    },
    {
        "question": "Do you _______ for training new employees?",
        "options": ["answer", "discover", "responsible"],
        "answer": "responsible"
    },
    {
        "question": "Please _______ the computer!",
        "options": ["turn", "put", "switch"],
        "answer": "switch"
    },
    {
        "question": "A: When does the new year start? B: _______",
        "options": ["First January.", "On the first of January.", "On the first of January."],
        "answer": "On the first of January."
    },
    {
        "question": "A: Can I be of any help to you? B:",
        "options": ["Yes, please.", "No, thank you.", "I'm not sure."],
        "answer": "No, thank you."
    },
    {
        "question": "A: How often do you go to the gym? B:",
        "options": ["How much", "How frequently", "How long"],
        "answer": "How frequently"
    },
    {
        "question": "During the summer camp, I got to know people well by _______.",
        "options": ["working", "worked", "working on"],
        "answer": "working on"
    },
    {
        "question": "An orange is an _______ fruit.",
        "options": ["emerging", "emitting", "allergic"],
        "answer": "allergic"
    },
    {
        "question": "I didn't order coffee, _______ tea!",
        "options": ["but", "however", "just"],
        "answer": "just"
    },
    {
        "question": "A: How often do you have to go on business trips? B: _______.",
        "options": ["From time to time.", "More or less.", "Maybe."],
        "answer": "From time to time."
    },
    {
        "question": "Where are you _______?",
        "options": ["coming from", "are", "getting"],
        "answer": "from"
    },
    {
        "question": "I don't like this idea _______.",
        "options": ["with me", "from me", "to me"],
        "answer": "to me"
    },
    {
        "question": "A: Would you open the window, please? B: _______.",
        "options": ["No, thank you. Not right now.", "Yes, if you are so kind.", "Yes, right away."],
        "answer": "Yes, right away."
    },
    {
        "question": "A: I encountered a problem with the toaster I bought from you. B: _______.",
        "options": ["No problem!", "Not my problem!", "What's the problem?"],
        "answer": "What's the problem?"
    },
    {
        "question": "A: How do you usually spend your weekends? B:",
        "options": ["By sleeping in", "To the cinema", "Usually spend"],
        "answer": "By sleeping in"
    },
    {
        "question": "A: Would you like some more cake? B:",
        "options": ["Yes, please.", "I am okay.", "No, I had enough."],
        "answer": "No, I had enough."
    },
    {
        "question": "A: Have you been to New York City? B:",
        "options": ["In the morning", "Yes, I have.", "For a long time"],
        "answer": "Yes, I have."
    },
    {
        "question": "A: Do you prefer tea or coffee? B:",
        "options": ["Me too", "I prefer coffee", "Both"],
        "answer": "I prefer coffee"
    },
    {
        "question": "A: What are you doing this weekend? B:",
        "options": ["Not sure", "To travel", "Going hiking"],
        "answer": "Going hiking"
    },
    {
        "question": "A: How long have you been studying English? B:",
        "options": ["For a year", "I like English", "Very long"],
        "answer": "For a year"
    },
    {
        "question": "A: Do you want to grab lunch together? B:",
        "options": ["Sounds good", "Maybe", "I am busy"],
        "answer": "Sounds good"
    },
    {
        "question": "A: What time is it? B:",
        "options": ["At three", "I have no watch", "Half past ten"],
        "answer": "Half past ten"
    },
    {
        "question": "A: Are you coming to the party tonight? B:",
        "options": ["I will come", "Maybe next time", "I don't like parties"],
        "answer": "I will come"
    },
    {
        "question": "A: Could you please pass the salt? B:",
        "options": ["No problem", "Yes, sure", "Here you go"],
        "answer": "Here you go"
    }
            ]
        self.create_widgets()

    def create_widgets(self):
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")
        self.title_label = tk.Label(self.frame_top, text="Английский тест A2-С1 уровня", font=("Helvetica", 16))
        self.title_label.pack()

        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")

        self.question_label = tk.Label(self.frame_questions, text="")
        self.question_label.pack(anchor="w")

        self.var = tk.StringVar()

        self.option_buttons = []
        for i in range(3):
            option_button = tk.Radiobutton(self.frame_questions, text="", variable=self.var, value="")
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(self.root, text="Следующий вопрос", command=self.next_question)
        self.next_button.pack()

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            self.var.set("")
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, value=option)
                self.option_buttons[i].pack(anchor="w")
        else:
            self.show_result()

    def next_question(self):
        answer = self.var.get()
        self.answers.append(answer)
        if answer == self.questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1
        self.display_question()

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
