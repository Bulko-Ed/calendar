import calend as c
import users
import json
import tkinter as t
from tkinter import messagebox


def Add_note(top, day):
    date = str(day)+str(c.Month(c.MONTH))+str(c.YEAR) #tuples cant be keys in json, lists cant be keys in dictionaries 
    next_top = t.Toplevel(top)
    next_top.title("Note")
    next_top.geometry("600x100")
    next_top.config(background = "#F5F5CD")
    insert = t.Entry(next_top, width = 50, font = "monospace", borderwidth = 1, bg = '#F5F5DC')
    insert.place(x = 1, y = 1)
    confirm = t.Button(next_top, text = "Confirm", borderwidth = 1, font = "monospace", relief = "solid", bg = '#F5F5DC', command = lambda: Note_added(next_top))
    confirm.place(x = 1, y = 30)

    def Note_added(next_top):
        entry = insert.get()
        next_top.destroy()
        n = open(f"{users.chosen_name}.json", "r")
        name_info = json.load(n)
        n.close()
        if date in name_info["notes"]:
            list = name_info["notes"][date]
            print(list)
            list.append(entry)
            name_info["notes"][date] = list
        else:
            name_info["notes"][date] = [(entry)]
        name_info_j = json.dumps(name_info)
        n = open(f"{users.chosen_name}.json", "w")
        n.write(name_info_j)
        n.close()    
        c.Create_month(c.where, c.YEAR, c.MONTH)



def Add_task(top, day):
    date = str(day)+str(c.Month(c.MONTH))+str(c.YEAR) #tuples cant be keys in json, lists cant be keys in dictionaries 
    next_top = t.Toplevel(top)
    next_top.title("Task")
    next_top.geometry("600x100")
    next_top.configure(background = "#F5F5DC")
    insert = t.Entry(next_top, width = 50, font = "monospace", borderwidth = 1, bg = '#F5F5DC')
    insert.place(x = 1, y = 1)
    confirm = t.Button(next_top, text = "Confirm", borderwidth = 1, font = "monospace", relief = "solid", bg = '#F5F5DC', command = lambda: Task_added(next_top))
    confirm.place(x = 1, y = 30)

    def Task_added(next_top):
        entry = insert.get()
        next_top.destroy()
        n = open(f"{users.chosen_name}.json", "r")
        name_info = json.load(n)
        n.close()
        if date in name_info["tasks"]:
            list = name_info["tasks"][date]
            print(list)
            list.append(entry)
            name_info["tasks"][date] = list
        else:
            name_info["tasks"][date] = [(entry)]
        name_info_j = json.dumps(name_info)
        n = open(f"{users.chosen_name}.json", "w")
        n.write(name_info_j)
        n.close()    
        c.Create_month(c.where, c.YEAR, c.MONTH)


def Show_note(top, day):
    date = str(day)+str(c.Month(c.MONTH))+str(c.YEAR)
    n = open(f"{users.chosen_name}.json", "r")
    name_info = json.load(n)
    n.close()
    if date not in name_info["notes"]:
        messagebox.showinfo(title = "No notes", message = f"{users.chosen_name}, there are not notes for today", bg ='#F5F5DC')
    else:
        next_top = t.Toplevel(top)
        next_top.title("Notes")
        next_top.geometry("600x100")
        next_top.configure(background= "#F5F5DC")
        tasks = name_info["notes"][date]
        _x = 2
        _y = 2
        for i in tasks:
            note = t.Label(next_top, text = i, font = "monospace", anchor = "center", padx = 3, pady = 2, borderwidth = 1, relief = "solid", bg = '#F5F5DC').place(x = _x, y = _y)
            _y += 30
                
def Show_task(top, day):
    date = str(day)+str(c.Month(c.MONTH))+str(c.YEAR)
    n = open(f"{users.chosen_name}.json", "r")
    name_info = json.load(n)
    n.close()
    def create_delete_task(note, text):
        def delete_task():
            print(text)
            #note.contents = t.StringVar(name = "_qqqtext", value = note.text)
            n = open(f"{users.chosen_name}.json", "r")
            name_info = json.load(n)
            n.close()
            task_to_delete = name_info["tasks"][date]
            if len(task_to_delete) == 1:
                del name_info["tasks"][date]
                top.destroy()
            else:
                print(text)
                name_info["tasks"][date].remove(text)
            info_deleted = json.dumps(name_info)   
            n = open(f"{users.chosen_name}.json", "w")
            n.write(info_deleted)
            n.close()
            note.destroy()    
        return delete_task    
     
    if date not in name_info["tasks"]:
        messagebox.showinfo(title = "No tasks", message = f"{users.chosen_name}, there are not tasks for today")
    else:
        next_top = t.Toplevel(top)
        next_top.title("Tasks")
        next_top.geometry("600x100")
        next_top.configure(background= "#F5F5DC")
        tasks = name_info["tasks"][date]
        _x = 2
        _y = 2
        for i in tasks:
            task = t.Checkbutton(next_top, text = i, font = "monospace", anchor = "center", padx = 3, pady = 2, borderwidth = 1, bg = '#F5F5DC', relief = "solid")
            _text = task.cget("text")
            task.config(command = create_delete_task(task, _text))
            task.place(x = _x, y = _y)

            _y += 30


           


