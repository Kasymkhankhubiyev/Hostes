import User
import tkinter as tk
from tkinter import ttk
import sqlite3 as db
from tkinter import messagebox
import calendar
import datetime
import mybutton as mbtn

class Registration_Table:
    def __init__(self, window, dbase, notebook):
        self.window = window
        self.dbase = dbase
        self.reg_table = ttk.Frame(notebook)
        notebook.add(self.reg_table, text='Регистрация')
        self.days = []
        self.reg_list_widgets = []
        self.living_date = None
        now = datetime.date.today() #datetime.now()
        self.year = now.year
        self.month = now.month
        self.btn_index = None
        self.btn_bg_color = ''
        self.draw_reg_table()

        # self.reg_button = tk.Button(self.window, command=self.draw_reg_table, text='Регистрация', font=('Arial', 17))
        # self.reg_button.place(x=10, y=0)

    def show_checkbtn_state(self):
        state = self.checkbtn_var1.get()
        if state == 1:
            pass
        else:
            pass

    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill_calendar()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill_calendar()

    def is_leap_year(self, year):
        """
        Проверяем, является ли год високосным
        :param year: год
        :return: False/True
        """
        if year % 400 == 0 and year % 100 != 100 or year % 400 == 0:
            return True
        else: return False

    def fill_calendar(self):

        self.Info_lbl['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
        month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            prew_month_days = calendar.monthrange(self.year-1, 12)[1]
        else:
            prew_month_days = calendar.monthrange(self.year, self.month-1)[1]
        week_day = calendar.monthrange(self.year, self.month)[0]

        """
        заполняем текущий месяц
        """
        for n in range(month_days):
            self.days[n + week_day]['text'] = n + 1
            self.days[n + week_day]['fg'] = 'black'
            self.days[n + week_day].set_day(n + 1)
            self.days[n + week_day].set_month(self.month)
            self.days[n + week_day].set_year(self.year)
            self.days[n + week_day].set_index(n + week_day)

            now = datetime.date.today() # datetime.now()
            if self.year == now.year and self.month == now.month and n + 1 == now.day:
                self.days[n + week_day]['background'] = 'greenyellow'
                #  проверка, если время до 12:00, то найм выбирается на текущий день, иначе до 12-ти следующего дня
                self.days[n + week_day ]['state'] = 'disabled'
                self.days[n + week_day]['fg'] = 'black'
            else:
                self.days[n + week_day]['background'] = 'lightgray'
                self.days[n + week_day].set_color('lightgray')
                if self.year <= now.year and self.month == now.month and n < now.day:
                    self.days[n + week_day]['state'] = 'disabled'
                elif self.year <= now.year and self.month < now.month or self.year < now.year:
                    self.days[n + week_day]['state'] = 'disabled'
                else:
                    self.days[n + week_day]['state'] = 'normal'

        """
        Заполняем дни из предыдущего месяца
        """
        for n in range(week_day):
            self.days[week_day - n - 1]['text'] = prew_month_days - n
            self.days[week_day - n - 1]['fg'] = 'gray'
            self.days[week_day - n - 1]['background'] = '#f3f3f3'
            self.days[week_day - n - 1].set_color('#f3f3f3')
            self.days[week_day - n - 1].set_day(prew_month_days - n)
            self.days[week_day - n - 1].set_index(week_day - n - 1)
            if self.month == 1:
                self.days[week_day - n - 1].set_month(12)
                self.days[week_day - n - 1].set_year(self.year - 1)
            else:
                self.days[week_day - n - 1].set_month(self.month - 1)
                self.days[week_day - n - 1].set_year(self.year)
            now = datetime.datetime.now()
            if self.year <= now.year and self.month <= now.month and n < now.day:
                self.days[week_day - n - 1]['state'] = 'disabled'
            else:
                self.days[week_day - n - 1]['state'] = 'normal'

        """
        Заполняем дни из следующего месяца
        """
        for n in range(6*7 - month_days - week_day):
            self.days[week_day + month_days + n]['text'] = n+1
            self.days[week_day + month_days + n]['fg'] = 'gray'
            self.days[week_day + month_days + n]['background'] = '#f3f3f3'
            self.days[week_day + month_days + n].set_color('#f3f3f3')
            self.days[week_day + month_days + n].set_day(n + 1)
            self.days[week_day + month_days + n].set_index(week_day + month_days + n)
            if self.month == 12:
                self.days[week_day + month_days + n].set_month(1)
                self.days[week_day + month_days + n].set_year(self.year + 1)
            else:
                self.days[week_day + month_days + n].set_month(self.month + 1)
                self.days[week_day + month_days + n].set_year(self.year)



    def draw_calendar(self, current_y):
        """
        графическая реализация календаря с возможностью выбора дня
        :param current_y:
        """
        self.reg_canvas = tk.Canvas(self.reg_table, width=300, height=300)
        self.prew_btn = tk.Button(self.reg_canvas, text='<', font=('Arial',17), command=self.prev_month)
        self.prew_btn.grid(row=0, column=0, sticky='nswe')
        self.next_btn = tk.Button(self.reg_canvas, text='>', font=('Arial',17), command=self.next_month)
        self.next_btn.grid(row=0, column=6, sticky='nswe')
        self.Info_lbl = tk.Label(self.reg_canvas, text='0', width=1, height=1, font=('Arial', 14, 'bold'), fg='blue')
        self.Info_lbl.grid(row=0, column=1, columnspan=5, sticky='nsew')

        for n in range(7):
            lbl = tk.Label(self.reg_canvas, text=calendar.day_abbr[n], width=1, height=1, font=('Arial', 10), fg='darkblue')
            lbl.grid(row=1, column=n, sticky='nsew')

        for row in range(6):
            for col in range(7):
                btn = mbtn.Mybutton(self.reg_canvas, text='0', width=4, height=2, font=('Arial', 15))
                btn.grid(row=row+2, column=col, sticky='nsew')
                btn.config(command=lambda button = btn: self.reserve_date(button))
                self.days.append(btn)
        self.fill_calendar()

        self.reg_canvas.place(x = 70, y = current_y)

    def reserve_date(self, button):
        """
        Выбираем дату выезда, дата окончания найма жилья.
        :param button:
        :return:
        """

        Months_lib = {1: 'Янв', 2: 'Фев', 3: 'Март', 4: 'Апр', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Авг', 9: 'Сен',
                      10: 'Окт', 11: 'Нояб', 12: 'Дек'}
        now = datetime.datetime.now()
        out_date, self.living_date = button.get_date()
        self.living_period_lbl['text'] = str(now.day) + ' ' + Months_lib[int(now.month)] + ' ' + str(now.year) + ' - ' + out_date
        delta = self.living_date - datetime.date.today()
        #delta = datetime.datetime(int(button.get_year()), int(button.get_month()), int(button.get_day())) - now
        self.days_amount['text'] = str(delta.days)
        button['background'] = 'cyan'
        if self.btn_index is not None:
            self.days[self.btn_index]['background'] = self.btn_bg_color
            self.btn_index = button.get_index()
            self.btn_bg_color = button.get_color()
        else:
            self.btn_index = button.get_index()
            self.btn_bg_color = button.get_color()


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

        self.living_period_lbl = tk.Label(self.reg_table, text='-', width=30, height=2, borderwidth=3, relief=tk.SUNKEN, background='white', font=('Arial', 15))
        self.living_period_lbl.place(x=90, y=current_y)

        tk.Label(self.reg_table, text='Кол-во дней', font=('Arial', 15)).place(x = 500, y=current_y)
        self.days_amount = tk.Label(self.reg_table, text= '', width=4, height=1, relief=tk.SUNKEN, font=('Arial', 12), background='white')
        self.days_amount.place(x=630, y=current_y)

        self.early_arrival_var = tk.IntVar()
        self.early_arrival_var.set(0)
        self.early_arrival_checkbtn = ttk.Checkbutton(self.reg_table, variable=self.early_arrival_var, onvalue=1,
                                                       offvalue=0)  # command=self.show_checkbtn_state

        self.late_leave_var = tk.IntVar()
        self.late_leave_var.set(0)
        self.late_leave_checkbtn = ttk.Checkbutton(self.reg_table, variable=self.late_leave_var, onvalue=1,
                                                      offvalue=0)
        self.early_arrival_checkbtn.place(x = 500, y = current_y + 65)
        self.late_leave_checkbtn.place(x = 500, y = current_y + 95)
        tk.Label(self.reg_table, text='Ранний заезд', font=('Arial', 17)).place(x= 520, y=current_y + 60)
        tk.Label(self.reg_table, text='Поздний выезд', font=('Arial', 17)).place(x=520, y=current_y + 90)

        current_y += 60

        self.draw_third_line()

        self.draw_calendar(current_y)

    def draw_third_line(self):
        """
        here we draw elements:
            room choosing
            ordering food
            ordering a towel
        :return: does not return anything
        """
        tk.Label(self.reg_table, text='Комната', font=('Arial', 17)).place(x = 750, y = 180)
        values = ['1 комната', '2 комната', '3 комната', '4 комната', '5 комната', '6 комната', '7 комната', '8 комната']
        self.rooms_combobox = ttk.Combobox(self.reg_table, values=values, font=('Arial', 15), state='readonly', width=11)
        self.rooms_combobox.place(x = 850, y = 180)
        self.room_canvas = tk.Canvas(self.reg_table, width=300, height=200, background='white')
        self.room_canvas.place(x = 1020, y = 180)




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