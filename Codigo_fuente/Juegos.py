import random as rd
import random
import xlrd
import turtle as tl
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pygame,sys,random
from pygame import *
import tkinter as tk
import time
from PIL import ImageTk,Image
from tkinter.messagebox import *
from random import randint
def deduccion_gramatical2(pantalla,frameant):
    """
    Esta funcion genera el primer juego (Deduccion Gramatical) y llama a sus respectivas funciones.
    :param pantalla: Se refiere a la ventana base de nuestro programa.
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
    :return None
    """
    Frame_d = tk.Frame()
    Frame_d.pack()  
    Frame_d.config(bg='#87CEFA')
    Frame_d.config(width='1280', height='700')
    Texto = Label(Frame_d,text = 'Bienvenido a', bg = '#87CEFA',fg = 'white',font =('Comic Sans',20)).place(relx = 0.5, y = 190, anchor = CENTER)
    Titulo_J = Label(Frame_d,text = 'DEDUCCIÓN GRAMATICAL', bg = '#87CEFA',fg = 'white',font =('Comic Sans',60)).place(relx = 0.5, y = 250, anchor = CENTER)
    Instrucciones = Label(Frame_d,text = 'El juego consiste en identificar el\nverbo adecuado que falta en la oracion.\nToma como ayuda el predicado de la\noracion que delata al verbo.',
                          bg = '#87CEFA',fg = 'white',font =('Comic Sans',25)).place(relx = 0.5, y = 420, anchor = CENTER)
    Boton_S = tk.Button(Frame_d, text = "Continuar", font = ("Agency",12), height=2, width = 20, bg = '#8EB7F3', fg ='white', command = lambda: ejercicios(frameant)).place(relx = 0.5, y = 600, anchor = CENTER)
    def ejercicios(frameant):
        """
        Esta funcion genera el segundo frame del juego deduccion gramatical
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        Frame_d.destroy()
        Frame_d2 = tk.Frame()
        Frame_d2.pack()  
        Frame_d2.config(bg='#87CEFA')
        Frame_d2.config(width='1280', height='700')
        
        documento=xlrd.open_workbook('../recursor/Base_de_datos.xlsx') #abrir documento
        oraciones=documento.sheet_by_index(1)  #escoger la hoja

        score=0
        contador=0
        Ejercicio=''
        Puntaje=''
        primer_num=-1
        segundo_num=-1

        def juego(score,primer_num,segundo_num,contador,Ejercicio,Puntaje):
            """
            Esta funcion genera el ejercicio del juego junto con las respuestas de seleccion multiple 
            :param int score: representa el puntaje del usuario
            :param int primer_num: representa el numero generado en la primera ronda del juego
            :param int segundo_num: representa el segundo numero generado en la segunda ronda del juego
            :param int contador: es un numero que cuenta las veces que se llama la funcion juego
            :param string Ejercicio: representa el ejercicio del usuario
            :param string Puntaje: es la palabra puntaje que se muestra en pantalla
            :return None
            """
            contador+=1
            num=random.randint(1,30)
            while num==primer_num or num==segundo_num:
                num=random.randint(1,30)
            resp2=random.randint(1,30)
            resp3=random.randint(1,30)
            while num==resp2 or num==resp3 or resp2==resp3:
                resp2=random.randint(1,30)
                resp3=random.randint(1,30)

            posicion_resp=random.randint(1,3)
        
            oracion=oraciones.cell_value(num,0)  #obtener el contenido de la hoja
            if contador==1:
                primer_num=num
                Ejercicio = Label(Frame_d2,text = oracion, bg = '#87CEFA',fg = 'white',font =('Comic Sans',40))
                Ejercicio.place(relx = 0.5, y = 100, anchor = CENTER)
                Puntaje = Label(Frame_d2,text = 'Puntaje:'+str(score), bg = '#87CEFA',fg = 'white',font =('Comic Sans',40))
                Puntaje.place(relx = 0.5, y = 620, anchor = CENTER) 
            elif contador==2 or contador==3:
                segundo_num=num
                Ejercicio['text']=oracion
                Puntaje['text']='Puntaje:',score
            else:
                messagebox.showinfo('Puntaje', 'Tu puntaje es '+str(score)+'/3')
                Frame_d2.destroy()
                frameant.pack()
            if posicion_resp==1 and contador!=4:
                Boton_r1 = tk.Button(Frame_d2, text = oraciones.cell_value(num,1), font = ("Agency",34), height=7, width = 10, bg = '#B088FC', fg ='white',
                                     command = lambda: resp_correcta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje) ).place(relx = 0.25, y = 360, anchor = CENTER)
                Boton_r2 = tk.Button(Frame_d2, text = oraciones.cell_value(resp2,1), font = ("Agency",34), height=7, width = 10, bg = '#F28B83', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.5, y = 360, anchor = CENTER)
                Boton_r3 = tk.Button(Frame_d2, text = oraciones.cell_value(resp3,1), font = ("Agency",34), height=7, width = 10, bg = '#87E2E6', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.75, y = 360, anchor = CENTER)
            elif posicion_resp==2 and contador!=4:
                Boton_r1 = tk.Button(Frame_d2, text = oraciones.cell_value(resp2,1), font = ("Agency",34), height=7, width = 10, bg = '#B088FC', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.25, y = 360, anchor = CENTER)
                Boton_r2 = tk.Button(Frame_d2, text = oraciones.cell_value(num,1), font = ("Agency",34), height=7, width = 10, bg = '#F28B83', fg ='white',
                                     command = lambda: resp_correcta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.5, y = 360, anchor = CENTER)
                Boton_r3 = tk.Button(Frame_d2, text = oraciones.cell_value(resp3,1), font = ("Agency",34), height=7, width = 10, bg = '#87E2E6', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.75, y = 360, anchor = CENTER)
            elif contador!=4:
                Boton_r1 = tk.Button(Frame_d2, text = oraciones.cell_value(resp2,1), font = ("Agency",34), height=7, width = 10, bg = '#B088FC', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.25, y = 360, anchor = CENTER)
                Boton_r2 = tk.Button(Frame_d2, text = oraciones.cell_value(resp3,1), font = ("Agency",34), height=7, width = 10, bg = '#F28B83', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.5, y = 360, anchor = CENTER)
                Boton_r3 = tk.Button(Frame_d2, text = oraciones.cell_value(num,1), font = ("Agency",34), height=7, width = 10, bg = '#87E2E6', fg ='white',
                                     command = lambda: resp_correcta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)).place(relx = 0.75, y = 360, anchor = CENTER)
            def resp_correcta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje):
                """
                Esta funcion suma uno al puntaje del usuario y vuelve a llamar a juego para hacer otra ronda 
                :param int score: representa el puntaje del usuario
                :param int primer_num: representa el numero generado en la primera ronda del juego
                :param int segundo_num: representa el segundo numero generado en la segunda ronda del juego
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Ejercicio: representa el ejercicio del usuario
                :param string Puntaje: es la palabra puntaje que se muestra en pantalla
                :return None
                """
                score+=1
                juego(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)
            def resp_incorrecta(score,primer_num,segundo_num,contador,Ejercicio,Puntaje):
                """
                Esta funcion vuelve a llamar a juego para hacer otra ronda 
                :param int score: representa el puntaje del usuario
                :param int primer_num: representa el numero generado en la primera ronda del juego
                :param int segundo_num: representa el segundo numero generado en la segunda ronda del juego
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Ejercicio: representa el ejercicio del usuario
                :param string Puntaje: es la palabra puntaje que se muestra en pantalla
                :return None
                """
                juego(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)

        juego(score,primer_num,segundo_num,contador,Ejercicio,Puntaje)
        
def identifica_la_figura2(pantalla,frameant):
    """
    Funcion principal del juego Adivina identifica la figura, el cual consiste en deduccir que figura geometrica basica se dibuja en pantalla 
    param Tk pantalla: es donde ubicaremos nuestros items frames y demás objetos de este juego
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar elo juego
    :return None
    """
    Frame_i = tk.Frame()
    Frame_i.pack()  
    Frame_i.config(bg='#87CEFA')
    Frame_i.config(width='1280', height='700')
    Texto = Label(Frame_i,text = 'Bienvenido a', bg = '#87CEFA',fg = 'white',font =('Comic Sans',20)).place(relx = 0.5, y = 190, anchor = CENTER)
    Titulo_J = Label(Frame_i,text = 'IDENTIFICA LA FIGURA', bg = '#87CEFA',fg = 'white',font =('Comic Sans',60)).place(relx = 0.5, y = 250, anchor = CENTER)
    Instrucciones = Label(Frame_i,text = 'En la pantalla se\ndibujará la forma de una figura basica,\nresponde que figura encaja\nen la zona blanca.',
                          bg = '#87CEFA',fg = 'white',font =('Comic Sans',25)).place(relx = 0.5, y = 420, anchor = CENTER)
    Boton_S = tk.Button(Frame_i, text = "Continuar", font = ("Agency",12), height=2, width = 20, bg = '#8EB7F3', fg ='white', command = lambda: Juego_iden(frameant)).place(relx = 0.5, y = 600, anchor = CENTER)
    def Juego_iden(frameant):
        """
        Esta funcion genera el segundo frame (area_de_dibujo) del juego identifica la figura
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        Frame_i.destroy()
        def cuadrado():
            """
            Dibuja en el centro un cuadrado en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(4):
                t.forward(200)
                t.left(90)
        def rectangulo():
            """
            Dibuja en el centro un rectángulo en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(100)
            t.left(90)
            t.forward(75)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(4):
                if i%2==0:
                    t.forward(200)
                    t.left(90)
                else:
                    t.forward(150)
                    t.left(90)
        def triangulo_rectangulo():
            """
            Dibuja en el centro un triángulo rectangulo en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(3):
                if i==0:
                    t.forward(200)
                    t.left(90)
                elif i==1:
                    t.forward(200)
                    t.left(135)
                else:
                    t.forward(280)
        def pentagono():
            """
            Dibuja en el centro un pentagono en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(75)
            t.left(90)
            t.forward(130)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(5):
                t.forward(150)
                t.left(72)
        def triangulo_equilatero():
            """
            Dibuja en el centro un triángulo equilatero en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(90)
            t.left(90)
            t.forward(78)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(3):
                t.forward(180)
                t.left(120)
        def circulo():
            """
            Dibuja en el centro un círculo en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.right(90)
            t.forward(120)
            t.left(90)
            t.down()
            t.begin_fill()
            t.circle(120)
        def rombo():
            """
            Dibuja en el centro un rombo en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.right(90)
            t.forward(141)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(4):
                if i==0:
                    t.left(45)
                    t.forward(200)
                else:
                    t.left(90)
                    t.forward(200)
        def trapecio():
            """
            Dibuja en el centro un trapecio en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(100)
            t.left(90)
            t.forward(70)
            t.left(90)
            t.down()
            t.begin_fill()
            t.forward(200)
            t.left(90)
            t.forward(140)
            t.left(90)
            t.forward(165)
        def cruz():
            """
            Dibuja en el centro un cruz en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.left(180)
            t.forward(50)
            t.left(90)
            t.forward(150)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(12):
                if i==2 or i==5 or i==8 or i==11:
                    t.right(180)
                    t.forward(100)
                    t.left(90)
                else:
                    t.forward(100)
                    t.left(90)
        def hexagono():
            """
            Dibuja en el centro un hexagono en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.right(90)
            t.forward(40)
            t.left(90)
            t.left(180)
            t.forward(75)
            t.left(90)
            t.forward(130)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(6):
                t.forward(150)
                t.left(60)
        def heptagono():
            """
            Dibuja en el centro un heptagono en la pantalla de turtle
            No recibe parametros
            :return None
            """
            t.right(90)
            t.forward(40)
            t.left(90)
            t.left(180)
            t.forward(75)
            t.left(90)
            t.forward(130)
            t.left(90)
            t.down()
            t.begin_fill()
            for i in range(7):
                t.forward(150)
                t.left(51.4285)
        primer_num=-1
        segundo_num=-2

        area_dibujo=tk.Canvas(master=pantalla,width=1280,height=700)
        area_dibujo.pack(side='right')
        t=tl.RawTurtle(area_dibujo)
        area_dibujo.config(bg = '#87CEFA')


        Texto_2 = Label(area_dibujo,text = '¿Que figura encaja en el area?', bg = '#87CEFA',fg = 'white',font =('Comic Sans',40)).place(relx = 0.5, y = 90, anchor = CENTER)
        
        score=0
        contador=0
        Puntaje=0
        lista_funciones=(cuadrado,rectangulo,triangulo_rectangulo,pentagono,triangulo_equilatero,circulo,rombo,trapecio,cruz,hexagono,heptagono)
        lista_respuestas=('Cuadrado','Rectangulo','Triangulo Rectangulo','Pentagono','Triangulo Equilatero','Circulo','Rombo','Trapecio','Cruz','Hexagono','Heptagono')
        def juego_I(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas):
            """
            Esta funcion genera el ejercicio del juego identifica la figura junto con las respuestas de seleccion multiple  
            :param int score: representa el puntaje del usuario
            :param int primer_num: representa el numero generado en la primera ronda del juego
            :param int segundo_num: representa el segundo numero generado en la segunda ronda del juego
            :param int contador: es un numero que cuenta las veces que se llama la funcion juego
            :param string Puntaje: es la palabra puntaje que se muestra en pantalla
            :param list lista_funciones: es una lista que contiene el nombre de las funciones de todas las figuras del juego
            :param list lista_respuestas: es una lista que contiene el nombre de las figuras del juego
            :return None
            """
            t.hideturtle()  #esconder tortuga
            t.pensize(4) #ancho del trazo
            t.up()
            t.left(90)
            t.forward(50)
            t.right(90)
            t.color('white')  #color trazo
            
            contador+=1
            num=random.randint(0,10)
            while num==primer_num or num==segundo_num:
                num=random.randint(0,10)
            resp2=random.randint(0,10)
            resp3=random.randint(0,10)
            while num==resp2 or num==resp3 or resp2==resp3:
                resp2=random.randint(0,10)
                resp3=random.randint(0,10)

            figura=lista_funciones[num]
            posicion_resp=random.randint(1,3)
        
            if contador==1:
                primer_num=num
                Puntaje = Label(area_dibujo,text = 'Puntaje:'+str(score), bg = '#87CEFA',fg = 'white',font =('Comic Sans',30))
                Puntaje.place(relx = 0.5, y = 650, anchor = CENTER) 
            elif contador==2 or contador==3:
                segundo_num=num
                Puntaje['text']='Puntaje:',score
            else:
                messagebox.showinfo('Puntaje', 'Tu puntaje es '+str(score)+'/3')
                area_dibujo.destroy()
                frameant.pack()
            if posicion_resp==1 and contador!=4:
                Boton_r1 = tk.Button(area_dibujo, text = lista_respuestas[num], font = ("Agency",24), height=2, width = 16, bg = '#F28B83', fg ='white',
                                     command = lambda: resp_correcta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.25, y = 550, anchor = CENTER)
                Boton_r2 = tk.Button(area_dibujo, text = lista_respuestas[resp2], font = ("Agency",24), height=2, width = 16, bg = '#B088FC', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.5, y = 550, anchor = CENTER)
                Boton_r3 = tk.Button(area_dibujo, text = lista_respuestas[resp3], font = ("Agency",24), height=2, width = 16, bg = '#F5D594', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.75, y = 550, anchor = CENTER)
            elif posicion_resp==2 and contador!=4:
                Boton_r1 = tk.Button(area_dibujo, text = lista_respuestas[resp2], font = ("Agency",24), height=2, width = 16, bg = '#F28B83', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.25, y = 550, anchor = CENTER)
                Boton_r2 = tk.Button(area_dibujo, text = lista_respuestas[num], font = ("Agency",24), height=2, width = 16, bg = '#B088FC', fg ='white',
                                     command = lambda: resp_correcta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.5, y = 550, anchor = CENTER)
                Boton_r3 = tk.Button(area_dibujo, text = lista_respuestas[resp3], font = ("Agency",24), height=2, width = 16, bg = '#F5D594', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.75, y = 550, anchor = CENTER)
            elif contador!=4:
                Boton_r1 = tk.Button(area_dibujo, text = lista_respuestas[resp2], font = ("Agency",24), height=2, width = 16, bg = '#F28B83', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.25, y = 550, anchor = CENTER)
                Boton_r2 = tk.Button(area_dibujo, text = lista_respuestas[resp3], font = ("Agency",24), height=2, width = 16, bg = '#B088FC', fg ='white',
                                     command = lambda: resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.5, y = 550, anchor = CENTER)
                Boton_r3 = tk.Button(area_dibujo, text = lista_respuestas[num], font = ("Agency",24), height=2, width = 16, bg = '#F5D594', fg ='white',
                                     command = lambda: resp_correcta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)).place(relx = 0.75, y = 550, anchor = CENTER)
            if contador!=4:
                figura()
                t.end_fill()
            def resp_correcta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas):
                """
                Esta funcion suma uno al score y reinicia la posicion del trazo, vuelve a llamar a juego_I para otra ronda  
                :param int score: representa el puntaje del usuario
                :param int primer_num: representa el numero generado en la primera ronda del juego
                :param int segundo_num: representa el segundo numero generado en la segunda ronda del juego
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Puntaje: es la palabra puntaje que se muestra en pantalla
                :param list lista_funciones: es una lista que contiene el nombre de las funciones de todas las figuras del juego
                :param list lista_respuestas: es una lista que contiene el nombre de las figuras del juego
                :return None
                """
                score+=1
                t.reset()
                juego_I(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)
            def resp_incorrecta(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas):
                """
                Esta funcion reinicia la posicion del trazo y vuelve a llamar a juego_I para la otra ronda  
                :param int score: representa el puntaje del usuario
                :param int primer_num: representa el numero generado en la primera ronda del juego
                :param int segundo_num: representa el segundo numero generado en la segunda ronda del juego
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Puntaje: es la palabra puntaje que se muestra en pantalla
                :param list lista_funciones: es una lista que contiene el nombre de las funciones de todas las figuras del juego
                :param list lista_respuestas: es una lista que contiene el nombre de las figuras del juego
                :return None
                """
                t.reset()
                juego_I(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)

        juego_I(score,primer_num,segundo_num,contador,Puntaje,lista_funciones,lista_respuestas)
        
def organiza_la_oracion(pantalla,frameant):
    """
    Funcion principal del juego organiza la oracion, este consiste en ordenar de la forma correcta una serie de palabras en pantalla
    param Tk pantalla: es donde ubicaremos nuestros items frames y demás objetos de este juego
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
    :return None
    """
    Frame_o = tk.Frame()
    Frame_o.pack()  
    Frame_o.config(bg='#87CEFA')
    Frame_o.config(width='1280', height='700')
    Texto = Label(Frame_o,text = 'Bienvenido a', bg = '#87CEFA',fg = 'white',font =('Comic Sans',20)).place(relx = 0.5, y = 190, anchor = CENTER)
    Titulo_J = Label(Frame_o,text = 'ORGANIZA LA ORACION', bg = '#87CEFA',fg = 'white',font =('Comic Sans',60)).place(relx = 0.5, y = 250, anchor = CENTER)
    Instrucciones = Label(Frame_o,text = 'El juego consiste en que ordenes la\noración que se muestre en pantalla,\nspresiona los botones como lo creas.\nToma en cuenta como pista\nla letra que inicie con mayúscula.',
                          bg = '#87CEFA',fg = 'white',font =('Comic Sans',22)).place(relx = 0.5, y = 420, anchor = CENTER)
    Boton_S = tk.Button(Frame_o, text = "Continuar", font = ("Agency",12), height=2, width = 20, bg = '#8EB7F3', fg ='white', command = lambda: Juego_orga(frameant)).place(relx = 0.5, y = 600, anchor = CENTER)
    def Juego_orga(frameant):
        """
        Esta funcion genera el segundo frame del juego organiza la oracion
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        Frame_o.destroy()
        Frame_o2 = tk.Frame()
        Frame_o2.pack()  
        Frame_o2.config(bg='#87CEFA')
        Frame_o2.config(width='1280', height='700')
        
        documento=xlrd.open_workbook('../recursor/Base_de_datos.xlsx') #llamar el documento
        ejercicios=documento.sheet_by_index(0)

        num=random.randint(1,25)
        posicion_ejercicio1=num
        texto=ejercicios.cell_value(num,0)  #obtener contenido de una celda random
        respuesta_correcta=ejercicios.cell_value(num,1)

        lista_texto=texto.split()
        resp_u=''

        Ejercicio = Label(Frame_o2,text = texto, bg = '#87CEFA',fg = 'white',font =('Comic Sans',48))
        Ejercicio.place(relx = 0.5, y = 70, anchor = CENTER)

        score=0
        contador=0
        Resp=''
        num_letras_texto=len(lista_texto)
        def Juego_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant):
            """
            Esta funcion genera el ejercicio del juego identifica la figura junto con las respuestas de seleccion multiple
            :param string resp_u: representa la respuesta del usuario
            :param int contador: es un numero que cuenta las veces que se llama la funcion juego
            :param string Resp: es la respuesta del usuario que se muestra en pantalla
            :param respuesta_correcta: es una cadena que representa la oracion ya organizada
            :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
            :param list lista_texto: es una lista que contiene las letras del ejercicio
            :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
            :return None
            """
            contador+=1
            if contador==2:
                Resp = Label(Frame_o2,text = resp_u, bg = '#87CEFA',fg = 'white',font =('Comic Sans',42))
                Resp.place(relx = 0.5, y = 620, anchor = CENTER) 
            elif contador!=1:
                Resp['text']= resp_u

            if num_letras_texto==4:
                Boton_r1 = tk.Button(Frame_o2, text = lista_texto[0], font = ("Agency",32), height=3, width = 14, bg = '#F28B83', fg ='white',
                                    command = lambda: construyendo_resp(0,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.3, y = 260, anchor = CENTER)
                Boton_r2 = tk.Button(Frame_o2, text = lista_texto[1], font = ("Agency",32), height=3, width = 14, bg = '#B088FC', fg ='white',
                                    command = lambda: construyendo_resp(1,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.7, y = 260, anchor = CENTER)
                Boton_r3 = tk.Button(Frame_o2, text = lista_texto[2], font = ("Agency",32), height=3, width = 14, bg = '#87E2E6', fg ='white',
                                    command = lambda: construyendo_resp(2,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.3, y = 470, anchor = CENTER)
                Boton_r4 = tk.Button(Frame_o2, text = lista_texto[3], font = ("Agency",32), height=3, width = 14, bg = '#87E2E6', fg ='white',
                                    command = lambda: construyendo_resp(3,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.7, y = 470, anchor = CENTER)
            elif num_letras_texto==5:
                Boton_r1 = tk.Button(Frame_o2, text = lista_texto[0], font = ("Agency",32), height=3, width = 10, bg = '#F28B83', fg ='white',
                                    command = lambda: construyendo_resp(0,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.25, y = 260, anchor = CENTER)
                Boton_r2 = tk.Button(Frame_o2, text = lista_texto[1], font = ("Agency",32), height=3, width = 10, bg = '#B088FC', fg ='white',
                                    command = lambda: construyendo_resp(1,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.5, y = 260, anchor = CENTER)
                Boton_r3 = tk.Button(Frame_o2, text = lista_texto[2], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                    command = lambda: construyendo_resp(2,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.75, y = 260, anchor = CENTER)
                Boton_r4 = tk.Button(Frame_o2, text = lista_texto[3], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                    command = lambda: construyendo_resp(3,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.37, y = 470, anchor = CENTER)
                Boton_r5 = tk.Button(Frame_o2, text = lista_texto[4], font = ("Agency",32), height=3, width = 10, bg = '#BBFC88', fg ='white',
                                    command = lambda: construyendo_resp(4,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.62, y = 470, anchor = CENTER)
            elif num_letras_texto==6:
                Boton_r1 = tk.Button(Frame_o2, text = lista_texto[0], font = ("Agency",32), height=3, width = 10, bg = '#F28B83', fg ='white',
                                    command = lambda: construyendo_resp(0,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.25, y = 260, anchor = CENTER)
                Boton_r2 = tk.Button(Frame_o2, text = lista_texto[1], font = ("Agency",32), height=3, width = 10, bg = '#B088FC', fg ='white',
                                    command = lambda: construyendo_resp(1,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.5, y = 260, anchor = CENTER)
                Boton_r3 = tk.Button(Frame_o2, text = lista_texto[2], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                    command = lambda: construyendo_resp(2,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.75, y = 260, anchor = CENTER)
                Boton_r4 = tk.Button(Frame_o2, text = lista_texto[3], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                    command = lambda: construyendo_resp(3,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.25, y = 470, anchor = CENTER)
                Boton_r5 = tk.Button(Frame_o2, text = lista_texto[4], font = ("Agency",32), height=3, width = 10, bg = '#BBFC88', fg ='white',
                                    command = lambda: construyendo_resp(4,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.5, y = 470, anchor = CENTER)
                Boton_r6 = tk.Button(Frame_o2, text = lista_texto[5], font = ("Agency",32), height=3, width = 10, bg = '#8EB7F3', fg ='white',
                                    command = lambda: construyendo_resp(5,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.75, y = 470, anchor = CENTER)

            Boton_reini = tk.Button(Frame_o2, text = 'Reiniciar', font = ("Agency",16), height=1, width = 10, bg = '#8EB7F3', fg ='white',
                                command = lambda: reiniciar(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.82, y = 625, anchor = CENTER)

            def construyendo_resp(n,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant):
                """
                Esta funcion suma la palabra seleccionada del usuario a su respuesta y verifica al estar completa si esta bien o mal
                :param string resp_u: representa la respuesta del usuario
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Resp: es la respuesta del usuario que se muestra en pantalla
                :param respuesta_correcta: es una cadena que representa la oracion ya organizada
                :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
                :param list lista_texto: es una lista que contiene las letras del ejercicio
                :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
                :return None
                """
                if lista_texto[n] in resp_u.split():
                    messagebox.showerror('Organiza la oracion','Ya oprimiste ese boton')  #widget mensaje de error
                elif contador==1:
                    resp_u+=lista_texto[n]
                else:
                    resp_u+=(' '+lista_texto[n])
                if resp_u==respuesta_correcta:
                    messagebox.showinfo('Muy bien', 'Respuesta correcta,felicidades')
                    ronda2(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)
                elif len(resp_u)==len(respuesta_correcta):
                    messagebox.showinfo('Mal', 'Esta mal,intentalo de nuevo')
                    Juego_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
                else:
                    Juego_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
            def reiniciar(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant):
                """
                Esta funcion reinicia la respuesta del usuario
                :param string resp_u: representa la respuesta del usuario
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Resp: es la respuesta del usuario que se muestra en pantalla
                :param respuesta_correcta: es una cadena que representa la oracion ya organizada
                :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
                :param list lista_texto: es una lista que contiene las letras del ejercicio
                :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
                :return None
                """
                resp_u=''
                contador=0
                Resp['text']=''
                Juego_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
        def ronda2(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant):
            """
            Esta funcion genera el segundo frame del juego identifica la figura
            :param string resp_u: representa la respuesta del usuario
            :param int contador: es un numero que cuenta las veces que se llama la funcion juego
            :param string Resp: es la respuesta del usuario que se muestra en pantalla
            :param respuesta_correcta: es una cadena que representa la oracion ya organizada
            :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
            :param list lista_texto: es una lista que contiene las letras del ejercicio
            :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
            :return None
            """
            Frame_o2.destroy()
            Frame_o3 = tk.Frame()
            Frame_o3.pack()  
            Frame_o3.config(bg='#87CEFA')
            Frame_o3.config(width='1280', height='700')
                    
            num=random.randint(1,25)

            while num==posicion_ejercicio1:
                num=random.randint(1,25)

            texto=ejercicios.cell_value(num,0)  #obtener contenido de una celda random
            respuesta_correcta=ejercicios.cell_value(num,1)

            lista_texto=texto.split()
            resp_u=''
            Ejercicio = Label(Frame_o3,text = texto, bg = '#87CEFA',fg = 'white',font =('Comic Sans',40))
            Ejercicio.place(relx = 0.5, y = 70, anchor = CENTER)
            contador=0
            num_letras_texto=len(lista_texto)
            def Juego2_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant):
                """
                Esta funcion genera el segundo ejercicio del juego identifica la figura junto con las respuestas de seleccion multiple
                :param string resp_u: representa la respuesta del usuario
                :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                :param string Resp: es la respuesta del usuario que se muestra en pantalla
                :param respuesta_correcta: es una cadena que representa la oracion ya organizada
                :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
                :param list lista_texto: es una lista que contiene las letras del ejercicio
                :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
                :return None
                """
                contador+=1
                if contador==2:
                    Resp = Label(Frame_o3,text = resp_u, bg = '#87CEFA',fg = 'white',font =('Comic Sans',42))
                    Resp.place(relx = 0.5, y = 620, anchor = CENTER) 
                elif contador!=1:
                    Resp['text']= resp_u

                if num_letras_texto==4:
                    Boton_r1 = tk.Button(Frame_o3, text = lista_texto[0], font = ("Agency",32), height=3, width = 14, bg = '#F28B83', fg ='white',
                                        command = lambda: construyendo_resp(0,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.3, y = 260, anchor = CENTER)
                    Boton_r2 = tk.Button(Frame_o3, text = lista_texto[1], font = ("Agency",32), height=3, width = 14, bg = '#B088FC', fg ='white',
                                        command = lambda: construyendo_resp(1,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.7, y = 260, anchor = CENTER)
                    Boton_r3 = tk.Button(Frame_o3, text = lista_texto[2], font = ("Agency",32), height=3, width = 14, bg = '#87E2E6', fg ='white',
                                        command = lambda: construyendo_resp(2,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.3, y = 470, anchor = CENTER)
                    Boton_r4 = tk.Button(Frame_o3, text = lista_texto[3], font = ("Agency",32), height=3, width = 14, bg = '#87E2E6', fg ='white',
                                        command = lambda: construyendo_resp(3,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.7, y = 470, anchor = CENTER)
                elif num_letras_texto==5:
                    Boton_r1 = tk.Button(Frame_o3, text = lista_texto[0], font = ("Agency",32), height=3, width = 10, bg = '#F28B83', fg ='white',
                                        command = lambda: construyendo_resp(0,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.25, y = 260, anchor = CENTER)
                    Boton_r2 = tk.Button(Frame_o3, text = lista_texto[1], font = ("Agency",32), height=3, width = 10, bg = '#B088FC', fg ='white',
                                        command = lambda: construyendo_resp(1,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.5, y = 260, anchor = CENTER)
                    Boton_r3 = tk.Button(Frame_o3, text = lista_texto[2], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                        command = lambda: construyendo_resp(2,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.75, y = 260, anchor = CENTER)
                    Boton_r4 = tk.Button(Frame_o3, text = lista_texto[3], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                        command = lambda: construyendo_resp(3,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.37, y = 470, anchor = CENTER)
                    Boton_r5 = tk.Button(Frame_o3, text = lista_texto[4], font = ("Agency",32), height=3, width = 10, bg = '#BBFC88', fg ='white',
                                        command = lambda: construyendo_resp(4,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.62, y = 470, anchor = CENTER)
                elif num_letras_texto==6:
                    Boton_r1 = tk.Button(Frame_o3, text = lista_texto[0], font = ("Agency",32), height=3, width = 10, bg = '#F28B83', fg ='white',
                                        command = lambda: construyendo_resp(0,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.25, y = 260, anchor = CENTER)
                    Boton_r2 = tk.Button(Frame_o3, text = lista_texto[1], font = ("Agency",32), height=3, width = 10, bg = '#B088FC', fg ='white',
                                        command = lambda: construyendo_resp(1,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.5, y = 260, anchor = CENTER)
                    Boton_r3 = tk.Button(Frame_o3, text = lista_texto[2], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                        command = lambda: construyendo_resp(2,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.75, y = 260, anchor = CENTER)
                    Boton_r4 = tk.Button(Frame_o3, text = lista_texto[3], font = ("Agency",32), height=3, width = 10, bg = '#87E2E6', fg ='white',
                                        command = lambda: construyendo_resp(3,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.25, y = 470, anchor = CENTER)
                    Boton_r5 = tk.Button(Frame_o3, text = lista_texto[4], font = ("Agency",32), height=3, width = 10, bg = '#BBFC88', fg ='white',
                                        command = lambda: construyendo_resp(4,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.5, y = 470, anchor = CENTER)
                    Boton_r6 = tk.Button(Frame_o3, text = lista_texto[5], font = ("Agency",32), height=3, width = 10, bg = '#8EB7F3', fg ='white',
                                        command = lambda: construyendo_resp(5,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.75, y = 470, anchor = CENTER)

                Boton_reini = tk.Button(Frame_o3, text = 'Reiniciar', font = ("Agency",16), height=1, width = 10, bg = '#8EB7F3', fg ='white',
                                    command = lambda: reiniciar(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant)).place(relx = 0.82, y = 625, anchor = CENTER)

                def construyendo_resp(n,resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant):
                    """
                    Esta funcion suma la palabra seleccionada a la respuesta del usuario y al estar terminada dice si esta bien o mal en la segunda ronda
                    :param string resp_u: representa la respuesta del usuario
                    :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                    :param string Resp: es la respuesta del usuario que se muestra en pantalla
                    :param respuesta_correcta: es una cadena que representa la oracion ya organizada
                    :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
                    :param list lista_texto: es una lista que contiene las letras del ejercicio
                    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
                    :return None
                    """
                    if lista_texto[n] in resp_u.split():
                        messagebox.showerror('Organiza la oracion','Ya oprimiste ese boton')  #widget mensaje de error
                    elif contador==1:
                        resp_u+=lista_texto[n]
                    else:
                        resp_u+=(' '+lista_texto[n])
                    if resp_u==respuesta_correcta:
                        messagebox.showinfo('Muy bien', 'Respuesta correcta,felicidades')
                        Frame_o3.destroy()
                        frameant.pack()
                    elif len(resp_u)==len(respuesta_correcta):
                        messagebox.showinfo('Mal', 'Esta mal,intentalo de nuevo')
                        Juego2_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
                    else:
                        Juego2_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
                def reiniciar(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,frameant):
                    """
                    Esta funcion reinicia la respuesta del usuario en la segunda ronda
                    :param string resp_u: representa la respuesta del usuario
                    :param int contador: es un numero que cuenta las veces que se llama la funcion juego
                    :param string Resp: es la respuesta del usuario que se muestra en pantalla
                    :param respuesta_correcta: es una cadena que representa la oracion ya organizada
                    :param int num_letras: es un numero que indica la cantidad de letras del ejercicio
                    :param list lista_texto: es una lista que contiene las letras del ejercicio
                    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
                    :return None
                    """
                    resp_u=''
                    contador=0
                    Resp['text']=''
                    Juego2_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
            Juego2_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)
            

        Juego_O_E(resp_u,contador,Resp,respuesta_correcta,num_letras_texto,lista_texto,frameant)

def adivina_el_num(pantalla,frameant):
    """
    Funcion principal del juego Adivina el número, minijuego que consiste en adivinar un numero del 1 al 100.
    :param Tk pantalla: es donde ubicaremos nuestros items frames y demás objetos de este juego
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
    :return None
    """
    global intentos
    intentos  = 9
    nums_usados = []
    def comprueba_numeros(frameant):
        """
        Compara un número ingrasado con el numero al azar escogido por el computador y da pista sobre su aproximacion
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        global intentos
        oportunidades = Label(fadi_num,text = "                               " , bg = '#87CEFA',fg = 'white',font =('Comic Sans',20)).place(x = 760, y = 250) 
        if intentos == 9:
            oportunidades = Label(fadi_num,text = "Intentos disponibles:  " + str(intentos), bg = '#87CEFA',fg = 'white',font =('Comic Sans',20)).place(x = 760, y = 250) 
        else:
            oportunidades = Label(fadi_num,text = "Intentos disponibles:    " + str(intentos), bg = '#87CEFA',fg = 'white',font =('Comic Sans',20)).place(x = 760, y = 250)     
        try:
            if intentos != 0 :

                if int(num_get.get()) == num_surprise:
                    pista = Label(fadi_num,text = '                             ' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                    showwarning(title = "¡GANASTE MASTER!", message = "¡HAS GANADO, FELICIDADES!")
                    pista = Label(fadi_num,text = '¡LO LOGRASTE ADIVINAR!' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                    fadi_num.destroy()
                    frameant.pack()
                else:
                    intentos -= 1
                    if int(num_get.get()) > num_surprise:
                        pista = Label(fadi_num,text = '                             ' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                        pista = Label(fadi_num,text = '¡Tu número es muy grande  !' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                    else:
                        pista = Label(fadi_num,text = '                             ' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                        pista = Label(fadi_num,text = '¡Tu número es muy pequeño!' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                    nums_usados.append(num_get.get())
            else:
                pista = Label(fadi_num,text = '                             ' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                pista = Label(fadi_num,text = '¡Mala suerte, has perdido! El número era:' , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 90,y = 300)
                num_correct = Label(fadi_num,text = str(num_surprise) , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 300,y = 360)
                showwarning(title = "¡Perdiste!", message = "¡Has perdido, inténtalo otra vez!")
        except ValueError:
            showwarning(title = "Ups!", message = "¡Eso no es un número!")
    fadi_num = tk.Canvas(pantalla, width=1280, height=700)
    fadi_num.pack()
    fadi_num.config(bg = '#87CEFA')
    fadi_num.config(width = '1280', height = '700')
    fadi_num.config(bd = 20)
    fadi_num.config(relief = "groove")
    num_get = StringVar()
    num_surprise = rd.randint(0,101)
    numeros_q_ya_se_usaron = [Label(fadi_num,text = j , bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x =700,y = 900) for j in nums_usados]
    titulo_adi_num = Label(fadi_num,text = '¡ADIVINA EL NÚMERO!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',40)).place(x = 310, y = 50)
    sub_titulo = Label(fadi_num,text = 'Empiezas con 10 intentos para adivinar el número', bg = '#87CEFA', fg = 'white', font = ('Comic Sans',20)).place(x = 290,y = 120)
    ingresa_el_numero = Label(fadi_num,text = '¡Vamos, inténtalo!: ', 
    bg = '#87CEFA', fg = 'white', 
    font = ('Comic Sans',24)
    ).place(x = 270 ,y= 250) 
    img = ImageTk.PhotoImage(Image.open("../recursor/Imagenes juegos/pensando.png").resize((200,200)))
    fadi_num.background = img
    bg = fadi_num.create_image(450,400, anchor=tk.NW, image=img)
    recibe_nums = Entry(fadi_num, width = 3, font = ("Comic Sans", 26),textvariable = num_get).place(x = 590, y = 250) 
    boton_probar = tk.Button(fadi_num, text = "¡PRUEBA!", font = ("Agency",20), height=8, width = 15, bg = '#8EB7F3', fg ='white', command = lambda: comprueba_numeros(frameant) ).place(x = 780 , y = 320)

def ahorcado_global(p_ahor,frameant):
    """
    Funcion encargada de llamar a los tres niveles disponibles del ahorcado
    :param Tk p_ahor: es donde ubicaremos nuestros items frames y demás objetos de este juego
    :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
    :return None
    """
    def menu (frameant):
        """
        Funcion encargada de crear el menu princiapal del juego Ahorcado
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        fh1 = Canvas(p_ahor, width = "1280", height = "700")
        fh1.pack()
        fh1.config(bg = '#87CEFA')
        fh1.config(width = '1280', height = '700')
        fh1.config(bd = 20)
        fh1.config(relief = "groove")
        titulo_ahorcado = Label(fh1,text = '¡AHORCADO EXÁMEN!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',40)).place(x = 340, y = 50)
        Acompañamiento_titulo = Label(fh1,text = '!Escoge un nivel!',bg = '#87CEFA', fg = 'white', font = ('Comic Sans',15)).place(x = 550,y=120)
        boton_basico_p_ahor = tk.Button(fh1, text = "Nivel Básico", font = ("Agency",20), height=8, width = 15, bg = '#8EB7F3', fg ='white', command = lambda: cambiar_frame(fh1, 0,frameant)).place(x = 100 , y = 280)
        boton_intermedio_p_ahor = tk.Button(fh1, text = "Nivel Intermedio", font = ("Agency",20), height=8, width = 15, bg = '#8EB7F3', fg ='white', command = lambda: cambiar_frame(fh1, 1, frameant)).place(x = 500 , y = 280)
        boton_EXPERTO_p_ahor = tk.Button(fh1, text = "Nivel EXPERTO", font = ("Agency",20), height=8, width = 15, bg = '#8EB7F3', fg ='white', command = lambda: cambiar_frame(fh1 ,2,frameant)).place(x = 900 , y = 280)
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes juegos/juego-del-ahorcado.png").resize((130,130)))
        fh1.background = img1
        bg1 = fh1.create_image(1040,60, anchor=tk.NW, image=img1)
    menu(frameant)   
    def cambiar_frame(frame_dest, numero,frameant):
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param string numero: representa el numero de la pantalla que nos encontramos
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        frame_dest.destroy()
        if numero == 0:
            ahorcado_nivel1(frameant)
        elif numero==1:
            ahorcado_intermedio(frameant)
        elif numero == 2:
            ahorcado_EXPERTO(frameant)
        else:    
            ahorcado_global()
    def ahorcado_nivel1(frameant):
        """
        Primer nivel del ahorcado
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        global letras_usadas 
        global oportunities 
        global l_correctas 
        letras_usadas = []
        oportunities = 0
        l_correctas =  0
        def mira_letras():
            """
            Evalua la letra ingresada y verifica si está en la palabra que se debe adivinar
            :param None
            :return None
            """
            global oportunities
            global l_correctas
            letras_usadas.append(letra_get.get())
            if len(letra_get.get()) > 1:
                showwarning(title = "Alto ahí velocista!", message = "Sólo puedes ingresar una letra a la vez unu")
            if letra_get.get() in word:
                if w_sust.count(letra_get.get()) > 1:
                    l_correctas += word.count(letra_get.get())
                    for i in range(word_size):
                        if w_sust[i] == letra_get.get():
                            guiones[i].config(text = "" + letra_get.get())
                        if letra_get.get() in word:
                            word.remove(letra_get.get())
                else:
                    if letra_get.get() in word:
                        word.remove(letra_get.get())
                    l_correctas += 1
                    guiones[w_sust.index(letra_get.get())].config(text = "" + letra_get.get())
                if l_correctas == word_size:
                    showwarning(title = "¡GANASTE MASTER!", message = "¡HAS GANADO, FELICIDADES!")
                    frame.destroy()
                    frameant.pack()
                if letra_get.get() in word:
                    word.remove(letra_get.get())
            else:
                if letra_get.get() in word:
                    word.remove(letra_get.get())
                if oportunities < 5:
                    frame.itemconfig(imagenes_de_un_ahorcado, image = image_s[oportunities + 1])
                oportunities += 1
                if oportunities >= 6:
                    showwarning(title = "Perdiste :c", message = "¡Ya no tienes más intentos!")
                    frame.destroy()
                    frameant.pack()
        palabras = open("../recursor/lista_de_nivel_1.txt", "r")
        pistas = ["Estructura de control condicional: ",
        "Función que permite ingresar valores por teclado: ",
        "Evalua otra condición después del if: ",
        "Tipo de estructura control que permite hacer tareas\n repetitivamente mientras se \ncumpla una condición:",
        "Estructura de control que evalua si una condición se cumple:",
        "Tipo de valor de una cadena de caracteres:",
        "Qué tipo de valor es True? ",
        "Símbolo usado para concatenar:",
        "En qué lenguaje se hizo este juego? "
        ]
        conj_words = list(palabras.read().split("\n"))
        n = randint(0, (len(conj_words) - 1))
        word = conj_words[n]
        global pista
        pista = pistas[n]
        word = list(word) 
        global word_size
        global w_sust
        w_sust = word[:]
        word_size = len(word) 
        letra_get = StringVar()
        frame = Canvas(p_ahor, width = "1280", height = "700")
        frame.config(bg = "#87CEFA")
        frame.config(relief = "groove", bd = 10)
        frame.pack(expand = True, fill = "both")
        
        image_s =[
            PhotoImage(file = "../recursor/Imagenes juegos/01.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/02.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/03.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/04.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/05.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/06.png"),
        ]
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes juegos/engranaje.png").resize((130,130)))
        frame.background = img1
        bg1 = frame.create_image(630,220, anchor=tk.NW, image=img1)

        imagenes_de_un_ahorcado = frame.create_image(1000,350, image = image_s[0])
        titulazo = Label(frame,text = 'AHORCADO!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',35)).place(x = 70, y = 50)
        pregunta_la_letra = Label(frame,text = 'Vamos! Ingresa una letra: ', bg = '#87CEFA',fg = 'white',font =('Comic Sans', 18)).place(x = 70, y = 120)
        recibe_la_letra = Entry(frame, width = 3, font = ("Comic Sans", 25),textvariable = letra_get).place(x = 430, y = 120) 
        mueve_y_compruebe  = tk.Button(frame, text = "¡Listo!", font = ("Agency", 20), height = 2, width = 20, bg = '#8EB7F3',fg = 'white', command = mira_letras).place(x = 200, y = 240)
        PISTA_en_pantalla = Label(frame,text = "Pista: " + pista, bg = '#87CEFA',fg = 'white',font =('Comic Sans', 18)).place(x = 100, y = 400)
        guiones = [Label(frame, text = "_", font = ("Comic Sans", 20), bg = '#87CEFA', fg = "black" ) for _ in word]
        inicialx = 200
        for i in range(len(word)):
            guiones[i].place(x = inicialx, y = 600)
            inicialx += 50
        
    def ahorcado_intermedio(frameant):
        """
        Segundo nivel del ahorcado
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        global letras_usadas 
        global oportunities 
        global l_correctas 
        letras_usadas = []
        oportunities = 0
        l_correctas =  0
        def mira_letras():
            """
            Evalua la letra ingresada y verifica si está en la palabra que se debe adivinar
            :param None
            :return None
            """
            global oportunities
            global l_correctas
            if len(letra_get.get()) > 1:
                showwarning(title = "Alto ahí velocista!", message = "Sólo puedes ingresar una letra a la vez, unu")
            if letra_get.get() in word:
                if w_sust.count(letra_get.get()) > 1: 
                    l_correctas += word.count(letra_get.get())
                    for i in range(word_size):
                        if w_sust[i] == letra_get.get(): 
                            guiones[i].config(text = "" + letra_get.get())
                        if letra_get.get() in word:
                            word.remove(letra_get.get())
                else:
                    if letra_get.get() in word:
                            word.remove(letra_get.get())
                    l_correctas += 1
                    guiones[w_sust.index(letra_get.get())].config(text = "" + letra_get.get())
                if l_correctas == word_size:
                    showwarning(title = "¡GANASTE MASTER!", message = "¡HAS GANADO, FELICIDADES!\n            0_0")
                    frame.destroy()
                    frameant.pack()
                if letra_get.get() in word:
                    word.remove(letra_get.get())
            else:
                if oportunities < 5:
                    frame.itemconfig(imagenes_de_un_ahorcado, image = image_s[oportunities + 1])
                oportunities += 1
                if oportunities >= 6:
                    showwarning(title = "Perdiste :c", message = "¡Ya no tienes más intentos!")
                    frame.destroy()
                    frameant.pack()
        
        palabras = open("../recursor/lista_de_nivel_intermedio.txt", "r")
        conj_words = list(palabras.read().split("\n"))
        n = randint(0, (len(conj_words) - 1))
        global pista
        word = conj_words[n]
        word = list(word)
        pistas = ["Actúa si el if o el elif no lo hace: ",
        "Función que permite imprimir un valor en pantalla: ",
        "Puede romper un ciclo",
        'Qué tipo de dato es "1457" ? ',
        "Con qué palabra reservada se declara un función?",
        "Que forma tiene un 'if' en un diagrama de flujo?",
        "Cómo se escribe el operador de división entera?",
        'La operacion: print("Hola mundo" * 5 ), es válida? si/no,\nEscríbelo en minúsculas!',
        "Función que convierte un string a mayúsculas",
        "Variable que recorre un ciclo for:"]
        pista = pistas[n]
        global word_size
        global w_sust
        w_sust = word[:]
        word_size = len(word)
        
        letra_get = StringVar()
        frame = Canvas(p_ahor, width = "1280", height = "700")
        frame.config(bg = "#87CEFA")
        frame.config(relief = "groove", bd = 10)
        frame.pack(expand = True, fill = "both")
        image_s =[
            PhotoImage(file = "../recursor/Imagenes juegos/01.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/02.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/03.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/04.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/05.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/06.png"),
        ]
        imagenes_de_un_ahorcado = frame.create_image(1000,350, image = image_s[0])
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes juegos/meditacion.png").resize((150,150)))
        frame.background = img1
        bg1 = frame.create_image(630,220, anchor=tk.NW, image=img1)

        titulazo = Label(frame,text = 'AHORCADO!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',35)).place(x = 70, y = 50)
        pregunta_la_letra = Label(frame,text = 'Vamos! Ingresa una letra: ', bg = '#87CEFA',fg = 'white',font =('Comic Sans', 18)).place(x = 70, y = 120)
        recibe_la_letra = Entry(frame, width = 3, font = ("Comic Sans", 25),textvariable = letra_get).place(x = 430, y = 120) 
        mueve_y_compruebe  = tk.Button(frame, text = "¡Prueba!", font = ("Agency", 20), height = 2, width = 20, bg = '#8EB7F3',fg = 'white', command = mira_letras).place(x = 200, y = 240)
    
        pista_en_pantalla = Label(frame,text = "Pista: " + pista, bg = '#87CEFA',fg = 'white',font =('Comic Sans', 18)).place(x = 80, y = 430)
        guiones = [Label(frame, text = "_", font = ("Comic Sans", 25), bg = '#87CEFA', fg = "black" ) for _ in word]
        inicialx = 200
        
        for i in range(len(word)):
            guiones[i].place(x = inicialx, y = 600)
            inicialx += 75
    def ahorcado_EXPERTO(frameant):
        """
        Ahorcado solo apto para 'expertos'
        :param tkinter.Canvas frameant: Se refiere al frame anterior al que nos encontremos actualmente y al cual se regresa luego de terminar el juego
        :return None
        """
        global letras_usadas 
        global oportunities 
        global l_correctas 
        letras_usadas = []
        oportunities = 0
        l_correctas =  0
        def mira_letras():
            """
            Evalua la letra ingresada y verifica si está en la palabra que se debe adivinar
            :param None
            :return None
            """
            global oportunities
            global l_correctas
            letras_usadas.append(letra_get.get())
            if len(letra_get.get()) > 1:
                showwarning(title = "Alto ahí velocista!", message = "Sólo puedes ingresar una letra a la vez, unu")
            if letra_get.get() in word:
                if w_sust.count(letra_get.get()) > 1: 
                    l_correctas += word.count(letra_get.get())
                    for i in range(word_size):
                        if w_sust[i] == letra_get.get(): 
                            guiones[i].config(text = "" + letra_get.get())
                        if letra_get.get() in word:
                            word.remove(letra_get.get())
                else:
                    if letra_get.get() in word:
                            word.remove(letra_get.get())
                    l_correctas += 1
                    guiones[w_sust.index(letra_get.get())].config(text = "" + letra_get.get())
                if l_correctas == word_size:
                    showwarning(title = "¡GANASTE MASTER!", message = "¡HAS GANADO, FELICIDADES!\n            0_0")
                    frame.destroy()
                    frameant.pack()
                if letra_get.get() in word:
                    word.remove(letra_get.get())
            else:
                if oportunities < 5:
                    frame.itemconfig(imagenes_de_un_ahorcado, image = image_s[oportunities + 1])
                oportunities += 1
                if oportunities >= 6:
                    showwarning(title = "Perdiste :c", message = "¡Ya no tienes más intentos!")
                    frame.destroy()
                    frameant.pack()
        
        palabras = open("../recursor/lista_de_experto.txt", "r")
        conj_words = list(palabras.read().split("\n"))
        n = randint(0, (len(conj_words) - 1))
        global pista
        word = conj_words[n]
        word = list(word)
        pistas = ["Cuantos espacios pone 'tab' en un print? (Escríbelo con letras)",
        "lambda es una función?",
        "El código:\nwhile cont <= 10:\n  print('Hola')\n       cont = cont += 1\nEs correcto? si/no",
        "Que tipo de lenguaje es un lenguaje de programación? ",
        "La sentencia, True and False = ,\n tiene como resultado booleano:",
        "Si aplicaramos la función round en\n 4.4999, que valor tendríamos?",
        "Esta función está bien escrita:\ndef hola_mundo()\n    print('Hola a todos!')\nhola_mundo()",
        "Se puede imprimir esto?:\nprint('Hasta aquí, vamos' +  941 + 'lineas de código!')\nSi/No: ",
        "Que función puede convertir la siguiente cadena:\n'Saber Python es lo máximo'\n a la siguiente cadena:\nsABER pYTHON ES LO MAXIMO\n$).swappcase()\n|)No existe esa función\n^).upper()"]
        pista = pistas[n]
        global word_size
        global w_sust
        w_sust = word[:]
        word_size = len(word)
        
        letra_get = StringVar()
        frame = Canvas(p_ahor, width = "1280", height = "700")
        frame.config(bg = "#87CEFA")
        frame.config(relief = "groove", bd = 10)
        frame.pack(expand = True, fill = "both")
        image_s =[
            PhotoImage(file = "../recursor/Imagenes juegos/01.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/02.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/03.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/04.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/05.png"),
            PhotoImage(file = "../recursor/Imagenes juegos/06.png"),
        ]
        imagenes_de_un_ahorcado = frame.create_image(1000,350, image = image_s[0])
        img1 = ImageTk.PhotoImage(Image.open("../recursor/Imagenes juegos/competencia.png").resize((150,150)))
        frame.background = img1
        bg1 = frame.create_image(630,180, anchor=tk.NW, image=img1)

        titulazo = Label(frame,text = 'AHORCADO!', bg = '#87CEFA',fg = 'white',font =('Comic Sans',35)).place(x = 70, y = 50)
        pregunta_la_letra = Label(frame,text = 'Vamos! Ingresa una letra: ', bg = '#87CEFA',fg = 'white',font =('Comic Sans', 18)).place(x = 70, y = 120)
        recibe_la_letra = Entry(frame, width = 3, font = ("Comic Sans", 25),textvariable = letra_get).place(x = 430, y = 120) 
        mueve_y_compruebe  = tk.Button(frame, text = "¡Prueba!", font = ("Agency", 20), height = 2, width = 20, bg = '#8EB7F3',fg = 'white', command = mira_letras).place(x = 200, y = 240)
    
        pista_en_pantalla = Label(frame,text = "Pista: " + pista, bg = '#87CEFA',fg = 'white',font =('Comic Sans', 18)).place(x = 80, y = 370)
        guiones = [Label(frame, text = "_", font = ("Comic Sans", 25), bg = '#87CEFA', fg = "black" ) for _ in word]
        inicialx = 200
        
        for i in range(len(word)):
            guiones[i].place(x = inicialx, y = 600)
            inicialx += 75

def paint():
    """
    Esta funcion genera nuestro paint.
    No recibe
    :return None
    """
    global color
    color="black"
    vinicialx,vinicialy=0,0
    def nuevahoja():
        """
        Esta funcion borra la hoja actual y crea una nueva
        No recibe
        :return None
        """
        canvas.delete("all")
        paleta_de_colores()

    def mostrarcolor(color_nuevo):
        """
        Esta funcion cambia de color al lapiz, en base a la seleccion del usuario.
        :param str color_nuevo:Representa un color disponible
        :return None
        """
        global color
        color=color_nuevo
    def localizarxy(event):
        """
        Esta funcion localiza la posicion del mouse tomando los ejes x y y, ademas que accion se esta haciendo.
        (En este caso presionar un boton)
        :param event: Representa la accion de presionar un boton con el mouse, y la posicion de este en x y y.
        :return None
        """
        global vinicialx,vinicialy
        vinicialx, vinicialy=event.x,event.y
    def anadirLinea(event): #Generamos las lineas
        """
        Esta funcion dibujar una linea en base a la posicion del mouse
        :param event: Representa la accion de presionar un boton con el mouse, y la posicion de este en x y y.
        """
        global vinicialx, vinicialy
        canvas.create_line((vinicialx,vinicialy,event.x,event.y),fill=color)
        vinicialx,vinicialy=event.x,event.y

    def paleta_de_colores():
        """
        Esta funcion, representa la paleta de colores de nuestro programa, y que colores se pueden elegir
        :return None
        """
        id=canvas.create_rectangle((10,130,30,150),fill="orange")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("orange"))

        id=canvas.create_rectangle((10,40,30,60),fill="gray")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("gray"))

        id=canvas.create_rectangle((10,10,30,30),fill="black")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("black"))

        id=canvas.create_rectangle((10,100,30,120),fill="red")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("red"))

        id=canvas.create_rectangle((10,190,30,210),fill="green")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("green"))

        id=canvas.create_rectangle((10,220,30,240),fill="blue")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("blue"))

        id=canvas.create_rectangle((10,250,30,270),fill="purple")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("purple"))

        id=canvas.create_rectangle((10,70,30,90),fill="brown")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("brown"))

        id=canvas.create_rectangle((10,160,30,180),fill="yellow")
        canvas.tag_bind(id,"<Button-1>",lambda valor:mostrarcolor("yellow"))


    ventana=Tk()
    ventana.title('Libera tu creatividad')
    ventana.resizable(False, False)
    ventana.geometry('1280x700')
    ventana.rowconfigure(0,weight=1)
    ventana.columnconfigure(0,weight=1)
    canvas=Canvas(ventana,bg="white")
    ventana.iconbitmap("Imagenes/icono.ico")
    canvas.grid(row=0,column=0,sticky="nsew")#Expandimos el canva en toda direccion
    menu=Menu(ventana)
    ventana.config(menu=menu)
    segundo_menu=Menu(menu,tearoff=0)
    menu.add_cascade(label="Archivo",menu=segundo_menu)
    segundo_menu.add_command(label="Nueva hoja",command=nuevahoja)
    canvas.bind("<Button-1>",localizarxy)
    canvas.bind("<B1-Motion>",anadirLinea)
    paleta_de_colores()



