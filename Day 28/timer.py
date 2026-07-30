import threading
from constants import WORK_MINUTES,WORK_SECONDS,BREAK_SECONDS,BREAK_MINUTES
class Pomodoro:
    def __init__(self):
        self.wminutes = WORK_MINUTES
        self.wseconds = WORK_SECONDS
        self.bminutes = BREAK_MINUTES
        self.bseconds = BREAK_SECONDS



    def countdown(self):
        if self.wminutes ==0 and self.wseconds ==0:
            return f"{self.wminutes}: {self.wseconds}"
        else:
            if self.wminutes ==0:
                self.wminutes -= 1
                self.wseconds = 59
            else:
                self.wseconds -= 1

        self.thread = threading.Timer(1, self.countdown).start()
        return f"{self.wminutes}: {self.wseconds}"

    def stop_timer(self):
        self.thread.cancel()





