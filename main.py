import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as db

import User
import Login
import Registration

def clear_window(window):
    array = window.place_slaves()
    for i in array:
        i.destroy()

def on_closing():
    """
    Обрабатываем закрытие программы.
    """
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти?'):
        win.destroy()
        dbase.close()

def create_window():
    """
    Создаем главное окно
    :return: window
    """
    window = tk.Tk()
    window.title("RNBCoffee")
    # window.attributes('-fullscreen', True)
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    # w //= 2  # центрируем
    # h //= 2
    # w -= 450  # переносим левый верхний угол
    # h -= 350
    # window.geometry("900x700")
    window.geometry("{}x{}".format(w, h))
    icon = tk.PhotoImage(file='Hostel Arzu.png')
    window.iconphoto(False, icon)
    return window

if __name__ == '__main__':
    try:
        dbase = db.connect('Hostel.db')
        cursor = dbase.cursor()
        user = User.User()

        # with open('loginpwd_create_table.sql', 'r') as sql_file:
        #     sql_script = sql_file.read()
        # cursor.execute(sql_script)
        # dbase.commit()

        win = create_window()
        win.protocol('WM_DELETE_WINDOW', on_closing)

        login = Login.Login(dbase, win)
        user = login.log_into_system()

        if user.get_uid() is not None:
            commands_line = ttk.Notebook(win)
            registration_table = Registration.Registration_Table(window=win, dbase=dbase, notebook=commands_line)
            commands_line.pack()

        win.mainloop()

    except db.Error as error:
        print('Connection error occurred')
    finally:
        if dbase:
            dbase.close()
            print('Connection with SQL is closed')
