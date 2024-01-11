from tkinter import *
import time

class TypingSpeedTest:
    def __init__(self, window):
        self.master = window
        window.title('Type Speed Test')
        window.minsize(width=1000, height=600)

        self.instruction_text = 'Type the Sentence below as fast as possible then press enter or click on submit'
        self.instruction_text = Label(window, text=self.instruction_text, font=("Courier", 15, 'bold'))
        self.instruction_text.grid(row=0, column=1, pady=20)

        self.sample_text = 'THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG'
        self.text_displayed = Label(window, text=self.sample_text, font=("Courier", 30, 'bold'))
        self.text_displayed.grid(row=2, column=1, pady=20)

        self.text_entry = Entry(window, width=100)
        self.text_entry.grid(row=4, column=1, pady=10)

        self.text_entry.bind('<Return>', lambda event: self.check_typing_speed())

        self.submit_button = Button(window, text='Submit', command=self.check_typing_speed)
        self.submit_button.grid(row=6, column=1, pady=20)

        self.reset_button = Button(window, text='Reset', command=self.reset_typing_test)
        self.reset_button.grid(row=8, column=1, pady=20, padx=10)

    def check_typing_speed(self):
        '''Checks typed message and typing speed'''
        user_input = self.text_entry.get()
        elapsed_time = time.time() - TIMER
        words_per_minute = int((len(self.sample_text.split()) / elapsed_time) * 60)
        if user_input == self.sample_text:
            self.result_label = Label(self.master, text=f'Typing speed: {words_per_minute} WPM', font=("Courier", 18, 'bold'))
        else:
            self.result_label = Label(self.master, text='You misspelled something try again', font=("Courier", 18, 'bold'))
        self.result_label.grid(row=10, column=1, pady=20)

    def reset_typing_test(self):
        '''Resets the time to 0 and clears the screen'''
        self.text_entry.delete(0, 'end')
        self.start_time = time.time()
        self.result_label.config(text='')

if __name__ == "__main__":
    window = Tk()
    TIMER = time.time()
    app = TypingSpeedTest(window)
    window.mainloop()
