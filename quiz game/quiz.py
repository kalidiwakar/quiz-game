from tkinter import *

questions = (
    "Question 1: What is the capital of France?",
    "Question 2: Which planet is known as the 'Red Planet'?",
    "Question 3: What is the largest organ in the human body?",
    "Question 4: What gas do plants primarily use for photosynthesis?",
)

options = (
    ("A. MADRID", "B. BERLIN", "C. LONDON", "D. PARIS"),
    ("A. VENUS", "B. MARS", "C. JUPITER", "D. SATURN"),
    ("A. HEART", "B. LIVER", "C. SKIN", "D. BRAIN"),
    ("A. OXYGEN", "B. NITROGEN", "C. CARBON DIOXIDE", "D. HYDROGEN"),
)

answers = ("D", "B", "C", "C")

current_question = 0
score = 0

def submit_answer(answer):
    global current_question, score
    correct_answer = answers[current_question]
    
    if answer == correct_answer:
        score += 1

    current_question += 1
    if current_question < len(questions):
        create_question(current_question)
    else:
        display_result()

def create_question(question_number):
    clear_frame(question_frame)

    question_text = Label(question_frame, text=questions[question_number])
    question_text.pack()

    selected_option=StringVar()
    selected_option.set("-2")

    option_texts = options[question_number]
    for i, option_text in enumerate(option_texts):
        option_widget = Radiobutton(question_frame, text=option_text, variable=selected_option, value=option_text[0])
        option_widget.pack(anchor=W)
        option_widgets.append(option_widget)


    option_widget = Radiobutton(question_frame, text="DONT KNOW", variable=selected_option, value="-1")
    option_widget.pack(anchor=W)
    option_widgets.append(option_widget)

    submit_button = Button(question_frame, text="Submit", command=lambda: submit_answer(selected_option.get()))
    submit_button.pack()

def display_result():
    clear_frame(question_frame)
    

    result_label = Label(win, text=f"Quiz Completed!\nYour Score: {score}/{len(questions)}", font=("Georgia", 16))
    result_label.pack()
    lab1=Label(win,text="Question 1: What is the capital of France==>   paris")
    lab1.pack()
    lab2=Label(win,text="Question 2: Which planet is known as the 'Red Planet'==>  mars")
    lab2.pack()
    lab3=Label(win,text="Question 3: What is the largest organ in the human body==>  skin")
    lab3.pack()
    lab4=Label(win,text="Question 4: What gas do plants primarily use for photosynthesis==>  carbon dioxide")
    lab4.pack()





def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def startquiz():
    labelImage1.destroy()
    label2.destroy()
    btnstrt.destroy()
    labelImage4.destroy()
    create_question(0)

win = Tk()
win.geometry("500x500+10+10")
win.title("QUIZ APP")
win.config(bg="#f0e9e9")
win.resizable(False, False)

img1 = PhotoImage(file="tr.png")
labelImage1 = Label(win, image=img1)
labelImage1.place(x=200, y=40)

label2 = Label(win, text="TEST HOW MUCH YOU KNOW?", font=("Georgia", 20), fg="black", justify=CENTER)
label2.place(x=0, y=200, relwidth=1)

img2 = PhotoImage(file="s.png")
btnstrt = Button(win, image=img2, command=startquiz)
btnstrt.place(x=200, y=250)

img3 = PhotoImage(file="o.png")
labelImage4 = Label(win, image=img3)
labelImage4.place(x=0, y=370, relwidth=1)


question_frame = Frame(win)
question_frame.pack()

question_label = Label(question_frame, text="")
selected_option = StringVar()

option_widgets = []

win.mainloop()
