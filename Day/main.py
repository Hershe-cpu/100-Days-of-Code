import tkinter as tk


# ---------------------------COLORS---------------------#
PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# ---------------------------TIMES---------------------#
WORK_MINUTES = 0
WORK_SECONDS = 5

BREAK_MINUTES = 0
BREAK_SECONDS = 2

LONGBM = 0
LONGBS = 4

# ---------------------------FONTS---------------------#
HEADING_FONT = ("Arial", 40, "bold")
TIMER_FONT = ("Times New Roman", 24, "bold")

# ---------------------------VARIABLES---------------------#
timer_id = None
mode = "work"
completed_sessions = 0

MINUTES = WORK_MINUTES
SECONDS = WORK_SECONDS

# ---------------------------WINDOW---------------------#
root = tk.Tk()
root.title("Pomodoro")
root.configure(background=YELLOW, pady=60, padx=80)

# ---------------------------CANVAS---------------------#
canvas = tk.Canvas(root,
                   width=220,
                   height=224,
                   bg=YELLOW,
                   highlightthickness=0
                   )

tm_img = tk.PhotoImage(file="tomat.png", format="png")

canvas.create_image(110, 112, image=tm_img)
pomo = canvas.create_text(
                        112,
                        130,
                        text=f"{MINUTES:02}:{SECONDS:02}",
                        font=TIMER_FONT,
                        fill="black"
                         )
canvas.grid(row=1, column=1)

def update_display():
    canvas.itemconfig(pomo, text = f"{MINUTES:02}:{SECONDS:02}")


def count_down():
    global MINUTES, SECONDS, timer_id, mode, completed_sessions


    if SECONDS == 0 and MINUTES == 0:
        if mode == "work":
            completed_sessions += 1
            tick_label.config(text="✔"*completed_sessions)

            # Start Break
            mode = "break"

            timer["text"] = "Break"
            reset["text"] = "Skip"
            if completed_sessions % 4 == 0:
                MINUTES = LONGBM
                SECONDS = LONGBS
                completed_sessions = 0

            else:
                MINUTES = BREAK_MINUTES
                SECONDS = BREAK_SECONDS

            update_display()

            return

        else:

            MINUTES = WORK_MINUTES
            SECONDS = WORK_SECONDS
            mode = "work"
            timer["text"] = "Work"
            reset["text"] = "Reset"
            update_display()
            timer_id = None
            if completed_sessions % 4 == 0:
                completed_sessions = 0
                tick_label.config(text="✔" * completed_sessions)
            return


    if SECONDS == 0:
        MINUTES = MINUTES - 1
        SECONDS = 59
    else:
        SECONDS = SECONDS - 1
    update_display()
    timer_id = root.after(1000, count_down)


def start_timer():
    global timer_id
    if timer_id is None:
        timer.config(text="Work" if mode == "work" else "Break")
        count_down()

    if mode == "break":
        count_down()


def reset_timer():
    global MINUTES, SECONDS, timer_id, mode,completed_sessions

    if mode == "break":
        if completed_sessions % 4 == 0:
            completed_sessions = 0
            tick_label.config(text="✔" * completed_sessions)
        if timer_id is not None:
            root.after_cancel(timer_id)
        timer_id = None
        mode = "work"
        MINUTES = WORK_MINUTES
        SECONDS = WORK_SECONDS

        timer["text"] = "Work"
        reset["text"] = "Reset"
        update_display()
        return
    if timer_id is not None:
        root.after_cancel(timer_id)

    timer_id = None
    mode = "work"
    MINUTES = WORK_MINUTES
    SECONDS = WORK_SECONDS
    timer["text"] = "Timer"
    reset["text"] = "Reset"
    update_display()


# Timer
timer = tk.Label(
    root,
    text="Timer",
    font=HEADING_FONT,
    fg=GREEN,
    bg=YELLOW)
timer.grid(row=0, column=1)

#tick mark
tick_label = tk.Label(
    root,
    text="",
    font=TIMER_FONT,
    fg=GREEN,
    bg=YELLOW
)
tick_label.grid(row=3, column=1)


# start
start = tk.Button(root, text="Start", command=start_timer)
start.grid(row=2, column=0)
start.config(background="white")

# reset
reset = tk.Button(root, text="Reset", command=reset_timer)
reset.grid(row=2, column=2)
reset.config(background="white", justify="right")

# tick


root.mainloop()
