import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk   

class AppView(object):

    def __init__(self, frame, controller):

        top_frame = tk.Frame(frame, width=500, height=60,bg = 'red')
        top_frame.pack()

        main_frame = tk.Frame(frame, width=330, height=390,bg = 'white')
        main_frame.pack()

        self.controller = controller
        self.top_view = TopView(top_frame, controller)
        self.main_view = MainView(main_frame, controller)


class TopView:

    def __init__(self, frame, controller) -> None:
        self.icon = Image.open('images/icon.png')
        self.icon = self.icon.resize((60,30))
        self.icon = ImageTk.PhotoImage(self.icon)
        self.app_name = tk.Label(frame, image = self.icon, compound=tk.LEFT, text = "Convertor Valutar", height=20, padx=20, pady=20, anchor=tk.CENTER, font= ('Arial 20 bold'), bg='red',fg= 'white')
        self.app_name.place(x=0,y=0)


class MainView:

    def __init__(self, frame, controller):
        self.controller = controller

        self.result = tk.Label(frame, text = " ", width = 20, height = 3, pady=7, relief="solid", anchor=tk.CENTER, font=('Georgia 15 bold'), bg='white', fg= 'black')
        self.result.place(x=20,y=50)

        self.from_label = tk.Label(frame, text = "From", width = 5, height = 1, padx=0, pady=0, relief="flat", anchor=tk.NW, font=('Ivy 25 bold'), bg='white', fg= 'black')
        self.from_label.place(x=7,y= 180)
        self.from_combo = ttk.Combobox(frame, width=8, justify=tk.CENTER, font=("Ivy 16 bold"))
        self.from_combo['values'] = self.controller.get_curency_list()
        self.from_combo.bind('<<ComboboxSelected>>', self.controller.handle_curency_changes)
        self.from_combo.current(self.from_combo['values'].index("EUR"))
        self.from_combo.place(x=2, y = 222)
       
        self.to_label = tk.Label(frame, text = "To", width = 5, height = 1, padx=0, pady=0, relief="flat", anchor=tk.NE, font=('Ivy 25 bold'), bg='white', fg= 'black')
        self.to_label.place(x=144, y = 180)
        self.to_combo = ttk.Combobox(frame, width=8, justify=tk.CENTER, font=("Ivy 16 bold"))
        self.to_combo['values'] = self.controller.get_curency_list()
        self.to_combo.bind('<<ComboboxSelected>>', self.controller.handle_curency_changes)
        self.to_combo.current(self.from_combo['values'].index("RON"))
        self.to_combo.place(x=180, y = 222)

        self.value_label = tk.Label(frame, text="Enter Value:",width = 12, height = 1, padx=0, pady=0, relief="flat", anchor=tk.NW, font=('Ivy 13 bold'), bg='white', fg= 'black' )
        self.value_label.place(x=6,y=270)

        self.value_entry = tk.Entry(frame, width=15, justify=tk.CENTER, font=("Ivy 14 bold"), relief=tk.SOLID)
        self.value_entry.insert(0, "1")
        self.value_entry.place(x=130, y=270)

        self.convert_button = tk.Button(frame, text="CONVERT", width= 10, bg='#f8f8f8', height = 2, pady=5, anchor=tk.CENTER, font=('Ivy 15 bold'), command=self.controller.convert)
        self.convert_button.bind('<Enter>', self.controller.handle_enterbutton)
        self.convert_button.bind('<Leave>', self.controller.handle_leavebutton)
        self.convert_button.place(x=95,y= 310)
    