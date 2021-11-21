from tkinter import *  #импортивуем библиотеку для создания GUI
from vk_api import main
from data_api_vk import manual


class Window:
    def __init__(self, geometry='430x150+500+400', title='ПАРСИНГ АЛЬБОМ(А\ОВ) VK от Артёма', resizable=(False, False), icon='vk.ico'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)

        self.lable_1 = Label(self.root, text='ЧТО-БЫ НАЧАТЬ ПАРСИНГ ПО УМОЛЧАНИЮ, НАЖМИТЕ КНОПКУ ВНИЗУ ', bg='#9292ed', relief=RIDGE, font='Consolas 10')
        self.button_1 = Button(self.root, text='НАЧАТЬ ПАРСИНГ', bg='#6aca50', relief=RIDGE, width=17, height=2, font='Consolas 8', command=main)
        self.lable_2 = Label(self.root, text='ВНИМАНИЕ:\nперед началом (и что-бы настроить парсер) прочитайте MANUAL', bg='#f4eb26', relief=RIDGE, font='Consolas 10')
        self.button_2 = Button(self.root, text='ОТКРЫТЬ MANUAL', bg='#73b0e6', relief=RIDGE, width=17, height=2, font='Consolas 8', command=manual)
        # self.button_3 = Button(self.root, text='ОТКРЫТЬ НАСТРОЙКИ', bg='#e11d2b', relief=RIDGE, width=17, height=2, font='Consolas 8', command=customization)
    def run(self):
        self.draw_widgets()
        self.root.mainloop()


    def draw_widgets(self):
        self.lable_1.pack(anchor=N, pady=15)
        self.lable_2.pack()
        self.button_1.pack(anchor=NW, padx=15, pady=10, side=LEFT)
        self.button_2.pack(anchor=NE, padx=15, pady=10, side=RIGHT)
        # self.button_3.pack(anchor=NE, padx=15, pady=10, side=TOP)


window = Window()
window.run()