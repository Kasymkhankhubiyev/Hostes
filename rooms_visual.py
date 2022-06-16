import tkinter as tk

def instructions():
    pass

def draw_room_one(canvas):

    # одноярусная кровать
    btn1 = tk.Button(canvas, text='1A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=9, height=2)
    btn1.place(x=10, y=10)

    # двухярусная кровать напротив одноместной
    btn2 = tk.Button(canvas, text='2A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4, height=2)
    btn2.place(x=10, y=110)
    btn3 = tk.Button(canvas, text='2B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4, height=2)
    btn3.place(x=60,y=110)

    # двуярусная кровать напротив двери и окна
    btn4 = tk.Button(canvas, text='3A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4, height=2)
    btn4.place(x=180, y=10)
    btn4 = tk.Button(canvas, text='3B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4,
                     height=2)
    btn4.place(x=180, y=62)

def draw_room_two(canvas):
    btn = tk.Button(canvas, text='1A', font=('Arial', 15, 'bold'), background='deep sky blue', fg='black', width=4,
                     height=2)
    btn.place(x=10, y=10)
    btn = tk.Button(canvas, text='1B', font=('Arial', 15, 'bold'), background='orange', fg='black', width=4,
                     height=2)
    btn.place(x=10, y=75)

def draw_room_three(canvas):
    # одноярусная кровать
    btn1 = tk.Button(canvas, text='1A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=9,
                     height=2)
    btn1.place(x=10, y=10)

    # двухярусная кровать напротив одноместной
    btn2 = tk.Button(canvas, text='2A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4,
                     height=2)
    btn2.place(x=10, y=110)
    btn3 = tk.Button(canvas, text='2B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4, height=2)
    btn3.place(x=60, y=110)

    # двуярусная кровать напротив двери и окна
    btn4 = tk.Button(canvas, text='3A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4,
                     height=2)
    btn4.place(x=180, y=10)
    btn4 = tk.Button(canvas, text='3B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4,
                     height=2)
    btn4.place(x=180, y=62)

def draw_room_four(canvas):
    # двухярусная кровать
    btn1 = tk.Button(canvas, text='1A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4,
                     height=2)
    btn1.place(x=10, y=10)
    btn2 = tk.Button(canvas, text='1B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4,
                     height=2)
    btn2.place(x=60,y=10)

    # двухярусная кровать напротив двери
    btn3 = tk.Button(canvas, text='2A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4,
                     height=2)
    btn3.place(x=10, y=150)
    btn4 = tk.Button(canvas, text='2B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4, height=2)
    btn4.place(x=60, y=150)

    # двуярусная кровать у стены бойлерной
    btn4 = tk.Button(canvas, text='3A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=4,
                     height=2)
    btn4.place(x=130, y=10)
    btn5 = tk.Button(canvas, text='3B', font=('Arial', 13, 'bold'), background='orange', fg='black', width=4,
                     height=2)
    btn5.place(x=130, y=62)

    #рисуем бойлерную
    tk.Label(canvas, background='seashell3', borderwidth=3, width=15, height=7).place(x=186, y=5)

    # одноярусная кровать
    btn6 = tk.Button(canvas, text='4A', font=('Arial', 13, 'bold'), background='deep sky blue', fg='black', width=9,
                     height=2)
    btn6.place(x=195, y=120)

def draw_room_five(canvas):
    pass

def draw_room_six(canvas):
    pass

def draw_room_seven(canvas):
    pass

def draw_room_eight(canvas):
    pass