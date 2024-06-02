# Build a writing desktop app.
# The design should allow a user to type and if they stop for
# more than 5 seconds, it should delete everything they've written so far.


# Import Modules
from tkinter import *
from writing import Writing


#Create Tkinter window
window = Tk()
window.title("Squibler - Writing App")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)
window.config(background="white")

# Create class instance from the writing class
writing_class = Writing(window)

# Label For introducing the app and how it works
intro_label = Label(window, text="The Most Dangerous Writing App", font=("Arial", 18, "bold"))
intro_label.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

desc_label = Label(window, text="Don't stop writing, or all progress will be lost.", font=("Arial", 14))
desc_label.grid(column=1, row=5, columnspan=2, padx=5, pady=5)

# Generate Prompt Button
prompt_button = Button()
prompt_button = Button(text="Generate a Prompt", command=writing_class.prompt_text_widget)
prompt_button.grid(column=1, row=8, padx=10, pady=10)

# Start Writing Prompt Button
writing_button = Button()
writing_button = Button(text="Start writing w/o prompt", command=writing_class.without_prompt)
writing_button.grid(column=2, row=8, padx=10, pady=10)

window.mainloop()