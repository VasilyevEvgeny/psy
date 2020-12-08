# python3

import os
import tkinter as tk
from tkinter import Tk, PhotoImage, LEFT, IntVar, Label
from tkinter.ttk import Frame, Scale, Label, Style
import pandas as pd
import operator
from functools import reduce
from datetime import datetime


NAME = 'Самооценка'


class Psy(Frame):
    def __init__(self):
        super().__init__()

        self.__questions = [
            [
                'Рост',
                'Здоровый',
                'Умный',
            ],
            [
                'Сильный',
                'Хороший ученик',
                'Красивый'
            ],
            [
                'Хороший друг',
                'Счастлив',
                'Доволен собой'
            ]
        ]

        self.__labels = []
        self.__scales = []
        self.__vars = [[0, 0, 0] for _ in range(3)]

        self.__configure_ui()

    def __configure_ui(self):
        self.master.title(NAME)
        self.master.resizable(0, 0)
        self.master.geometry('870x400+500+200')
        #path = os.path.dirname(os.path.realpath(__file__))
        #self.master.tk.call('wm', 'iconphoto', self.master._w, PhotoImage(file=path+'/icon.png'))

        i_labels = 0
        i_scales = 0
        for i in range(7):

            # instruction
            if not i:
                Label(self.master, text='Оцени себя по каждой шкале').grid(row=0, column=0, columnspan=3, padx=(100, 10), pady=(10, 20))
                continue

            # grid with scales
            if i % 2:
                self.__labels.append([])
            else:
                self.__scales.append([])
            for j in range(3):
                if i % 2:
                    self.__labels[i_labels].append(Label(self.master, text=self.__questions[i_labels][j]).
                                                   grid(row=i, column=j, padx=(100, 10), pady=(10, 10)))
                else:
                    self.__scales[i_scales].append(Scale(self.master, from_=0, to=100, length=150,
                                                         command=lambda val, i=i_scales, j=j: self.__on_scale(val, i, j)).
                                                   grid(row=i, column=j, padx=(100, 10), pady=(10, 10)))

            if i % 2:
                i_labels += 1
            else:
                i_scales += 1

        # button 'save'
        tk.Button(self.master, text='СОХРАНИТЬ', width=70,
                  command=self.__save_results).grid(row=9, column=0, columnspan=3, padx=(100, 10), pady=40)

    def __on_scale(self, val, i, j):
        var = IntVar()
        var.set(int(float(val)))
        self.__vars[i][j] = var.get()

    def __save_results(self):
        q = reduce(operator.concat, self.__questions)
        v = reduce(operator.concat, self.__vars)
        res_dict = {'Вопросы': q, 'Ответы': v}
        df = pd.DataFrame(res_dict)
        path = os.path.join(os.environ['HOMEPATH'], 'Desktop')
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        df.to_excel(path + '\\{}.xlsx'.format(name), sheet_name=NAME, index=False)


def main():
    root = Tk(className=NAME)
    psy = Psy()
    root.mainloop()


if __name__ == '__main__':
    main()
