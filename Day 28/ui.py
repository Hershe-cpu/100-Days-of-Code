CANVAS_WIDTH = 220
CANVAS_HEIGHT = 224

IMAGE_X = 110
IMAGE_Y = 112

TEXT_X = 112
TEXT_Y = 130

import tkinter as tk
from constants import YELLOW,TIMER_FONT
class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pomodoro")
        self.root.configure(bg=YELLOW, pady=60, padx=80)
        self.create_canvas()
        self.load_image("./assets/tomato.png")
        self.create_timer()
        self.create_buttons()
        self.create_labels()




    def create_canvas(self) -> None:
        self.canvas = tk.Canvas(self.root,
                width=CANVAS_WIDTH,
                height=CANVAS_HEIGHT,
                bg=YELLOW,
                highlightthickness=0
                )
    def load_image(self,img:str) -> None:
        self.tm_img = tk.PhotoImage(file=img)
        self.canvas.create_image(IMAGE_X, IMAGE_Y, image=self.tm_img)

    def create_timer(self) -> None:
        self.timer_text = self.canvas.create_text(
            TEXT_X,
            TEXT_Y,
            text="25:00",
            font=TIMER_FONT,
            fill="black"
        )
        self.canvas.grid(row=1, column=1)


    def create_labels(self) -> None:
        self.timer_label = tk.Label(self.root,
                text = "Timer",
                font=TIMER_FONT,
                bg=YELLOW,)
        self.timer_label.grid(row=0, column=1)


    def create_buttons(self) -> None:
        self.start_button = tk.Button(self.root,
                                      text="Start",
                                      bg="white",)
        self.start_button.grid(row=2, column=0)

        self.reset_button = tk.Button(self.root,
                                      text="Reset",
                                      bg="white",
                                      justify="right")
        self.reset_button.grid(row=2, column=2)



    def update_timer_text(self, text: str) -> None:
        self.canvas.itemconfig(self.timer_text, text=text)

    def update_timer_label(self, text: str) -> None:
        self.timer_label.config(text=text)

    def update_reset_button(self, text: str) -> None:
        self.reset_button.config(text=text)

    def start_command(self,cmd):
        self.start_button.config(command=cmd)

    def reset_command(self,cmd):
        self.reset_button.config(command=cmd)
ui = Window()


ui.root.mainloop()
