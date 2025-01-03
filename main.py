from tkinter import *
import math

from numba.core.ir import Global

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=1
reset=None
# ---------------------------- TIMER RESET ------------------------------- #
# Reset Clicked
def rest_clicked():
    global reset
    window.after_cancel(reset)
    canvas.itemconfig(timer_text, text=f"0{0}:{0}0")
    text.config(text="TIMER", fg=GREEN)
    tick.config(text="")
def timer_reset():
    global REPS
    global WORK_MIN
    global SHORT_BREAK_MIN
    global LONG_BREAK_MIN
    if REPS-1==0:
        mar = ""
        tick.config(text=mar)
    if REPS in[1,3,5,7]:
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        window.lift()
        text.config(text="TIMER", fg=GREEN)
        count_down(WORK_MIN*60)
    elif REPS in [2,4,6]:
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        for i in range(int(REPS/2)+1):
            mar = "✔"*i
            tick.config(text=mar)
        text.config(text="SHORT BREAK", fg=PINK)
        text.grid(column=2, row=1)
        count_down(SHORT_BREAK_MIN*60 )

    elif REPS==8:
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        window.lift()
        mar = "✔✔✔✔"
        tick.config(text=mar)
        count_down(LONG_BREAK_MIN*60 )
        text.config(text="LONG BREAK", fg=RED)
        REPS=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def restart_time():
    global WORK_MIN
    count=WORK_MIN*60
    count_down(count)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minu=math.floor(count/60)
    sec= count%60
    global REPS

    if count==0:
        REPS+=1
        timer_reset()
    if sec in range(0,10):
        sec="0"+str(sec)

    canvas.itemconfig(timer_text,text=f"{minu}:{sec}")
    if count>0:
        global reset
        reset=window.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady= 50,bg=YELLOW)
# "timer"
text=Label( text = "TIMER",font=(FONT_NAME,35,"bold"))
text.config(bg=YELLOW,fg=GREEN)
text.grid(column=2, row=1)
#start
button = Button(text="Start",command=restart_time)
button.grid(column=1, row=3)
#start
button = Button(text="Reset",command=rest_clicked)
button.grid(column=3, row=3)
# Tomato
canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="C:/Users/sivasoorya/Downloads/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2, row=2)
# Tick
tick=Label( text = "",font=(FONT_NAME,15,"bold"))
tick.config(bg=YELLOW,fg=GREEN)
tick.grid(column=2, row=3)

window.mainloop()