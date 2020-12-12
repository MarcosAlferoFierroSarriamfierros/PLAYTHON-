import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os, time
from PIL import ImageTk,Image
from Juegos import *
from Lecciones import *
from Juegoparejas import *
from Juego_Triqui import *
from Webscrapping import *
def pantalla():
    """
    Esta funcion crea la pantalla base de nuestro programa, con sus dimensiones y caracteristicas.
    :No recibe
    :return None
    """
    global pantalla
    pantalla = tk.Tk()
    pantalla.title('Plaython')
    pantalla.resizable(False, False)
    pantalla.geometry('1280x700')
    pantalla.config(bg='blue')
    pantalla.iconbitmap("../recursor/icono.ico")

def cambiar_frame(frame_dest, numero,diccionario):
    """
    Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
    :param string frame_dest: representa el frame que vamos a destruir
    :param string numero: representa el numero de la pantalla que nos encontramos
    :param dict diccionario: Representa el diccionario donde se encuentran nuestros usuarios y sus contraseñas.
    :return None
    """
    frame_dest.destroy()
    if numero==1:
        inicio_plaython(diccionario)
        archivo(diccionario)
    elif numero == 2:
        diccionario=registro(diccionario)
    elif numero==3:
        iniciar_sesion(diccionario)
    elif numero==4:
        usuarios(diccionario)
    elif numero==5:
        menu()
    elif numero==6:
        entrenatucerebromenu()
    elif numero==7:
        vamosaaprender()
    elif numero==8:
        progreso()
    else:
        archivo(diccionario)
        exit()
def juegos(frame,n_juego):
    """
    Esta funcion cambia entre los distintos Frames de los juegos, dando la posibilidad de elegir determinado
     juego segun se clickee un boton.
    :param str frame: Representa determinado Frame que se encuentre en uso
    :param int n_juego: Representa el juego seleccionado segun se clickee
    :return None
    """
    if n_juego==1:
        frame.pack_forget()
        deduccion_gramatical2(pantalla,frame)
    elif n_juego==2:
        pantalla.withdraw()
        JUEGOPAREJAS()
        pantalla.deiconify()
    elif n_juego==3:
        frame.pack_forget()
        adivina_el_num(pantalla,frame)
    elif n_juego==4:
        frame.pack_forget()
        identifica_la_figura2(pantalla,frame)
    elif n_juego==5:
        pantalla.withdraw()
        TRIQUI()
        pantalla.deiconify()
    elif n_juego==6:
        frame.pack_forget()
        organiza_la_oracion(pantalla,frame)
    elif n_juego==7:
        pantalla.withdraw()
        paint()
        pantalla.deiconify()
    elif n_juego==8:
        frame.pack_forget()
        ahorcado_global(pantalla,frame)
def Lecciones(frame,n_leccion):
    """
    Esta funcion cambia entre los distintos Frames de las lecciones, seleccionando determinada leccion
    segun se clickee un boton.
    :param str frame: Representa determinado Frame que se encuentre en uso
    :param int n_juego: Representa el la leccion seleccionada segun se clickee
    :return None
    """
    frame.pack_forget()
    if n_leccion==1:
        leccion_print(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(1)
    if n_leccion==2:
        leccion_variables(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(2)
    if n_leccion==3:
        leccion_de_palabras_reservadas(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(3)
    if n_leccion==4:
        nombres_de_funciones(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(4)
    if n_leccion==5:
        leccion_if(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(5)
    if n_leccion==6:
        leccion_while(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(6)
    if n_leccion==7:
        leccion_break(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(7)
    if n_leccion==8:
        leccion_for(pantalla,frame)
        diccionario[usuario_iniciado][1]+=str(8)
        
def webscra(frame):
    """
    Esta funcion, genera el Frame de nuestro WebScraper, con el cual presenta la informacion
    obtenida de la web.
    :param str frame: Representa determinado Frame que se encuentre en uso
    :return None
    """
    frame.pack_forget()
    global textos_fil
    textos_fil=web_scrapping()
    crearpantallaWS(pantalla,textos_fil,frame)
        
def inicio_plaython(diccionario):
    """
    Esta funcion, crea nuestro primer Frame, en el cual se encuentran caracteristicas de nuestro programa
    como el login, el registro y otros.
    :param dict diccionario: Representa el diccionario donde se encuentran nuestros usuarios y sus contraseñas.
    :return None
    """
    Frame_1 = Canvas(pantalla, width="1280", height="700")
    Frame_1.pack(expand=True, fill="both")
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='700')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")
    imagen0=tk.PhotoImage(file='../recursor/Registro.png')
    boton0 = tk.Button(Frame_1, image=imagen0, bg='#8EB7F3',fg='white',command=lambda:cambiar_frame(Frame_1, 2,diccionario)).place(x=700,y=60)
    imagen1 = tk.PhotoImage(file='../recursor/login1.png')
    boton1 = tk.Button(Frame_1, image=imagen1, bg='#8EB7F3',fg='white',command=lambda:cambiar_frame(Frame_1, 3,diccionario)).place(x=700, y=210)
    imagen2 = tk.PhotoImage(file='../recursor/Usuarios.png')
    boton2 = tk.Button(Frame_1, text="Usuarios", image=imagen2, bg='#8EB7F3',fg='white',command=lambda:cambiar_frame(Frame_1, 4,diccionario)).place(x=700, y=360)
    imagen3 = tk.PhotoImage(file='../recursor/Salir.png')
    boton3 = tk.Button(Frame_1, image=imagen3, bg='#8EB7F3',fg='white',command=lambda:cambiar_frame(Frame_1,0,diccionario)).place(x=700, y=510)
    img = ImageTk.PhotoImage(Image.open("../recursor/playthoninicio1.png"))
    Frame_1.background = img
    bg = Frame_1.create_image(125, 0, anchor=tk.NW, image=img)
    pantalla.mainloop()


def registro(diccionario):
    """
    Esta funcion, crea el Frame de nuestro registro a la base de datos.
    :param dict diccionario: Representa el diccionario donde se encuentran nuestros usuarios y sus contraseñas.
    :return None
    """
    Frame_2 = Canvas(pantalla, width="1280", height="700")
    Frame_2.pack(expand=True, fill="both")
    Frame_2.config(bg='#87CEFA')
    Frame_2.config(width='1280', height='700')
    Frame_2.config(bd=20)
    Frame_2.config(relief="groove")
    botonaretroceso = tk.Button(Frame_2, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_2,1,diccionario)).place(x=60, y=580)
    img = ImageTk.PhotoImage(Image.open("../recursor/Registro00.png"))
    Frame_2.background = img
    bg = Frame_2.create_image(125,20, anchor=tk.NW, image=img)
    resp_1_get = StringVar()
    respuesta_1 =  Entry(Frame_2, width = 20, font = ("Comic Sans", 30),textvariable = resp_1_get).place(x=750,y=245)
    resp_2_get = StringVar()
    respuesta_2 =  Entry(Frame_2, width = 20, font = ("Comic Sans", 30),textvariable = resp_2_get).place(x=750,y=430)
    boton_si_no_1 = tk.Button(Frame_2, text="Comprueba", font=("Comic Sans", 15), height=1, width=15, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_1_get,resp_2_get,diccionario)).place(x=900, y=540)
    def comprobar(resp_1_get,resp_2_get,diccionario):
        """
        Esta funcion, guarda los datos de los usuarios en base, si cumplen determinadas condiciones
        :param str resp_1_get: Representa el nombre del usuario
        :param str resp_2_get: Representa la contraseña del usuario
        :param dict diccionario: Representa un diccionario que almacena los nombres y contraseñas de usuarios
        :return diccionario
        """
        if resp_1_get.get() in diccionario :
                messagebox.showwarning('ERROR', 'Ya existe este usuario')
        elif resp_1_get.get()==resp_2_get.get():
                messagebox.showwarning('ERROR', 'No es posible usar el mismo nombre de usuario como contraseña')
        elif len(resp_1_get.get())<4 or len(resp_2_get.get())<4:
            messagebox.showwarning('ERROR', 'El usuario o la contraseña es demasiado corta')

        else:
            diccionario[resp_1_get.get()] = [resp_2_get.get()]
            diccionario[resp_1_get.get()].append(str(0))
            messagebox.showinfo('Muy bien :D', 'Registro Exitoso')
            return diccionario


def iniciar_sesion(diccionario):
    """
    Esta funcion crea nuestro Frame del inicio de sesion.
    :param dict diccionario: Representa el diccionario donde se encuentran almacenados los nombres y contraseñas
    de los usuarios.
    :return None
    """
    Frame_3 = Canvas(pantalla, width="1280", height="700")
    Frame_3.pack(expand=True, fill="both")
    Frame_3.config(bg='#87CEFA')
    Frame_3.config(width='1280', height='700')
    Frame_3.config(bd=20)
    Frame_3.config(relief="groove")
    botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 1, diccionario)).place(x=60, y=580)
    img = ImageTk.PhotoImage(Image.open("../recursor/Registro1.png"))
    Frame_3.background = img
    bg = Frame_3.create_image(125, 20, anchor=tk.NW, image=img)
    resp_1_get = StringVar()
    respuesta_1 = Entry(Frame_3, width=20, font=("Comic Sans", 30), textvariable=resp_1_get).place(x=750, y=245)
    resp_2_get = StringVar()
    respuesta_2 = Entry(Frame_3, width=20, font=("Comic Sans", 30), textvariable=resp_2_get).place(x=750, y=430)
    boton_si_no_1 = tk.Button(Frame_3, text="Comprueba", font=("Comic Sans", 15), height=1, width=15, bg='#8EB7F3',fg='white', command=lambda: comprobar(resp_1_get, resp_2_get, diccionario)).place(x=900,y=540)
    def comprobar(resp_1_get, resp_2_get, diccionario):
        """
        Esta funcion, evidencia si el usuario ingreso los datos correctamente a la hora de ingresar.
        :param str resp_1_get: Representa el nombre de usuario ingresado
        :param str resp_2_get: Representa la contraseña del usuario ingresado.
        :param dict diccionario:Representa el diccionario donde se encuentran almacenados los nombres y contraseñas
        :return None
        """
        global usuario_iniciado
        usuario_iniciado=resp_1_get.get()
        if diccionario.get(usuario_iniciado)==None:
            messagebox.showwarning('ERROR', 'Usuario no registrado')
        else:
            contra=resp_2_get.get()
            if diccionario.get(usuario_iniciado)[0]==contra:
                messagebox.showinfo('Muy bien :D', 'Contraseña ingresada correctamente')
                cambiar_frame(Frame_3,5,diccionario)
            else:
                messagebox.showwarning('ERROR', 'Ingresaste mal la contraseña')


def usuarios(diccionario):
    """
    Esta funcion, presenta los usuarios de nuestro programa y sus contraseñas.
    :param dict diccionario: Representa el duccionario en el que se encuentran almacenados los nombres de usuarios
    y sus contraseñas
    :return None
    """
    Frame_4 = Canvas(pantalla, width="1280", height="700")
    Frame_4.pack()
    Frame_4.config(bg='#87CEFA')
    Frame_4.config(width='1280', height='700')
    Frame_4.config(bd=20)
    Frame_4.config(relief="groove")
    img = ImageTk.PhotoImage(Image.open("../recursor/Usuarios1.png"))
    Frame_4.background = img
    bg = Frame_4.create_image(300,30, anchor=tk.NW, image=img)
    botonaretroceso = tk.Button(Frame_4, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_4, 1, diccionario)).place(x=60, y=580)
    Texto0 = tk.Label(Frame_4, text="USUARIO : CONTRASEÑA", font=('Comic Sans', 20,"bold"), bg='#87CEFA', fg='white').place(relx=0.40, y=205)
    i=265
    for u in diccionario:
        usuario=tk.Label(Frame_4,text=u,font=('Comic Sans',20),bg='#87CEFA',fg='white').place(relx=0.42, y=i)
        a=diccionario[u][0]
        contra=tk.Label(Frame_4,text=a,font=('Comic Sans',20),bg='#87CEFA',fg='white').place(relx=0.52, y=i)
        i+=45
def progreso():
    """
    Esta funcion representa al Frame que muestra el progreso del usuario en las lecciones
    :param None
    :return None
    """
    Frame_8 = Canvas(pantalla, width="1280", height="700")
    Frame_8.pack()
    Frame_8.config(bg='#87CEFA')
    Frame_8.config(width='1280', height='700')
    Frame_8.config(bd=20)
    Frame_8.config(relief="groove")
    img = ImageTk.PhotoImage(Image.open("../recursor/MIPROGRESO00.png"))
    Frame_8.background = img
    bg = Frame_8.create_image(50, 0, anchor=tk.NW, image=img)
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Azul.Horizontal.TProgressbar',background='#8EB7F3')
    bar1=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '1' in diccionario[usuario_iniciado][1]:
        bar1['value']=400
    else:
        bar1['value']=0
    bar1.place(relx=0.5,y=165)
    bar2=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '2' in diccionario[usuario_iniciado][1]:
        bar2['value']=400
    else:
        bar2['value']=0
    bar2.place(relx=0.5,y=225)
    bar3=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '3' in diccionario[usuario_iniciado][1]:
        bar3['value']=400
    else:
        bar3['value']=0
    bar3.place(relx=0.5,y=295)
    bar4=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '4' in diccionario[usuario_iniciado][1]:
        bar4['value']=400
    else:
        bar4['value']=0
    bar4.place(relx=0.5,y=365)
    bar5=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '5' in diccionario[usuario_iniciado][1]:
        bar5['value']=400
    else:
        bar5['value']=0
    bar5.place(relx=0.5,y=435)
    bar6=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '6' in diccionario[usuario_iniciado][1]:
        bar6['value']=400
    else:
        bar6['value']=0
    bar6.place(relx=0.5,y=495)
    bar7=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '7' in diccionario[usuario_iniciado][1]:
        bar7['value']=400
    else:
        bar7['value']=0
    bar7.place(relx=0.5,y=560)
    bar8=Progressbar(Frame_8,length=400,style='Azul.Horizontal.TProgressbar')
    if '8' in diccionario[usuario_iniciado][1]:
        bar8['value']=400
    else:
        bar8['value']=0
    bar8.place(relx=0.5,y=630)
    botonaretroceso = tk.Button(Frame_8, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_8, 5,diccionario)).place(x=60, y=580)
    
def menu():
    """
    Esta funcion representa al Frame que se genera luego de haber ingresado. En este podemos evidenciar
    la seleccion a las diferentes funciones de nuestro programa.
    :param None
    :return None
    """
    Frame_5 = Canvas(pantalla, width="1280", height="700")
    Frame_5.pack()
    Frame_5.config(bg='#87CEFA')
    Frame_5.config(width='1280', height='700')
    Frame_5.config(bd=20)
    Frame_5.config(relief="groove")
    img = ImageTk.PhotoImage(Image.open("Imagenes/Opcion0.png"))
    Frame_5.background = img
    bg = Frame_5.create_image(365, 45, anchor=tk.NW, image=img)
    img0 = ImageTk.PhotoImage(Image.open("../recursor/Entrenatucerebro.png"))
    img1 = ImageTk.PhotoImage(Image.open("../recursor/Vamosaaprender.png"))
    img2 = ImageTk.PhotoImage(Image.open("../recursor/Ponteaprueba.png"))
    img3 = ImageTk.PhotoImage(Image.open("../recursor/Liberatucreatividad.png"))
    img4 = ImageTk.PhotoImage(Image.open("../recursor/InstalarPython.png"))
    img5 = ImageTk.PhotoImage(Image.open("../recursor/Miprogreso.png"))
    boton0 = Button(Frame_5, image=img0, bg='#8EB7F3', fg='white',command=lambda:cambiar_frame(Frame_5, 6,diccionario)).place(x=120,y=200)
    boton1 = Button(Frame_5, image=img1, bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_5, 7, diccionario)).place(x=670, y=200)
    boton2 = Button(Frame_5, image=img2, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_5,8)).place(x=120, y=400)
    boton3 = Button(Frame_5, image=img3, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_5,7)).place(x=670, y=400)
    boton4 = Button(Frame_5, image=img4, bg='#596EFF', fg='white',command=lambda: webscra(Frame_5)).place(x=945, y=560)
    boton5 = Button(Frame_5, image=img5, bg='#954DFF', fg='white',command=lambda: cambiar_frame(Frame_5, 8,diccionario)).place(x=670, y=560)
    botonaretroceso = tk.Button(Frame_5, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_5, 1,diccionario)).place(x=60, y=580)
    pantalla.mainloop()
def vamosaaprender():
    """
    Esta funcion representa al Frame que se genera para la seccion de vamos a aprender, dandole la posibilidad al usuario
    de ir a las actividades planteadas para esta seccion.
    :param None
    :return None
    """
    Frame_7 = Canvas(pantalla, width="1280", height="700")
    Frame_7.pack()
    Frame_7.config(bg='#87CEFA')
    Frame_7.config(width='1280', height='700')
    Frame_7.config(bd=20)
    Frame_7.config(relief="groove")
    img = ImageTk.PhotoImage(Image.open("Imagenes/Op2.png"))
    Frame_7.background = img
    bg = Frame_7.create_image(365, 45, anchor=tk.NW, image=img)
    img0 = ImageTk.PhotoImage(Image.open("../recursor/Imprimir.png"))
    img1 = ImageTk.PhotoImage(Image.open("../recursor/Variables.png"))
    img2 = ImageTk.PhotoImage(Image.open("../recursor/Palabrasreservadas.png"))
    img3 = ImageTk.PhotoImage(Image.open("../recursor/Nombredefunciones.png"))
    img4 = ImageTk.PhotoImage(Image.open("../recursor/LeccionIF.png"))
    img5 = ImageTk.PhotoImage(Image.open("../recursor/LeccionMientras.png"))
    img6 = ImageTk.PhotoImage(Image.open("../recursor/LeccionBREAK.png"))
    img7 = ImageTk.PhotoImage(Image.open("../recursor/LeccionFOR.png"))
    boton0 = Button(Frame_7, image=img0, bg='#8EB7F3', fg='white',command=lambda:Lecciones(Frame_7,1)).place(x=160,y=200)
    boton1 = Button(Frame_7, image=img1, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,2)).place(x=410, y=200)
    boton2 = Button(Frame_7, image=img2, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,3)).place(x=660, y=200)
    boton3 = Button(Frame_7, image=img3, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,4)).place(x=910, y=200)
    boton4 = Button(Frame_7, image=img4, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,5)).place(x=160, y=400)
    boton5 = Button(Frame_7, image=img5, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,6)).place(x=410, y=400)
    boton6 = Button(Frame_7, image=img6, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,7)).place(x=660, y=400)
    boton7 = Button(Frame_7, image=img7, bg='#8EB7F3', fg='white',command=lambda: Lecciones(Frame_7,8)).place(x=910, y=400)
    botonaretroceso = tk.Button(Frame_7, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_7, 5, diccionario)).place(x=60, y=580)
    pantalla.mainloop()

def entrenatucerebromenu():
    """
    Esta funcion representa al Frame que se genera para la seccion de entrena tu cerebro, dandole la posibilidad al usuario
    de ir a las actividades planteadas para esta seccion.
    :param None
    :return None
    """
    Frame_6 = Canvas(pantalla, width="1280", height="700")
    Frame_6.pack()
    Frame_6.config(bg='#87CEFA')
    Frame_6.config(width='1280', height='700')
    Frame_6.config(bd=20)
    Frame_6.config(relief="groove")
    img = ImageTk.PhotoImage(Image.open("Imagenes/Op1.png"))
    Frame_6.background = img
    bg = Frame_6.create_image(365, 45, anchor=tk.NW, image=img)
    img0 = ImageTk.PhotoImage(Image.open("../recursor/Deducciongramatical.png"))
    img1 = ImageTk.PhotoImage(Image.open("../recursor/Encuentralasparejas.png"))
    img2 = ImageTk.PhotoImage(Image.open("../recursor/Adivinaelnumero.png"))
    img3 = ImageTk.PhotoImage(Image.open("../recursor/Identificalafigura.png"))
    img4 = ImageTk.PhotoImage(Image.open("../recursor/Triqui.png"))
    img5 = ImageTk.PhotoImage(Image.open("../recursor/Organizalahoracion.png"))
    boton0 = Button(Frame_6, image=img0, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_6,1)).place(x=120,y=200)
    boton1 = Button(Frame_6, image=img1, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_6,2)).place(x=480, y=200)
    boton2 = Button(Frame_6, image=img2, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_6,3)).place(x=840, y=200)
    boton3 = Button(Frame_6, image=img3, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_6,4)).place(x=120, y=400)
    boton4 = Button(Frame_6, image=img4, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_6,5)).place(x=480, y=400)
    boton5 = Button(Frame_6, image=img5, bg='#8EB7F3', fg='white',command=lambda: juegos(Frame_6,6)).place(x=840, y=400)
    botonaretroceso = tk.Button(Frame_6, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_6, 5, diccionario)).place(x=60, y=580)
    pantalla.mainloop()
def d_doc():
  """
  Esta funcion crea escribe en un archivo determinado, los datos de ingreso de los usuarios (nombre y contraseña), y
  los almacena ordenandamente.
  :param None
  :return diccionario
  """
  diccionario={}
  doc=open('login.csv','a+')
  doc.seek(0)
  while True:
    a=doc.readline()
    a=a[:-1]
    if a=='':
      break
    lista=a.split(',',1)
    if lista[0]=='Usuario':
      continue
    dat=lista[1].split(',',1)
    dat[0]=dat[0][2:-1]
    dat[1]=dat[1][2:-2]
    diccionario[lista[0]]=dat
  doc.close()
  return diccionario

def archivo(diccionario):
  """
  Esta funcion guarda en un archivo especifico, cada uno de los usuarios con sus contraseñas
  :param dict diccionario: Se refiere al diccionario de nuestro programa, que almacena nombres y contraseñas.
  :return None
  """
  doc=open('login.csv','w')
  doc.write('Usuario,Datos\n')
  for usuario,clave in sorted(diccionario.items()):
    doc.write('{},{}\n'.format(usuario,clave))
  doc.close()

def main():
    """
    Funcion principal de nuestro programa, comienza con la ejecucion de todos los procesos.
    :param None
    :return None
    """
    global diccionario
    diccionario = d_doc()
    pantalla()
    inicio_plaython(diccionario)
main()
