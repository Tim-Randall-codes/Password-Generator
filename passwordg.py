from random import randint
import tkinter as tk

win = tk.Tk()
win.title('Password Generator')
win.geometry('800x600+100+100')
select = 1
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
       '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F',
       'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', ':', ';', '/', '?', '!', '$']

def generate():
    lower = randint(0, 25)
    lower_num = randint(0, 35)
    lower_num_upper = randint(0, 61)
    lower_num_upper_spec = randint(0, 69)
    if select == 1:
        password = lst[lower]
    elif select == 2:
        password = lst[lower_num]
    elif select == 3:
        password = lst[lower_num_upper]
    elif select == 4:
        password = lst[lower_num_upper_spec]
    print(select)
    print(password)



password_display = tk.Label(win, text='hi')
password_display.place(x=50, y=50)

copyb = tk.Button(win, text='copy')
copyb.place(x=200, y=50)

generateb = tk.Button(win, text='generate', command=generate)
generateb.place(x=400, y=50)

s1 = tk.Radiobutton(win, text="Lower case only", variable=select, value=1)
s1.place(x=50, y=150)
s2 = tk.Radiobutton(win, text="Lower case and numbers", variable=select, value=2)
s2.place(x=50, y=200)
s3 = tk.Radiobutton(win, text="Lower case, upper case and numbers", variable=select,
                    value=3)
s3.place(x=50, y=250)
s4 = tk.Radiobutton(win, text="Lower case, upper case, numbers and special characters",
                    variable=select, value=4)

win.mainloop()
