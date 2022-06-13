import User
import tkinter as tk
from tkinter import ttk
import sqlite3 as db
from tkinter import messagebox
import calendar
import datetime

class Registration_Table:
    def __init__(self, window, dbase, notebook):
        self.window = window
        self.dbase = dbase
        self.reg_table = ttk.Frame(notebook)
        notebook.add(self.reg_table, text='Регистрация')
        self.draw_reg_table()
        self.reg_list_widgets = []
        # self.reg_button = tk.Button(self.window, command=self.draw_reg_table, text='Регистрация', font=('Arial', 17))
        # self.reg_button.place(x=10, y=0)

    def show_checkbtn_state(self):
        state = self.checkbtn_var1.get()
        if state == 1:
            pass
        else:
            pass

    def is_leap_year(self, year):
        """
        Проверяем, является ли год високосным
        :param year: год
        :return: False/True
        """
        if year % 400 == 0 and year % 100 != 100 or year % 400 == 0:
            return True
        else: return False

    def draw_calendar(self, current_y, year=None, month=None):
        self.reg_canvas = tk.Canvas(self.reg_table, width = 300, height=300, bg='green')
        tk.Label(self.reg_canvas, text='month', font=('Arial', 10), background='blue').place(x=1, y=1)
        reg_calendar = calendar.TextCalendar()
        today_date = datetime.datetime.date(datetime.datetime.now())
        #print(reg_calendar.pryear(today_date.year))
        month_cal = reg_calendar.formatmonth(today_date.year, today_date.month, w=0, l=0)
        print(month_cal)

        lines = month_cal.split('  ')
        print(lines)
        days = month_cal.split()
        print(days)


        self.reg_canvas.place(x=10, y=current_y)


    def draw_reg_table(self):
        """
        Рисуем основную вкладку для регистрации клинетов
        :return:
        """
        current_y = 10
        current_x = 10
        tk.Label(self.reg_table, font=('Arial', 17), text='ИИН').place(x=10, y=current_y)
        tk.Button(self.reg_table, font=('Arial', 15), text='Проверить', command=self.check_iin).place(x=280, y=current_y/2)
        self.iin_entry = tk.Entry(self.reg_table, font=('Arial', 17), width=14)
        self.iin_entry.place(x=80, y=current_y)
        self.checkbtn_var1 = tk.IntVar()
        self.checkbtn_var1.set(0)
        self.set_new_client_checkbtn = ttk.Checkbutton(self.reg_table, variable=self.checkbtn_var1, onvalue=1, offvalue=0,command=self.show_checkbtn_state)
        self.set_new_client_checkbtn.place(x=420, y=current_y * 1.5)
        tk.Label(self.reg_table, text=' Новый клиент ', font=('Arial', 16), relief=tk.GROOVE).place(x=440, y=current_y)
        current_y += 60

        tk.Label(self.reg_table, font=('Arial', 17), text='ИМЯ').place(x=10, y=current_y)
        self.name_entry = tk.Entry(self.reg_table, font=('Arial', 17), width=31)
        self.name_entry.place(x=80, y=current_y)
        current_y += 60

        tk.Label(self.reg_table, font=('Arial', 17), text='Фамилия').place(x=10, y=current_y)
        self.secname_entry = tk.Entry(self.reg_table, font=('Arial', 17), width=28)
        self.secname_entry.place(x=120, y=current_y)
        current_y += 60

        self.draw_calendar(current_y)

        # self.reg_button = tk.Button(self.window, command=self.draw_reg_table, text='Регистрация', font=('Arial', 17))
        # self.reg_button.grid(row=0, column=0)


    def check_iin(self):
        """
        проверяем наличие указанного ИИН в базе
        :return:
        """
        if self.iin_entry.get() != '' and len(self.iin_entry.get()) == 12:
            num = self.iin_entry.get()
            if self.is_integer(num):
                pass
            else:
                messagebox.showerror(title='Ошибка ввода.', message=f'Неверно введен ИИН = {self.iin_entry.get()}, \nИИН должен состоять только из цифр')
        else:
            messagebox.showerror(title='Ошибка ввода.', message=f'Неверно введен ИИН = {self.iin_entry.get()}, \nИИН должен состоять из 12 цифр')

    def is_integer(self, string):
        """
        Проверяем, составлена ли строка исключительно из цифр.
        :param string: строка с 12-тью цифрами
        :return: False or True
        """
        for i in string:
            if i not in '01234567890':
                return False
            else: pass

        return True