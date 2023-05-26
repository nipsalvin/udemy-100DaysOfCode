from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain:QuizBrain):
        '''Initializes the object with the defined parameters'''
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score:', 
                           font=('ariel', 20, 'italic'), 
                           bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,125, 
                                                     width=280,
                                                     text='Question Text', 
                                                     font=('ariel', 20, 'italic'), 
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_img = PhotoImage(file='day-34/quizzler-app-start/images/true.png')
        self.true_button=Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file='day-34/quizzler-app-start/images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Calls 'next_question()' from self.quiz then returns and sets question_texts """
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz" )
            self.score_label.config(text=f'Your final score is {self.quiz.score}')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    
    def true_pressed(self):
        '''If true button is clicked it returns true'''
        #method 1 (catch the value in a variable)
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        '''If False button is clicked it returns False'''
        #method 2
        self.give_feedback(self.quiz.check_answer('False'))
    
    def give_feedback(self, is_right):
        '''Takes the "is_right"'''
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(100,self.get_next_question)

        


