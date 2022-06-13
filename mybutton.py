import tkinter as tk
import datetime

class Mybutton(tk.Button):
    def __init__(self,master, day, month, year, *args, **kwargs):
        super(Mybutton, self).__init__(master, *args, **kwargs)
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_date(self):
        return datetime.date(int(self.year), int(self.month), int(self.day))
