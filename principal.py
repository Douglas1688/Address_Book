from tkinter import *
from tkinter import ttk
from database import *
from tkinter import messagebox

import os
from tkinter import filedialog
import sqlite3
from PIL import Image, ImageTk

def limpiar():
    entryName.delete(0,END)
    entryPhone.delete(0,END)
    entryInfo.delete(0,END)

def add_customer():

    answer = messagebox.askquestion(message="¿Desea continuar?",title="Mensaje de confirmación")
    if answer == "yes":
        name_contact = entryName.get()
        phono_contact = entryPhone.get()
        info_contact =entryInfo.get()
        contact_array =[name_contact,phono_contact,info_contact]
        insertarDB(contact_array)
        select= mostrarDBDesc()
        select = list(select)
        tree.insert("",END,values=select[0])
        limpiar()

def delete_customer():
    idselection = tree.item(tree.selection())['values'][0]
    answer = messagebox.askquestion(message="¿Desea continuar?", title="Mensaje de confirmación")
    if answer == "yes":
        eliminarDato(idselection)
        tree.delete(tree.selection())
        select = mostrarDBDesc()
        select = list(select)
        tree.insert("", END, values=select[0])

def edit_customer():
    idselection = tree.item(tree.selection())['values'][0]
    name_contact = entryName.get()
    phono_contact = entryPhone.get()
    info_contact = entryInfo.get()
    contact_tuple = (name_contact, phono_contact, info_contact,idselection)
    answer = messagebox.askquestion(message="¿Desea continuar?", title="Mensaje de confirmación")
    if answer == "yes":
        editarDato(contact_tuple)
        tree.delete(tree.selection())
        select = mostrarDBDesc()
        select = list(select)
        tree.insert("", END, values=select[0])
        limpiar()

def browserPhoto():
    entryPhoto.delete(0,END)
    filename = filedialog.askopenfilename(initialdir="/",title="Select File")
    entryPhoto.insert(END,filename)

try:
    crearDB()

except:
    print("Base de datos existente")

root = Tk()
root.title("Agenda de Contactos")
root.geometry("550x480")
lblTitle = Label(root,text="Contactos",font=("Arial",21),bg="darkblue",fg="white")
lblTitle.place(x=0,y=0,width=250,height=41)

####################################
lblsearch_name = Label(root,text="Por nombre:",bg="darkblue",fg="white")
lblsearch_name.place(x=250,y=0,width=120)
lblsearch_phone=Label(root,text="Por teléfono",bg="darkblue",fg="white")
entrySearch_name=Entry(root)
entrySearch_name.place(x=380,y=0,width=160)

lblsearch_phone.place(x=250,y=20,width=120)
entrySearch_phone=Entry(root)
entrySearch_phone.place(x=380,y=20,width=160)


###################################
lblName=Label(root,text="Nombre:",bg="black",fg="yellow")
lblName.place(x=2,y=43,width=160)
entryName=Entry(root)
entryName.place(x=165,y=43,width=375)

lblPhone=Label(root,text="Número telefónico:",bg="black",fg="yellow")
lblPhone.place(x=2,y=65,width=160)
entryPhone=Entry(root)
entryPhone.place(x=165,y=65,width=375)

lblPhoto=Label(root,text="Foto:",bg="black",fg="yellow")
lblPhoto.place(x=2,y=87,width=160)
entryPhoto=Entry(root)
entryPhoto.place(x=165,y=87,width=280)
btnPath = Button(root,text="Buscar",bg="darkblue",fg="yellow",command=browserPhoto)
btnPath.place(x=460,y=87,width=80)

lblInfo=Label(root,text="Más información:",bg="black",fg="yellow")
lblInfo.place(x=2,y=109,width=160)
entryInfo=Entry(root)
entryInfo.place(x=165,y=109,width=375)

###########################################################

btnAdd=Button(root,text="Agregar contacto",bg="darkblue",fg="yellow",command=add_customer)
btnAdd.place(x=0,y=140,width=225,height=40)
btnDelete=Button(root,text="Borrar Seleccionado",bg="darkblue",fg="yellow",command=delete_customer)
btnDelete.place(x=0,y=180,width=225,height=40)
btnEdit=Button(root,text="Editar Seleccionado",bg="darkblue",fg="yellow",command=edit_customer)
btnEdit.place(x=0,y=220,width=225,height=40)
btnSort_Name=Button(root,text="Ordenar por Nombre",bg="darkblue",fg="yellow")
btnSort_Name.place(x=0,y=260,width=225,height=40)
btnExit=Button(root,text="Salir",bg="darkblue",fg="yellow",command=quit)
btnExit.place(x=0,y=300,width=225,height=40)

load = Image.open("src/profile.png")
load.thumbnail((150,150))
photo = ImageTk.PhotoImage(load)
lbl_image = Label(root,image=photo)
lbl_image.place(x=10,y=350)






#########################################################


tree = ttk.Treeview(root,columns=(1,2,3,4),height=5,show="headings")
tree.place(x=245,y=140,width=290,height=200)

tree.heading(1,text="ID")
tree.heading(2,text="Nombre")
tree.heading(3,text="Teléfono")
tree.heading(4,text="Información")
tree.column(1,width=5)
tree.column(2,width=50)
tree.column(3,width=50)
tree.column(4,width=50)
#insertarDB()
sel = mostrarDB()
for elem in sel:
    tree.insert("",END,value=elem)



mainloop()