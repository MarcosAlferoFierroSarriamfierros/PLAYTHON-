import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from keyword import iskeyword, kwlist
import random
def leccion_break(pantalla,frameant):
    """
    Inicia la leccion de la sentencia break
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
    :param tkinter.Canvas pantalla: es donde unicaremos los frames de esta lección y demas items
    :return None
    """
    Frame_1 = tk.Frame()
    Frame_1.pack()
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='720')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")

    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        else:
            frameant.pack()

    Texto_Titulo=Label(Frame_1,text = 'Bienvenido a la lección de:', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(relx=0.5,y=150,anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='Break', bg='#87CEFA', fg='white',font=('Comic Sans', 60,"bold")).place(relx=0.5, y=300, anchor=CENTER)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_1, 2,frameant)).place(relx=0.5, y=500, anchor=CENTER)

    def Segundo_Frame(frameant):
        """
        Tiene la funcion de crear el segundo frame de esta leccion (break)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_2 = Canvas(pantalla, width="1280", height="700")
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/pensar.png").resize((200,200)))
        Frame_2.background = img
        bg = Frame_2.create_image(160,350, anchor=tk.NW, image=img)
        Text_titulo_frame_2 = Label(Frame_2,text='LA SENTENCIA BREAK',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='En diversos algoritmos a veces necesitamos cambiar el flujo de un ciclo.\nLa sentencia break permite romper el ciclo antes de que termine,haciendo\nuso de la sentencia mas una condición dentro del ciclo.',
                              bg='#87CEFA', fg='white', font=('Comic Sans', 26)).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Estructura:', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=270, anchor=CENTER)
        Texto_frame_2_ejemplo = Label(Frame_2,text='ciclo:\n\tif condicion:\n\tbreak',bg='#87CEFA', fg='white', font=('Comic Sans', 26,"bold"))
        Texto_frame_2_ejemplo.place(relx=0.4, y=350,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Escribelo tu', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.4, y=430, anchor=CENTER)
        resp_u_get = StringVar()
        respuesta_1 =  Entry(pantalla, width = 20, font = ("Comic Sans", 26),textvariable = resp_u_get).place(relx=0.5, y=500, anchor=CENTER)
        boton_si_no_1 = tk.Button(pantalla, text="Vamos", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_u_get,Texto_frame_2_ejemplo )).place(x=850, y=480)
        def comprobar(resp_u_get,Texto_frame_2_ejemplo ):
            """
            Tiene la funcion de verificar la respuesta del usuario
            :param string resp_u_get: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
            :param Tkinter.Label Texto_frame_2_ejemplo: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
            :return None
            """
            res_u=resp_u_get.get()
            resp_en_p='ciclo:\n\tif condicion:\n\t'+res_u
            Texto_frame_2_ejemplo['text']=resp_en_p
            if res_u=='break':
                messagebox.showinfo('Muy bien', 'Felicidades,ya puedes utilizar break en tus codigos')
                botonfin = tk.Button(Frame_2, text="FIN", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 0,frameant)).place(x=1090,y=580)
            else:
                messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')
def leccion_if(pantalla,frameant):
    """
    Inicia la leccion de la sentencia if
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
    :param tkinter.Canvas pantalla: es donde unicaremos los frames de esta lección y demas items
    :return None
    """
    Frame_1 = tk.Frame()
    Frame_1.pack()
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='720')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")

    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        elif numero==5:
            Quinto_Frame(frameant)
        else:
            frameant.pack()
            
    Texto_Titulo=Label(Frame_1,text = 'Bienvenido a la lección de:', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(relx=0.5,y=150,anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='If', bg='#87CEFA', fg='white',font=('Comic Sans', 60,"bold")).place(relx=0.5, y=300, anchor=CENTER)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_1, 2,frameant)).place(relx=0.5, y=500, anchor=CENTER)

    def Segundo_Frame(frameant):
        """
        Tiene la funcion de crear el segundo frame de esta leccion (if)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_2 = Canvas(pantalla, width="1280", height="700")
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/If.png").resize((200,200)))
        Frame_2.background = img
        bg = Frame_2.create_image(160,350, anchor=tk.NW, image=img)
        Text_titulo_frame_2 = Label(Frame_2,text='LA SENTENCIA IF',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='En ocasiones para nuestro codigo necesitamos verificar ciertas condiciones\ny apartir de eso transformar el comportamiento del algoritmo.', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text='¿Como lo hacemos?',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='La sentencia "if" permite hacer esto,de modo que podemos establecer dos caminos\nuno en el cual la condicion es verdadera y otro donde es falsa.',
                              bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(relx=0.5, y=260, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text='Por ejemplo:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.4, y=340, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text='Coloca un numero',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=380, anchor=CENTER)
        resp_1_get = StringVar()
        respuesta_1 =  Entry(pantalla, width = 20, font = ("Comic Sans", 26),textvariable = resp_1_get).place(relx=0.5, y=450, anchor=CENTER)
        boton_enviar = tk.Button(pantalla, text="Enviar", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:enviar(resp_1_get)).place(x=850, y=430)

        def enviar(resp_1_get):
            """
            Tiene la funcion de revisar la respuesta del usuario y mostrar en pantalla la respuesta
            :param string resp_1_get: representa las respuesta del usuario
            :return None
            """
            palabra=resp_1_get.get()
            Text0_frame_2 = Label(Frame_2,text='Una condición seria:¿tu número es 5?',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=500, anchor=CENTER)
            try:
                palabra=int(palabra)
                if palabra==5:
                    Text0_frame_2 = Label(Frame_2,text='Listo, la condición tomo el camino verdadero, al ser tu número el 5.',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=560, anchor=CENTER)
                else:
                    Text0_frame_2 = Label(Frame_2,text=("La condición tomo el camino falso,al no ser {} el numero 5".format(palabra)),bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=560, anchor=CENTER)
            except:
                messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')

            boton1 = tk.Button(Frame_2, text="Siguiente", font=("comicsansms", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 3,frameant)).place(x=1090,y=580)

    def Tercer_Frame(frameant):
        """
        Tiene la funcion de crear el tercer frame de esta leccion (if)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_3 = Canvas(pantalla, width="1280", height="700")
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='LA SENTENCIA IF',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='La sentencia se escribe asi:', bg='#87CEFA', fg='white', font=('Comic Sans', 26)).place(relx=0.5, y=140, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3,text='if (tu condición):',bg='#87CEFA', fg='white', font=('Comic Sans', 26,"bold")).place(relx=0.5, y=200,anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='Intentalo tu siguiendo la estructura y con esta condicion: 20>17.', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(relx=0.5, y=290, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("comicsansms", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2, frameant)).place(x=20, y=580)
        resp_u_get = StringVar()
        respuesta_1 =  Entry(pantalla, width = 20, font = ("Comic Sans", 26),textvariable = resp_u_get).place(relx=0.5, y=450, anchor=CENTER)
        boton_si_no_1 = tk.Button(pantalla, text="Vamos", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_u_get)).place(x=850, y=430)
        def comprobar(resp_u_get):
            """
            Tiene la funcion de verificar la respuesta del usuario
            :param string resp_u_get: representa las respuesta del usuario
            :return None
            """
            res_u=resp_u_get.get()
            if 'f' in res_u and ':' in res_u:
                for i in range(len(res_u)):
                    if res_u[i]=="f":
                        p1=i
                    elif res_u[i]==":":
                        p2=i
                cadena_1='if'+res_u[p1+1:p2]+':'
                cadena_2='if 20>17:'
                if cadena_1==res_u:
                    if cadena_2==res_u:
                        messagebox.showinfo('Muy bien', 'Felicidades')
                        botonavance = tk.Button(Frame_3, text="Siguiente", font=("comicsansms", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_3, 4,frameant)).place(x=1090,y=580)
                        img2 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/happy.png").resize((200,200)))
                        Frame_3.background = img2
                        bg = Frame_3.create_image(200,350, anchor=tk.NW, image=img2)
                    else:
                        messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')
                else:
                    messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')
            else:
                messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')

    def Cuarto_Frame(frameant):
        """
        Tiene la funcion de crear el cuarto frame de esta leccion (if)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_4 = tk.Frame()
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        Text_titulo_frame_4 = Label(Frame_4,text='LA SENTENCIA IF',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Las instrucciones que siguen luego del if se llaman\nun "bloque" y tienen un espacio a la izquierda.', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=140, anchor=CENTER)
        Text_titulo_frame_4 = Label(Frame_4,text='if (tu condición)\n\tinstrucción:',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=240,anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Para el camino donde la condición es falsa se coloca:', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=325, anchor=CENTER)
        Text_titulo_frame_4 = Label(Frame_4,text='else:',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.43, y=370,anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Escribelo tu', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.4, y=430, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_4, text="Atras", font=("comicsansms", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 3,frameant)).place(x=20, y=580)
        resp_u_get = StringVar()
        respuesta_1 =  Entry(pantalla, width = 20, font = ("Comic Sans", 26),textvariable = resp_u_get).place(relx=0.5, y=500, anchor=CENTER)
        boton_si_no_1 = tk.Button(pantalla, text="Vamos", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_u_get)).place(x=850, y=480)
        def comprobar(resp_u_get):
            """
            Tiene la funcion de verificar la respuesta del usuario
            :param string resp_u_get: representa las respuesta del usuario
            :return None
            """
            res_u2=resp_u_get.get()
            if res_u2=='else:':
                messagebox.showinfo('Muy bien', 'Felicidades')
                Text0_frame_4 = Label(Frame_4, text='No es obligatorio utilizar "else" sino es necesario.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=560, anchor=CENTER)
                botonavance = tk.Button(Frame_4, text="Siguiente", font=("comicsansms", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_4, 5,frameant)).place(x=1090,y=580)
            else:
                messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')

    def Quinto_Frame(frameant):
        """
        Tiene la funcion de crear el quinto frame de esta leccion (if)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_5 = Canvas(pantalla, width="1280", height="700")
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        Text_titulo_frame_5 = Label(Frame_5,text='LA SENTENCIA IF\nDATO EXTRA',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text='¿Que sucede si queremos colocar una condición extra?\nPuedes poner otro if debajo del anterior,pero\npython te proporciona la opción de hacer lo mismo',
                              bg='#87CEFA', fg='white', font=('Comic Sans', 26)).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text='mediante la seguiente sentencia:', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=290, anchor=CENTER)
        Text_titulo_frame_5 = Label(Frame_5,text='elif:',bg='#87CEFA', fg='white', font=('Comic Sans', 26,"bold")).place(relx=0.5, y=340,anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text='Escribelo tu', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.4, y=380, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("comicsansms", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_5, 4,frameant)).place(x=20, y=580)
        resp_u_get = StringVar()
        respuesta_1 =  Entry(pantalla, width = 20, font = ("Comic Sans", 26),textvariable = resp_u_get).place(relx=0.5, y=450, anchor=CENTER)
        boton_si_no_1 = tk.Button(pantalla, text="Vamos", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_u_get)).place(x=850, y=430)
        def comprobar(resp_u_get):
            """
            Tiene la funcion de verificar la respuesta del usuario
            :param string resp_u_get: representa las respuesta del usuario
            :return None
            """
            res_u3=resp_u_get.get()
            if res_u3=='elif:':
                messagebox.showinfo('Muy bien', 'Lección terminada,¡YA SABES UTILIZAR LA SENTENCIA IF!')
                img2 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/ganador.png").resize((200,200)))
                Frame_5.background = img2
                bg = Frame_5.create_image(200,350, anchor=tk.NW, image=img2)
                botonfin = tk.Button(Frame_5, text="FIN", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_5, 0,frameant)).place(x=1090,y=580)
            else:
                messagebox.showwarning('ERROR','Ingresaste mal los datos, intenta nuevamente')

def leccion_print(pantalla,frameant):
    """
    Tiene la funcion de generar la primera leccion, acerca del imprimir o print.
    :param tkinter.Canvas pantalla: Se refiere a nuestra pantalla diseñada por medio de la libreria Tkinter.
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
    :return None
    """
    Frame_1 = Canvas(pantalla,width="1280",height="700")
    Frame_1.pack(expand=True,fill="both")
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='700')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")
    def cambiar_frameprint(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        else:
            frameant.pack()
    Texto_Titulo=Label(Frame_1,text = 'Bienvenido a la lección de:', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(relx=0.5,y=150,anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='Imprimir o print ', bg='#87CEFA', fg='white',font=('Comic Sans', 50,"bold")).place(relx=0.5, y=300, anchor=CENTER)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frameprint(Frame_1, 2,frameant)).place(relx=0.5, y=500, anchor=CENTER)
    def Segundo_Frame(frameant):
        """
        Tiene la funcion de llamar al segundo Frame de nuestra leccion (Imprimir)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_2 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        Text_titulo_frame_2 = Label(Frame_2,text='LA SENTENCIA PRINT',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='En resumidas cuentas, la sentencia print nos sirve para imprimir un mensaje por pantalla.', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text='Esto se hace de la siguiente forma: ',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='print("Tu mensaje") ', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(relx=0.5, y=260, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Esto lo podriamos ver en el siguiente ejemplo, en el cual imprimimos por pantalla la frase "Hello World" ', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx=0.5, y=350, anchor=CENTER)
        boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frameprint(Frame_2, 3,frameant)).place(x=1090,y=580)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/Impresion.png"))
        Frame_2.background = img
        bg = Frame_2.create_image(230,290, anchor=tk.NW, image=img)
    def Tercer_Frame(frameant):
        """
        Tiene la funcion de llamar al tercer Frame de nuestra leccion (Imprimir)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_3 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='LA SENTENCIA PRINT',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='Ahora, intentalo tu!', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3,text='Imprime un mensaje por pantalla, usando esta sintaxis:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='TIP: Recuerda escribir comillas si es una cadena o sin comillas si es un dato entero o flotante") ', bg='#87CEFA', fg='white',font=('Comic Sans', 15,"bold")).place(relx=0.5, y=290, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='print("Tu mensaje") ', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=230, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frameprint(Frame_3, 2,frameant)).place(x=60, y=580)
        resp_1_get = StringVar()
        respuesta_1 =  Entry(Frame_3, width = 20, font = ("Comic Sans", 26),textvariable = resp_1_get).place(relx=0.5, y=450, anchor=CENTER)
        boton_si_no_1 = tk.Button(Frame_3, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_1_get)).place(x=850, y=430)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/question.png").resize((150,150)))
        Frame_3.background = img
        bg = Frame_3.create_image(220,360, anchor=tk.NW, image=img)
        def comprobar(resp_1_get):
            """
            Esta funcion comprueba si se realizo la instruccion de imprimir de una manera correcta.
            :param tkinter.StringVar resp_1_get: Representa la respuesta obtenida por medio de la entrada.
            :return None
            """
            try:
                cont,cont2=0,0
                palabra=resp_1_get.get()
                for i in range (len(palabra)):
                    if palabra[i] == "(":
                        valor = i
                    if palabra[i] == ")":
                        valor2 = i
                    if palabra[i]=="'" or palabra[i]=='"':
                        cont+=1
                    if palabra[i]==".":
                        cont2+=1
                imprimir = "print('"
                cerrar = "')"
                if palabra == (imprimir + (palabra[valor + 2:valor2 - 1]) + cerrar) and (type(palabra)==str):
                    messagebox.showinfo('Muy bien :D', 'Imprimiste por pantalla: ' + str(palabra[valor + 2:valor2 - 1]))
                    botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frameprint(Frame_3, 4,frameant)).place(x=1090, y=580)
                elif palabra == ('print("' + (palabra[valor + 2:valor2 - 1]) +'")') and (type(palabra)==str):
                    messagebox.showinfo('Muy bien :D', 'Imprimiste por pantalla: '+str(palabra[valor + 2:valor2 - 1]))
                    botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frameprint(Frame_3, 4,frameant)).place(x=1090, y=580)
                elif palabra == ("print(" + (palabra[valor+1:valor2]) +")") and cont==0:
                    try:
                        if cont2>0:
                            valor0=float(palabra[valor+1:valor2])
                        else:
                            valor0=int(palabra[valor+1:valor2])
                        messagebox.showinfo('Muy bien :D', 'Imprimiste por pantalla: ' + str(palabra[valor + 1:valor2]))
                        botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frameprint(Frame_3, 4,frameant)).place(x=1090, y=580)
                    except:
                        messagebox.showwarning('ERROR', 'Ingresaste mal los datos, intenta nuevamente')
                else:
                    messagebox.showwarning('ERROR', 'Ingresaste mal los datos, intenta nuevamente')
            except:
                messagebox.showwarning('ERROR', 'Ingresaste mal los datos, intenta nuevamente')

    def Cuarto_Frame(frameant):
        """
        Tiene la funcion de llamar al cuarto Frame de nuestra leccion (Imprimir)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_4 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        Text_titulo_frame_4 = Label(Frame_4, text='LA SENTENCIA PRINT', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='De esta manera, es como funciona la sentencia print.', bg='#87CEFA', fg='white',font=('Comic Sans', 30)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Recuerda siempre que la función print() permite mostrar texto en pantalla. \nEl texto a mostrar se escribe como argumento de la función', bg='#87CEFA',fg='white', font=('Comic Sans', 25)).place(relx=0.5, y=250, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_4, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frameprint(Frame_4, 3,frameant)).place(x=60, y=580)
        botonavance = tk.Button(Frame_4, text="FIN", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frameprint(Frame_4, 5,frameant)).place(x=1090,y=580)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/final0.png").resize((800,400)))
        Frame_4.background = img
        bg = Frame_4.create_image(230, 270, anchor=tk.NW, image=img)

def leccion_variables(pantalla,frameant):
    """
    Tiene la funcion de generar la segunda leccion, acerca de las variables y los tipos de datos.
    :param tkinter.Canvas pantalla: Se refiere a nuestra pantalla diseñada por medio de la libreria Tkinter.
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
    :return None
    """
    Frame_1 = tk.Frame()
    Frame_1.pack()
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='700')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")

    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        elif numero==5:
            Quinto_Frame(frameant)
        elif numero==6:
            Sexto_Frame(frameant)
        elif numero==7:
            Septimo_Frame(frameant)
        elif numero==8:
            Octavo_Frame(frameant)
        elif numero==9:
            Noveno_Frame(frameant)
        elif numero==10:
            Decimo_Frame(frameant)
        else:
            frameant.pack()

    Texto_Titulo=Label(Frame_1,text = 'Bienvenido a la lección de:', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(relx=0.5,y=150,anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='Variables ', bg='#87CEFA', fg='white',font=('Comic Sans', 50,"bold")).place(relx=0.5, y=300, anchor=CENTER)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_1, 2,frameant)).place(relx=0.5, y=500, anchor=CENTER)

    def Segundo_Frame(frameant):
        """
        Tiene la funcion de llamar al segundo Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_2 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        Text_titulo_frame_2 = Label(Frame_2,text='Las Variables',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Primeramente, para comprender las variables de una manera correcta, es necesario \nconocer los tipos de datos.', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=160, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text="En esta ocasion, presentaremos los tipos de datos enteros, flotantes y caracteres.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=270, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text="Vamos a iniciar primeramente con los tipos de datos enteros",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=380, anchor=CENTER)
        boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 3,frameant)).place(x=1090,y=580)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/variables1.png").resize((500,200)))
        Frame_2.background = img
        bg = Frame_2.create_image(380, 430, anchor=tk.NW, image=img)

    def Tercer_Frame(frameant):
        """
        Tiene la funcion de llamar al tercer Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_3 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='LOS DATOS DE TIPO ENTERO',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3, text='Los datos de tipo entero o int, se refieren principalmente al conjunto de los numeros naturales,\n incluyendo a 0 y a los numeros negativos.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3,text='Ejemplos de estos son los numeros: 1, 2, 0, -5 y -10. Por nombrar algunos.',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=260,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/variables2.png").resize((500,200)))
        Frame_3.background = img
        bg = Frame_3.create_image(380, 330, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2,frameant)).place(x=60, y=580)
        botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_3, 4,frameant)).place(x=1090,y=580)

    def Cuarto_Frame(frameant):
        """
         Tiene la funcion de llamar al cuarto Frame de nuestra leccion (Variables)
         :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
         :return None
         """
        Frame_4 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        valoresrandom=["A","B","C","D","Z""X","Y","G","D",1.22,4.55,4.88,6.43,8.88,1.0,3.55,3.77,8.69,9.87,7.02]
        valoresenteros=[4,3,2,67,69,4,9,10,13,16,15,19,32,34,22,88]
        Text_titulo_frame_4 = Label(Frame_4, text='LOS DATOS DE TIPO ENTERO', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Ahora, buscaremos ver que se evidencio el concepto de una manera correcta.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text='Selecciona un dato de tipo entero ',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=240, anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/thinking.png").resize((150,150)))
        Frame_4.background = img
        bg = Frame_4.create_image(1065, 300, anchor=tk.NW, image=img)
        valor1 = str(random.choice(valoresrandom))
        valor2 = str(random.choice(valoresenteros))
        valor3 = str(random.choice(valoresrandom))
        selected = IntVar()
        rad1 = Radiobutton(Frame_4, text=valor1, font=("Comic Sans", 40), value=1, bg='#87CEFA',variable=selected).place(x=280, y=350)
        rad2 = Radiobutton(Frame_4, text=valor2, font=("Comic Sans", 40), value=2, bg='#87CEFA',variable=selected).place(x=590, y=350)
        rad3 = Radiobutton(Frame_4, text=valor3, font=("Comic Sans", 40), value=3, bg='#87CEFA',variable=selected).place(x=850, y=350)
        boton_si_no_1 = tk.Button(Frame_4, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(selected)).place(x=590,y=500)
        def comprobar(selected):
            """
            Esta funcion comprueba si se eligio la opcion correcta de la lista de opciones
            :param tkinter.IntVar selected: Representa  la seleccion del jugador.
            :return None
            """
            if(selected.get())==2:
                messagebox.showinfo('Muy bien :D', 'Elegiste el dato de tipo entero: ' + str(valor2))
                botonavance = tk.Button(Frame_4, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 5,frameant)).place(x=1090, y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste el dato de tipo entero, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_4, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 3,frameant)).place(x=60, y=580)


    def Quinto_Frame(frameant):
        """
        Tiene la funcion de llamar al quinto Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_5 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_5,text='LOS DATOS DE TIPO FLOTANTE',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_5, text='Los datos de tipo flotante, pueden ser similares a los de tipo entero, pero en este caso, \nrepresentan los numeros decimales. \n \nEstos datos de tipo flotante, estan separados por medio de un punto.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_5,text='Ejemplos de estos, pueden ser numeros tales como: 3.2, 2.3, 1.58, o -5.8',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=250,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/variables3.png").resize((800,400)))
        Frame_5.background = img
        bg = Frame_5.create_image(230, 270, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_5, 4,frameant)).place(x=60, y=580)
        botonavance = tk.Button(Frame_5, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_5, 6,frameant)).place(x=1090,y=580)
    
    def Sexto_Frame(frameant):
        """
        Tiene la funcion de llamar al sexto Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_6 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_6.pack()
        Frame_6.config(bg='#87CEFA')
        Frame_6.config(width='1280', height='700')
        Frame_6.config(bd=20)
        Frame_6.config(relief="groove")
        Text_titulo_frame_6 = Label(Frame_6, text='LOS DATOS DE TIPO FLOTANTE', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_6, text='Ahora, buscaremos ver que se evidencio el concepto de una manera correcta.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_6 = Label(Frame_6,text='Ingresa un dato de tipo flotante',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=240, anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/variables4.png").resize((500, 250)))
        Frame_6.background = img
        bg = Frame_6.create_image(390, 400, anchor=tk.NW, image=img)
        resp_1_get = StringVar()
        respuesta_1 = Entry(Frame_6, width=20, font=("Comic Sans", 26), textvariable=resp_1_get).place(relx=0.5, y=350,anchor=CENTER)
        boton_si_no_1 = tk.Button(Frame_6, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(resp_1_get)).place(x=850, y=330)
        def comprobar(resp_1_get):
            """
            Esta funcion comprueba si la entrada de la persona es correcta.
            :param tkinter.StringVar resp_1_get:Representa la entrada de la persona.
            :return None
            """
            cont = 0
            numero = resp_1_get.get()
            try:
                for i in range(len(numero)):
                    if numero[i]==".":
                        posicion=i
                        cont+=1
                if cont==1 and (type(float(numero)==float)):
                    messagebox.showinfo('Muy bien :D', 'Ingresaste el numero ' + str(numero))
                    botonavance = tk.Button(Frame_6, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_6, 7,frameant)).place(x=1090, y=580)
                else:
                    messagebox.showwarning('ERROR', 'No ingresaste un dato de tipo flotante. Intenta nuevamente')
            except:
                messagebox.showwarning('ERROR', 'No ingresaste un dato de tipo flotante. Intenta nuevamente')

        botonaretroceso = tk.Button(Frame_6, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_6, 5,frameant)).place(x=60, y=580)


    def Septimo_Frame(frameant):
        """
        Tiene la funcion de llamar al septimo Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_7 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_7.pack()
        Frame_7.config(bg='#87CEFA')
        Frame_7.config(width='1280', height='700')
        Frame_7.config(bd=20)
        Frame_7.config(relief="groove")
        Text_titulo_frame_7 = Label(Frame_7,text='LAS CADENAS O STRINGS',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_7, text='Las cadenas o strings, sirven para almacenar cadenas, que pueden ser tanto de letras como de numeros.\nPero es importante tener en cuenta, que asi almacenamos un numero, seguira siendo una cadena.', bg='#87CEFA', fg='white',font=('Comic Sans', 19)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_7,text="Las cadenas, se pueden identificar, ya que van encerradas entre comillas. (')",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=250,anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_7,text="Un ejemplo de la sintaxis de una cadena, puede ser por ejemplo 'hola', o '2342'.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=350,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/variables5.png").resize((500, 250)))
        Frame_7.background = img
        bg = Frame_7.create_image(390, 400, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_7, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_7, 6,frameant)).place(x=60, y=580)
        botonavance = tk.Button(Frame_7, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_7, 8,frameant)).place(x=1090,y=580)

    def Octavo_Frame(frameant):
        """
        Tiene la funcion de llamar al octavo Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_8 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_8.pack()
        Frame_8.config(bg='#87CEFA')
        Frame_8.config(width='1280', height='700')
        Frame_8.config(bd=20)
        Frame_8.config(relief="groove")
        valoresrandom = [1,5,7,5,3,2,8,90,1.22, 4.55, 4.88, 6.43, 8.88, 1.0, 3.55, 3.77, 8.69,9.87, 7.02,15,67,32,66]
        valorescad = ["'hola'","'perro'","'niño'","'Juan'","'gato'","'lapiz'","'caballo'","'libro'","'esfero'","'carro'","'auto'"]
        Text_titulo_frame_8 = Label(Frame_8, text='LAS CADENAS O STRINGS', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_8 = Label(Frame_8, text='Ahora, buscaremos ver que se evidencio el concepto de una manera correcta.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_8 = Label(Frame_8,text='Selecciona la cadena',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=240, anchor=CENTER)
        valor1 = str(random.choice(valorescad))
        valor2 = str(random.choice(valoresrandom))
        valor3 = str(random.choice(valoresrandom))
        selected = IntVar()
        rad1 = Radiobutton(Frame_8, text=valor1, font=("Comic Sans", 40), value=1, bg='#87CEFA',variable=selected).place(x=280, y=350)
        rad2 = Radiobutton(Frame_8, text=valor2, font=("Comic Sans", 40), value=2, bg='#87CEFA',variable=selected).place(x=590, y=350)
        rad3 = Radiobutton(Frame_8, text=valor3, font=("Comic Sans", 40), value=3, bg='#87CEFA',variable=selected).place(x=850, y=350)
        boton_si_no_1 = tk.Button(Frame_8, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(x=590, y=500)
        def comprobar(selected):
            """
            Esta funcion comprueba si se eligio la opcion correcta de la lista de opciones
            :param tkinter.IntVar selected: Representa  la seleccion del jugador.
            :return None
            """
            if (selected.get()) == 1:
                messagebox.showinfo('Muy bien :D', 'Elegiste el dato de tipo string: ' + (valor1))
                botonavance = tk.Button(Frame_8, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_8, 9,frameant)).place(x=1090, y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste el dato de tipo string, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_8, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_8, 7,frameant)).place(x=60, y=580)


    def Noveno_Frame(frameant):
        """
        Tiene la funcion de llamar al noveno Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_9 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_9.pack()
        Frame_9.config(bg='#87CEFA')
        Frame_9.config(width='1280', height='700')
        Frame_9.config(bd=20)
        Frame_9.config(relief="groove")
        Text_titulo_frame_9 = Label(Frame_9,text='LA ASIGNACIÓN DE VARIABLES',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_9 = Label(Frame_9, text='Ya que conocemos los tipos de datos, enseñaremos a asignarlos a variables. \n\nPara asignar valores a una variable, usamos el = ', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_9 = Label(Frame_9,text='En otras palabras, la asignacion, se realizaria de la siguiente forma: ',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=275,anchor=CENTER)
        Text_titulo_frame_9 = Label(Frame_9,text='variable = valor asignado ',bg='#87CEFA', fg='white', font=('Comic Sans', 25,"bold")).place(relx=0.5, y=320,anchor=CENTER)
        Text_titulo_frame_9 = Label(Frame_9,text='Esto se puede evidenciar mejor en el siguiente ejemplo:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=410,anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/variables6.png").resize((300, 180)))
        Frame_9.background = img
        bg = Frame_9.create_image(490, 450, anchor=tk.NW, image=img)
        botonaretroceso = tk.Button(Frame_9, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_9, 8,frameant)).place(x=60, y=580)
        botonavance = tk.Button(Frame_9, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_9, 10,frameant)).place(x=1090,y=580)

    def Decimo_Frame(frameant):
        """
        Tiene la funcion de llamar al decimo Frame de nuestra leccion (Variables)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_10 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_10.pack()
        Frame_10.config(bg='#87CEFA')
        Frame_10.config(width='1280', height='700')
        Frame_10.config(bd=20)
        Frame_10.config(relief="groove")
        Text_titulo_frame_10 = Label(Frame_10, text='LA ASIGNACIÓN DE VARIABLES', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_10 = Label(Frame_10, text='Ahora, vamos a intentarlo de una manera practica.', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_10 = Label(Frame_10,text='Ingresa una variable y un dato asignado a esta (puede ser entero, flotante o cadena).',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=240, anchor=CENTER)
        Text0_frame_10 = Label(Frame_10,text='TIP: Recuerda que la asignacion es de la siguiente forma: variable = valor asignado',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=500, anchor=CENTER)
        resp_1_get = StringVar()
        respuesta_1 = Entry(Frame_10, width=20, font=("Comic Sans", 26), textvariable=resp_1_get).place(relx=0.5, y=350,anchor=CENTER)
        boton_si_no_1 = tk.Button(Frame_10, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(resp_1_get)).place(x=850, y=330)
        def comprobar(resp_1_get):
            """
            Esta funcion comprueba si la entrada del usuario es correcta en base a distintos parametros.
            :param StringVar resp_1_get: Representa la entrada del usuario.
            :return None
            """
            cont,cont1 = 0,0
            cadena = (resp_1_get.get())
            try:
                if len(cadena)>=3:
                    for i in range(len(cadena)):
                        if cadena[i]=="=":
                            pos0=i
                            cont+=1
                        if cadena[i]=="'" or cadena[i]=='"':
                            cont1+=1
                    parte_cad1 = cadena[:pos0]
                    parte_cad2 = cadena[pos0 + 1:len(cadena)]
                    if (parte_cad1 + "=" + parte_cad2) == cadena and cont==1 and cont1==0:
                        if cont==1 and type(int(parte_cad2))==int or type(float(parte_cad2))==float:
                            messagebox.showinfo('Muy bien :D', 'Asignaste a la variable ' + str(parte_cad1)+" el valor de "+str(parte_cad2))
                            botonavance = tk.Button(Frame_10, text="FIN", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_10, 11,frameant)).place(x=1090,y=580)
                        else:
                            messagebox.showwarning('ERROR','No hiciste la asignacion de manera correcta. Intenta nuevamente')
                    elif cont1==2:
                        if (parte_cad1+"="+"'"+parte_cad2[1:len(parte_cad2)-1]+"'")==cadena or ((parte_cad1+"="+'"'+parte_cad2[1:len(parte_cad2)-1])+'"')==cadena:
                            messagebox.showinfo('Muy bien :D', 'Asignaste a la variable ' + str(parte_cad1) + " el valor de " + str (parte_cad2[:len(parte_cad2)]))
                            botonavance = tk.Button(Frame_10, text="FIN", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_10, 11,frameant)).place(x=1090,y=580)
                        elif (parte_cad1+"="+" '"+parte_cad2[2:len(parte_cad2)-1]+"'")==cadena or ((parte_cad1+"="+' "'+parte_cad2[2:len(parte_cad2)-1])+'"')==cadena:
                            messagebox.showinfo('Muy bien :D','Asignaste a la variable ' + str(parte_cad1) + " el valor de " + str(parte_cad2[:len(parte_cad2)]))
                            botonavance = tk.Button(Frame_10, text="FIN", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_10, 11,frameant)).place(x=1090,y=580)
                        else:
                            messagebox.showwarning('ERROR','No hiciste la asignacion de manera correcta. Intenta nuevamente')
                    else:
                        messagebox.showwarning('ERROR', 'No hiciste la asignacion de manera correcta. Intenta nuevamente')
            except:
                messagebox.showwarning('ERROR', 'No hiciste la asignacion de manera correcta. Intenta nuevamente')
        botonaretroceso = tk.Button(Frame_10, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_10, 9,frameant)).place(x=60, y=580)

def leccion_while(pantalla,frameant):
    """
    Tiene la funcion de generar la sexta leccion, acerca del ciclo while.
    :param tkinter.Canvas pantalla: Se refiere a nuestra pantalla diseñada por medio de la libreria Tkinter.
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
    :return None
    """
    Frame_1 = tk.Frame()
    Frame_1.pack()
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='700')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")

    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        elif numero==5:
            Quinto_Frame(frameant)
        elif numero==6:
            Sexto_Frame(frameant)
        elif numero==7:
            Septimo_Frame(frameant)
        elif numero==8:
            Octavo_Frame(frameant)
        else:
            frameant.pack()

    Texto_Titulo=Label(Frame_1,text = 'Bienvenido a la lección de:', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(relx=0.5,y=150,anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='El Ciclo While', bg='#87CEFA', fg='white',font=('Comic Sans', 50,"bold")).place(relx=0.5, y=300, anchor=CENTER)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_1, 2,frameant)).place(relx=0.5, y=500, anchor=CENTER)

    def Segundo_Frame(frameant):
        """
        Tiene la funcion de llamar al segundo Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_2 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        Text_titulo_frame_2 = Label(Frame_2,text='EL CICLO WHILE',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Podriamos mencionar que while se puede identificar en español como "mientras".', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=160, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text="Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras\n se cumpla una condición (es decir, mientras la condición tenga el valor True).",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=270, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text="Vamos a iniciar presentando la sintaxis del ciclo while",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=380, anchor=CENTER)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/while0.png").resize((400,200)))
        Frame_2.background = img
        bg = Frame_2.create_image(440, 440, anchor=tk.NW, image=img)
        boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 3,frameant)).place(x=1090,y=580)

    def Tercer_Frame(frameant):
        """
        Tiene la funcion de llamar al tercer Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_3 = tk.Frame()
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='EL CICLO WHILE',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3, text='La sintaxis del bucle while es la siguiente: ', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3,text='while condicion:\n\tcuerpo del codigo',bg='#87CEFA', fg='white', font=('Comic Sans', 35,"bold")).place(relx=0.5, y=290,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3, text='Las condiciones que debemos tener en cuenta con el ciclo while, son las siguientes: ', bg='#87CEFA',fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=450, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_3, 4,frameant)).place(x=1090,y=580)

    def Cuarto_Frame(frameant):
        """
        Tiene la funcion de llamar al cuarto Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_4 = tk.Frame()
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        Text_titulo_frame_4 = Label(Frame_4,text='EL CICLO WHILE',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='1. Primeramente, evalua la condicion, devolviendo ya sea True o False ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=160, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text="2. Si la condicion es falsa, sale de la sentencia while.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=270, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text="3.Si la condición es verdadera, ejecuta cada una de las sentencias en el cuerpo del bucle while,\n y luego vuelve al paso 1.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=380, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text="Esto se puede visualizar mejor por el siguiente ejemplo:",bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=550, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_4,text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 3,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_4, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_4, 5,frameant)).place(x=1090,y=580)

    def Quinto_Frame(frameant):
        """
        Tiene la funcion de llamar al quinto Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_5 = tk.Frame()
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_5,text='EL CICLO WHILE',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_5, text='Ejemplo:', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(relx=0.5, y=120, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_5, text='contador = 1', bg='#87CEFA', fg='white',font=('Comic Sans', 25,"bold")).place(x=450, y=180)
        Text_titulo_frame_3 = Label(Frame_5, text='numero = 5', bg='#87CEFA', fg='white',font=('Comic Sans', 25,"bold")).place(x=450, y=218)
        Text_titulo_frame_3 = Label(Frame_5, text='while contador <= numero:', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=450, y=260)
        Text_titulo_frame_3 = Label(Frame_5, text='\tprint (contador)', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=450, y=300)
        Text_titulo_frame_3 = Label(Frame_5, text='\tcontador = contador + 1  ', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=450, y=340)
        Text_titulo_frame_3 = Label(Frame_5,text='Lo que imprimiria nuestro bucle, seria los numeros desde el numero 1, hasta el numero 5.',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=460,anchor=CENTER)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_5, 4,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_5, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_5, 6,frameant)).place(x=1090,y=580)

    def Sexto_Frame(frameant):
        """
        Tiene la funcion de llamar al sexto Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_6 = tk.Frame()
        Frame_6.pack()
        Frame_6.config(bg='#87CEFA')
        Frame_6.config(width='1280', height='700')
        Frame_6.config(bd=20)
        Frame_6.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_6, text='EL CICLO WHILE', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_6, text='Vamos a ponernos en practica! ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=105, anchor=CENTER)
        Text0_frame_6 = Label(Frame_6, text='Si tenemos el siguiente codigo, y queremos imprimir desde el numero 2 hasta el 6: ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=165, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_6, text='contador = 2', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(x=450, y=210)
        Text_titulo_frame_3 = Label(Frame_6, text='numero = 6', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(x=450, y=250)
        Text_titulo_frame_3 = Label(Frame_6, text='while _____________:', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=290)
        Text_titulo_frame_3 = Label(Frame_6, text='\tprint (contador)', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=330)
        Text_titulo_frame_3 = Label(Frame_6, text='\tcontador = contador + 1  ', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=370)
        Text0_frame_6 = Label(Frame_6, text='¿Cual es las parte de codigo faltante?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=460, anchor=CENTER)
        valorescad=["contador<=numero"]
        valoresrandom=["contador>=numero","contador!=numero","contador==numero","numero!=contador","numero<contador","numero"]
        valor1 = str(random.choice(valorescad))
        valor2 = str(random.choice(valoresrandom))
        valor3 = str(random.choice(valoresrandom))
        selected = IntVar()
        rad1 = Radiobutton(Frame_6, text=valor1, font=("Comic Sans", 15), value=1, bg='#87CEFA',variable=selected).place(x=260, y=500)
        rad2 = Radiobutton(Frame_6, text=valor2, font=("Comic Sans", 15), value=2, bg='#87CEFA',variable=selected).place(relx=0.5, y=518, anchor=CENTER)
        rad3 = Radiobutton(Frame_6, text=valor3, font=("Comic Sans", 15), value=3, bg='#87CEFA',variable=selected).place(x=800, y=500)
        boton_si_no_1 = tk.Button(Frame_6, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(relx=0.5, y=585, anchor=CENTER)
        def comprobar(selected):
            """
            Esta funcion comprueba si se eligio la opcion correcta de la lista de opciones
            :param tkinter.IntVar selected: Representa  la seleccion del jugador.
            :return None
            """
            if (selected.get()) == 1:
                messagebox.showinfo('Muy bien :D', 'Elegiste la opcion correcta (' + (valor1)+")")
                botonavance = tk.Button(Frame_6, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_6, 7,frameant)).place(x=1090, y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste la opcion correcta, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_6, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_6, 5,frameant)).place(x=20, y=580)


    def Septimo_Frame(frameant):
        """
        Tiene la funcion de llamar al septimo Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_7 = tk.Frame()
        Frame_7.pack()
        Frame_7.config(bg='#87CEFA')
        Frame_7.config(width='1280', height='700')
        Frame_7.config(bd=20)
        Frame_7.config(relief="groove")
        Text_titulo_frame_7 = Label(Frame_7, text='EL CICLO WHILE', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_7 = Label(Frame_7, text='Vamos a ponernos en practica! ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=105, anchor=CENTER)
        Text0_frame_7 = Label(Frame_7, text='Si tenemos el siguiente codigo: ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=165, anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_7, text='contador = 2', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(x=450, y=230)
        Text_titulo_frame_7 = Label(Frame_7, text='numero = 6', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(x=450, y=270)
        Text_titulo_frame_7 = Label(Frame_7, text='while contador <= numero:', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=310)
        Text_titulo_frame_7 = Label(Frame_7, text='\tprint (contador)', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=350)
        Text0_frame_7 = Label(Frame_7, text='¿Cual seria la salida de este?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=460, anchor=CENTER)
        valorescad=["ERROR"]
        valoresrandom=["2-6","1-6","2-7","1-8","1,3","HOLA","A","4-6","7-8"]
        valor1 = str(random.choice(valoresrandom))
        valor2 = str(random.choice(valoresrandom))
        valor3 = str(random.choice(valorescad))
        selected = IntVar()
        rad1 = Radiobutton(Frame_7, text=valor1, font=("Comic Sans", 15), value=1, bg='#87CEFA',variable=selected).place(x=400, y=500)
        rad2 = Radiobutton(Frame_7, text=valor2, font=("Comic Sans", 15), value=2, bg='#87CEFA',variable=selected).place(relx=0.5, y=518, anchor=CENTER)
        rad3 = Radiobutton(Frame_7, text=valor3, font=("Comic Sans", 15), value=3, bg='#87CEFA',variable=selected).place(x=750, y=500)
        boton_si_no_1 = tk.Button(Frame_7, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(relx=0.5, y=585, anchor=CENTER)
        def comprobar(selected):
            """
            Esta funcion comprueba si se eligio la opcion correcta de la lista de opciones
            :param tkinter.IntVar selected: Representa  la seleccion del jugador.
            :return None
            """
            if (selected.get()) == 3:
                messagebox.showinfo('Muy bien :D', 'Elegiste la opcion correcta (' + (valor3)+")")
                botonavance = tk.Button(Frame_7, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_7, 8,frameant)).place(x=1090, y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste la opcion correcta, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_7, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_7, 6,frameant)).place(x=20, y=580)


    def Octavo_Frame(frameant):
        """
        Tiene la funcion de llamar al octavo Frame de nuestra leccion (While)
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente.
        :return None
        """
        Frame_8 = tk.Frame()
        Frame_8.pack()
        Frame_8.config(bg='#87CEFA')
        Frame_8.config(width='1280', height='700')
        Frame_8.config(bd=20)
        Frame_8.config(relief="groove")
        Text_titulo_frame_8 = Label(Frame_8, text='EL CICLO WHILE', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_8= Label(Frame_8, text='Vamos a ponernos en practica! ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=105, anchor=CENTER)
        Text0_frame_8 = Label(Frame_8, text='Si tenemos el siguiente codigo, y queremos imprimir desde el numero 3 hasta el 7: ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=165, anchor=CENTER)
        Text_titulo_frame_8 = Label(Frame_8, text='contador = _', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(x=450, y=210)
        Text_titulo_frame_8 = Label(Frame_8, text='numero = _', bg='#87CEFA', fg='white',font=('Comic Sans', 20,"bold")).place(x=450, y=250)
        Text_titulo_frame_8 = Label(Frame_8, text='while contador<=numero:', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=290)
        Text_titulo_frame_8 = Label(Frame_8, text='\tprint (contador)', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=330)
        Text_titulo_frame_8 = Label(Frame_8, text='\tcontador = contador + 1  ', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(x=450, y=370)
        Text0_frame_8 = Label(Frame_8, text='¿Cuales valores deberiamos asignarle al numero y al contador?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=460, anchor=CENTER)
        valorescad=["3 y 7"]
        valoresrandom=["4 y 6","5 y 8","6 y 7","1 y 8","2 y 6","3 y 8","8 y 10","9 y 11","4 y 5"]
        valor1 = str(random.choice(valoresrandom))
        valor2 = str(random.choice(valorescad))
        valor3 = str(random.choice(valoresrandom))
        selected = IntVar()
        rad1 = Radiobutton(Frame_8, text=valor1, font=("Comic Sans", 15), value=1, bg='#87CEFA',variable=selected).place(x=350, y=500)
        rad2 = Radiobutton(Frame_8, text=valor2, font=("Comic Sans", 15), value=2, bg='#87CEFA',variable=selected).place(relx=0.5, y=518, anchor=CENTER)
        rad3 = Radiobutton(Frame_8, text=valor3, font=("Comic Sans", 15), value=3, bg='#87CEFA',variable=selected).place(x=800, y=500)
        boton_si_no_1 = tk.Button(Frame_8, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(relx=0.5, y=585, anchor=CENTER)
        def comprobar(selected):
            """
            Esta funcion comprueba si se eligio la opcion correcta de la lista de opciones
            :param tkinter.IntVar selected: Representa  la seleccion del jugador.
            :return None
            """
            if (selected.get()) == 2:
                messagebox.showinfo('Muy bien :D', 'Elegiste la opcion correcta (' + (valor2)+")")
                botonavance = tk.Button(Frame_8, text="Fin", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_8, 9,frameant)).place(x=1090,y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste la opcion correcta, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_8, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_8, 7,frameant)).place(x=20, y=580)

def nombres_de_funciones(pantalla,frameant):
    """
    Enseña algunos nombres de funciones integradas al lenguaje de Python, y como usarlas,
    además de una introducción a funciones.
    :param tkinter.Canvas pantalla: es donde ubicaremos los frames de esta leccion y sus items o imagenes
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
    :return None
    """
    # fale_nafun, es la abreviación de Frame: names de funciones: Frame para nombres de funciones
    fale_nafun = tk.Canvas(pantalla, width=1280, height=700)
    fale_nafun.pack()
    fale_nafun.config(bg = '#87CEFA')
    fale_nafun.config(width = '1280', height = '700')
    fale_nafun.config(bd = 20)
    fale_nafun.config(relief = "groove")
    resp_1_get = StringVar()
    cont_de_preguntas = 0
    titulo_adi_num = Label(fale_nafun,text = '¡NOMBRES DE FUNCIONES!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',35)).place(x = 270, y = 50)
    sub_titulo = Label(fale_nafun,text = '¡Bienvenido a otra lección con PLAYTHON!', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',17)).place(x = 395,y = 120)
        
    linea_1 = Label(fale_nafun,text = "Seguramente, ya aprendiste algo sobre las palabras reservadas no es así?", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 150,y = 170)
    pista_1 = Label(fale_nafun,text = "Eso te habrá servido como una introducción para nuestro siguiente tema...", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 130,y = 215)  
   
    linea_2 = Label(fale_nafun,text = "NOMBRES DE FUNCIONES", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 450, y = 270)
    linea_3 = Label(fale_nafun,text = "Las funciones, son por por así decirlo, pequeños algoritmos dentro de uno más grande\nAl igual que los órganos de tu cuerpo cumplen una función, por ejemplo,\n las venas, transportan sangre, y los ojos observan\nLas funciones, son como 'órganos' pero de tu código\nDe hecho, tu ya has usado funciones! Recuerda un poco y verás que es así",
    bg = '#87CEFA', fg = 'white', 
    font = ('Comic Sans',20)).place(x = 60,y = 330)
    boton0 = tk.Button(fale_nafun, text="¡Continuemos!", font=("Comic Sans", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(fale_nafun, 2,frameant)).place(relx=0.5, y=600, anchor=CENTER)
    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        elif numero == 5:
            Quinto_Frame(frameant)
        elif numero == 6:
            Sexto_Frame(frameant)
        elif numero == 7:
            Septimo_Frame(frameant)
        elif numero == 8:
            Octavo_Frame(frameant)
        elif numero == 9:
            Noveno_Frame(frameant)
        elif numero == 10:
            Decimo_Frame(frameant)        
        elif numero == 11:
            Onceavo_Frame(frameant)
        elif numero == 12:
            Doceavo_Frame(frameant)
        elif numero == 13:
            Trece_Doceavo(frameant)
        elif numero == 14:
            Treceavo_Frame(frameant)
        else:
            frameant.pack()
    
    def Segundo_Frame(frameant):
        """
        Tiene la funcion de crear el segundo frame de esta leccion.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            if resp_1_get.get() == "si" or resp_1_get.get() == "Si" or resp_1_get.get() == "SI" or resp_1_get.get() == "sI":
                mensaje_1 = Label(Frame_2,text = 'Nos alegra que lo recuerdes!', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(relx = 0.5,y = 250, anchor = CENTER)
                vdd = 1
            elif resp_1_get.get() == "no" or resp_1_get.get() == "No" or resp_1_get.get() == "NO" or resp_1_get.get() == "nO":
                mensaje_1 = Label(Frame_2,text = 'Bueno, no hay problema!     ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(relx = 0.5,y = 250, anchor = CENTER)
                vdd = 1
            else:
                messagebox.showwarning(title = "Eso es un sí o un no?", message = "Eso no cuenta como respuesta listillo")
                mensaje_1 = Label(Frame_2,text = 'Responde bien >:v           ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(relx = 0.5,y = 250, anchor = CENTER)
            if vdd == 1:
                Text0_frame_2 = Label(Frame_2, text='La función iskeyword, recibía un valor de tipo string, y verificaba\n si ese valor estaba en la lista de palabras reservadas. Esa era la "función" del órgano "iskeyword"\nDefinir una función es muy fácil, sólo debes escribir esto:\n \ndef nombre_de_tu_función ():                                             \n  Y aquí pones las tareas que va ha hacer tu función ', 
                bg='#87CEFA', fg='white',font=('Comic Sans', 20)
                ).place(x = 20, y=280)
                Text0_frame_2 = Label(Frame_2, text='Fácil verdad?, Sin embargo no te enseñaremos a crear funciones en este momento', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(x=30, y=500)   
                boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 3,frameant)).place(x = 950 ,y = 500)
        Frame_2 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        resp_1_get = StringVar()
        Text_titulo_frame_2 = Label(Frame_2,text='¡NOMBRES DE FUNCIONES!',bg='#87CEFA', fg='white', font=('Comic Sans', 40)).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Por ejemplo, anteriormente, aprendiste a usar la función "iskeyword", recuerdas que hacía?', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text=' Si / No: ',bg='#87CEFA', fg='white', font=('Comic Sans', 26,)).place(x = 500, y=180, anchor=CENTER)
        boton_comprov = tk.Button(Frame_2, text = "!Listo¡", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=760, y = 180, anchor = CENTER)
        respuesta_2 =  Entry(Frame_2, width = 3, font = ("Comic Sans", 26),textvariable = resp_1_get).place(relx = 0.5, y = 180, anchor = CENTER)
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/website.png").resize((90,90)))
        Frame_2.background = img1
        bg1 = Frame_2.create_image(880,180, anchor=tk.NW, image=img1)

    def Tercer_Frame(frameant):
        """
        Tiene la funcion de crear el tercer frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_3 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='¡NOMBRES DE FUNCIONES!',bg='#87CEFA', fg='white', font=('Comic Sans', 40,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='Te enseñaremos algunas funciones que puedes usar como ya lo hicimos con "iskeyword"\nHay una gran cantidad de funciones, sin embargo, trataremos de enseñarte algunas\n que suelen ser muy útiles. Antes de cualquier cosa, para usar una función debemos "llamarla",\n hay muchas formas de hacerlo dependiendo de la función ¡Pero no te preocupes!\nCasi todas las funciones que te enseñaremos aquí, se llaman de esta manera:\n \n variable_sobre_la_que_trabajamos.nombre_de_la_función()\n \nO también podría hacerse así:\n \nnombre_de_la_funcion(variable_sobre_la_que_trabajamos)', bg='#87CEFA', fg='white', font=('Comic Sans', 20)
        ).place(relx=0.5, y = 250, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 20), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2,frameant)).place(x = 100, y=480)
        resp_2_get = StringVar()
        botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_3, 4,frameant)).place(x=900,y=480) 
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/codigo-binario.png").resize((150,150)))
        Frame_3.background = img
        bg = Frame_3.create_image(580,470, anchor=tk.NW, image=img)

    def Cuarto_Frame(frameant):
        """
        Tiene la funcion de crear el cuarto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_4 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        resp_3_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_4, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='No te asustes por ver todo eso! Te pondré un ejemplo más simple,\nobserva el siguiente código, aquí usaremos la función .upper():', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='variable = "Soy bueno programando!"\nvariable.upper()                                 \nprint(variable)                                    ', bg='#87CEFA',fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Que crees que imprimirá este código?\n1)soy bueno programando!                  \n2)SOY BUENO PROGRAMANDO!     ',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x=200, y = 340)
        respuesta_3 =  Entry(Frame_4, width = 3, font = ("Comic Sans", 20),textvariable = resp_3_get).place(x =780, y = 330)
        Text0_frame_4 = Label(Frame_4, text=' 1/ 2: ',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x = 700, y = 330)  
        boton_comprov = tk.Button(Frame_4, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=960, y = 350, anchor = CENTER)
        botonaretroceso = tk.Button(Frame_4, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 3,frameant)).place(x=100, y=480)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/mayusculas.png").resize((130,130)))
        Frame_4.background = img
        bg = Frame_4.create_image(200,200, anchor=tk.NW, image=img)

        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            if resp_3_get.get() == "2":
                mensaje_1 = Label(Frame_4,text = 'Eres muy inteligente,  \n respuesta correcta', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.75,y = 430, anchor = CENTER)
                vdd = 1
            elif resp_3_get.get() == "1":
                mensaje_1 = Label(Frame_4,text = 'Oh, fallaste, pero     \n no importa!   ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.75,y = 430, anchor = CENTER)
                vdd = 1
            else:
                messagebox.showwarning(title = "Eso es un sí o un no?", message = "Eso no cuenta como respuesta listillo")
                mensaje_1 = Label(Frame_4,text = 'Responde bien >:v       \n              ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.75,y = 430, anchor = CENTER)
            if vdd == 1:
                Text0_frame_2 = Label(Frame_4, text='Como te habrás dado cuenta ahora, la\n función .upper(), pasa los caracteres de un\n string a MAYÚSCULAS', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx= 0.5, y=550, anchor = CENTER)
                boton1 = tk.Button(Frame_4, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_4, 5,frameant)).place(x = 900 ,y = 480)  
    def Quinto_Frame(frameant):
        """
        Tiene la funcion de crear el quinto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_5 = tk.Canvas(pantalla, width=1280, height=700)
        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            if resp_4_get.get() == "2":
                mensaje_1 = Label(Frame_5,text = 'Eres muy inteligente,\n respuesta correcta', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.75,y = 430, anchor = CENTER)
                vdd = 1
            else:
                messagebox.showwarning(title = "Te equivocaste unu", message = "Lee de nuevo la explicación")
            if vdd == 1:
                Text0_frame_2 = Label(Frame_5, text='Bueno, ahora ya puedes defenderte\n debidamente en cuanto a funciones,\n pero te enseñaremos algunas más:', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx= 0.5, y=550, anchor = CENTER)
                boton1 = tk.Button(Frame_5, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_5, 6,frameant)).place(x = 900 ,y = 480)  
        
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        resp_4_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_5, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_4 = Label(Frame_5, text='La función que hace lo contrario es la función .lower()\n, esta pasa los caracteres de una función a minúsculas', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_4 = Label(Frame_5, text='Si aplicaras la función .lower() sobre el string "H0LA Mundo" cuál de estos resultados obtendrías?\n1) hola mundo\n2) h0la mundo', bg='#87CEFA',fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        respuesta_3 =  Entry(Frame_5, width = 3, font = ("Comic Sans", 20),textvariable = resp_4_get).place(x =780, y = 330)
        Text0_frame_4 = Label(Frame_5, text='1 / 2:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x = 700, y = 330)  
        boton_comprov = tk.Button(Frame_5, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=960, y = 350, anchor = CENTER)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_5, 4,frameant)).place(x=100, y=480)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/minuscula.png").resize((130,130)))
        Frame_5.background = img
        bg = Frame_5.create_image(180,300, anchor=tk.NW, image=img)
        
    def Sexto_Frame(frameant):
        """
        Tiene la funcion de crear el sexto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_6 = tk.Canvas(pantalla, width=1280, height=700)
        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            if resp_5_get.get() == "6":
                mensaje_1 = Label(Frame_6,text = 'Eres muy inteligente,\n respuesta correcta', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.5,y = 500, anchor = CENTER)
                vdd = 1
            else:
                messagebox.showwarning(title = "Incorrecto unu", message = "Mira bien la palabra")
            if vdd == 1:
                Text0_frame_2 = Label(Frame_6, text='', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx= 0.5, y=550, anchor = CENTER)
                boton1 = tk.Button(Frame_6, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_6, 7,frameant)).place(x = 900 ,y = 480)  
        Frame_6.pack()
        Frame_6.config(bg='#87CEFA')
        Frame_6.config(width='1280', height='700')
        Frame_6.config(bd=20)
        Frame_6.config(relief="groove")
        resp_5_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_6, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_6, text='Hay una función que te permite saber la longitud de una cadena, como si la midieras con una regla\nEsta función se llama....\nlen()\nEn este caso no la llamamos con .len(), simplemente debemos poner\n la palabra dentro de los paréntesis de len() .Intenta contestar esta pregunta! \n¿Que valor imprime por pantalla esto? len("cadena")', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=190, anchor=CENTER)
        respuesta_3 =  Entry(Frame_6, width = 3, font = ("Comic Sans", 20),textvariable = resp_5_get).place(relx = 0.5, y = 360, anchor = CENTER)
        Text0_frame_6 = Label(Frame_6, text='Es un número del cero al diez:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x = 190, y = 340)  
        boton_comprov = tk.Button(Frame_6, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=800, y = 330)
        botonaretroceso = tk.Button(Frame_6, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_6, 5,frameant)).place(x=100, y=480)                 
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/gobernante.png").resize((130,130)))
        Frame_6.background = img
        bg = Frame_6.create_image(1000,300, anchor=tk.NW, image=img)
        
    def Septimo_Frame(frameant):
        """
        Tiene la funcion de crear el septimo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_7 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_7.pack()
        Frame_7.config(bg='#87CEFA')
        Frame_7.config(width='1280', height='700')
        Frame_7.config(bd=20)
        Frame_7.config(relief="groove")
        resp_5_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_7, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_7 = Label(Frame_7, text='Déjanos agradecerte por haber jugado nuestro juego hasta este punto!\nContinuemos aprendiendo! Ahora miremos la funcion .split(),\n esta convierte las "palabras" de una cadena en una lista.\ncadena = "Ahora sé programar"\ncadena.split()                           \nprint(cadena)                            \n', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        Text0_frame_7 = Label(Frame_7, text='Qué crees que imprima este código?\n1)["Ahora se programar"]     \n2)["Ahora","sé","programar"]',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x=100, y = 340)
        respuesta_3 =  Entry(Frame_7, width = 3, font = ("Comic Sans", 20),textvariable = resp_5_get).place(x = 800, y = 340)
        Text0_frame_7 = Label(Frame_7, text='1 / 2: ',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x = 700, y = 340)  
        boton_comprov = tk.Button(Frame_7, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=900, y = 330)
        botonaretroceso = tk.Button(Frame_7, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_7, 6,frameant)).place(x=100, y=480)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/impresora.png").resize((130,130)))
        Frame_7.background = img
        bg = Frame_7.create_image(50,180, anchor=tk.NW, image=img)

        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            if resp_5_get.get() == "2":
                mensaje_1 = Label(Frame_7,text = 'Eres muy inteligente,\n respuesta correcta', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.5,y = 500, anchor = CENTER)
                vdd = 1
            else:
                messagebox.showwarning(title = "Incorrecto unu", message = "Revisa la frase y la definición")
            if vdd == 1:
                Text0_frame_2 = Label(Frame_7, text = '', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx= 0.5, y=550, anchor = CENTER)
                boton1 = tk.Button(Frame_7, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_7, 8,frameant)).place(x = 900 ,y = 480)  
    def Octavo_Frame(frameant):
        """
        Tiene la funcion de crear el octavo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_8 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_8.pack()
        Frame_8.config(bg='#87CEFA')
        Frame_8.config(width='1280', height='700')
        Frame_8.config(bd=20)
        Frame_8.config(relief="groove")
        resp_5_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_8, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_8 = Label(Frame_8, text='Sigamos viendo funciones! \nContinuemos con una interesante, y una que usaras mucho, osea...\nLa función "range()", esta devuelve nos devuelve una lista de valores \nnuméricos que empieza desde 0, dependiendo de el valor ingresado\nTIP: Un buen programador, siempre cuenta desde 0. La función range() \nrecibe datos tipo string o números enteros. Veamos el siguiente ejemplo:\n \nrango = range(10)       \nprint(rango)                \n>>>[0,1,2,3,4,5,6,7,8,9]\nBastante simple no?,Te acostumbrarás con el tiempo así que no te preocupes\n', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=300, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_8, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_8, 7,frameant)).place(x=100, y=480)
        boton1 = tk.Button(Frame_8, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_8, 9,frameant)).place(x = 900 ,y = 480)  

        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/lista-de-verificacion.png").resize((130,130)))
        
        Frame_8.background = img
        bg = Frame_8.create_image(580,480, anchor=tk.NW, image=img)
        
    def Noveno_Frame(frameant):
        """
        Tiene la funcion de crear el noveno frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_9 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_9.pack()
        Frame_9.config(bg='#87CEFA')
        Frame_9.config(width='1280', height='700')
        Frame_9.config(bd=20)
        Frame_9.config(relief="groove")
        resp_6_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_9, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_9, text='Para que puedas usar un range() con un dato tipo string, debes hacer algo como esto:\nrange(len(aquí_pones_tu_string))\nAtento!Pregunta!Cuál sería el resultado de imprimir:\nrange(len("10"))\na) [0,1,2,3,4,5,6,7,8,9]        \n!) [0,1]                                \n2) No es posible imprimirlo   ', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        Text0_frame_4 = Label(Frame_9, text='Ingresa tu respuesta a/2/!:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x=260, y = 400)
        respuesta_3 =  Entry(Frame_9, width = 3, font = ("Comic Sans", 20),textvariable = resp_6_get).place(relx = 0.5, y = 400)
        boton_comprov = tk.Button(Frame_9, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=760, y = 400)
        botonaretroceso = tk.Button(Frame_9, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_9, 8,frameant)).place(x=100, y=480)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/portapapeles.png").resize((80,80)))
        Frame_9.background = img
        bg = Frame_9.create_image(25,235, anchor=tk.NW, image=img)

        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            if resp_6_get.get() == "!":
                mensaje_1 = Label(Frame_9,text = 'Eres muy inteligente,\nesa estaba difícil', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',18)).place(relx = 0.5,y = 500, anchor = CENTER)
                Text0_frame_2 = Label(Frame_9, text='Lo ves? Después de\n todo no fue nada del\n otro mundo', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx= 0.8, y=300, anchor = CENTER)
                vdd = 1
            else:
                messagebox.showwarning(title = "Respondiste mal :(", message = "Tómate tu tiempo, esta es un poco difícil...")
            if vdd == 1:
                ext0_frame_2 = Label(Frame_9, text='Ahora veremos otras funciones interesantes', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(x =400 , y=580)
                boton1 = tk.Button(Frame_9 , text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_9, 10,frameant)).place(x = 900 ,y = 480)  
    def Decimo_Frame(frameant):
        """
        Tiene la funcion de crear el decimo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_10 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_10.pack()
        Frame_10.config(bg='#87CEFA')
        Frame_10.config(width='1280', height='700')
        Frame_10.config(bd=20)
        Frame_10.config(relief="groove")
        Text_titulo_frame_4 = Label(Frame_10, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_10, text='Ahora te enseñaremos una función basada en el código ASCII. Bueno, para evitarnos\n una larga explicación aburrida, diremos que el código ASCII, le asigna un número a una letra\n, caracater o símbolo. El código ASCII, es muy largo, y es tedioso tener que buscar en \nla tabla el valor que necesitemos, sin embargo el código ASCII, suele ser muy útil en ocasiones\nPara tu fortuna y la de todos, existe una función que le asigna ese número a la letra que queramos!\nEl nombre de esta función es: ord()\nGrandioso no?, con esto podrías hacer códigos secretos, contraseñas fuertes, e incluso juegos!', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        Text0_frame_4 = Label(Frame_10, text='',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x=260, y = 400)
        botonaretroceso = tk.Button(Frame_10, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_10, 9,frameant)).place(x=100, y=480)         
        boton1 = tk.Button(Frame_10 , text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_10, 11,frameant)).place(x = 900 ,y = 480)                  
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/ascii.png").resize((130,130)))
        Frame_10.background = img
        bg = Frame_10.create_image(580,485, anchor=tk.NW, image=img)

    def Onceavo_Frame(frameant):
        """
        Tiene la funcion de crear el onceavo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_11 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_11.pack()
        Frame_11.config(bg='#87CEFA')
        Frame_11.config(width='1280', height='700')
        Frame_11.config(bd=20)
        Frame_11.config(relief="groove")
        resp_8_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_11, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_11, text='Para usarla sólo debes escribir algo como esto:\nord(aquí_pones_la_letra_símbolo_o_signo)\nInténtalo tú mismo, recuerda que la función ord()\nSOLAMENTE, recibe UN caracter,signo o símbolo', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        Text0_frame_4 = Label(Frame_11, text='Vamos! Intentalo!:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x= 280, y = 320)
        respuesta_3 =  Entry(Frame_11, width = 10, font = ("Comic Sans", 20),textvariable = resp_8_get).place(relx = 0.5, y = 340,anchor = CENTER)
        boton_comprov = tk.Button(Frame_11, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(relx=0.60, y = 320)
        botonaretroceso = tk.Button(Frame_11, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_11, 10,frameant)).place(x = 100, y = 480)            
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/traducir.png").resize((130,130)))
        Frame_11.background = img
        bg = Frame_11.create_image(59,300, anchor=tk.NW, image=img)

        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            rpt_ord = resp_8_get.get()
            if rpt_ord[:4] == "ord(":
                if rpt_ord[-1] == ")":
                    if rpt_ord[4] == '"' or rpt_ord[4] == "'":
                        if rpt_ord[-2] == '"' or rpt_ord[-2] == "'":
                            if len(rpt_ord) == 8:
                                    Text1_frame_4 = Label(Frame_11, text='Bien hecho, el ord de este caracter es:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x= 380, y = 500)
                                    Text3_frame_4 = Label(Frame_11, text= ord(rpt_ord[5]),bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx= 0.5, y = 550)
                                    vdd = 1      
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass            
                else:
                    pass             
            if vdd != 1:
                messagebox.showwarning(title = "Incorrecto unu", message = "Vamos, inténtalo de nuevo!")
            else: 
                vdd = 1
                boton1 = tk.Button(Frame_11 , text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_11, 12,frameant)).place(x = 900 ,y = 480)  
    def Doceavo_Frame(frameant):
        """
        Tiene la funcion de crear el doceavo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_12 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_12.pack()
        Frame_12.config(bg='#87CEFA')
        Frame_12.config(width='1280', height='700')
        Frame_12.config(bd=20)
        Frame_12.config(relief="groove")
        resp_10_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_12, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_12, text='Ahora aprenderemos una función llamada round(), esta\n función, redondea un valor al entero más cercano\nPara que lo veas más claro mira este ejemplo:      \nprint(round(4.14172695))                            \n>>> 4                                                          \nMira este otro ejemplo:                                          \nprint(round(5.6))                                           \n>>> 6                                                         \n', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=300, anchor = CENTER)
        botonaretroceso = tk.Button(Frame_12, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_12, 11,frameant)).place(x=100, y=480)
        boton1 = tk.Button(Frame_12 , text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_12, 13,frameant)).place(x = 900 ,y = 480)  
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/regalo.png").resize((130,130)))
        Frame_12.background = img
        bg = Frame_12.create_image(1050,300, anchor=tk.NW, image=img)

    def Trece_Doceavo(frameant):
        """
        Tiene la funcion de crear el frame intermedio entre el doceavo y el treceavo de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_12 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_12.pack()
        Frame_12.config(bg='#87CEFA')
        Frame_12.config(width='1280', height='700')
        Frame_12.config(bd=20)
        Frame_12.config(relief="groove")
        resp_10_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_12, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_12, text='Puede parecer muy simple, pero esta función es muy útil\nInténtalo hacer tú mismo con base a los ejemplos anteriores\nPor ejemplo: podrías hacer algo como: round(2.17) ', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=240, anchor = CENTER)
        Text0_frame_4 = Label(Frame_12, text='Vamos! Intentalo!:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x= 280, y = 362)
        botonaretroceso = tk.Button(Frame_12, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_12, 12,frameant)).place(x=100, y=480)
        respuesta_3 =  Entry(Frame_12, width = 10, font = ("Comic Sans", 20),textvariable = resp_10_get).place(relx = 0.5, y = 380,anchor = CENTER) 
        boton_comprov = tk.Button(Frame_12, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=760, y = 350)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/es-aproximadamente-igual-a.png").resize((90,90)))
        Frame_12.background = img
        bg = Frame_12.create_image(600,550, anchor=tk.NW, image=img)

        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            vdd = 0
            rpt_round = resp_10_get.get()
            if rpt_round[:6] == "round(":
                if rpt_round[6] != '"' and rpt_round[6] != "'":
                    if rpt_round[-2] != '"' and rpt_round[-2] != "'":
                        if rpt_round[6:-1] not in "qwertyuiopasdfghjklñzxcvbnmWERTYUIOPASDFGJKLÑZXCVBNM'" and rpt_round[6:-1] not in '"qwertyuiopasdfghjklñzxcvbnmWERTYUIOPASDFGJKLÑZXCVBNM':
                            if rpt_round[-1] == ")":
                                n = float(rpt_round[6:-1])
                                r = (round(n))
                                mensaje = ("Muy bien!, el resultado es:")
                                Text0_frame_4 = Label(Frame_12, text = mensaje +"\n" + str(r),bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y = 480, anchor = CENTER)
                                boton1 = tk.Button(Frame_12 , text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_12,0,frameant)).place(x = 900 ,y = 480)  
                                vdd = 1
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            if vdd != 1:                    
                messagebox.showwarning(title = "Incorrecto unu", message = "Vamos, inténtalo de nuevo!")
                vdd_round = 0
    def Treceavo_Frame(frameant):
        """
        Tiene la funcion de crear el treceavo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_13 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_13.config(bg='#87CEFA')
        Frame_13.config(width='1280', height='700')
        Frame_13.config(bd=20)
        Frame_13.config(relief="groove")
        Frame_13.pack() 
        resp_10_get = StringVar()
        Text_titulo_frame_4 = Label(Frame_13, text='¡NOMBRES DE FUNCIONES!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_6 = Label(Frame_13, text="Finalmente tenemos la función type(), esta nos devuelve el tipo de valor\n puesto dentro de sus paréntesis; Mira el siguiente ejemplo:\nprint(type('3.14'))\n>>> <class'str'>     \nATENTO! Pregunta! que respuesta crees que retorne la siguiente sección de código?\ntype(3/4)\n#)<class'float'                                                             \n*)<class'int'>                                                              \n=)<class'float'>                                                            ", bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=250, anchor=CENTER)
        Text0_frame_4 = Label(Frame_13, text='Adelante!',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(x=480, y = 400) 
        respuesta_3 =  Entry(Frame_13, width = 3, font = ("Comic Sans", 20),textvariable = resp_10_get).place(relx = 0.5, y = 400)
        boton_comprov = tk.Button(Frame_13, text = "!Listo¡", font=("Comic Sans", 20), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: mira_respuestas()).place(x=720, y = 400)
        botonaretroceso = tk.Button(Frame_13, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_13, 12,frameant)).place(x=100, y=480)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/archivo.png").resize((60,60)))
        Frame_13.background = img
        bg = Frame_13.create_image(1050,35, anchor=tk.NW, image=img)

        def mira_respuestas():
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            rpt_type = resp_10_get.get()
            if rpt_type == "=":
                Text0_frame_4 = Label(Frame_13, text='Muy bien! Hasta pronto!',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y = 500, anchor = CENTER)     
                boton1 = tk.Button(Frame_13 , text="Finalizar", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_13, 14,frameant)).place(x = 900 ,y = 480)  
            else:                    
                messagebox.showwarning(title = "Incorrecto unu", message = "Oh no, respuesta incorrecta, inténtalo otra vez!")

def leccion_de_palabras_reservadas(pantalla,frameant):
    """
    En esta funcion se enseñan las bases de las palabras reservadas
    :param tkinter.Canvas pantalla: es la pantalla donde se ubicaran los siguiente frames
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
    :return None
    """
    fale_reser = tk.Canvas(pantalla, width=1280, height=700)
    fale_reser.pack()
    fale_reser.config(bg = '#87CEFA')
    fale_reser.config(width = '1280', height = '700')
    fale_reser.config(bd = 20)
    fale_reser.config(relief = "groove")
    resp_1_get = StringVar()
    cont_de_preguntas = 0
    titulo_adi_num = Label(fale_reser,text = '¡PALABRAS RESERVADAS!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',40)).place(x = 270, y = 50)
    sub_titulo = Label(fale_reser,text = '¡Bienvenido a otra lección con PLAYTHON!', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',17)).place(x = 395,y = 120)
   
    linea_1 = Label(fale_reser,text = "¿Alguna vez, trataste de usar la palabra print como nombre de una variable?", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 150,y = 170)
    pista_1 = Label(fale_reser,text = "Si/No: ", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 430,y = 215)  
    respuesta_1 =  Entry(fale_reser, width = 3, font = ("Comic Sans", 26),textvariable = resp_1_get).place(x = 560, y = 215) 
    boton_si_no_1 = tk.Button(fale_reser, text = "Responde!", font = ("Agency",20), height=1, width = 10, bg = '#8EB7F3', fg ='white', command = lambda: mira_respuestas(cont_de_preguntas,frameant) ).place(x = 660 , y = 215)
    img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/reservado.png").resize((100,100)))
    fale_reser.background = img1
    bg1 = fale_reser.create_image(600,400, anchor=tk.NW, image=img1)

    
    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        elif numero == 5:
            Quinto_Frame(frameant)
        else:
            frameant.pack()
   

    def Segundo_Frame(frameant):
        """
        Tiene la funcion de crear el segundo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_2 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        Text_titulo_frame_2 = Label(Frame_2,text='¡PALABRAS RESERVADAS!',bg='#87CEFA', fg='white', font=('Comic Sans', 40)).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Estas palabras están "RESERVADAS" para una tarea en específico', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text='Por ejemplo, no puedes clavar un clavo con un vaso de porcelana, ni escribir con un pedazo de cartón. ',bg='#87CEFA', fg='white', font=('Comic Sans', 18,"bold")).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='De la misma forma, no puedes usar un print como nombre de una variable', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=260, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Un print está hecho para imprimir un mensaje por pantalla, no para alojar un valor, para eso están las variables ', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx=0.5, y=350, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='No te preocupes, no es nada del otro mundo, sólo ten en cuenta que las cosas son hechas para una tarea específica ', bg='#87CEFA', fg='white',font=('Comic Sans', 15,"bold")).place(relx=0.5, y=400, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Exactamente hay 28 palabras reservadas en Python', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=450, anchor=CENTER)
        boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 3,frameant)).place(x = 950 ,y = 500)
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/reloj.jpg").resize((130,130)))
        Frame_2.background = img1
        bg1 = Frame_2.create_image(580,520, anchor=tk.NW, image=img1)

    def Tercer_Frame(frameant):
        """
        Tiene la funcion de crear el tercer frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        def comprobar(res_2_get):
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param res_get_get: Hace referencia al valor obtenido del cuadro de texto, necesario para poder evaluarlo 
            :return None
            """
            word = resp_2_get.get()
            if word == "kwlist" :
                lista_kwlist = [Label(Frame_3, text = palabra, 
                font = ("Comic Sans", 20), bg = '#87CEFA', 
                fg = "white" ).place(x=630, y = 460, anchor=CENTER) for palabra in lista_2kw]
                etiqta_feliz = Label(Frame_3, text='!Ahora puedes ver \nlas palabras reservadas!', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(x= 70, y = 200)
                messagebox.showwarning('Wow!', 'Lo has hecho bien!')    
                etiqta_orden = Label(Frame_3, text='!Observalas \ncon detenimiento', bg='#87CEFA', fg='white',font=('Comic Sans', 19)).place(x= 930, y = 200)
                botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_3, 4,frameant)).place(x=900,y=480)
            else:
                messagebox.showwarning('Ups!', 'Has hecho algo mal, inténtalo otra vez!') 
        Frame_3 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='¡PALABRAS RESERVADAS!',bg='#87CEFA', fg='white', font=('Comic Sans', 40,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='Te enseñaremos a buscarlas por tí mismo, lo único que debes hacer es escribir:', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3,text='kwlist',bg='#87CEFA', fg='white', font=('Comic Sans', 25, "bold")).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='Adelante, inténtalo ! ', bg='#87CEFA', fg='white',font=('Comic Sans', 18)).place(relx=0.5, y=230, anchor=CENTER)
        Text0_frame_3 = Label(Frame_3, text='>>>', bg='#87CEFA', fg='white',font=('Comic Sans', 26)).place(x= 500, y=290, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 20), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2,frameant)).place(x = 100, y=480)
        resp_2_get = StringVar()
        lista_2kw = ["['False', 'None', 'True', 'and', 'as,' 'assert',\n 'async', 'await', 'break', 'class', 'continue',\n 'def',  'del',  'elif',  'else',  'except',  'finally',\n 'for',  'from',  'global', 'if',  'import',  'in', 'is',\n 'lambda',   'nonlocal',  'not',   'or',   'pass', \n 'raise',  'return', 'try', 'while', 'with', 'yield']"]
        
        respuesta_2 =  Entry(Frame_3, width = 8, font = ("Comic Sans", 26),textvariable = resp_2_get).place(relx = 0.5, y = 290, anchor = CENTER)

        boton_comprov = tk.Button(Frame_3, text = "!Listo¡", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command = lambda: comprobar(resp_2_get)).place(x=780, y = 290, anchor = CENTER)
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/observacion.png").resize((180,180)))
        Frame_3.background = img1
        bg1 = Frame_3.create_image(940,300, anchor=tk.NW, image=img1)

           
    def Cuarto_Frame(frameant):
        """
        Tiene la funcion de crear el cuarto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_4 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        Text_titulo_frame_4 = Label(Frame_4, text='¡PALABRAS RESERVADAS!', bg='#87CEFA', fg='white',font=('Comic Sans', 40, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='¿Buscar una palabra en esta lista para saber si es reservada puede ser un poco aburrido verdad?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=130, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='Pero como siempre, nosotros tenemos la solución!\nSólo debes escribir: iskeyword("aquí pones la palabra") y problema resuelto!\nEsto te dará como resultado un:\nTrue en caso de que la palabra sea reservada\nFalse en caso de que la palabra NO sea reservada', bg='#87CEFA',fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=300, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_4, text="Atras", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 3,frameant)).place(x=100, y=480)
        botonavance = tk.Button(Frame_4, text = "Siguiente", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_4, 5,frameant)).place(x=900,y=480)
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/buscar.png").resize((100,100)))
        Frame_4.background = img1
        bg1 = Frame_4.create_image(630,500, anchor=tk.NW, image=img1)

    def Quinto_Frame(frameant):
        """
        Tiene la funcion de crear el quinto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        def comprobar(resp_3_get):
            """
            Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta o actividad propuesta en este frame.
            :param None
            :return None
            """
            intermedia = resp_3_get.get()
            primera = "iskeyword("
            segunda = ")"
            if intermedia[:10] == primera:
                if intermedia[10] == '"' or intermedia[10] == "'" :
                    if intermedia[-2] == '"' or intermedia[-2] == "'":
                        if intermedia[-1] == ")":
                            if intermedia[11:-2] not in "'" and intermedia[11:-2] not in '"':
                                mensajito = Label(Frame_5, text= "Felicidades, lo hiciste bien", bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=530, anchor=CENTER)              
                                messagebox.showwarning('Muy bien!', "Felicidades, lo lograste!")    
                                if iskeyword(intermedia[11:-2]) == True:
                                    otro_mensajito = Label(Frame_5, text= "True", bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=590, anchor=CENTER)
                                else:
                                    otro_mensajito = Label(Frame_5, text= "False", bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=590, anchor=CENTER)    
                                botonavance = tk.Button(Frame_5, text = "FIN", font=("Comic Sans", 20), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_5, 6,frameant)).place(x=900,y=480)
                            else:
                                messagebox.showwarning('Algo anda mal unu!', "¡Intentalo de nuevo!")
                        else:
                            messagebox.showwarning('Algo anda mal unu!', "¡Intentalo de nuevo!")
                    else:
                        messagebox.showwarning('Algo anda mal unu!', "¡Intentalo de nuevo!")           
                else:
                    messagebox.showwarning('Algo anda mal unu!', "¡Intentalo de nuevo!")
            else:                     
                messagebox.showwarning('Algo anda mal unu!', "¡Intentalo de nuevo!")    
        Frame_5 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        Text_titulo_frame_5 = Label(Frame_5,text='¡PALABRAS RESERVADAS!',bg='#87CEFA', fg='white', font=('Comic Sans', 40,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text='Ahora, intentalo tu!', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y = 100, anchor=CENTER)
        Text0_frame_5 = Label(Frame_5,text='Imprime un mensaje por pantalla, usando la anterior sintaxis:',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=140, anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text='TIP: recuerda poner la palabra "entre comillas" ', bg='#87CEFA', fg='white',font=('Comic Sans', 15,"bold")).place(relx=0.5, y=180, anchor=CENTER)
        Text0_frame_5 = Label(Frame_5, text='iskeyword("La palabra") ', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=230, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("comicsansms", 20), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_5, 4,frameant)).place(x=100, y=480)
        resp_3_get = StringVar()
        respuesta_3 =  Entry(Frame_5, width = 20, font = ("Comic Sans", 26),textvariable = resp_3_get).place(x=430, y=300)
        boton_si_no_3 = tk.Button(Frame_5, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda:comprobar(resp_3_get)).place(x=850, y=300)
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/comprobar.png").resize((90,90)))
        Frame_5.background = img1
        bg1 = Frame_5.create_image(880,180, anchor=tk.NW, image=img1)

        
                           
    def mira_respuestas(cont,frameant):
        """
        Tiene la funcion de evaluar o ejecutar una acción de acuerdo a la pregunta del primer frame de la leccion de palabras reservadas.
        :param int cont: sirve para tener un control del boton y que no se use varias veces para evitar errores
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        if cont == 0: 
            vdd = 0
            if resp_1_get.get() == "si" or resp_1_get.get() == "Si" or resp_1_get.get() == "SI" or resp_1_get.get() == "sI":
                mensaje_1 = Label(fale_reser,text = 'Seguramente te salió un error........        ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 395,y = 290)
                vdd = 1
            elif resp_1_get.get() == "no" or resp_1_get.get() == "No" or resp_1_get.get() == "NO" or resp_1_get.get() == "nO":
                mensaje_1 = Label(fale_reser,text = 'Muy bien, de hecho no puedes hacerlo            ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 395,y = 290)
                vdd = 1
            else:
                messagebox.showwarning(title = "Eso es un sí o un no?", message = "Eso no cuenta como respuesta listillo")
                mensaje_1 = Label(fale_reser,text = 'Responde bien >:v              ', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 395,y = 290)
            linea_2 = Label(fale_reser,text = "Esto es debido a que en Python existe algo llamado...                   ", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 100,y = 335)  

            linea_3 = Label(fale_reser,text = "Palabras reservadas del lenguaje", bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 100,y = 370)  
        if vdd != 0:
            boton0 = tk.Button(fale_reser, text="¡Continuemos!", font=("Comic Sans", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(fale_reser, 2,frameant)).place(relx=0.5, y=600, anchor=CENTER)

def leccion_for(pantalla,frameant):
    """
    Enseñamos el funcionamiento del ciclo for y sus usos.
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
    :param tkinter.Canvas pantalla: es donde unicaremos los frames de esta lección y demas items
    :return None
    """
    Frame_1 = tk.Frame()
    Frame_1.pack()
    Frame_1.config(bg='#87CEFA')
    Frame_1.config(width='1280', height='720')
    Frame_1.config(bd=20)
    Frame_1.config(relief="groove")

    def cambiar_frame(frame_dest, numero, frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param int numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        frame_dest.destroy()
        if numero == 2:
            Segundo_Frame(frameant)
        elif numero==3:
            Tercer_Frame(frameant)
        elif numero==4:
            Cuarto_Frame(frameant)
        elif numero==5:
            Quinto_Frame(frameant)
        elif numero==6:
            Sexto_Frame(frameant)
        elif numero==7:
            Septimo_Frame(frameant)
        elif numero==8:
            Octavo_Frame(frameant)
        elif numero==9:
            Noveno_Frame(frameant)
        elif numero==10:
            Decimo_Frame(frameant)
        else:
            frameant.pack()

    Texto_Titulo=Label(Frame_1,text = 'Bienvenido a la lección de:', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(relx=0.5,y=150,anchor=CENTER)
    Texto_imprimir = Label(Frame_1, text='El Ciclo For', bg='#87CEFA', fg='white',font=('Comic Sans', 50,"bold")).place(relx=0.5, y=300, anchor=CENTER)
    boton0 = tk.Button(Frame_1, text="Click para continuar", font=("comicsansms", 20), height=3, width=30, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_1, 2, frameant)).place(relx=0.5, y=500, anchor=CENTER)

    def Segundo_Frame(frameant):
        """
        Tiene la funcion de crear segundo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_2 = tk.Canvas(pantalla, width=1280, height=700)
        Frame_2.pack()
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='1280', height='700')
        Frame_2.config(bd=20)
        Frame_2.config(relief="groove")
        Text_titulo_frame_2 = Label(Frame_2,text='EL CICLO FOR',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_2 = Label(Frame_2, text='Un ciclo for es un bucle que repite el bloque de instrucciones un número prederminado de veces.', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=160, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text="El bloque de instrucciones que se repite se suele llamar cuerpo del bucle \ny cada repetición se llama iteración.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=270, anchor=CENTER)
        Text0_frame_2 = Label(Frame_2,text="Vamos a iniciar presentando la sintaxis del ciclo for.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=380, anchor=CENTER)
        boton1 = tk.Button(Frame_2, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_2, 3,frameant)).place(x=1090,y=580)
        img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes lecciones/for0.png").resize((500, 250)))
        Frame_2.background = img
        bg = Frame_2.create_image(400, 415, anchor=tk.NW, image=img)
    def Tercer_Frame(frameant):
        """
        Tiene la funcion de crear el tercer frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_3 = tk.Frame()
        Frame_3.pack()
        Frame_3.config(bg='#87CEFA')
        Frame_3.config(width='1280', height='700')
        Frame_3.config(bd=20)
        Frame_3.config(relief="groove")
        Text_titulo_frame_3 = Label(Frame_3,text='EL CICLO FOR',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3, text='La sintaxis del bucle for es la siguiente: ', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3,text='for variable in elemento iterable (lista, cadena, range, etc.):\ncuerpo del codigo',bg='#87CEFA', fg='white', font=('Comic Sans', 30,"bold")).place(relx=0.5, y=290,anchor=CENTER)
        Text_titulo_frame_3 = Label(Frame_3, text='Las condiciones que debemos tener en cuenta con el ciclo for, son las siguientes: ', bg='#87CEFA',fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=450, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_3, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_3, 2,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_3, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_3, 4, frameant)).place(x=1090,y=580)

    def Cuarto_Frame(frameant):
        """
        Tiene la funcion de crear el cuarto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_4 = tk.Frame()
        Frame_4.pack()
        Frame_4.config(bg='#87CEFA')
        Frame_4.config(width='1280', height='700')
        Frame_4.config(bd=20)
        Frame_4.config(relief="groove")
        Text_titulo_frame_4 = Label(Frame_4,text='EL CICLO FOR',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text0_frame_4 = Label(Frame_4, text='1. No es necesario definir la variable de control antes del bucle, \naunque se puede utilizar como variable de control una variable ya definida en el programa. ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=160, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text="2. Un bucle for puede tener multiples usos como en listas, tuplas, etc.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=270, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text="3.El cuerpo del bucle se ejecuta tantas veces como elementos tenga el elemento \nrecorrible (elementos de una lista o de un range(), caracteres de una cadena, etc.",bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=380, anchor=CENTER)
        Text0_frame_4 = Label(Frame_4,text="Esto se puede visualizar mejor por el siguiente ejemplo:",bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=550, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_4,text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_4, 3,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_4, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_4, 5,frameant)).place(x=1090,y=580)

    def Quinto_Frame(frameant):
        """
        Tiene la funcion de crear el quinto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_5 = tk.Frame()
        Frame_5.pack()
        Frame_5.config(bg='#87CEFA')
        Frame_5.config(width='1280', height='700')
        Frame_5.config(bd=20)
        Frame_5.config(relief="groove")
        Text_titulo_frame_5 = Label(Frame_5,text='EL CICLO FOR',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_5 = Label(Frame_5, text='Ejemplo: Vamos a imprimir las letras de la palabra "Amigo"', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(relx=0.5, y=120, anchor=CENTER)
        Text_titulo_frame_5 = Label(Frame_5, text='for i in "AMIGO":', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=500, y=190)
        Text_titulo_frame_5 = Label(Frame_5, text='\tprint (i)', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=405, y=230)
        Text_titulo_frame_5 = Label(Frame_5,text='De esta forma, el iterador (i) iria recorriendo la palabra AMIGO,\nimprimiendo letra por letra de la palabra.\n\n\nO en otras palabras, imprimiria A, luego M, luego I, luego G y por ultimo O.\n(Todo separado por un salto de linea)',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=420,anchor=CENTER)
        botonaretroceso = tk.Button(Frame_5, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_5, 4,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_5, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_5, 6,frameant)).place(x=1090,y=580)

    def Sexto_Frame(frameant):
        """
        Tiene la funcion de crear el sexto frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_6 = tk.Frame()
        Frame_6.pack()
        Frame_6.config(bg='#87CEFA')
        Frame_6.config(width='1280', height='700')
        Frame_6.config(bd=20)
        Frame_6.config(relief="groove")
        Text_titulo_frame_6 = Label(Frame_6,text='EL CICLO FOR',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_6 = Label(Frame_6, text='Ahora, vamos a enseñarte otra funcion que es muy util en el ciclo for, la funcion range. \nSu sintaxis es muy similar a la del for inicial, pero en este caso ubicamos la palabra range,\nde la siguiente forma:', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=150, anchor=CENTER)
        Text_titulo_frame_6 = Label(Frame_6,text='for variable in range(numero de veces que se ejecuta el bucle):\ncuerpo del codigo',bg='#87CEFA', fg='white', font=('Comic Sans', 30,"bold")).place(relx=0.5, y=290,anchor=CENTER)
        Text_titulo_frame_6 = Label(Frame_6, text='Debes saber que range() controla el número de veces que se ejecuta el bucle, \ny puede estar definido como por ejemplo, con la longitud de los elementos\n de un elemento iterable.', bg='#87CEFA',fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=450, anchor=CENTER)
        botonaretroceso = tk.Button(Frame_6, text="Atras", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_6, 5,frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_6, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_6, 7,frameant)).place(x=1090,y=580)

    def Septimo_Frame(frameant):
        """
        Tiene la funcion de crear el septimo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_7 = tk.Frame()
        Frame_7.pack()
        Frame_7.config(bg='#87CEFA')
        Frame_7.config(width='1280', height='700')
        Frame_7.config(bd=20)
        Frame_7.config(relief="groove")
        Text_titulo_frame_7 = Label(Frame_7,text='EL CICLO FOR',bg='#87CEFA', fg='white', font=('Comic Sans', 20,"bold")).place(relx=0.5, y=50,anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_7, text='Ejemplo: Vamos a imprimir la palabra HOLA, 3 veces.', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(relx=0.5, y=120, anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_7, text='for i in range(3):', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=500, y=190)
        Text_titulo_frame_7 = Label(Frame_7, text='\tprint("Hola")', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=405, y=230)
        Text_titulo_frame_7 = Label(Frame_7,text='De esta forma, el iterador (i) iria recorriendo desde el numero 0, hasta el numero 2,\nesto sucede, por que toma el rango desde 0 hasta n-1.\n\n\nPodemos mencionar, que se imprimiria HOLA, por cada iteracion.',bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=420,anchor=CENTER)
        botonaretroceso = tk.Button(Frame_7, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_7, 6, frameant)).place(x=20, y=580)
        botonavance = tk.Button(Frame_7, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white', command=lambda: cambiar_frame(Frame_7, 8,frameant)).place(x=1090,y=580)

    def Octavo_Frame(frameant):
        """
        Tiene la funcion de crear el octavo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_8 = tk.Frame()
        Frame_8.pack()
        Frame_8.config(bg='#87CEFA')
        Frame_8.config(width='1280', height='700')
        Frame_8.config(bd=20)
        Frame_8.config(relief="groove")
        Text_titulo_frame_8 = Label(Frame_8, text='EL CICLO FOR', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_8= Label(Frame_8, text='Vamos a ponernos en practica! ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=105, anchor=CENTER)
        Text0_frame_8 = Label(Frame_8, text='Si tenemos el siguiente codigo:', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=180, anchor=CENTER)
        Text_titulo_frame_7 = Label(Frame_8, text='for i in range(3):', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=500, y=260)
        Text_titulo_frame_7 = Label(Frame_8, text='\tprint("i")', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=405, y=300)
        Text0_frame_8 = Label(Frame_8, text='¿Cuales son las salidas?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=460, anchor=CENTER)
        valorescad=["0,1 y 2"]
        valoresrandom=["1,2 y 3","0,1,2 y 3","4,5 y 6","8,9 y 6","ERROR","0,2,3","3,4 y 5","7,6,3 y 4"]
        valor1 = str(random.choice(valoresrandom))
        valor2 = str(random.choice(valorescad))
        valor3 = str(random.choice(valoresrandom))
        selected = IntVar()
        rad1 = Radiobutton(Frame_8, text=valor1, font=("Comic Sans", 15), value=1, bg='#87CEFA',variable=selected).place(x=350, y=500)
        rad2 = Radiobutton(Frame_8, text=valor2, font=("Comic Sans", 15), value=2, bg='#87CEFA',variable=selected).place(relx=0.5, y=518, anchor=CENTER)
        rad3 = Radiobutton(Frame_8, text=valor3, font=("Comic Sans", 15), value=3, bg='#87CEFA',variable=selected).place(x=800, y=500)
        boton_si_no_1 = tk.Button(Frame_8, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(relx=0.5, y=585, anchor=CENTER)
        def comprobar(selected):
            """
            Esta funcion comprueba si la entrada del usuario es correcta en base a distintos parametros.
            :param IntVar selected: Representa la entrada del usuario.
            :return None
            """
            if (selected.get()) == 2:
                messagebox.showinfo('Muy bien :D', 'Elegiste la opcion correcta (' + (valor2)+")")
                botonavance = tk.Button(Frame_8, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_8, 9, frameant)).place(x=1090, y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste la opcion correcta, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_8, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_8, 7, frameant)).place(x=20, y=580)


    def Noveno_Frame(frameant):
        """
        Tiene la funcion de crear el noveno frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_9 = tk.Frame()
        Frame_9.pack()
        Frame_9.config(bg='#87CEFA')
        Frame_9.config(width='1280', height='700')
        Frame_9.config(bd=20)
        Frame_9.config(relief="groove")
        Text_titulo_frame_9 = Label(Frame_9, text='EL CICLO FOR', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_9= Label(Frame_9, text='Vamos a ponernos en practica! ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=105, anchor=CENTER)
        Text0_frame_9 = Label(Frame_9, text='Si tenemos el siguiente codigo:', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=180, anchor=CENTER)
        Text_titulo_frame_9 = Label(Frame_9, text='for i in range(len("hola")):', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=440, y=260)
        Text_titulo_frame_9 = Label(Frame_9, text='\tprint("i")', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=350, y=300)
        Text0_frame_9 = Label(Frame_9, text='¿Cuales son las salidas?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=460, anchor=CENTER)
        valorescad=["0,1 ,2 y 3"]
        valoresrandom=["1,2,3 y 4","5,6,7 y 8","0,1,2","1,2,3","0,1,3","5,6,7 y 9","8,9,0 y 1","5,6,7 y 8","1,2 y 0"]
        valor1 = str(random.choice(valorescad))
        valor2 = str(random.choice(valoresrandom))
        valor3 = str(random.choice(valoresrandom))
        selected = IntVar()
        rad1 = Radiobutton(Frame_9, text=valor1, font=("Comic Sans", 15), value=1, bg='#87CEFA',variable=selected).place(x=350, y=500)
        rad2 = Radiobutton(Frame_9, text=valor2, font=("Comic Sans", 15), value=2, bg='#87CEFA',variable=selected).place(relx=0.5, y=518, anchor=CENTER)
        rad3 = Radiobutton(Frame_9, text=valor3, font=("Comic Sans", 15), value=3, bg='#87CEFA',variable=selected).place(x=800, y=500)
        boton_si_no_1 = tk.Button(Frame_9, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(relx=0.5, y=585, anchor=CENTER)
        def comprobar(selected):
            """
            Esta funcion comprueba si la entrada del usuario es correcta en base a distintos parametros.
            :param IntVar selected: Representa la entrada del usuario.
            :return None
            """
            if (selected.get()) == 1:
                messagebox.showinfo('Muy bien :D', 'Elegiste la opcion correcta (' + (valor1)+")")
                botonavance = tk.Button(Frame_9, text="Siguiente", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_9, 10, frameant)).place(x=1090, y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste la opcion correcta, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_9, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_9, 8, frameant)).place(x=20, y=580)


    def Decimo_Frame(frameant):
        """
        Tiene la funcion de crear el decimo frame de esta lección.
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar la leccion
        :return None
        """
        Frame_10 = tk.Frame()
        Frame_10.pack()
        Frame_10.config(bg='#87CEFA')
        Frame_10.config(width='1280', height='700')
        Frame_10.config(bd=20)
        Frame_10.config(relief="groove")
        Text_titulo_frame_10 = Label(Frame_10, text='EL CICLO FOR', bg='#87CEFA', fg='white',font=('Comic Sans', 20, "bold")).place(relx=0.5, y=50, anchor=CENTER)
        Text0_frame_10= Label(Frame_10, text='Vamos a ponernos en practica! ', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=105, anchor=CENTER)
        Text0_frame_9 = Label(Frame_10, text='Si tenemos el siguiente codigo, y queremos imprimir desde 0 hasta 6:', bg='#87CEFA', fg='white', font=('Comic Sans', 20)).place(relx=0.5, y=180, anchor=CENTER)
        Text_titulo_frame_9 = Label(Frame_10, text='for i in range(_):', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=520, y=260)
        Text_titulo_frame_9 = Label(Frame_10, text='\tprint("i")', bg='#87CEFA', fg='white',font=('Comic Sans', 25, "bold")).place(x=430, y=300)
        Text0_frame_9 = Label(Frame_10, text='¿Cual es el valor que le falta a nuestro codigo?', bg='#87CEFA', fg='white',font=('Comic Sans', 20)).place(relx=0.5, y=460, anchor=CENTER)
        valorescad=["7"]
        valoresrandom=["2","3","6","5","8","9","12","17","1","4","12","1","10"]
        valor1 = str(random.choice(valoresrandom))
        valor2 = str(random.choice(valoresrandom))
        valor3 = str(random.choice(valorescad))
        selected = IntVar()
        rad1 = Radiobutton(Frame_10, text=valor1, font=("Comic Sans", 15), value=1, bg='#87CEFA',variable=selected).place(x=350, y=500)
        rad2 = Radiobutton(Frame_10, text=valor2, font=("Comic Sans", 15), value=2, bg='#87CEFA',variable=selected).place(relx=0.5, y=518, anchor=CENTER)
        rad3 = Radiobutton(Frame_10, text=valor3, font=("Comic Sans", 15), value=3, bg='#87CEFA',variable=selected).place(x=800, y=500)
        boton_si_no_1 = tk.Button(Frame_10, text="Comprueba", font=("Comic Sans", 15), height=1, width=10, bg='#8EB7F3',fg='white', command=lambda: comprobar(selected)).place(relx=0.5, y=585, anchor=CENTER)
        def comprobar(selected):
            """
            Esta funcion comprueba si la entrada del usuario es correcta en base a distintos parametros.
            :param IntVar selected: Representa la entrada del usuario.
            :return None
            """
            if (selected.get()) == 3:
                messagebox.showinfo('Muy bien :D', 'Elegiste la opcion correcta (' + (valor3)+")")
                botonavance = tk.Button(Frame_10, text="Fin", font=("Comic Sans", 10), height=3, width=15, bg='#8EB7F3',fg='white', command=lambda: cambiar_frame(Frame_10, 11, frameant)).place(x=1090,y=580)
            else:
                messagebox.showwarning('ERROR', 'No elegiste la opcion correcta, intenta nuevamente')
        botonaretroceso = tk.Button(Frame_10, text="Atras", font=("Comic Sans", 10), height=3, width=15,bg='#8EB7F3', fg='white',command=lambda: cambiar_frame(Frame_10, 9, frameant)).place(x=20, y=580)

