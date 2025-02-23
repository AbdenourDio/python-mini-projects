
from tkinter import *
import math

# Constants
FONT_NAME = "Courier"
GREEN = "#629584"
PINK = "#FDAB9E"
RED = "#E50046"
WHITE = "#F7F7F7"
WORKING_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 15
timer = None       # TODO: I didn't fully understand why we did this.

window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=10, bg=WHITE)

#repetion tracker
reps = 0

# RESET TIMER
def reset_timer():
    window.after_cancel(timer)      # TODO: this (timer) is underlined by yellow line why?
    label.configure(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.configure(text="")


# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1
    if reps % 8 in [1,3,5,7]:
        label.configure(text="Work",fg=GREEN)
        count_down(WORKING_TIME * 60)

    elif reps % 8 in [2,4,6]:
        count_down(SHORT_BREAK_TIME * 60)
        label.configure(text="Break",fg=PINK)

    elif reps % 8 == 0:
        count_down(LONG_BREAK_TIME * 60)
        label.configure(text="Break",fg=RED)


# COUNTDOWN MECHANISM
mark = ""
def count_down(count):
    global mark,timer
    count_minute = math.floor(count / 60)       #TODO: what is the difference between round() and math.floor()??
    count_second = count % 60
    if count_second <= 9:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark += "✔"
            check_mark.config(text=mark)




#UI

#just a tomato image
tomato_image = PhotoImage(file="pomodoro_thumbnail.png")
canvas = Canvas(width=360, height=360, bg=WHITE, highlightthickness=0)
canvas.create_image(180,183,image=tomato_image)

#countdown text
timer_text = canvas.create_text(180,204,text="00:00",fill="white",font=(FONT_NAME,48,"bold"))
canvas.grid(column=1,row=1)

# Timer label text
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,40,"bold"), bg=WHITE)
label.grid(column=1,row=0)

# start the counter button
start_button = Button(text="Start",command=start_timer,highlightthickness=0,width=6,height=2)
start_button.grid(column=0,row=2)

#reset the timer button
reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer,width=6,height=2)
reset_button.grid(column=2,row=2)

#work session tracker
check_mark = Label(fg=GREEN, font=(FONT_NAME,15,"bold"), bg=WHITE)
check_mark.grid(column=1,row=3)







window.mainloop()