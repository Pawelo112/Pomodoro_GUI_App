from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = 10#WORK_MIN * 60
    short_break_sec = 4#SHORT_BREAK_MIN * 60
    long_break_sec = 5#LONG_BREAK_MIN * 60

    # Work and break mechanism

    # If it's the 1st/3rd/5th/7th rep:
    if reps % 2 != 0:
        count_down(work_sec)
        main_text.config(text="Work", fg=GREEN)
    # If it's the 8th rep:
    elif reps % 8 == 0:
        count_down(long_break_sec)
        main_text.config(text="Break", fg=RED)
    # If it's the 2nd/4th/6th:
    else:
        count_down(short_break_sec)
        main_text.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minute = floor(count / 60)
    second = count % 60
    # Making sure that text is properly displayed
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        # Restarting the timer after count down goes to 0
        start_timer()

        # Adding checkmark for every work session completed
        marks = ""
        for i in range(floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

# Labels
main_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
main_text.grid(column=1, row=0)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(107, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
