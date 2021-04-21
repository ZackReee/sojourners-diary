import tkinter as tk

window = tk.Tk()

empty = tk.Label(text="Your diary seems empty")
empty.pack()

text_entry = tk.Text()
text_entry.pack()

tk.mainloop()