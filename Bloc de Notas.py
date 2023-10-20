from customtkinter import * 
from CTkMenuBar import *
from tkinter import filedialog
from io import *
from CTkMessagebox import * 
from CTkColorPicker import *
from pywinstyles import *
from tkfontchooser import askfont

url_file = ""
title = "Bloc de Notas-2023"
global seleccion
seleccion = False
global n
global x
n = "Arial"
x = 14
#Funciones
def Nuevo():
    global url_file
    if texto.get(1.0,"end-1c") != "":
        Abrir_Guardar = CTkMessagebox(title="Bloc de Notas-2023",
                                        message= "Desea guardar este Documento?",
                                        icon="question",
                                        option_1="Guardar",
                                        option_2= "No Guardar",
                                        option_3="Cancelar",
                                        sound=True
                                        )

        if Abrir_Guardar.get() == "Guardar":
           Guardar()
           texto.delete(1.0,"end")
           ventana.title("Sin Nombre" + " - " + title)

        elif Abrir_Guardar.get() == "No Guardar":
            texto.delete(1.0,"end")
            ventana.title("Sin Nombre" + " - " + title)

        elif Abrir_Guardar.get() == "Cancelar":
            Abrir_Guardar.destroy()

    url_file = ""

global Guard
global NoGuardar
Guard =False
NoGuardar = False

def Abrir():
    global url_file
    url_file = filedialog.askopenfilename(title="Abrir archivo",initialdir='C:',
                                        filetypes=[("Archivos de texto", "*.txt"), 
                                                   ("Todos los archivos", "*.*")])
    if url_file != "":
        with open(url_file, 'r') as file:
            file = open(url_file, 'r')
            contenido = file.read()
            texto.delete(1.0, "end-1c")
            texto.insert('insert', contenido)
            ventana.title(f"{url_file} {title}")

def Guardar():
    global url_file
    if url_file == "":
        GuardarComo()
    else:
        contenido = texto.get(1.0, "end-1c")
        with open(url_file, "w+") as file:
            file.write(contenido)
            ventana.title(f"{url_file} {title}")

def GuardarComo():
    global url_file
    url_file = filedialog.asksaveasfile(initialdir='.',
                                        filetypes=[("Archivos de texto", "*.txt"), 
                                                   ("Todos los archivos", "*.*")], 
                                        title="Guardar como...")
    contenido = texto.get(1.0, "end-1c")
    if url_file not in [None, ""]:
        with open(url_file.name, "w+") as file:
            file.write(contenido)
            ventana.title(f"{url_file.name} {title}")


def Cortar(n):
    global seleccion
    if n:
        seleccion = ventana.clipboard_get()
    else:
        if texto.selection_get():
            seleccion = texto.selection_get()
            texto.delete(1.0,"end-1c")
            ventana.clipboard_clear()
            ventana.clipboard_append(seleccion)

def Copiar(n):
    global seleccion
    if n:
        seleccion = ventana.clipboard_get()
    else:
        if texto.selection_get():
            seleccion = texto.selection_get() 
            ventana.clipboard_clear()
            ventana.clipboard_append(seleccion)

def Pegar(n):
    global seleccion
    if n:
        seleccion = ventana.clipboard_get()
    else:   
        if seleccion:
            posicion = texto.index(INSERT)
            texto.insert(posicion, seleccion)

def Acerca():
    CTkMessagebox(title= "Acerca de...",message="Creado por Yunier Lima Ricardo\nTeléfono: 59738605\nVersión: 1.0",
                    icon="D:\Programas\Python\Aprendiendo\Bloc de Notas\Iconos\info.png",option_1="Aceptar",
                    font=('Arial',20),fg_color="black",
                    text_color="white",bg_color="black",corner_radius=16,
                    border_width=2,border_color="gold",width=450,height=200)
    
def ZoomAumentar():
    global x
    if x < 30:
        x += 3
        texto.configure(font=(n,x))

def ZoomDisminuir():
    global x
    if x > 8:
        x -= 3
        texto.configure(font=(n,x))

def CambiarFondo():
    pick_color = AskColor(title= "Seleccionar color de fondo")
    fondo = pick_color.get()
    texto.configure(fg_color= fondo,bg_color= fondo)
    
def CambiarLetra():
    global n
    global x
    letra = askfont(texto,title= "Seleccionar letra")
    n = letra['family']
    x = letra['size']
    texto.configure(font=(letra['family'],letra['size']))

def deshacer():
    texto.undo()

def rehacer():
    texto.edit_redo()

#Creacion de la ventana
ventana = CTk()
ventana.title("Bloc de Notas-2023")
ventana.geometry("600x400")
ventana.configure(bg="black")


ventana.iconbitmap(r'D:\Programas\Python\Aprendiendo\Bloc de Notas\Iconos\Principal.ico')

ventana.bind('<Control-Key-x>',Cortar)
ventana.bind('<Control-Key-c>',Copiar)
ventana.bind('<Control-Key-v>',Pegar)

#Creacion de la barra de menu
menu = CTkMenuBar(ventana,bg_color="black")

texto = CTkTextbox(ventana,font=(n,x),text_color="white"
                   ,border_color="white",fg_color="black",bg_color="black",
                    scrollbar_button_color="white",scrollbar_button_hover_color="gold")
texto.pack(fill = BOTH,expand= 1)

label = CTkLabel(ventana,text="Creado por: Yunier Lima Ricardo",width=2000,height=30,
                 anchor="w",font=('Comic Sans MS',14),fg_color="black",text_color="white")
label.pack(side="left")

#Creacion de los botones de la barra de menu
boton_1 = menu.add_cascade("Archivo")
boton_2 = menu.add_cascade("Editar")
boton_3 = menu.add_cascade("Opciones")
boton_4 = menu.add_cascade("Ayuda")

#Creacion de dropdown de botones
dropdown_1 = CustomDropdownMenu(widget=boton_1, fg_color="black",text_color="white",
                                font=('Comic Sans MS',13),bg_color="black",hover_color="grey25"
                                ,border_color="gold",border_width= 2,separator_color="gold")
dropdown_1.add_option(option="Nuevo",command=lambda:Nuevo())
dropdown_1.add_option(option="Abrir",command=lambda:Abrir())
dropdown_1.add_option(option="Guardar",command=Guardar)
dropdown_1.add_option(option="Guardar como ...",command=GuardarComo)
dropdown_1.add_separator()
dropdown_1.add_option(option="Salir",command=ventana.quit)

dropdown_2 = CustomDropdownMenu(widget=boton_2,fg_color="black",text_color="white",
                                font=('Comic Sans MS',13),bg_color="black",hover_color="grey25"
                                ,border_color="gold",border_width= 2,separator_color="gold")

dropdown_2.add_option("Deshacer",command=deshacer)
dropdown_2.add_option("Rehacer",command=rehacer)
dropdown_2.add_separator()
dropdown_2.add_option(option="Copiar",command=lambda:Copiar(0))
dropdown_2.add_option(option="Cortar",command=lambda:Cortar(0))
dropdown_2.add_option(option="Pegar",command=lambda:Pegar(0))

dropdown_3 = CustomDropdownMenu(widget=boton_3,fg_color="black",text_color="white",
                                font=('Comic Sans MS',13),bg_color="black",hover_color="grey25"
                                ,border_color="gold",border_width= 2,separator_color="gold"
                                )


subMenu = dropdown_3.add_submenu("Zoom")
subMenu.configure(fg_color="black",bg_color="black",border_width= 2,border_color="gold")
subMenu.add_option("Aumentar",command=lambda:ZoomAumentar())
subMenu.add_option("Disminuir",command=lambda:ZoomDisminuir())
dropdown_3.add_separator()
dropdown_3.add_option("Cambiar Fondo",command=CambiarFondo)
dropdown_3.add_option("Letra",command=CambiarLetra)


dropdown_4 = CustomDropdownMenu(widget=boton_4,fg_color="black",text_color="white",
                                font=('Comic Sans MS',13),bg_color="black",hover_color="grey25"
                                ,border_color="gold",border_width= 2)
dropdown_4.add_option("Acerca de...",command=lambda:Acerca())

ventana.mainloop()