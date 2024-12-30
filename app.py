import tkinter as tk
from tkinter import messagebox


# logic
def countdown(count):
    minutes, seconds = divmod(count, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        messagebox.showinfo("attention", "good work! time to take a break!")


def work():
    countdown(1500)


def short():
    countdown(300)


def long():
    countdown(900)


# window display
window = tk.Tk()
window.title("attention")
window.geometry("200x150")
window.configure(bg="#B5C6E0")

# frame (center info)
frame = tk.Frame(window, bg="#B5C6E0")
frame.pack(pady=20)

# timer display
timer_label = tk.Label(
    window,
    text="25:00",
    font=(
        "Inter",
        28),
    bg="#B5C6E0",
    fg="#2A3B47")
timer_label.pack()

# timer button
start_button = tk.Button(
    window,
    text="start",
    font=("Inter"),
    command=work,
    bg="#B5C6E0",
    fg="#2A3B47",
    borderwidth=0)
start_button.pack(pady=5)


def main():
    window.mainloop()


if __name__ == '__main__':
    main()
