import tkinter as t
from tkinter import messagebox
import json

def Users(where):
    global WHERE
    new = t.Button(
        where, 
        text = "Create new user", 
        font = ("monospace", 25),  
        borderwidth = 1, 
        pady = 25, padx = 20, 
        relief = "solid", 
        bg = '#F5F5DC',
        command = lambda: Create_new(where))
    new.place(x = 120, y = 300)
    choose  = t.Button(
        where, 
        text = "Choose user", 
        font = ("monospace", 25), 
        borderwidth = 1, 
        pady = 25, padx = 40, 
        relief = "solid", 
        bg = '#F5F5DC',
        command = lambda: Show_users(where))
    choose.place(x = 650, y = 300)


def Create_new(where):
    next = t.Toplevel()
    next.geometry("500x100")
    next.title("Enter name")
    next.configure(background='#F5F5DC')
    get_name = t.Entry(next, font = "monospace", width = 30, borderwidth = 1, relief = "solid")
    get_name.place(x = 20, y = 20) # I have to do it separatly, otherwise get_name is a result of a().b() so it has no type

    def NameCreated(next):
        global chosen_name
        entry = get_name.get()
        with open("accounts.json", "r") as acc:
            acc_names = json.load(acc)
        a = acc_names["names"]
        if entry not in a:
            a.append(entry)
            with open("accounts.json", "w") as acc:
                json.dump(acc_names, acc)
            print(acc_names)
            next.destroy()
            for widget in where.winfo_children():
                print(widget)
                widget.destroy()
            new_json = open(f"{entry}.json", "w")
            initialize = {"notes":{}, "tasks":{}}
            initialize_j = json.dumps(initialize)
            new_json.write(initialize_j)
            #tasks = {}
            #tasks_j = json.dumps(tasks)
            #new_json.write(tasks_j)
            new_json.close()    
            where.contents.set(True)
            chosen_name = entry
        else: #if this name already exists, user have to choose another one, or data an be lost
            messagebox.showinfo(title = "warning", message = "this name already exists, please, choose another one")

    

    confirm = t.Button(next, text = "Confirm", borderwidth = 1, font = "monospace", relief = "solid", command = lambda: NameCreated(next), bg = "#F5F5DC")
    confirm.place(x = 30, y = 50)

    #NameCreated(next)    

    #if get_name.get() in users:
     #   messagebox.showinfo(title = "warning", message = "the name already exists, please, choose another one")
    #new = open(f"{get_name.get()}.json", "x")
    #users.append(get_name.get())




def Show_users(where):
    _next = t.Toplevel()
    _next.geometry("300x300")
    _next.title("Choose user")
    _next.configure(background='#F5F5DC')
    names  = t.Listbox(_next, bg="#F5F5DC")
    names.place(x = 10, y = 10)
    with open("accounts.json", "r") as acc:
        acc_names = json.load(acc)
    a = acc_names["names"]
    for name in a:
        names.insert("end", name)
        
    
    def Chosen_user():
        global chosen_name
        chosen_name = names.get("anchor")  
        _next.destroy()
        for widget in where.winfo_children():
            widget.destroy()
        where.contents.set(True)           
    
    confirm = t.Button(_next, text = "Confirm", borderwidth = 1, font = "monospace", relief = "solid", bg = "#F5F5DC", command = lambda: Chosen_user())
    confirm.place(x = 10, y = 220)



