import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as db


if __name__ == '__main__':
    try:
        dbase = db.connect('Hostel.db')
        cursor = dbase.cursor()


    except db.Error as error:
        print('Connection error occurred')
    finally:
        if dbase:
            cursor.close()
            dbase.close()
            print('Connection with SQL is closed')
