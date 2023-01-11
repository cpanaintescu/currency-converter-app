import tkinter as tk
import tkinter.messagebox as tkm
import pygame
from views import AppView
from models import AppModel


class AppController:

    def __init__(self):
        window = tk.Tk()

        window.geometry('500x550')
        window.title('Convertor')
        window.configure(bg='white')
        window.resizable(height=tk.FALSE, width=tk.FALSE)

        pygame.init()
        pygame.mixer.music.load("sound/Sound.mp3")

        self.root = window
        self.root.bind('<Return>', self.handle_returnbtn)
        self.model = AppModel()
        self.view = AppView(self.root, self)
        self.convert()
        self.root.mainloop()


    def handle_enterbutton(self, e):
        self.view.main_view.convert_button['bg'] = '#A0FFE1'

    def handle_leavebutton(self, e):
        self.view.main_view.convert_button['bg'] = '#FAFFFD'  

    def play(self):
        pygame.mixer.music.play()
   
    def handle_returnbtn(self, e):
        self.convert()

    def handle_curency_changes(self, e):
        self.convert()

    def get_curency_list(self):
        return self.model.valutes_list

    def get_curency_ration(self, c_from, c_to):
        return float(self.model.data[c_from][-1]) / self.model.data[c_to][-1]

    def compute(self, c_from: str, c_to: str, value: str):
        try:
            if c_from not in self.get_curency_list():
                raise Exception(f"{c_from} is not a valid currency value")
            if c_to not in self.get_curency_list():
                raise Exception(f"{c_to} is not a valid currency value")
            converted_value = float(value)
        except ValueError as exp:
            self.play()
            tkm.showerror(title="Input Error", message=f"{value} is kinda sus. Please insert a not sus input!")
            return "ERROR!"
        except Exception as exp:
            self.play()
            tkm.showerror(title="Input Error", message=exp)
            return "ERROR!"
        return converted_value * self.get_curency_ration(c_from, c_to)\

    def convert(self):
        c_from = self.view.main_view.from_combo.get()
        c_to = self.view.main_view.to_combo.get()
        c_value = self.view.main_view.value_entry.get()
        self.view.main_view.result.config(
            text=str(self.compute(c_from, c_to, c_value))
        )
