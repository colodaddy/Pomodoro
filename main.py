from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def StartTimer():
    pass


def ResetTimer():
    pass


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 32, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", command=StartTimer,
               highlightthickness=0, font=(FONT_NAME, 16, "bold"), bg=GREEN)
start.grid(row=3, column=0)

reset = Button(text="Reset", command=ResetTimer,
               highlightthickness=0, font=(FONT_NAME, 16, "bold"), bg=RED)
reset.grid(row=3, column=2)

check_marks = Label(text=CHECK_MARK * 3, fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 16, "bold"))
check_marks.grid(row=4, column=1)


window.mainloop()
