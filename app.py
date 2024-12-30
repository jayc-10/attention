import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Attention")
timer_label = tk.Label(window, text="00:00", font=("Inter", 28))
timer_label.pack()

start_button = tk.Button(window, text="Start")
start_button.pack()

window.mainloop()