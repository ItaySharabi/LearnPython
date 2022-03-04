import tkinter as tk


def print_contents(event):
    print("Hi. The current entry content is:",
          frame.contents.get())
    print(f'event -> {event}')


root = tk.Tk()

frame = tk.Frame(master=root)
frame.configure(height=400, width=400)
frame.grid(rows=3, columns=3)
frame.pack()

entrythingy = tk.Entry(master=frame)
print(entrythingy.configure().keys())


# Create the application variable.
frame.contents = tk.StringVar()
# Set it to some value.
frame.contents.set("this is a variable")
# Tell the entry widget to watch this variable.
entrythingy["textvariable"] = frame.contents

# Define a callback for when the user hits return.
# It prints the current value of the variable.
entrythingy.bind('<Key-Return>',
                       print_contents)

# Add the entry to the frame
entrythingy.pack()

root.mainloop()
# myapp.mainloop()
