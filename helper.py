import tkinter as tk
from tkinter import messagebox

def create_window(window_title: str, width=None, height=None, icon_path=None) -> tk.Tk:
    """
    Создаем главное окно
    :return: window
    """

    window = tk.Tk()
    window.title(window_title)
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    if width is not None and height is not None:
        w = width
        h = height
    window.geometry("{}x{}".format(w, h))
    if icon_path is not None:
        icon = tk.PhotoImage(file=icon_path)
        window.iconphoto(False, icon)
    return window

def clear_window(window):
    array = window.place_slaves()
    for i in array:
        i.destroy()

def on_closing(win, dbase):
    """
    Обрабатываем закрытие программы.
    """
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти?'):
        win.destroy()
        dbase.close()