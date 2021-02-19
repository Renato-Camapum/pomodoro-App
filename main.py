import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#61b15a"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Rest", fg=RED)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Rest", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


mark = ""


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        if reps % 2 == 0:
            global mark
            mark += "✔"
            check_label.config(text=mark)
            check_label.grid(column=1, row=3)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_pic)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, fg="white", bg=GREEN, bd=0)
start_button.config(padx=4, pady=4)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, fg="white", bg=GREEN, bd=0)
reset_button.config(padx=4, pady=4)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)


window.mainloop()
