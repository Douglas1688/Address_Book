from tkinter import *

############   ROOT   #################
root = Tk()
root.geometry("550x480")
root.title("Agenda de Contactos")
############  FRAME #1  ################
frame1 = Frame(root)
frame1.place(x=5,y=5)
lblTitle = Label(frame1,text="Address Book",font=("Arial",21),bg="darkblue",fg="white")
lblTitle.grid(column=0,row=0,columnspan=1)


lblsearch_name = Label(frame1,text="Por nombre:",bg="darkblue",fg="white")
lblsearch_name.grid(column=1,row=0,sticky=W)
lblsearch_phone = Label(frame1,text="Por teléfono:",bg="darkblue",fg="white")
lblsearch_phone.grid(column=1,row=1,sticky=EW,rowspan=1)






############  FRAME #2  ################
frame2 = Frame(root)


############  FRAME #3  ################
frame3=Frame(root)


############  FRAME #4  ################
frame4 = Frame(root)


root.mainloop()
