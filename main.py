from tkinter import messagebox
from tkinter import ttk
from helper import create_window, on_closing, clear_window

import sqlite3 as db
import tkinter as tk
import ExtendedClasses.User as User
import mainModules.Login as Login
import mainModules.Registration as Registration


if __name__ == '__main__':
    try:
        dbase = db.connect('Hostel.db')
        cursor = dbase.cursor()
        # user = User.User()

        win = create_window(window_title='Arzu Hostel', icon_path='media/Hostel Arzu.png')
        win.protocol('WM_DELETE_WINDOW', lambda db=dbase, window = win: on_closing(win=window, dbase=db))

        login = Login.Login(dbase, win)
        user = login.log_into_system()

        ##можно попробовать через исключения?

        # if user.get_uid() is not None:
        #     s = ttk.Style()
        #     s.configure('TNotebook', font=('Helvetica', '17', 'bold'))
        #     commands_line = ttk.Notebook(win) # , style='My.TNotebook'
        #     frame1 = tk.Frame(commands_line, width=200, height=100)
        #     commands_line.add(frame1, text='Frame1')
        #     registration_table = Registration.Registration_Table(window=win, dbase=dbase, notebook=commands_line)
        #
        #     commands_line.grid(row=0, column=0, sticky='nw') # pack(fill=tk.BOTH, expand=1)

        win.mainloop()

    except db.Error as error:
        print('Connection error occurred')
        messagebox.showerror(title='Упс, ошибочка...', message='Ошибка соединения с Бд')
    finally:
        if dbase:
            dbase.close()
            print('Connection with SQL is closed')
