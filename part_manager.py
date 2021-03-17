from tkinter import *

# Create A Window Object
app = Tk()


# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)


# Window Dimensions
app.title('Part Manager')
app.geometry('700x350')


# Start Program
app.mainloop()
