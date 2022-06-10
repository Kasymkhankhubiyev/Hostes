import User
import tkinter as tk
from tkinter import ttk
import sqlite3 as db
from tkinter import messagebox

class Registration_Table:
    def __init__(self, window, dbase, notebook):
        self.window = window
        self.dbase = dbase
        self.reg_table = ttk.Frame(notebook)
        notebook.add(self.reg_table, text='Регистрация')
        self.draw_reg_table()
        # self.reg_button = tk.Button(self.window, command=self.draw_reg_table, text='Регистрация', font=('Arial', 17))
        # self.reg_button.place(x=10, y=0)

    def draw_reg_table(self):
        """
        Рисуем основную вкладку для регистрации клинетов
        :return:
        """
        tk.Label(self.reg_table, font=('Arial', 15), text='ИИН').place(x=10, y=10)
        tk.Button(self.reg_table, font=('Arial', 12), text='Проверить', command=self.check_iin).place(x=240, y=10)
        self.iin_entry = tk.Entry(self.reg_table, font=('Arial', 15), width=14)
        self.iin_entry.place(x=70, y = 10)
        # self.reg_button = tk.Button(self.window, command=self.draw_reg_table, text='Регистрация', font=('Arial', 17))
        # self.reg_button.grid(row=0, column=0)

    def check_iin(self):
        if self.iin_entry.get() != '' and len(self.iin_entry.get()) == 12:
            pass
        else:
            messagebox.showerror(title='Ошибка ввода.', message=f'Неверно введен ИИН = {self.iin_entry.get()}, \nИИН должен состоять из 12 цифр')