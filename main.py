import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as db

import User
import Login


def on_closing():
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти?'):
        win.destroy()
        dbase.close()

def create_window():
    window = tk.Tk()
    window.title("RNBCoffee")
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w //= 2  # центрируем
    h //= 2
    w -= 350  # переносим левый верхний угол
    h -= 250
    window.geometry("700x500+{}+{}".format(w, h))
    # icon = tk.PhotoImage(file='rnb.png')
    # window.iconphoto(False, icon)
    return window

if __name__ == '__main__':
    try:
        dbase = db.connect('Hostel.db')
        cursor = dbase.cursor()

        # with open('loginpwd_create_table.sql', 'r') as sql_file:
        #     sql_script = sql_file.read()
        # cursor.execute(sql_script)
        # dbase.commit()


        win = create_window()

        login = Login.Login(dbase, win)
        user = login.log_into_system()

        win.mainloop()

        #tab_control = ttk.Notebook(win)






    except db.Error as error:
        print('Connection error occurred')
    finally:
        if dbase:
            cursor.close()
            dbase.close()
            print('Connection with SQL is closed')
