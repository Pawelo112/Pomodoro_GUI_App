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

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

# Labels
main_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
main_text.grid(column=1, row=0)

check_marks = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
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
