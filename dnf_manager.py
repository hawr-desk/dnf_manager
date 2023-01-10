from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import scrolledtext


import subprocess
import os

def dnfpack():
    lstbox.delete(1.0, END)
    cmd = [ ]
    cmd = "dnf list installed" # Здесь вместо date Ваша команда для git
    
    returned_output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) # returned_output содержит вывод в виде строки байтов
    
    lstbox.insert(INSERT, returned_output.decode("utf-8"))


def delpack():
    value = pack.get()
    answer = mb.askyesno(
        title='Удалить пакет' + value,
        message="Вы хотите удалить пакет" + value 
    )
    pack.delete(0, END)
    if answer == True:
        cli_command = ("sudo dnf remove ", value)
        print("удаление находится в разработке")

#настройки окна
root = Tk()
root.title("DNF Manager")
root.geometry('1000x800')
root.resizable(False, False)

#list dnf - команда отображения списка пакетов
dnfbut = tk.Button(text = "DNF", command=dnfpack)
dnfbut.place(x = 840, y = 760, width=70, height= 25)



#delete - удаление нужного пакета
delbut = tk.Button(text = "Delete", command=delpack)
delbut.place(x  = 760, y = 760, width=70, height= 25)

#entry - для ввода наименования пакета
pack = tk.Entry(borderwidth="1px")
pack.place(x = 450, y = 760, width=300, height=25)

#для отображения списка пакетов
lstbox = scrolledtext.ScrolledText()
lstbox.place(x = 10, y= 50, width = 980, height= 700)

root.mainloop()