import User
import tkinter as tk
from tkinter import ttk
import sqlite3 as db
from tkinter import messagebox

class Login:
    def __init__(self, dbase, window):
        self.dbase = dbase
        self.user = User.User()
        self.win = window

        tk.Label(self.win, text='login', font=('Arial', 14)).place(x=200, y=150)
        tk.Label(self.win, text='password', font=('Arial', 14)).place(x=200, y=190)

        self.login = tk.Entry(self.win, font=('Arial', 14))
        self.login.place(x=300, y=150)
        self.password = tk.Entry(self.win, show='*', font=('Arial', 14))
        self.password.place(x=300, y=190)
        tk.Button(self.win, command=self.check_loginpwd, text='Enter', font=('Arial', 14)).place(x=350, y=250)

    def check_loginpwd(self):
        if self.check_input():
            cursor = self.dbase.cursor()
            with open('login.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            cursor.execute(sql_script, [self.login.get()])  # implement funtion to get login
            self.dbase.commit()
            result = cursor.fetchall()
            if len(result) > 0:
                if self.password.get == result[0][0]:
                    pass
                else:
                    messagebox.showerror(title='Упс, ошибка...', message='неверный Логин/Пароль.')
                    self.login.delete(0, tk.END)
                    self.password.delete(0, tk.END)
            else:
                messagebox.showerror(title='Упс, ошибка...', message='неверный Логин/Пароль.')
                self.login.delete(0, tk.END)
                self.password.delete(0, tk.END)
        else: pass

    def check_input(self):
        if self.login.get() != '':
            if self.password.get() != '':
                return True
            else:
                messagebox.showerror(title='Упс, ошибка...', message='поле "Пароль" пустое!!!')
                return False
        else:
            messagebox.showerror(title='Упс, ошибка...', message='поле "Логин" пустое!!!')
            return False



    def log_into_system(self):
        pass