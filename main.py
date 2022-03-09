# Music by <a href="/users/sergequadrado-24990007/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral
# &amp;utm_campaign=audio&amp;utm_content=21091">SergeQuadrado</a> from <a
# href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp
# ;utm_content=21091">Pixabay</a>

# Name: Samuel Burke
# Date: 03/07/22
# GUI general design and inspiration from 100 Days of Code by Angela Yu
# NOTE: this program uses tkmacosx to utilize the greater Button customization for Mac OSX, which
# does not support other operating systems. If you would like to use this software on another platform,
# replace the tkmacosx Buttons with the standard tkinter Button options and customize to your preference
from tkinter import *
import tkmacosx
import pygame

PINK = "#e2979c"
RED = "#e7305b"
ON_RED = "#db8086"
CLICKED_RED = "#d26067"
GREEN = "#9bdeac"
CLICKED_GREEN = "#66cc80"
ON_GREEN = "#85d699"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def play():
    pygame.mixer.music.play()


def restart():
    # Start Button remains inactive until timer is reset
    pass


def reset():
    start_button.config(command=start)
    global reps
    reps = 0
    try:
        window.after_cancel(timer)
    except ValueError:
        print("Nothing to reset yet!")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks["text"] = ""


def start():
    start_button.config(command=restart)
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)
    play()
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
        count_down(work_sec)
    elif reps % 8 == 0:
        play()
        timer_label["text"] = "Break"
        timer_label["fg"] = RED
        count_down(long_break_sec)
    else:
        play()
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        count_down(short_break_sec)


def count_down(count):
    global timer
    time = "{:02d}:{:02d}".format(int(count // 60), int(count % 60))
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start()
        mark = "✔"
        global reps
        mark *= reps//2
        checkmarks["text"] = mark
        if reps >= 8:
            reps = 0


pygame.mixer.init()
pygame.mixer.music.load("crystal-logo-21091.mp3")
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)
window.resizable(0, 0)
canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.config(background=YELLOW)

start_button = tkmacosx.CircleButton(text="Start", command=start, borderless=True, overbackground=ON_GREEN,
                                     overforeground="white", font=FONT_NAME, bg="white", fg=GREEN, focuscolor="",
                                     activebackground=CLICKED_GREEN,
                                     )
start_button.grid(column=0, row=2)

reset_button = tkmacosx.CircleButton(text="Reset", command=reset, borderless=True, overbackground=ON_RED,
                                     overforeground="white", font=FONT_NAME, bg="white", fg=PINK, focuscolor="",
                                     activebackground=CLICKED_RED,
                                     )
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 55, "normal"), foreground=GREEN, background=YELLOW)
timer_label.grid(column=1, row=0)

checkmarks = Label(font=(FONT_NAME, 25, "normal"), foreground=GREEN, background=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
