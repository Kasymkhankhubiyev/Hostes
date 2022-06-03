import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as db


if __name__ == '__main__':
    try:
        dbase = db.connect('Hostel.db')
        cursor = dbase.cursor()
        # нужно создать класс юзер - логинемся и получаем класс, в котором помимо прочего хранится уровень доступа.

        # with open('loginpwd_create_table.sql', 'r') as sql_file:
        #     sql_script = sql_file.read()
        # cursor.execute(sql_script)
        # dbase.commit()


    except db.Error as error:
        print('Connection error occurred')
    finally:
        if dbase:
            cursor.close()
            dbase.close()
            print('Connection with SQL is closed')
