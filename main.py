from tkinter import *

def button_clicked():
    print("got clicked")
    new_text = input.get()
    my_text_label.config(text=new_text)



#Screen-Window

window = Tk()
window.title("GUI with 100 Days Python")
window.minsize(width=500, height=350)


#Label
my_text_label = Label(text="I am a text-it got clicked!", font=("Arial", 25, "bold"))
my_text_label.config(text="new text")
my_text_label.pack()


#Button
button = Button(text="Click", command=button_clicked)




#ENTRY
input = Entry(width=15)
input.pack()
print(input.get())




window.mainloop()