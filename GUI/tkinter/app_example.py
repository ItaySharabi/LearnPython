import tkinter as tk


def print_contents(event):
    print("Hi. The current entry content is:",
          frame.contents.get())
    print(f'event -> {event}')


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()
frame.configure(height=400, width=400)
frame.grid(rows=2, columns=1)

frame.entrythingy = tk.Entry()
print(frame.entrythingy.configure().keys())
frame.entrythingy.pack(row=1, column=0)


# Create the application variable.
frame.contents = tk.StringVar()
# Set it to some value.
frame.contents.set("this is a variable")
# Tell the entry widget to watch this variable.
frame.entrythingy["textvariable"] = frame.contents

# Define a callback for when the user hits return.
# It prints the current value of the variable.
frame.entrythingy.bind('<Key-Return>',
                       print_contents)
root.mainloop()
# myapp.mainloop()
