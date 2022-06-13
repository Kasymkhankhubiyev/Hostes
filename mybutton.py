import tkinter as tk
import datetime

class Mybutton(tk.Button):
    def __init__(self,master, day=None, year=None, month=None, index=None, *args, **kwargs):
        super(Mybutton, self).__init__(master, *args, **kwargs)
        self.day = day
        self.month = month
        self.year = year
        self.index = index
        self.chosen = False
        self.enable = True
        self.color = ''

    def get_state(self):
        return self.enable

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

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
