from tkinter import *
import random

class Writing:

    def __init__(self, window):
        self.window = window
        self.random_prompt = None
        self.writing_option = False
        self.timer_running = False
        self.user_text = None
        self.top = None

        # Create Entry Widgets for HH MM SS
        self.sec = StringVar()
        self.mins = StringVar()
        self.hrs = StringVar()

        # Intialize countdown if user stops writing parameters
        self.timer = None
        self.stop_timer = None
        self.typing_timeout = 10000  #10 seconds



    # Function for generate prompt button
    def prompt_text_widget(self):
        # Select Random Prompt from the list of prompts
        prompt_txt = open("generate_prompt.txt", "r", encoding="utf-8")
        prompt_txt = prompt_txt.read().split('\n')
        self.random_prompt = random.choice(prompt_txt)

        self.writing_option = True

        # Generate Prompt Text Widget
        prompt_widget = Label(self.window, anchor=CENTER, justify=CENTER, wraplength=250,
                 relief=RAISED,  text=self.random_prompt, font=("Arial", 12), width=30, height=10)
        prompt_widget.grid(column=1, row=20, columnspan=2)

        writing_prompt = Button()
        writing_prompt = Button(text="Start Writing with Prompt", command=self.writing_widget)
        writing_prompt.grid(column=1, row=60, columnspan=2, padx=10, pady=10)


    # Function to write without a prompt
    def without_prompt(self):
        self.writing_option = False
        self.writing_widget()


    # Function for start writing button
    def writing_widget(self):
        self.top = Toplevel(self.window)
        self.top.title("Start Writing")
        self.top.minsize(width=400, height=400)

        # If prompt_option = True and self.random_prompt is not None:
        if self.writing_option is True:
            prompt_widget = Label(self.top, anchor=CENTER, justify=CENTER, wraplength=200,
                                  relief=RAISED, text=self.random_prompt, font=("Arial", 12), width=30, height=7)
            prompt_widget.grid(column=1, row=1, columnspan=2)


        # Create Text Widget
        self.user_text = Text(self.top, height=10, width=60)
        self.user_text.grid(column=1, row=5, columnspan=2, padx=10, pady=10)

        # Create Entry Widgets for HH MM SS
        Entry(self.top, textvariable=self.sec, width=2, font='Helvetica 12').place(x=290, y=350)
        self.sec.set('00')

        Entry(self.top, textvariable=self.mins, width=2, font='Helvetica 12').place(x=250, y=350)
        self.mins.set('01')

        Entry(self.top, textvariable=self.hrs, width=2, font='Helvetica 12').place(x=210, y=350)
        self.hrs.set('00')

        # Condition to monitor if text is being writing in the text widget
        self.user_text.bind("<KeyPress>", self.start_writing_timer)
        self.user_text.bind("<KeyRelease>", self.handle_keyrelease)



    # Function to start timer when user has started writing
    def start_writing_timer(self, event=None):
        if not self.timer_running:
            self.timer_running = True
            self.countdown_timer()


    #Timer for user to write
    def countdown_timer(self):

        # Timer functionality
        times = int(self.hrs.get()) * 3600 + int(self.mins.get()) * 60 + int(self.sec.get())

        def timer_step():
            nonlocal times
            if times > 0:
                minute, second = (times // 60, times % 60)
                hour = 0
                if minute > 60:
                    hour, minute = (minute // 60, minute % 60)
                self.sec.set(second)
                self.mins.set(minute)
                self.hrs.set(hour)
                # Update the time - after method keeps GUI responsive
                times -= 1
                self.top.after(1000, timer_step)
            elif (times == 0):
                self.timer_running = False
                self.sec.set('00')
                self.mins.set('00')
                self.hrs.set('00')

        timer_step()

    # Function to monitor if user has stopped writing and erase text after timeout
    def handle_keyrelease(self, event):
        # If existing stop timer it will get cancelled to set a new one
        if self.stop_timer:
            self.top.after_cancel(self.stop_timer)

        self.stop_timer = self.top.after(self.typing_timeout, self.delete_text)

    def delete_text(self):
        # Unbind the keypress event temporarily
        self.user_text.unbind("<KeyPress>")
        self.user_text.delete("1.0", END)




