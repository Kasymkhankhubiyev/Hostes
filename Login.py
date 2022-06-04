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
        """
        Проверяем наличие зарегистрированного пользователя с указанным логином и паролем
        """
        if self.check_input():
            result = self.get_passwort()
            if len(result) > 0:
                if self.password.get == result[0][0]:
                    access = self.get_access_level()
                    self.user = User.User(login=self.login.get(), access=access, )
                else:
                    messagebox.showerror(title='Упс, ошибка...', message='неверный Логин/Пароль.')
                    self.login.delete(0, tk.END)
                    self.password.delete(0, tk.END)
            else:
                messagebox.showerror(title='Упс, ошибка...', message='неверный Логин/Пароль.')
                self.login.delete(0, tk.END)
                self.password.delete(0, tk.END)
        else: pass
        
        
    def get_access_level(self):
        """
        Получаем значение уровня доступа по логину
        :return: user_access_level
        """
        cursor = self.dbase.cursor()
        sql = """SELECT user_access_level FROM people WHERE user_login = ?"""
        cursor.execute(sql, [self.login.get()])
        self.dbase.commit()
        access = cursor.fetchall()
        cursor.close()
        return int(access[0][0])
        
    def get_passwort(self):
        """
        Получаем из БД пароль соответствующий логину и уровню доступа не менее 1
        :return: User_passwort
        """
        cursor = self.dbase.cursor()
        with open('login.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        cursor.execute(sql_script, [self.login.get()])  # implement funtion to get login
        self.dbase.commit()
        result = cursor.fetchall()
        cursor.close()
        return result[0][0]


    def get_uid(self):
        """
        Получаем id пользователя из БД, может быть полезе в будущем для аналища данных
        :return:
        """
        cursor = self.dbase.cursor()
        sql = """SELECT id FROM people WHERE user_access_level > 0 AND user_login = ? """ # заменить id на uid
        cursor.execute(sql, [self.login.get()])  # implement funtion to get login
        self.dbase.commit()
        result = cursor.fetchall()
        cursor.close()
        return int(result[0][0])


    def check_input(self):
        """
        Проверка вводимых пользователем данных.
        Проверяет заполнены ли все строки ввода, если нет - выдает ошибку.
        """
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
        """
        Передаем объект зарегистрированного пользователя в main
        :return: User.User()
        """
        return self.user