import tkinter as t
import datetime as d
import calend
import users


root = t.Tk()
length = 1120
width = 830
root.title("Calendar")
root.geometry(f'{length}x{width}')
root.configure(background='#F5F5DC')


users.Users(root)
root.contents = t.BooleanVar(name = "ready", value = False)
root.wait_variable(name = "ready")
print(users.chosen_name)
calend.Create_month(root, d.datetime.now().year, d.datetime.now().month)

root.mainloop()






    