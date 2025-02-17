from tkinter import *

window = Tk()
window.config(padx=25,pady=20)

FONT = ('Arial',8)

LABEL1 = Label(text="is equal to")

LABEL1.grid(column=0,row=2)

#input here in miles
entry = Entry(width=15)
entry.grid(column=1,row= 0)
entry.focus()

LABEL2 = Label(text="Miles")
LABEL2.grid(column=2,row= 0)

LABEL3 = Label(text="KM")
LABEL3.grid(column=2,row= 2)

result_label = Label(text="0")
result_label.grid(column=1,row=2 )
def converter():
    result_km = int(entry.get()) * 1.609
    result_label.config(text=f"{round(result_km)}")
button = Button(text="Convert", command=converter)
button.grid(column= 1, row= 3)











window.mainloop()
