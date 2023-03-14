import tkinter as t
import datetime as d
import calendar as c
import users
import json
import get_info as inf

def Create_month(where, year, month):
    global MONTH
    global YEAR
    MONTH = month
    YEAR = year
    move_left = t.Button(
        where, 
        text = "<", 
        font = "monospace", 
        padx = 69, 
        borderwidth = 1, 
        relief = "solid", 
        bg = '#F5F5DC', 
        command = lambda: Previous_month(where, year, month)).place(x = 1, y = 0)
    move_right = t.Button(
        where, 
        text = ">", 
        font = "monospace", 
        padx = 69, 
        borderwidth = 1, 
        relief = "solid", 
        bg = '#F5F5DC', 
        command = lambda: Next_month(where, year, month)).place(x = 961, y = 0)
    month_year = t.Label(where, text = f"{Month(month)} {year}", font = "monospace", padx = 345, pady = 5, borderwidth = 1, relief = "solid", bg = '#F5F5DC').place(x = 162, y = 1)

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    _y = 34
    _x = 2
    for i in range (0, 7): #creates names of weekdays
        lab = t.Label(where, text = weekdays[i], font = "monospace", anchor = "center", padx = 60, pady = 2, borderwidth = 1, relief = "solid", bg = '#F5F5DC').place(x = _x, y = _y)
        _x += 160
    first_weekday = d.datetime(year, month, 1).weekday()
    weekday = first_weekday
    _y = 70 #where to place a day on y axis
    _x = 2
    if weekday != 0: # if month doesnt start on Monday
        _x += 160 * weekday

    for i in range (1, c.monthrange(year, month)[1] + 1): # for i in range 1 ... length(month) creates days of a month

        if i <= 9:
            b = t.Button(
                where,
                name=f'abutton{i}',
                text = f"{i}",
                font = "monospace",
                padx = 68,
                pady = 60,
                borderwidth = 1,
                relief = "solid", 
                bg = '#F5F5DC')
            b.config(command = create_set_day(Month(month), i))
            b.place(x = _x, y = _y)

        else: # to make buttons even if nuber of the day requires more then 1 character
            b = t.Button(
                where,
                name=f'abutton{i}', 
                text = f"{i}",
                font = "monospace", 
                padx = 63, 
                pady = 60, 
                borderwidth = 1, 
                relief = "solid",
                bg = '#F5F5DC')
            b.place(x = _x, y = _y)
            b.config(command = create_set_day(Month(month), i))

        Check_task(b, i)

        weekday += 1
        _x += 160

        if weekday == 7:
            weekday = 0
            _x = 2
        if weekday == 0:    
            _y += 150

def Check_task(button, i):
    n = open(f"{users.chosen_name}.json", "r")    
    name_info = json.load(n)
    n.close()  
    _d = str(i)+str(Month(MONTH))+str(YEAR)
    if str(_d) in name_info["tasks"] and str(_d) in name_info["notes"]:
        button.config(bg = "#FFA07A")
        return
    if str(_d) in name_info["tasks"]:
        button.config(bg = "#ADD8E6")
    if str(_d) in name_info["notes"]:
        button.config(bg = "#90EE90")    


def create_set_day(month, day):
    def _Set_day():
        Set_day(month, day)
    return _Set_day

def Month(a): #returns a string instead of month number
    m = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
    return m[a - 1]
    
def Next_month(where, year, month): #moves to next month

    for widget in where.winfo_children():
        widget.destroy()
    
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1    
    Create_month(where, year, month)


def Previous_month(where, year, month): #moves to previous month

    for widget in where.winfo_children():
        widget.destroy()

    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1    
    Create_month(where, year, month)       
    
def Set_day(month, day):
    top = t.Toplevel()
    top.title(f"{month} {day}")
    top.geometry("720x170")
    top.configure(background= "#F5F5DC")

    add_note = t.Button (
        top,
        text = "Add a note", 
        font = "monospace", 
        padx = 118, pady = 20, 
        borderwidth = 1, 
        relief = "solid", 
        bg = '#F5F5DC',
        command = lambda: inf.Add_note(top, day))
    add_note.place(x = 5, y = 10)

    add_task = t.Button(
        top, 
        text = "Add a task", 
        font = "monospace", padx = 118, pady = 20, 
        borderwidth = 1, 
        relief = "solid",
        bg = '#F5F5DC',
        command = lambda: inf.Add_task(top, day))
    add_task.place(x = 365, y = 10)

    show_note = t.Button (
        top,
        text = "Show notes for today", 
        font = "monospace", 
        padx = 69, pady = 20, 
        borderwidth = 1, 
        relief = "solid", 
        bg = '#F5F5DC',
        command = lambda: inf.Show_note(top, day))
    show_note.place(x = 5, y = 90)

    show_task = t.Button (
        top,
        text = "Show tasks for today", 
        font = "monospace", 
        padx = 69, pady = 20, 
        borderwidth = 1, 
        relief = "solid", 
        bg = '#F5F5DC',
        command = lambda: inf.Show_task(top, day))
    show_task.place(x = 365,  y = 90)
