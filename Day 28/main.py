from timer import Pomodoro
from ui import Window

UI = Window()
TIMER = Pomodoro()
UI.start_command(TIMER.countdown)
if TIMER.countdown :
    UI.update_timer_label("Work")
    UI.update_timer_text(TIMER.countdown())
UI.reset_command(TIMER.stop_timer)
if TIMER.stop_timer :
    UI.update_timer_label("Timer")
