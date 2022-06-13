import tkinter as tk
import datetime

class Mybutton(tk.Button):
    def __init__(self,master, day, month, year, *args, **kwargs):
        super(Mybutton, self).__init__(master, *args, **kwargs)
        self.day = day
        self.month = month
        self.year = year
        self.chosen = False
        self.enable = True

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.year = month

    def set_day(self, day):
        self.year = day

    def desable_btn(self):
        self.enable = False

    def release_btn(self):
        self.chosen = False

    def choose_btn(self):
        self.chosen = True

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_date(self):
        return datetime.date(int(self.year), int(self.month), int(self.day))
