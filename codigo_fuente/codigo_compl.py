import tkinter as tk
from tkinter import *
from tkinter import ttk
import random as rd
from keyword import iskeyword, kwlist
import random
import xlrd
import time
from time import sleep
import turtle as tl
from os import system
import os

def pantalla_inicial(avance):
    """
    Genera la pantalla que contiene el logo y la seleccion inicial del programa.
    :param int avance: registra el avande del usuario en el area de aprendizaje de python
    No retorna algun valor
    """
    global pantalla
    pantalla = tk.Tk()
    pantalla.title('PLAYTHON')
    pantalla.resizable(False, False)
    pantalla.geometry('480x480')
    pantalla.config(bg = 'blue')
    pantalla.iconbitmap("icono.ico")

    Frame_1 = tk.Frame()  
    Frame_1.pack()
    Frame_1.config(bg = '#87CEFA')
    Frame_1.config(width = '480', height = '480')
    Frame_1.config(bd = 20)
    Frame_1.config(relief = "groove")
    
    imagenLogo = tk.PhotoImage(file = "plaython.png")
    Frameimagen = Label(Frame_1, image = imagenLogo, height = 290, width = 290).place(x = 70, y = 35)
    # creamos el boton

    def cambiar_frame(frame_dest,numero,avance):       
        """
        Tiene la funcion de destruir el frame que se esta utilizando y genera uno nuevo.
        :param string frame_dest: representa el frame que vamos a destruir
        :param string numero: representa el numero de la pantalla que nos encontramos
        :param int avance: registra el avande del usuario en el area de aprendizaje de python
        No retorna algun valor
        """
        frame_dest.destroy()
        if numero==2:
            Segunda_pantalla(avance)
    boton = tk.Button(Frame_1, text = "Click para continuar", font = ("Agency", 10), height = 2, width = 20, bg = '#8EB7F3',fg = 'white', command = lambda: cambiar_frame(Frame_1,2,avance)).place(x = 133, y = 320)
           
    def Segunda_pantalla(avance):
        """
        Esta funcion genera nuestra segunda pantalla
        :param int avance: registra el avande del usuario en el area de aprendizaje
        No recibe parametros, no retorna 
        """
        Frame_2 = tk.Frame()
        Frame_2.pack()  
        Frame_2.config(bg='#87CEFA')
        Frame_2.config(width='480', height='480')
        Frame_2.config(bd = 20)
        Frame_2.config(relief = "groove")
        
        Text_titulo_frame_2 = Label(Frame_2,text = 'PLAYTHON', bg = '#87CEFA',fg = 'white',font =('Comic Sans',42)).place(x = 70, y = 50)
        Acompañamiento_titulo = Label(Frame_2,text = 'Desarrolla tu lógica y aprende Python',bg = '#87CEFA', fg = 'white', font = ('Comic Sans',10)).place(x=110,y=110)
    
        boton4 = tk.Button(Frame_2, text = "Entrena tu cerebro!", font = ("Agency",12), height=2, width = 20, bg = '#8EB7F3', fg ='white', command = lambda: entrena_tu_cerebro(avance)).place(x = 130 , y = 170)
        
    
        boton2 = tk.Button(Frame_2, text = "Vamos a aprender Python!", font =("Agency", 12),height = 2, width = 20, bg = '#8EB7F3', fg = 'white',command=lambda: vamos_a_aprender(avance)).place(x = 130, y = 250)

        boton3 = tk.Button(Frame_2, text = "Ponte a prueba!", font = ("Agency",12), height = 2, width = 20, bg = '#8EB7F3', fg = 'white', command = lambda: Ponte_aprueba(avance)).place(x = 130 , y = 330)    
        system('cls')
    pantalla.mainloop()    
def entrena_tu_cerebro(avance):
    """
    Esta funcion llama a cada uno de los juegos que hacen parte de esta seccion. (Entrena tu cerebro)
    :param int avance: registra el avande del usuario en el area de aprendizaje
    No retorna algun valor
    """
    pantalla.destroy()
    juego1=-1
    juego2=-1
    for ronda in range(3):
        juego = random.randint(0,5)
        while juego==juego1 or juego==juego2:
            juego = random.randint(0,5)
        if ronda==0:
            juego1=juego
        elif ronda==1:
            juego2=juego
        if juego == 0:
            juego_TRIQUI()
        elif juego == 1:
            juego_ppt()
        elif juego == 2:
            identifica_la_figura()
        elif juego == 3:
            deduccion_gramatical()
        elif juego == 4:
            organiza_la_oracion()
        elif juego == 5:
            adivina_el_número()
        time.sleep(3)
        system('cls')
    pantalla_inicial(avance)
def vamos_a_aprender(avance):
    """
    Esta funcion llama a cada uno de los juegos que hacen parte de esta seccion. (Vamos a aprender)
    :param int avance: registra el avande del usuario en el area de aprendizaje de python
    No retorna algun valor
    """
    pantalla.destroy()
    if avance == 0:
        imprimir()
        time.sleep(3)
        system('cls')
        variables()
    elif avance == 1:
        palabras_reservadas()
        time.sleep(3)
        system('cls')
        nombres_de_funciones()
    elif avance == 2:
        leccion_if()
        time.sleep(3)
        system('cls')
        ciclo_while()
    elif avance == 3:
        leccion_break()
        time.sleep(3)
        system('cls')
        ciclo_for()
    avance+=1
    system('cls')
    time.sleep(2)
    pantalla_inicial(avance)

def Ponte_aprueba(avance):
    """
    Esta funcion llama a cada uno de los juegos que hacen parte de esta seccion. (Ponte a prueba)
    :param int avance: registra el avande del usuario en el area de aprendizaje
    No retorna algun valor
    """
    pantalla.destroy()
    Ahorcado_exámen ()
    time.sleep(3)
    system('cls')
    pantalla_inicial(avance)

def deduccion_gramatical():
    """
    Ejecuta el juego deduccion gramatical del area de entrena tu cerebro
    No recibe parametros
    No retorna algun valor
    """
    system('cls')
    print('***************************************')
    print('*                                     *')
    print('*                                     *')
    print('*  BIENVENIDO A DEDUCCIÓN GRAMATICAL  *')
    print('*                                     *')
    print('*                                     *')
    print('***************************************')
    time.sleep(2)
    system('cls')
    print('***************************************')
    print('* El juego consiste en identificar el *')
    print('* verbo adecuado que falta en la      *')
    print('* oración,solo responde a,b o c.      *')
    print('* Toma como ayuda el predicado de la  *')
    print('* oracion que delata al verbo.        *')
    print('***************************************')
    time.sleep(6)
    system('cls')
    documento=xlrd.open_workbook('Base_de_datos.xlsx') #abrir documento
    oraciones=documento.sheet_by_index(1)  #escoger la hoja
    primer_num=-1
    segundo_num=-1
    for i in range(3):
        time.sleep(1)
        system('cls')
        print('***************************************')
        print('*                                     *')
        print('*                                     *')
        print('*                 3                   *')
        print('*                                     *')
        print('*                                     *')
        print('***************************************')
        time.sleep(1)
        system('cls')
        print('***************************************')
        print('*                                     *')
        print('*                                     *')
        print('*                 2                   *')
        print('*                                     *')
        print('*                                     *')
        print('***************************************')
        time.sleep(1)
        system('cls')
        print('***************************************')
        print('*                                     *')
        print('*                                     *')
        print('*                 1                   *')
        print('*                                     *')
        print('*                                     *')
        print('***************************************')
        time.sleep(1)
        system('cls')
        print('***************************************')
        print('*                                     *')
        print('*                                     *')
        print('*                 YA                  *')
        print('*                                     *')
        print('*                                     *')
        print('***************************************')
        time.sleep(1)
        system('cls')
        num=random.randint(1,30)
        while num==primer_num or num==segundo_num:
            num=random.randint(1,30)
        if i==0:
            primer_num=num
        else:
            segundo_num=num
        resp2=random.randint(1,30)
        resp3=random.randint(1,30)
        posicion_resp=random.randint(1,3)
        oracion=oraciones.cell_value(num,0)  #obtener el contenido de la hoja
        respuesta=oraciones.cell_value(num,1)
        print('***************************************')
        print(oracion)
        print()
        while num==resp2 or num==resp3 or resp2==resp3:
            resp2=random.randint(1,9)
            resp3=random.randint(1,9)
        if posicion_resp==1:
            print('a.',oraciones.cell_value(num,1))
            print('b.',oraciones.cell_value(resp2,1))
            print('c.',oraciones.cell_value(resp3,1))
            respuesta_usuario=str(input())
            print('Tu respuesta es:'+respuesta_usuario)
            print('***************************************')
            time.sleep(2)
            system('cls')
            if respuesta_usuario.lower()=='a':
                print('***************************************')
                print('*                                     *')
                print('*                                     *')
                print('*   Respuesta correcta,felicidades    *')
                print('*                                     *')
                print('*                                     *')
                print('***************************************')
            else:
                print('***************************************')
                print('*                                     *')
                print('*                                     *')
                print('* Respuesta incorrecta,piensalo mejor *')
                print('*                                     *')
                print('*                                     *')
                print('***************************************')
        elif posicion_resp==2:
            print('a.',oraciones.cell_value(resp2,1))
            print('b.',oraciones.cell_value(num,1))
            print('c.',oraciones.cell_value(resp3,1))
            respuesta_usuario=str(input())
            print('Tu respuesta es:'+respuesta_usuario)
            print('***************************************')
            time.sleep(2)
            system('cls')
            if respuesta_usuario.lower()=='b':
                print('***************************************')
                print('*                                     *')
                print('*                                     *')
                print('*   Respuesta correcta,felicidades    *')
                print('*                                     *')
                print('*                                     *')
                print('***************************************')
            else:
                print('***************************************')
                print('*                                     *')
                print('*                                     *')
                print('* Respuesta incorrecta,piensalo mejor *')
                print('*                                     *')
                print('*                                     *')
                print('***************************************')
        else:
            print('a.',oraciones.cell_value(resp3,1))
            print('b.',oraciones.cell_value(resp2,1))
            print('c.',oraciones.cell_value(num,1))
            respuesta_usuario=str(input())
            print('Tu respuesta es:'+respuesta_usuario)
            print('***************************************')
            time.sleep(2)
            system('cls')
            if respuesta_usuario.lower()=='c':
                print('***************************************')
                print('*                                     *')
                print('*                                     *')
                print('*   Respuesta correcta,felicidades    *')
                print('*                                     *')
                print('*                                     *')
                print('***************************************')
            else:
                print('***************************************')
                print('*                                     *')
                print('*                                     *')
                print('* Respuesta incorrecta,piensalo mejor *')
                print('*                                     *')
                print('*                                     *')
                print('***************************************')

def identifica_la_figura():
    """
    Ejecuta el juego identifica la figura del area de entrena tu cerebro
    No recibe parametros
    No retorna algun valor
    """
    def cuadrado():
        """
        Dibuja en el centro un cuadrado en la pantalla de turtle
        No recibe parametros
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
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
        No retorna algun valor
        """
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
        No retorna algun valor
        """
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
    system('cls')
    primer_num=-1
    segundo_num=-2
    print('***************************************')
    print('*                                     *')
    print('*                                     *')
    print('*  BIENVENIDO A IDENTIFICA LA FIGURA  *')
    print('*                                     *')
    print('*                                     *')
    print('***************************************')
    time.sleep(2)
    system('cls')
    print('***************************************')
    print('* En la esquina superior derecha se   *')
    print('* dibujará la forma de una figura     *')
    print('* basica,responde que figura encaja   *')
    print('* en la zona blanca.                  *')
    print('*                                     *')
    print('***************************************')
    time.sleep(5)
    pantalla_2=tk.Tk()
    pantalla_2.title('Dibujo')
    pantalla_2.config(bg = 'lightblue')
    area_dibujo=tk.Canvas(master=pantalla_2,width=480,height=480)
    pantalla_2.geometry('-1+0')
    area_dibujo.pack()
    t=tl.RawTurtle(area_dibujo)
    area_dibujo.config(bg = 'lightblue')
    for i in range(3):
        t.hideturtle()  #esconder tortuga
        t.pensize(4) #ancho del trazo
        t.up()
        t.color('white')  #color trazo
        num=random.randint(0,10)
        while num==primer_num or num==segundo_num:
            num=random.randint(0,10)
        if i==0:
            primer_num=num
        elif i==1:
            segundo_num=num
        if num==0:
            cuadrado()
            resp='cuadrado'
        elif num==1:
            rectangulo()
            resp='rectángulo'
        elif num==2:
            triangulo_rectangulo()
            resp='triángulo rectangulo'
        elif num==3:
            pentagono()
            resp='pentágono'
        elif num==4:
            triangulo_equilatero()
            resp='triángulo equilatero'
        elif num==5:
            circulo()
            resp='círculo'
        elif num==6:
            rombo()
            resp='rombo'
        elif num==7:
            trapecio()
            resp='trapecio'
        elif num==8:
            cruz()
            resp='cruz'
        elif num==9:
            hexagono()
            resp='hexagono'
        elif num==10:
            heptagono()
            resp='heptagono'
        t.end_fill()
        system('cls')
        print('***************************************')
        print('*                                     *')
        print('*        ¿Que figura encaja?          *')
        print('*                                     *')
        print('* -                                   *')
        print('*                                     *')
        print('*                                     *')
        print('***************************************')
        resp_usuario=str(input())
        system('cls')
        print('***************************************')
        print('*                                     *')
        print('*        ¿Que figura encaja?          *')
        print('*                                     *')
        cadena_con_resp='* -'+resp_usuario+' *'
        if len(cadena_con_resp)==39:
            print(cadena_con_resp)
        else:
            for i in range(len(cadena_con_resp)):
                if cadena_con_resp[i]=='':
                    posicion_ultimoespacio=i
            espacios_faltantes=39-len(cadena_con_resp)
            cadena_resp=cadena_con_resp[:i]+(' '*espacios_faltantes)+'*'
            print(cadena_resp)
        print('*                                     *')
        print('*                                     *')
        print('***************************************')
        time.sleep(1)
        system('cls')
        if resp_usuario.lower()==resp:
            print('***************************************')
            print('*                                     *')
            print('*                                     *')
            print('*   Respuesta correcta,felicidades    *')
            print('*                                     *')
            print('*                                     *')
            print('***************************************')
        else:
            print('***************************************')
            print('*                                     *')
            print('*                                     *')
            print('* Respuesta incorrecta,piensalo mejor *')
            print('*                                     *')
            print('*                                     *')
            print('***************************************')
        t.reset()
    pantalla_2.destroy()
def organiza_la_oracion():
    """
    Ejecuta el juego organiza la oración del area de entrena tu cerebro
    No recibe parametros
    No retorna algun valor
    """
    system('cls')
    print('***************************************')
    print('*                                     *')
    print('*                                     *')
    print('*  BIENVENIDO A ORGANIZA LA ORACIÓN   *')
    print('*                                     *')
    print('*                                     *')
    print('***************************************')
    time.sleep(2)
    system('cls')
    print('***************************************')
    print('* El juego consiste en que ordenes la *')
    print('* oración que se muestre en pantalla, *')
    print('* solo separa las palabras por un     *')
    print('* espacio.Toma en cuenta como pista   *')
    print('* la letra que inicie con mayúscula.  *')
    print('***************************************')
    time.sleep(6)
    documento=xlrd.open_workbook('Base_de_datos.xlsx') #llamar el documento
    ejercicios=documento.sheet_by_index(0)
    posicion_ejercicio1=-1
    posicion_ejercicio2=-1
    for i in range(3):
        time.sleep(1)
        system('cls')
        num=random.randint(1,28)
        while num==posicion_ejercicio1 or num==posicion_ejercicio2:
            num=random.randint(1,28)
        if i==0:
            posicion_ejercicio1=num
        else:
            posicion_ejercicio2=num
        texto=ejercicios.cell_value(num,0)  #obtener contenido de una celda random
        time.sleep(1)
        print('***************************************')
        print()
        print(texto)
        respuesta_ejercicio=str(input())
        print()
        print('Tu respuesta es:'+respuesta_ejercicio)
        print()
        print('***************************************')
        respuesta_correcta=ejercicios.cell_value(num,1)
        time.sleep(2)
        system('cls')
        if respuesta_ejercicio==respuesta_correcta:
            print('***************************************')
            print('*                                     *')
            print('*                                     *')
            print('*   Respuesta correcta,felicidades    *')
            print('*                                     *')
            print('*                                     *')
            print('***************************************')
        else:
            print('***************************************')
            print('*                                     *')
            print('*                                     *')
            print('* Respuesta incorrecta,piensalo mejor *')
            print('*                                     *')
            print('*                                     *')
            print('***************************************')

def leccion_if():
    """
    Enseña la estructura del condicional if
    No recibe parámetros
    No retorna ningún valor
    """
    print("Lección IF")
    time.sleep(2)
    print("En ocasiones para nuestro codigo necesitamos verificar ciertas condiciones")
    print("y apartir de eso transformar el comportamiento del algoritmo.")
    time.sleep(4)
    print("¿Como lo hacemos?")
    time.sleep(3)
    print("La sentencia 'if' permite hacer esto,de modo que podemos establecer dos caminos")
    time.sleep(3)
    print("uno en el cual la condicion es verdadera y otro donde es falsa.")
    time.sleep(3)
    print("Por ejemplo")
    time.sleep(3)
    print("Coloca un numero de una cifra")
    a=int(input())
    print("Una condición seria:¿tu número es 5?")
    time.sleep(4)
    if a==5:
        print("Listo, la condición tomo el camino verdadero, al ser tu número el 5.")
    else:
        print("La condición tomo el camino falso,al no ser {} el numero 5".format(a))
    time.sleep(4)
    print("La sentencia se escribe asi: ---> if (tu condición):")
    time.sleep(3)
    print("Intentalo tu siguiendo la estructura y con esta condicion: 20>17.")
    v1='False'
    time.sleep(1)
    while v1=='False':
        res_u=str(input())
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
                    print("Muy Bien")
                    time.sleep(2)
                    print("Es correcto como lo escribiste-")
                    v1='True'
                else:
                    print("Escribiste mal,de nuevo.")
            else:
                print("Lo escribiste de manera erronea, intentalo otra vez.")
        else:
            print("Lo escribiste de manera erronea, intentalo otra vez.")
    print("Las instrucciones que siguen luego del if se llaman un 'bloque' y tienen un espacio a la izquierda.")
    time.sleep(5)
    print("if (condición):")
    print("    instrucción")
    time.sleep(4)
    print("Para el camino donde la condición es falsa se coloca --->else:")
    print("Escribelo tu")
    time.sleep(2)
    v2='False'
    while v2=='False':
        res_u2=str(input())
        if res_u2=='else:':
            print("Correcto, felicidades.")
            v2='True'
        else:
            print("Incorrecto, intentalo de nuevo.")
    time.sleep(3)
    print("No es obligatorio utilizar 'else' sino es necesario.")
    time.sleep(2)
    print("DATO EXTRA")
    time.sleep(2)
    print("¿Que sucede si queremos colocar una condición extra?")
    time.sleep(3)
    print("Puedes poner otro if debajo del anterior,pero python te proporciona la opción de hacer lo mismo")
    print("mediante la seguiente sentencia  ---> elif:")
    time.sleep(5)
    print("Vamos escribela")
    time.sleep(2)
    v3='False'
    while v3=='False':
        res_u3=str(input())
        if res_u3=='elif:':
            print("Muy bien, felicidades.")
            v3='True'
        else:
            print("Hay algo mal, intentalo otra vez.")
    print("Lección terminada,¡YA SABES UTILIZAR LA SENTENCIA IF!")

def leccion_break():
    """
    Enseña la sentencia break
    No recibe parámetros
    No retorna ningún valor
    """
    print("Bienvenido a la lección de la sentencia break")
    time.sleep(2)
    print("En diversos algoritmos a veces necesitamos cambiar el flujo de un ciclo.")
    time.sleep(2)
    print("La sentencia break permite romper el ciclo antes de que termine,haciendo")
    print("uso de la sentencia mas una condición dentro del ciclo.")
    time.sleep(5)
    print("")
    print("ciclo:")
    print("    if condición:")
    print("        break")
    time.sleep(2)
    print("Ahora escribela tu")
    v='False'
    while v=='False':
        res_u=str(input())
        time.sleep(1)
        print("ciclo:")
        print("    if condición:")
        print("        "+res_u)
        time.sleep(3)
        if res_u=='break':
            print('Excelente')
            v='True'
        else:
            print('Error')
            print('Esta mal escrito,intentalo de nuevo')
    print('Muy bien,ya puedes utilizar break en tus codigos')


def Ahorcado_exámen ():
    """
    Evalúa mediante la modalidad de adivinar una palabra
    dada una pista e invoca un nivel de acuerdo a la selección 
    del usuario.
    No recibe parámetros
    No retorna ningún valor
    """
    print("  Adivina la palabra")
    print("        Menú")
    print(" 1) Nivel 1: Básico")
    print("2) Nivel 2: Intermedio")
    print(" 3) Nivel 3: Experto")
    print()
    opcion = 5
    while opcion < 1 or opcion > 3:
        opcion = int(input("Selecciona un nivel:\n"))
    if opcion == 1:
        nivel_basico()
    elif opcion == 2:
        nivel_intermedio()
    else:
        nivel_experto()
def nivel_basico():
    """
    Primer nivel de la función Ahorcado_exámen()
    No recibe prámetros.
    No retorna ningún valor.
    """    
    puntaje = 0
    cont = 0
    vdd = [""]
    print("Comencemos")
    while cont < 5:
        liste = ["if","input()","elif", "ciclo","condicional","str","boolean","+","python"]
        piste = ["Estructura de control condicional: ","Función que permite ingresar valores por teclado: ","Evalua otra condición después del if: ","Tipo de estructura control que permite hacer tareas repetitivamente mientras se cumpla una condición:","Estructura de control que evalua si una condición se cumple:","Tipo de valor de una cadena de caracteres:","Qué tipo de valor es True? ","Símbolo usado para concatenar:","En qué lenguaje se hizo este juego? "]
        pregunta = rd.randint(0,len(liste) - 1)
        while str(pregunta) in vdd:
            pregunta =  rd.randint(0,len(liste) - 1)         
        piste = piste[pregunta]
        print(piste,"")
        casillas = " _ " * len(liste[pregunta])
        print(casillas)
        respuesta = input("Escribe tu respuesta:\n").strip()
        respuesta = respuesta.lower()
        print()
        if respuesta == liste[pregunta]:
            puntaje += 2
        else:
            puntaje += 0 
        cont += 1
        vdd += str(pregunta)
    if puntaje >= 10:
        print("¡Felicidades! Todas tus respuestas son correctas")
        print("Puntaje: ",puntaje,"/10")
    elif puntaje <=4:
        print("Nunca dije que las cosas fueran fáciles")
        print("Puntaje: ",puntaje,"/10")
    else:
        print("Buen intento, puedes hacerlo mejor?")
        print("Puntaje: ",puntaje,"/10")
    
def nivel_intermedio():
    """
    Segundo nivel del ahorcado
    No recibe prámetros.
    No retorna ningún valor.
    """
    vdd1 =[""]
    cont1 = 0
    puntaje = 0
    print("Comencemos")
    while cont1 < 5:
        lista = ["else:","print()","break","str","def","rombo","//","si",".upper()","iterador"]
        pista = ["Actúa si el if o el elif no lo hace: ","Función que permite imprimir un valor en pantalla: ","Puede romper un ciclo",'Qué tipo de dato es "1457" ? ',"Con qué palabra reservada se declara un función?","Que forma tiene un 'if' en un diagrama de flujo?","Cómo se escribe el operador de división entera?",'La operacion: "Hola mundo" * 5 , es válida? si/no',"Función que convierte un string a mayúsculas","Variable que recorre un ciclo for:"]
        pregunt = rd.randint(0,len(lista) - 1)
        while str(pregunt) in  vdd1:
            pregunt =  rd.randint(0,len(lista) - 1)         
        pista = pista[pregunt]
        print(pista)
        casillas = " _ " * len(lista[pregunt])
        print(casillas)
        respuesta = input("Escribe tu respuesta:\n").strip()
        respuesta = respuesta.lower()
        print()
        if respuesta == lista[pregunt]:
            puntaje += 2
        else:
            puntaje += 0 
        cont1 += 1
        vdd1 += str(pregunt)
    if puntaje >= 10:
        print("¡Felicidades! Todas tus respuestas son correctas")
        print("Puntaje: ",puntaje,"/10")
    elif puntaje < 6:
        print("Perdiste este nivel u.u")
        print("Puntaje: ",puntaje,"/10")
    else:
        print("Buen intento, puedes hacerlo mejor?")
        print("Puntaje: ",puntaje,"/10")
def nivel_experto():
    """
    Tercer nivel del ahorcado
    No recibe prámetros.
    No retorna ningún valor.
    """
    vdd2 = [""]
    cont2 = 0
    puntaje = 0
    print("Ahora no podrás saber cuantas letras tiene la palabra en cuestión: EMPIEZA!\n")
    while cont2 < 5:
        l = ["cuatro","si","no","formal","false","4","no","no","|"]
        pist = ["Cuantos espacios pone '\\t' en un print? (Escríbelo con letras)","lambda es una función?","El código:\nwhile cont <= 10:\n  print('Hola')\n  cont = cont += 1\nEs correcto? si/no","Que tipo de lenguaje es un lenguaje de programación? ","La sentencia, True and False = , tiene como resultado booleano:","Si aplicaramos la función round en 4.4999, que valor tendríamos?","Esta función está bien escrita:\ndef hola_mundo()\n    print('Hola a todos!')\nhola_mundo()","Se puede imprimir esto?:\nprint('Hasta aquí, vamos' +  941 + 'lineas de código!')\nSi/No: ","Que función puede convertir la siguiente cadena:\n'Saber Python es lo máximo'\n a la siguiente cadena:\nsABER pYTHON ES LO MAXIMO\n$).swappcase()\n|)No existe esa función\n^).upper()"]
        pregun = rd.randint(0,len(l) - 1)
        while str(pregun) in vdd2:
            pregun =  rd.randint(0,len(l) - 1)         
        pist = pist[pregun]
        print(pist,"")
        respuesta = input("Escribe tu respuesta:\n").strip()
        respuesta = respuesta.lower()
        print()
        if respuesta == l[pregun]:
            puntaje += 2
        else:
            puntaje += 0 
        cont2 += 1
        vdd2 +=str(pregun)
    if puntaje >= 10:
        print("¡Felicidades! Todas tus respuestas son correctas")
        print("Puntaje:",puntaje,"/10")
    elif puntaje < 8:
        print("No eres un experto :c, Esfuerzate más!")
        print("Puntaje:",puntaje,"/10")
    else:
        print("Buen intento, puedes hacerlo mejor?")
        print("Puntaje:",puntaje,"/10")

def adivina_el_número ():
    """
    Juego de adivinar el número
    No recibe parámetros
    No retorna ningún valor
    """
    numero_para_adivinar = rd.randint(0,100)
    print("                 Adivina el número\n")
    intentos = 0
    win = 0
    print("Tienes 10 intentos para adivinar un número del 1 al 100")
    intentos = 10
    intentos_al_final = 0
    for oportunidades in range(10):
        intentos -= 1
        intentos_al_final += 1
        respuesta = int(input("Escribe tu respuesta:\n"))
        if respuesta == numero_para_adivinar:
            if intentos == 9:
                print("Adivinaste el número en un sólo intento, ¡Menuda suerte la tuya!")
            else:
                print("Felicidades! Adivinaste el número en {} intentos!".format(intentos_al_final))
            win = 1
            break
        elif respuesta > numero_para_adivinar:
            if intentos == 1:
                print("Sólo te queda un intento! Usalo bien, ¡tu número fue muy grande!")
            else:    
                print("Tu número es muy grande! Te quedan {intentos_disponibles} intentos".format(intentos_disponibles = intentos))
        else:
            if intentos == 1:
                print("Sólo te queda un intento! Usalo bien, tu número fue muy pequeño!")
            else:
                print("Tu número es muy pequeño! Te quedan ",intentos,"intentos")
    if win != 1:
        print("Lo siento, has perdido :c ¡Inténtalo otra vez!")
        print("El número era: " + str(numero_para_adivinar) + " Suerte para la próxima!")


def palabras_reservadas():
    """
    Enseña bases sobre las palabras reservadas
    No recibe parámetros
    No retorna ningún valor
    """
    print("¡¡Hola de nuevo!!")
    time.sleep(2)
    print("Alguna vez, trataste de usar la palabra print como nombre de una variable?")
    respuesta_posible_p = ["No", "no", "NO","nO"]
    respuesta = input("Si / No : ")
    if respuesta in respuesta_posible_p:
        print("Muy bien, y no debes hacerlo ¿Sabes por qué?")
    else:
        print("Entonces, seguramente te salió un error ¿Sabes por qué?")
    print("Esto es debido a que en Python existe algo llamado...")
    time.sleep(3)
    print ("Palabras", end ="")
    print(" RESERVADAS")
    time.sleep(3)
    print("Estas palabras son usadas para que el intérprete de Python entienda tu programa")
    time.sleep(4)
    print("Estas palabras están 'reservadas' para una tarea en específico")
    time.sleep(3)
    print("Por ejemplo, no puedes clavar un clavo con un vaso de porcelana, ni escribir con un pedazo de cartón.")
    time.sleep(4)
    print("De la misma forma, no puedes usar un print como nombre de una variable")
    time.sleep(4)
    print("Un print está hecho para imprimir un mensaje por pantalla, no para alojar un valor, para eso están las variables")
    time.sleep(4)
    print("No te preocupes, no es nada del otro mundo, sólo ten en cuenta que las cosas son hechas para una tarea específica")
    time.sleep(4)
    print("Exactamente hay 28 palabras reservadas en Python")
    time.sleep(6)
    os.system("cls")
    print("Te enseñaremos a buscarlas por tí mismo, lo único que debes hacer es escribir:")
    time.sleep(3)
    print("kwlist")
    time.sleep(3) 
    print("Adelante, inténtalo ! ")
    llamado_lista = ""
    while llamado_lista != "kwlist":
        llamado_lista = input(">>> ").strip()
        if llamado_lista == "kwlist":
            print(kwlist)
            print("")
            print("Felicidades, lo lograste! Ahora puedes ver todas las palabras reservadas de Python")
            break 
        else:
            print("Vamos, inténtalo de nuevo, no saldrás de aquí hasta que lo logres!")
    print("Obsérvalas con detenimiento . . .")
    time.sleep(10)
    print("Buscar una palabra en esta lista para saber si es reservada puede ser un poco aburrido verdad?")
    time.sleep(4)
    print("Pero como siempre, nosotros tenemos la solución!")
    time.sleep(5)
    print("Sólo debes escribir: iskeyword('aquí pones la palabra') y problema resuelto!")
    time.sleep(3)
    print("Esto te dará como resultado un:")
    time.sleep(2)
    print("True en caso de que la palabra sea reservada")
    time.sleep(2)
    print("False en caso de que la palabra NO sea reservada")
    time.sleep(2)
    print("Vamos, inténtalo tu mismo!")
    time.sleep(3)
    primera = "iskeyword("
    segunda = ")"
    intermedia = ""
    vddificador = 0
    while vddificador != 1:
        intermedia = input(">>> ").strip()
        if intermedia[:10] == primera:
            if intermedia[10] == '"' or intermedia[10] == "'" :
                if intermedia[-2] == '"' or intermedia[-2] == "'":
                    if intermedia[-1] == ")":
                        print(iskeyword(intermedia[11:-2]))
                        time.sleep(1)
                        print("Felicidades, lo lograste!")                          
                        vddificador = 1
                        break
                    else:
                        continue
                else:
                    continue                 
            else:
                continue
        else:                     
            print("Vamos, inténtalo de nuevo!")
    time.sleep(1)
    print("Eso ha sido todo! Gracias y nos vemos en una próxima ocasión")
    time.sleep(8)
    os.system("cls")
def nombres_de_funciones():
    """
    Enseña algunos nombres de funciones integradas al lenguaje de Python, y como usarlas,
    además de una introducción a funciones.
    No recibe parámetros
    No retorna ningún valor
    """
    time.sleep(2)
    print("Hola y bienvenido a PLAYTHON!")
    time.sleep(2)
    print("Seguramente, ya aprendiste algo sobre las palabras reservadas no es así?")
    time.sleep(2)
    print("Eso te habrá servido como una introducción para nuestro siguiente tema...")
    time.sleep(3)
    print("NOMBRES DE FUNCIONES")
    time.sleep(2)
    print("Las funciones, son por por así decirlo, pequeños algoritmos dentro de uno más grande")
    time.sleep(4)
    print("Al igual que los órganos de tu cuerpo cumplen una función, por ejemplo, las venas, transportan sangre, y los ojos obsrvan")
    time.sleep(4)
    print("Las funciones, son como 'órganos' pero de tu código")
    time.sleep(3)
    print("De hecho, tu ya has usado funciones! Recuerda un poco y verás que es así")
    time.sleep(4)
    print("Por ejemplo, anteriormente, aprendiste a usar la función 'iskeyword', recuerdas que hacía?")
    time.sleep(1)
    recordad = input("Si / No:  ")
    if recordad in "SisisIsSI":
        time.sleep(1)
        print("Nos alegra que lo recuerdes!")
    else:
        time.sleep(1)
        print("Bueno, no hay problema!")
    time.sleep(1) 
    os.system("cls")
    time.sleep(2)
    print("La función iskeyword, recibía un valor de tipo string, y verificaba si ese valor estaba en la lista de palabras reservadas")
    time.sleep(4)
    print("Esa era la 'función' del órgano 'iskeyword'")
    time.sleep(3)
    print("Definir una función es muy fácil, sólo debes escribir esto:")
    time.sleep(3)
    print(" def nombre_de_tu_función (): \n   Y aquí pones las tareas que va ha hacer tu función ")
    time.sleep(4)
    print("Fácil verdad?, Sin embargo no te enseñaremos a definir funciones en este momento")
    time.sleep(43)
    print("Te enseñaremos algunas funciones que puedes usar como ya lo hicimos con 'iskeyword'")
    time.sleep(4)
    print("Hay una gran cantidad de funciones, sin embargo, trataremos de enseñarte algunas que suelen ser muy útiles")
    time.sleep(4)
    print("Antes de cualquier cosa, para usar una función debemos 'llamarla', hay muchas formas de hacerlo dependiendo de la función")
    time.sleep(4)
    os.system("cls")
    print("Pero no te preocupes!Casi todas las funciones que te enseñaremos aquí, se llaman de esta manera")
    time.sleep(3)
    print("nombre_de_las_variables_o_la_variable_sobre_la que_trabaja_el_objeto.nombre_de_la_función()")
    time.sleep(3)
    print("No te asustes por ver todo eso! Te pondré un ejemplo más simple, observa el siguiente código, aquí usaremos la función .upper():")
    print()
    time.sleep(3)
    print("variable = 'Soy bueno programando!'\nvariable.upper()\nprint(variable)")
    time.sleep(3)
    print("Que crees que imprimirá este código?\n1)soy bueno programando!\n2)SOY BUENO PROGRAMANDO!")
    que_crees = input("Pulsa 1 ó 2: ").strip()
    if que_crees == "2":
        time.sleep(1)
        time.sleep(3)
        print("Eres muy inteligente, respuesta correcta")
    else:
        time.sleep(1)
        print("Oh, fallaste, pero no importa!")
    time.sleep(2)
    os.system("cls")
    time.sleep(2)
    print("Como te habrás dado cuenta ahora, la función .upper(), pasa los caracteres de un string a MAYÚSCULAS")
    time.sleep(4)
    print("La función que hace lo contrario es la función .lower(), esta pasa lo caracteres de una función a minúsculas")
    time.sleep(4)
    print("Si aplicaras la función .lower() sobre el string 'H0LA Mundo' cuál de estos resultados obtendrías?")
    time.sleep(1)
    print("1) hola mundo") 
    print("2) h0la mundo")
    time.sleep(2)
    q_c_lowerr = ""
    while q_c_lowerr != 2:
        q_c_lowerr = input("Ingresa tu respuesta! 1 ó 2?: ").strip()
        if q_c_lowerr != "2":
            time.sleep(1)
            print("Oh, fallaste, mira bien el string y vuelvelo a intentar")
        else:
            time.sleep(1)
            print("Muy bien!")
            break
    time.sleep(1)
    os.system("cls")
    time.sleep(2)
    print("Bueno, ahora ya puedes defenderte debidamente en cuanto a funciones, pero te enseñaremos algunas más:")
    time.sleep(4)
    print("Hay una función que te permite saber la longitud de una cadena, como si la midieras con una regla")
    time.sleep(4)
    print("Esta función se llama....")
    time.sleep(2)
    print("len()")
    time.sleep(2)
    print("En este caso no la llamamos con .len(), simplemente debemos poner la palabra dentro de los paréntesis de len()")
    time.sleep(4)
    print("Ejemplo:\nlen(aquí_pones_el_string)")
    time.sleep(4)
    print("Intenta contestar esta pregunta! ¿Que valor imprime por pantalla esto? len('cadena')")
    lon_cad = ""
    while lon_cad != "6" :
        lon_cad = input().strip()
        if lon_cad == "6":
            time.sleep(5)
            print("Muy bien!")
            break
        else:
            time.sleep(1)
            print("Oh no! Lo has respondido mal, mira otra vez la pregunta!")
    time.sleep(3)
    print("Déjanos agradecerte por haber jugado nuestro juego hasta este punto!")
    time.sleep(4)
    os.system("cls")
    time.sleep(2)
    print("Continuemos aprendiendo! Ahora miremos la funcion .split(), esta convierte las 'palabras' de una cadena en una lista, veamos un ejemplo: ")
    time.sleep(4)
    print("cadena = 'Ahora sé programar'\ncadena.split()\nprint(cadena)\nQué crees que imprima este código?")
    time.sleep(4)
    print("1)['Ahora se programar']")
    print("2)['Ahora','sé','programar']")
    rpt = ""
    while rpt !="2":
        rpt = input("Ingresa tu respuesta (1 ó 2)\n").strip()
        if rpt == "2":
            time.sleep(1)
            print("Felicidades! entendíste esta función")
            break
        else:
            time.sleep(1)
            print("Respondiste mal,pero no te preocupes, vuelve a leer la parte en la que hablamos de .split()")
    time.sleep(2)
    print("Sigamos viendo funciones!")
    time.sleep(3)
    os.system("cls")
    time.sleep(2)
    print("Continuemos con una interesante, y una que usaras mucho, osea...")
    time.sleep(3)
    print("La función 'range()', esta devuelve nos devuelve una lista de valores numéricos que empieza desde 0, dependiendo de el valor ingresado")
    time.sleep(5)
    print("NOTA IMPORTANTE: Un buen programador, siempre cuenta desde 0")
    time.sleep(3)
    print("La función range() sirve para datos tipo string o números enteros")
    time.sleep(3)
    print("Esta función tiene muchas cosas por ser explicadas, pero no te asustes! Sólo veremos lo básico")
    time.sleep(4)
    print("Veamos el siguiente ejemplo:\nrango = range(10)\nprint(rango)\n>>>[0,1,2,3,4,5,6,7,8,9]")
    time.sleep(9)
    print("Bastante simple no?,Te acostumbrarás con el tiempo así que no te preocupes")
    time.sleep(4)
    print("Para que puedas usar un range() con un dato tipo string, debes hacer algo como esto:")
    time.sleep(4)
    print("range(len(aquí_pones_tu_string))")
    time.sleep(3)
    print("Atento!Pregunta!Cuál sería el resultado de imprimir:")
    time.sleep(3)
    print("range(len('10'))")
    time.sleep(3)
    print("a) [0,1,2,3,4,5,6,7,8,9]")
    print("2) [0,1] ")
    print("!) No es posible imprimirlo")
    rong_rpt = ""
    while rong_rpt != "2":
        rong_rpt = input("Ingresa tu respuesta!\n")
        if rong_rpt == "2":
            time.sleep(1)
            print("Wau, lo has hecho muy bien, esa era difícil!")
            break
        else:
            print("Tómate tu tiempo, esta es un poco difícil...")
    time.sleep(1)
    print("Lo ves? Después de todo no fue nada del otro mundo")
    time.sleep(6)
    os.system("cls")
    time.sleep(2)
    print("Ahora veremos otras funciones interesantes")
    time.sleep(2)
    print("Conoces el código ASCII?")
    rpt_ascci = input("Si|No: ").strip()
    if rpt_ascci in "SiSIsIsi":
        print("Muy bien, entonces no te costará problema entender esto!")
    else:
        print("No te preocupes! Si para eso estamos nosotros!")
    time.sleep(3)
    print("Bueno, para evitarnos una larga explicación aburrida, diremos que el código ASCII, le asigna un número a una letra, caracater o símbolo")
    time.sleep(6)
    print("El código ASCII, es muy largo, y es tedioso tener que buscar en la tabla el valor que necesitemos, sin embargo el código ASCII, suele ser muy útil en ocasiones")
    time.sleep(4)
    print("Para tu fortuna y la de todos, existe una función que le asigna ese número a la letra que queramos!")
    time.sleep(4)
    print("El nombre de esta función es: ord()")
    time.sleep(4)
    print("Grandioso no?, con esto podrías hacer códigos secretos, contraseñas fuertes, e incluso juegos!")
    time.sleep(4)
    print("Para usarla sólo debes escribir algo como esto:")
    time.sleep(4)
    print("ord(aquí_pones_la_letra_símbolo_o_signo)")
    time.sleep(4)
    print( )
    rpt_ord = ""
    vdd_ord = 0
    #
    print("Inténtalo tú mismo, recuerda que la función ord() SOLAMENTE, recibe UN caracter,signo o símbolo")
    rpt_ord = ""
    vdd_ord = 0
    while vdd_ord != 1: 
            rpt_ord = input("Adelante:\n").strip()
            if rpt_ord[:4] == "ord(":
                  if rpt_ord[-1] == ")":
                        if len(rpt_ord) == 8:
                              print(ord(rpt_ord[5]))
                              print("Muy bien, lo hiciste excelente!")
                              vdd_ord = 1
                              break
                        else:
                              print("Vamos, inténtalo de nuevo!")
                  else:
                       print("Vamos, inténtalo de nuevo!")             
            else:
                  print("Vamos, inténtalo de nuevo!")
                  vdd = 0                      
    
    time.sleep(2)
    print("Hemos aprendido mucho, no es así?")
    time.sleep(4)
    os.system("cls")
    print("Ahora aprenderemos una función llamada round(), esta función, redondea un valor al entero más cercano")
    time.sleep(4)
    print("Para que lo veas más claro mira este ejemplo:")
    time.sleep(3)
    print("esto = round(4.14172695)\nprint(esto)\n>>> 4")
    time.sleep(3)
    print("Mira este otro ejemplo:")
    time.sleep(3)
    print("esto_otro = round(5.6)\nprint(esto_otro)\n>>> 6")
    time.sleep(4)
    print("Puede parecer muy simple, pero esta función tiene una cantidad de usos casi infinitos")
    time.sleep(4)
    print("Inténtalo hacer tú mismo con base a los ejemplos anteriores")
    time.sleep(3)
    print("Por ejemplo: podrías hacer algo como: round(2.17) ")
    rpt_round = ""
    vdd_round = 0
    time.sleep(1)
    while vdd_round != 1: 
        rpt_round = input("Adelante:\n").strip()
        if rpt_round[:6] == "round(":
            if rpt_round[-1] == ")":
                time.sleep(1)
                print(round(float(rpt_round[6:-1])))
                print("Muy bien, lo hiciste excelente!")
                vdd_round = 1
                break
            else:
                continue
        else:                    
            print("Vamos, inténtalo de nuevo!")
            vdd_round = 0                
    time.sleep(2)
    os.system("cls")
    print("Por último aprenderemos la función type(), esta nos devuelve el tipo de valor que pones dentro de sus paréntesis")
    time.sleep(4)
    print("Mira el siguiente ejemplo:")
    time.sleep(3)
    print("tipo = type('3.14')\nprint(tipo)\n>>> <class'str'>")
    time.sleep(3)
    print("Sencillo no?")
    time.sleep(3)
    print("ATENTO! Pregunta! que respuesta crees que retorne la siguiente sección de código? ")
    time.sleep(2)
    print("type(3/4)")
    time.sleep(2)
    print("#)<class'float'")
    print("*)<class'int'>")
    print("=)<class'float'>")
    rpt_type = ""
    
    while rpt_type != "=": 
        rpt_type = input("Ingresa tu respuesta!: ")
        print()
        if rpt_type == "=":
            time.sleep(1)
            print("Felicidades, buen trabajo")
        else:                    
            print("Oh no, respuesta incorrecta, inténtalo otra vez!")
    time.sleep(2)
    print("Hasta aquí llegan las funciones, espero que ta hallas divertido!")
    time.sleep(5)
    print("Hasta una próxima ocasión")
    time.sleep(4)
    os.system("cls")

def juego_ppt():
    asterisco="*"
    espacio=" "
    opciones=["piedra","papel","tijera"]
    while True:
        os.system("cls")
        print("    ************************************************************************************************")
        print("    *                                                                                              *")
        print("    *                                Bienvenidos al juego de memoria!                              *")
        print("    *                                                                                              *")
        print("    *                Este juego esta basado en las mecanicas de piedra, papel o tijera             *")
        print("    *                                                                                              *")
        print("    ************************************************************************************************")
        print()
        sleep(5)
        os.system("cls")
        print("    ************************************************************************************************")
        print("    *                                                                                              *")
        print("    *                                        Instrucciones:                                        *")
        print("    *                                                                                              *")
        print("    *    Este juego, consiste en que el computador elegira una de las tres opciones del clasico    *")
        print("    *    juego de piedra, papel o tijeras, y las mostrara por un corto periodo de tiempo.          *")
        print("    *                                                                                              *")
        print("    *    Lo que debes hacer, es memorizar las opciones que eligio la computadora y elegir la que   *")
        print("    *                       le 'gane' a la opcion que elijio la computadora.                       *")
        print("    *                                                                                              *")
        print("    ************************************************************************************************")
        print()
        sleep(9)
        os.system("cls")
        print("    ************************************************************************************************")
        print("    *                                                                                              *")
        print("    *                                           TIP:                                               *")
        print("    *                                                                                              *")
        print("    *    Recuerda que tijera le gana a papel, papel le gana a piedra y piedra le gana a tijera.    *")
        print("    *                                                                                              *")
        print("    ************************************************************************************************")
        sleep(5)
        os.system("cls")
        print("    ************************************************************************************************")
        print("    *                                                                                              *")
        print("    *                                Elige el nivel que desees jugar:                              *")
        print("    *                                                                                              *")
        print("    *                1) Facil. Este tiene 6 segundos para ver las opciones y recordarlas           *")
        print("    *                2) Medio. Este tiene 4 segundos para ver las opciones y recordarlas           *")
        print("    *                3) Dificil. Este tiene 3 segundos para ver las opciones y recordarlas         *")
        print("    *                                                                                              *")
        print("    ************************************************************************************************")
        print()
        a=int(input("------------------------------------------->"))
        if a==1:
            eleccion_random0=random.choice(opciones)
            eleccion_random1=random.choice(opciones)
            eleccion_random2=random.choice(opciones)
            for i in range(0,3):
                if i==0:
                    valor=52-len(eleccion_random0)
                    cad=(espacio*valor)+asterisco
                    cadena1=eleccion_random0+cad
                elif i==1:
                    valor=52-len(eleccion_random1)
                    cad=(espacio*valor)+asterisco
                    cadena2=eleccion_random1+cad
                else:
                    valor=52-len(eleccion_random2)
                    cad=(espacio*valor)+asterisco
                    cadena3=eleccion_random2+cad
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                 Haz elegido el nivel Facil.                                  *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(3)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                 Las elecciones del computador, saldran en:                   *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(2)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                3                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                2                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                1                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                YA!                                           *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena1))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena2))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena3))
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(6)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                        Se te agoto el tiempo :O                              *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(2)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *             Ahora escribe las opciones que les ganan a las generadas por el computador.      *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            print()
            escritura0=input("Escribe tu primera eleccion: --------->")
            escritura1=input("Escribe tu segunda eleccion: --------->")
            escritura2=input("Escribe tu tercera eleccion: --------->")
            if (eleccion_random0=="papel" and escritura0=="tijera") or (eleccion_random0=="tijera" and escritura0=="piedra") or (eleccion_random0=="piedra" and escritura0=="papel"):
                if (eleccion_random1=="papel" and escritura1=="tijera") or (eleccion_random1=="tijera" and escritura1=="piedra") or (eleccion_random1=="piedra" and escritura1=="papel"):
                    if (eleccion_random2=="papel" and escritura2=="tijera") or (eleccion_random2=="tijera" and escritura2=="piedra") or (eleccion_random2=="piedra" and escritura2=="papel"):
                        print()
                        print("    ************************************************************************************************")
                        print("    *                                                                                              *")
                        print("    *                          Muy bien :D! Escribiste las elecciones correctas!                   *")
                        print("    *                                                                                              *")
                        print("    ************************************************************************************************")
                    else:
                        print()
                        print("    ************************************************************************************************")
                        print("    *                                                                                              *")
                        print("    *                          Lo sentimos, te equivocaste en una respuesta :(                     *")
                        print("    *                                                                                              *")
                        print("    ************************************************************************************************")
                else:
                    print()
                    print("    ************************************************************************************************")
                    print("    *                                                                                              *")
                    print("    *                          Lo sentimos, te equivocaste en dos respuestas :(                    *")
                    print("    *                                                                                              *")
                    print("    ************************************************************************************************")
            else:
                print()
                print("    ************************************************************************************************")
                print("    *                                                                                              *")
                print("    *                          Lo sentimos, te equivocaste en todas las respuestas :(              *")
                print("    *                                                                                              *")
                print("    ************************************************************************************************")
            sleep(3)
            os.system("cls")   
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                       Deseas volver a jugar?                                 *")
            print("    *                                                                                              *")
            print("    *                  Escribe si si deseas jugar o cualquier otro caracter para salir.            *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************") 
            print()
            eleccionfinal=input("------------------------------------------->").lower()
            if eleccionfinal=="si" or eleccionfinal=="s":
                juego_ppt()
            else:
                break
        if a==2:
            eleccion_random0=random.choice(opciones)
            eleccion_random1=random.choice(opciones)
            eleccion_random2=random.choice(opciones)
            eleccion_random3=random.choice(opciones)
            for i in range(0,4):
                if i==0:
                    valor=52-len(eleccion_random0)
                    cad=(espacio*valor)+asterisco
                    cadena1=eleccion_random0+cad
                elif i==1:
                    valor=52-len(eleccion_random1)
                    cad=(espacio*valor)+asterisco
                    cadena2=eleccion_random1+cad
                elif i==2:
                    valor=52-len(eleccion_random2)
                    cad=(espacio*valor)+asterisco
                    cadena3=eleccion_random2+cad
                else:
                    valor=52-len(eleccion_random3)
                    cad=(espacio*valor)+asterisco
                    cadena4=eleccion_random3+cad
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                 Haz elegido el nivel Medio.                                  *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(3)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                           Las elecciones del computador, saldran en:                         *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(2)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                3                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                2                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                1                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                YA!                                           *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena1))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena2))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena3))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena4))
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(4)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                        Se te agoto el tiempo :O                              *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(2)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *             Ahora escribe las opciones que les ganan a las generadas por el computador.      *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            print()
            escritura0=input("Escribe tu primera eleccion: --------->")
            escritura1=input("Escribe tu segunda eleccion: --------->")
            escritura2=input("Escribe tu tercera eleccion: --------->")
            escritura3=input("Escribe tu cuarta eleccion: --------->")
            if (eleccion_random0=="papel" and escritura0=="tijera") or (eleccion_random0=="tijera" and escritura0=="piedra") or (eleccion_random0=="piedra" and escritura0=="papel"):
                if (eleccion_random1=="papel" and escritura1=="tijera") or (eleccion_random1=="tijera" and escritura1=="piedra") or (eleccion_random1=="piedra" and escritura1=="papel"):
                    if (eleccion_random2=="papel" and escritura2=="tijera") or (eleccion_random2=="tijera" and escritura2=="piedra") or (eleccion_random2=="piedra" and escritura2=="papel"):
                        if (eleccion_random3=="papel" and escritura3=="tijera") or (eleccion_random3=="tijera" and escritura3=="piedra") or (eleccion_random3=="piedra" and escritura3=="papel"):
                            print()
                            print("    ************************************************************************************************")
                            print("    *                                                                                              *")
                            print("    *                          Muy bien :D! Escribiste las elecciones correctas!                   *")
                            print("    *                                                                                              *")
                            print("    ************************************************************************************************")
                        else:
                            print()
                            print("    ************************************************************************************************")
                            print("    *                                                                                              *")
                            print("    *                          Lo sentimos, te equivocaste en una respuesta :(                     *")
                            print("    *                                                                                              *")
                            print("    ************************************************************************************************")
                    else:
                        print()
                        print("    ************************************************************************************************")
                        print("    *                                                                                              *")
                        print("    *                          Lo sentimos, te equivocaste en dos respuestas :(                    *")
                        print("    *                                                                                              *")
                        print("    ************************************************************************************************")
                else:
                    print()
                    print("    ************************************************************************************************")
                    print("    *                                                                                              *")
                    print("    *                          Lo sentimos, te equivocaste en tres las respuestas :(               *")
                    print("    *                                                                                              *")
                    print("    ************************************************************************************************")
            else:
                print()
                print("    ************************************************************************************************")
                print("    *                                                                                              *")
                print("    *                          Lo sentimos, te equivocaste en todas las respuestas :(              *")
                print("    *                                                                                              *")
                print("    ************************************************************************************************")
            sleep(3)
            os.system("cls")   
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                       Deseas volver a jugar?                                 *")
            print("    *                                                                                              *")
            print("    *                  Escribe si, si deseas jugar o cualquier otro caracter para salir.           *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************") 
            print()
            eleccionfinal=input("------------------------------------------->").lower()
            if eleccionfinal=="si" or eleccionfinal=="s":
                juego_ppt()
            else:
                break
        if a==3:
            eleccion_random0=random.choice(opciones)
            eleccion_random1=random.choice(opciones)
            eleccion_random2=random.choice(opciones)
            eleccion_random3=random.choice(opciones)
            eleccion_random4=random.choice(opciones)
            for i in range(0,5):
                if i==0:
                    valor=52-len(eleccion_random0)
                    cad=(espacio*valor)+asterisco
                    cadena1=eleccion_random0+cad
                elif i==1:
                    valor=52-len(eleccion_random1)
                    cad=(espacio*valor)+asterisco
                    cadena2=eleccion_random1+cad
                elif i==2:
                    valor=52-len(eleccion_random2)
                    cad=(espacio*valor)+asterisco
                    cadena3=eleccion_random2+cad
                elif i==3:
                    valor=52-len(eleccion_random3)
                    cad=(espacio*valor)+asterisco
                    cadena4=eleccion_random3+cad
                else:
                    valor=52-len(eleccion_random4)
                    cad=(espacio*valor)+asterisco
                    cadena5=eleccion_random4+cad
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                     Haz elegido el nivel Dificil                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(3)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                               Las elecciones del computador, saldran en:                     *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(2)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                3                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                2                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                1                                             *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                                YA!                                           *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(1)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena1))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena2))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena3))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena4))
            print("    *                                                                                              *")
            print("    *                                          {}".format(cadena5))
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(4)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                        Se te agoto el tiempo :O                              *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            sleep(2)
            os.system("cls")
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *             Ahora escribe las opciones que les ganan a las generadas por el computador.      *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************")
            print()
            escritura0=input("Escribe tu primera eleccion: --------->")
            escritura1=input("Escribe tu segunda eleccion: --------->")
            escritura2=input("Escribe tu tercera eleccion: --------->")
            escritura3=input("Escribe tu cuarta eleccion: --------->")
            escritura4=input("Escribe tu cuarta eleccion: --------->")
            if (eleccion_random0=="papel" and escritura0=="tijera") or (eleccion_random0=="tijera" and escritura0=="piedra") or (eleccion_random0=="piedra" and escritura0=="papel"):
                if (eleccion_random1=="papel" and escritura1=="tijera") or (eleccion_random1=="tijera" and escritura1=="piedra") or (eleccion_random1=="piedra" and escritura1=="papel"):
                    if (eleccion_random2=="papel" and escritura2=="tijera") or (eleccion_random2=="tijera" and escritura2=="piedra") or (eleccion_random2=="piedra" and escritura2=="papel"):
                        if (eleccion_random3=="papel" and escritura3=="tijera") or (eleccion_random3=="tijera" and escritura3=="piedra") or (eleccion_random3=="piedra" and escritura3=="papel"):
                            if (eleccion_random4=="papel" and escritura4=="tijera") or (eleccion_random4=="tijera" and escritura4=="piedra") or (eleccion_random4=="piedra" and escritura4=="papel"):
                                print()
                                print("    ************************************************************************************************")
                                print("    *                                                                                              *")
                                print("    *                          Muy bien :D! Escribiste las elecciones correctas!                   *")
                                print("    *                                                                                              *")
                                print("    ************************************************************************************************")
                            else:
                                print()
                                print("    ************************************************************************************************")
                                print("    *                                                                                              *")
                                print("    *                          Lo sentimos, te equivocaste en una respuesta :(                     *")
                                print("    *                                                                                              *")
                                print("    ************************************************************************************************")
                        else:
                            print()
                            print("    ************************************************************************************************")
                            print("    *                                                                                              *")
                            print("    *                          Lo sentimos, te equivocaste en dos respuestas :(                    *")
                            print("    *                                                                                              *")
                            print("    ************************************************************************************************")
                    else:
                        print()
                        print("    ************************************************************************************************")
                        print("    *                                                                                              *")
                        print("    *                          Lo sentimos, te equivocaste en tres las respuestas :(               *")
                        print("    *                                                                                              *")
                        print("    ************************************************************************************************")
                else:
                    print()
                    print("    ************************************************************************************************")
                    print("    *                                                                                              *")
                    print("    *                          Lo sentimos, te equivocaste en cuatro las respuestas :(             *")
                    print("    *                                                                                              *")
                    print("    ************************************************************************************************")
            else:
                print()
                print("    ************************************************************************************************")
                print("    *                                                                                              *")
                print("    *                          Lo sentimos, te equivocaste en todas las respuestas :(             *")
                print("    *                                                                                              *")
                print("    ************************************************************************************************")
            sleep(3)
            os.system("cls")   
            print("    ************************************************************************************************")
            print("    *                                                                                              *")
            print("    *                                       Deseas volver a jugar?                                 *")
            print("    *                                                                                              *")
            print("    *                  Escribe si si deseas jugar o cualquier otro caracter para salir.            *")
            print("    *                                                                                              *")
            print("    ************************************************************************************************") 
            print()
            eleccionfinal=input("------------------------------------------->").lower()
            if eleccionfinal=="si" or eleccionfinal=="s":
                juego_ppt()
            else:
                break

def juego_TRIQUI():
    def campeon(pizarra, participante):
        """
        Determina si hay un ganador(triqui).
        :param string pizarra: Representa el tablero
        :param string participante:Representa el jugador
        Retorna un booleano 
        """
        if pizarra[4] == pizarra[2] == pizarra[6] == participante or pizarra[6] == pizarra[8] == pizarra[
            7] == participante or pizarra[4] == pizarra[5] == pizarra[3] == participante or pizarra[4] == pizarra[1] == \
                pizarra[7] == participante or pizarra[6] == pizarra[0] == pizarra[3] == participante or pizarra[8] == \
                pizarra[4] == pizarra[0] == participante or pizarra[5] == pizarra[2] == pizarra[8] == participante or \
                pizarra[1] == pizarra[2] == pizarra[0] == participante:
            return True
        else:
            return False

    def pizarra_llena(pizarra):
        """
        :param string pizarra: Representa el tablero de juego
        Determina si el tablero esta lleno.
        Retorna un booleano 
        """
        for i in pizarra:
            if i == " ":
                return False
        else:
            return True

    def lugar_libre(pizarra, lugar):
        """
        Determina si hay algun lugar libre
        :param string pizarra: Representa el tablero de juego
        :param string lugar: Representa las casillas del tablero
        Recibe parametros y retorna el lugar si hay un espacio libre.
        
        """
        return pizarra[lugar] == " "

    def movimiento_participante(pizarra):
        """
        Presenta el movimiento al participante, y si alguna posicion esta ocupada
        :param string pizarra: Representa el tablero de juego
        Retorna la ubicacion seleccionada por el usuario
        """
        ubicaciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ubicacion = None
        while True:
            if ubicacion not in ubicaciones:
                ubicacion = input("      Es tu turno de jugar. Escribe el numero: ")
            else:
                ubicacion = int(ubicacion)
                if not lugar_libre(pizarra, ubicacion - 1):
                    print("              Esta posicion esta ocupada ")
                else:
                    return ubicacion - 1

    def movimiento_computador_facil(lugarjuego):
        """
        Representa el movimiento del nivel facil del computador
        :param string lugarjuego: representan las casillas del tablero
        retorna el lugar en el cual jugara el computador
        """
        while True:
            lugar = random.randint(0, 8)
            if lugarjuego[lugar] == " ":
                return lugar

    def mov_computador_dificil(lugarjuego, participante):
        """
        Determina donde debe jugar el computador si hay dos fichas seguidas
        :param string lugarjuego: representan las casillas del tablero
        :param string participante: representa el jugador en el momento(humano o computador)
        Retorna el lugar en el cual jugara el computador
        """
        if lugarjuego[5] == lugarjuego[3] == participante and lugarjuego[4] == " ":
            lugar = 4
        elif lugarjuego[4] == lugarjuego[3] == participante and lugarjuego[5] == " ":
            lugar = 5
        elif lugarjuego[5] == lugarjuego[4] == participante and lugarjuego[3] == " ":
            lugar = 3

        elif lugarjuego[7] == lugarjuego[8] == participante and lugarjuego[6] == " ":
            lugar = 6
        elif lugarjuego[6] == lugarjuego[8] == participante and lugarjuego[7] == " ":
            lugar = 7
        elif lugarjuego[6] == lugarjuego[7] == participante and lugarjuego[8] == " ":
            lugar = 8

        elif lugarjuego[1] == lugarjuego[0] == participante and lugarjuego[2] == " ":
            lugar = 2
        elif lugarjuego[2] == lugarjuego[1] == participante and lugarjuego[0] == " ":
            lugar = 0
        elif lugarjuego[2] == lugarjuego[0] == participante and lugarjuego[1] == " ":
            lugar = 1

        elif lugarjuego[7] == lugarjuego[1] == participante and lugarjuego[4] == " ":
            lugar = 4
        elif lugarjuego[4] == lugarjuego[1] == participante and lugarjuego[7] == " ":
            lugar = 7
        elif lugarjuego[7] == lugarjuego[4] == participante and lugarjuego[1] == " ":
            lugar = 1

        elif lugarjuego[8] == lugarjuego[5] == participante and lugarjuego[2] == " ":
            lugar = 2
        elif lugarjuego[5] == lugarjuego[2] == participante and lugarjuego[8] == " ":
            lugar = 8
        elif lugarjuego[8] == lugarjuego[2] == participante and lugarjuego[5] == " ":
            lugar = 5


        elif lugarjuego[4] == lugarjuego[2] == participante and lugarjuego[6] == " ":
            lugar = 6
        elif lugarjuego[4] == lugarjuego[6] == participante and lugarjuego[2] == " ":
            lugar = 2
        elif lugarjuego[6] == lugarjuego[2] == participante and lugarjuego[4] == " ":
            lugar = 4


        elif lugarjuego[8] == lugarjuego[0] == participante and lugarjuego[4] == " ":
            lugar = 4
        elif lugarjuego[4] == lugarjuego[0] == participante and lugarjuego[8] == " ":
            lugar = 8
        elif lugarjuego[8] == lugarjuego[4] == participante and lugarjuego[0] == " ":
            lugar = 0

        elif lugarjuego[6] == lugarjuego[0] == participante and lugarjuego[3] == " ":
            lugar = 3
        elif lugarjuego[3] == lugarjuego[0] == participante and lugarjuego[6] == " ":
            lugar = 6
        elif lugarjuego[6] == lugarjuego[3] == participante and lugarjuego[0] == " ":
            lugar = 0
        else:
            while True:
                lugar = random.randint(0, 8)
                if lugarjuego[lugar] == " ":
                    break
        return lugar
    def primera_pantalla():
        """
        Genera la primera pantalla del triqui, donde selecciona el nivel del triqui.
        No recibe, retorna el nivel del juego seleccionado
        """
        print()
        print("                 ****************************************      ")
        print("                 *                TRIQUI                *      ")
        print("                 *  Escribe el nivel que deseas jugar.  *        ")
        print("                 *               1.Facil                *       ")
        print("                 *              2.Dificil               *        ")
        print("                 ****************************************  ")
        print()
        print()
        juego_nivel = ""
        while juego_nivel != "1" or juego_nivel != "2":
            juego_nivel = input("                    --->")
            return int(juego_nivel)

    def segunda_pantalla():
        """
        Genera la segunda pantalla, donde se selecciona la ficha a usar(O/X)
        No recibe, retorna humano,computador(fichas que usaran en el juego)
        """
        print()
        print("                 ****************************************      ")
        print("                 *                TRIQUI                *      ")
        print("                 *       Elije entre la ficha O o X     *        ")
        print("                 *              Escribe(O/X)            *       ")
        print("                 *           Empieza la ficha O         *        ")
        print("                 ****************************************  ")
        print()
        print()
        figura = ""
        while figura != "X" and figura != "O":
            figura = input("                    --->").upper()

        if figura == "X":
            humano = "X"
            computador = "O"
        else:
            humano = "O"
            computador = "X"
        return humano, computador

    def mostrar_pizarra(pizarra):
        """
        Genera el tablero del triqui, con sus distintos espacios
        :param string pizarra: Representa el tablero de juego
        
        """
        print()
        print("                               TRIQUI ")
        print()
        print("                  __________________________________      ")
        print("                 | 1         |2          |3         |")
        print("                 |      {}    |     {}     |     {}    |".format(pizarra[0], pizarra[1], pizarra[2]))
        print("                 |___________|___________|__________|  ")
        print("                 | 4         |5          |6         | ")
        print("                 |      {}    |     {}     |     {}    |".format(pizarra[3], pizarra[4], pizarra[5]))
        print("                 |___________|___________|__________|")
        print("                 | 7         |8          |9         |")
        print("                 |      {}    |     {}     |     {}    |".format(pizarra[6], pizarra[7], pizarra[8]))
        print("                 |___________|___________|__________|")
        print()

    def continuarjugando():
        """
        Tiene la funcion de preguntar si se quiere volver a jugar.
        No recibe parametros, retorna un booleano
        """
        print()
        respuesta = input("              Otra partida ? Escribe si  ").lower()
        if respuesta == "s" or respuesta == "si":
            return True
        else:
            return False

    jugando = True
    while jugando:

        pizarra = [" "] * 9  # elejiremos la ficha y el turno

        os.system("cls")

        nivel = primera_pantalla()

        os.system("cls")

        humano, computador = segunda_pantalla()

        os.system("cls")

        mostrar_pizarra(pizarra)
        if humano == "O":
            turno = "Humano"
        else:
            turno = "Computador"

        partida = True

        while partida:
            if pizarra_llena(pizarra):
                print("                  Ninguno pudo ganar en esta ocasion! ")
                partida = False
            elif turno == "Humano":
                lugar = movimiento_participante(pizarra)
                pizarra[lugar] = humano
                turno = "Computador"
                os.system("cls")
                mostrar_pizarra(pizarra)
                if campeon(pizarra, humano):
                    print("           Felicidades! Haz ganado! ")
                    partida = False
            elif turno == "Computador":
                print("   El computador esta eligiendo ...")
                time.sleep(2)
                if nivel == 1:
                    lugar = movimiento_computador_facil(pizarra)
                elif nivel == 2:
                    lugar = mov_computador_dificil(pizarra, humano)
                pizarra[lugar] = computador
                turno = "Humano"
                os.system("cls")
                mostrar_pizarra(pizarra)
                if campeon(pizarra, computador):
                    print("                  Haz perdido :( ")
                    partida = False

        jugando = continuarjugando()
def imprimir():
    """
    Representa la actividad para explicar la funcion print
    No recibe, no retorna
    """
    time.sleep(1)
    print("Bienvenido a nuestra primera actividad, en este buscaremos enseñar conceptos basicos "
          "en cuanto a la sintaxis y logica en Python.")
    time.sleep(4)
    print("Primeramente, vamos a presentar la sentencia print()")
    time.sleep(3)
    print()
    print("En resumidas cuentas, la sentencia print nos sirve para imprimir un mensaje por pantalla.")
    time.sleep(3)
    print()
    print("Esto lo hacemos de la siguiente forma: ---->print('tu mensaje')")
    time.sleep(3)
    print("Ahora intentalo tu!. Escribe un mensaje usando print, como el ejemplo de arriba.")
    while True:
        a = input()
        for i in range(len(a)):
            if a[i] == "(":
                valor = i
            if a[i] == ")":
                valor2 = i
        imprimir = "print('"
        cerrar = "')"
        try:
            if a == (imprimir + (a[valor + 2:valor2 - 1]) + cerrar)and (type(a)==str):
                time.sleep(1)
                print("Muy bien!")
                time.sleep(1)
                print("El mensaje que imprimiste por pantalla, fue: {}".format(a[valor + 2:valor2 - 1]))
                break
            elif a == ((imprimir[:len(imprimir) - 1] + (a[valor + 1:valor2 + 1]))):
                time.sleep(1)
                print("Muy bien!")
                time.sleep(1)
                print("El mensaje que imprimiste por pantalla, fue: {}".format(a[valor + 1:valor2]))
                break
            else:
                time.sleep(2)
                print("Haz escrito el ejercicio de una manera incorrecta. Intenta nuevamente. ")
        except ValueError:
            time.sleep(2)
            print("Haz escrito el ejercicio de una manera incorrecta. Intenta nuevamente. ")
    time.sleep(4)
    print("Como puedes observar, por medio de la función print, imprimimos un texto por pantalla.")

def variables():
    """
    Representa la actividad para explicar las variables, tipos y asignaciones
    No recibe, no retorna
    """
    contador, contador2, contador3, contador4 = 0, 0, 0, 0
    time.sleep(1)
    print("Ahora, vamos a aprender acerca de variables.")
    time.sleep(4)
    print(
        "Primeramente, para comprender las variables de una manera correcta, es necesario conocer los tipos de datos.")
    time.sleep(5)
    print("En esta ocasion, presentaremos los tipos de datos enteros, flotantes y caracteres.")
    time.sleep(4)
    print(
        "Los datos de tipo entero o int, se refieren principalmente al conjunto de los numeros naturales, incluyendo a 0 y a los numeros negativos.")
    time.sleep(6)
    print("Ejemplos de estos son los numeros: 1, 2, 0, -5 y -10. Por nombrar algunos.")
    time.sleep(4)
    print("Ahora, buscaremos ver que se evidencio el concepto de una manera correcta.")
    time.sleep(1)
    while True:
        posible_entero = input("Ingresa un numero, el cual sea entero. ")
        try:
            entero = int(posible_entero)
            time.sleep(1)
            print("Muy bien! Escribiste un numero que puede ir almacenado en una variable de tipo entero.")
            time.sleep(3)
            print("Escribiste el numero {}".format(entero))
            time.sleep(3)
            os.system("cls")
            break
        except ValueError:
            time.sleep(1)
            print("El numero que escribiste no es entero. Intenta nuevamente. ")
    print("Continuando, observaremos los datos de tipo flotante o 'float'.")
    time.sleep(4)
    print("Los datos de tipo flotante, pueden ser similares a los de tipo entero, pero en este caso, representan los numeros decimales. ")
    time.sleep(5)
    print("Estos datos de tipo flotante, estan separados por medio de un punto.")
    time.sleep(4)
    print("Ejemplos de estos, pueden ser numeros tales como: 3.2, 2.3, 1.58, o -5.8")
    time.sleep(4)
    print("Ahora, intentalo tu!")
    time.sleep(1)
    while True:
        posible_flotante = input("Ingresa un numero que sea flotante ")
        for i in range(len(posible_flotante)):
            if posible_flotante[i] == ".":
                contador += 1
        if contador == 1:
            try:
                flotante = float(posible_flotante)
                time.sleep(2)
                print(
                    "Muy bien! Escribiste un numero que puede ir almacenado en una variable de tipo flotante.")
                time.sleep(2)
                print("Escribiste el numero {}".format(flotante))
                time.sleep(2)
                break
            except ValueError:
                time.sleep(1)
                print("El numero que escribiste no es flotante. Intenta nuevamente.  ")
                time.sleep(1)
        else:
            time.sleep(1)
            print("El numero que escribiste no es flotante. Intenta nuevamente.  ")
            time.sleep(1)
    os.system("cls")
    time.sleep(2)
    print("Finalmente, mencionaremos las cadenas o 'strings'.")
    time.sleep(4)
    print("Las cadenas o strings, sirven para almacenar cadenas, que pueden ser tanto de letras como de numeros.")
    time.sleep(5)
    print("Pero es importante tener en cuenta, que asi almacenamos un numero, seguira siendo una cadena.")
    time.sleep(5)
    print("Las cadenas, se pueden identificar, ya que van encerradas entre comillas. (')")
    time.sleep(5)
    print("Un ejemplo de la sintaxis de una cadena, puede ser por ejemplo 'hola', o '2342'.")
    time.sleep(5)
    while True:
        time.sleep(1)
        prob_cadena = input("Ingresa una cadena de caracteres. Recuerda escribirla entre comillas (')  ")
        if prob_cadena[0] == "'":
            contador2 += 1
            if prob_cadena[len(prob_cadena) - 1] == "'":
                contador2 += 1
        if contador2 == 2:
            cadena_string = prob_cadena[1:(len(prob_cadena) - 1)]
            time.sleep(1)
            print("Muy bien! Escribiste la cadena de una manera correcta.")
            time.sleep(3)
            print("Escribiste la cadena: {}".format(cadena_string))
            time.sleep(3)
            break
        else:
            time.sleep(1)
            print("Intenta nuevamente, escribiste la cadena de una manera incorrecta. Recuerda las comillas.")
            time.sleep(1)
    os.system("cls")
    time.sleep(3)
    print("Ya que conocemos los tipos de variables que usaremos a lo "
          "largo de nuestro programa, ahora enseñaremos a asignarlas.")
    time.sleep(5)
    print("Para asignar valores a una variable, usamos el = ")
    time.sleep(5)
    print("La sentencia de asignación vincula un nombre, en el lado izquierdo del operador, "
          "con un valor, en el lado derecho.")
    time.sleep(5)
    print("En otras palabras, la asignacion, se realizaria de la siguiente forma: ")
    time.sleep(3)
    print("variable = valor asignado")
    time.sleep(3)
    print("De una manera mas real, podria presentarse una variable, asignada de la siguiente manera:")
    time.sleep(4)
    print(" x = 2 ")
    time.sleep(3)
    print("En este caso, como podemos ver, le asignamos el valor de 2 a la variable de nombre 'x'")
    time.sleep(4)
    print("Como hemos enseñado, a lo largo de este programa, poseemos distintos tipos de datos"
          "y es muy importante saber que estos pueden ser almacenados en variables. ")
    time.sleep(5)
    print("Ahora, vamos a intentarlo de una manera practica.")
    while True:
        time.sleep(1)
        variable_asig = input(
            "Ingresa una variable y un dato asignado a esta (puede ser entero, flotante o cadena).  ").strip()
        if len(variable_asig) >= 3:
            for i in range(len(variable_asig)):
                if variable_asig[i] == "=":
                    contador3 += 1
                    lugarvar = i
                if variable_asig[i] == "'":
                    contador4 += 1
            parte_cad1 = variable_asig[:lugarvar]
            parte_cad2 = variable_asig[lugarvar + 1:]
            if (parte_cad1 + "=" + parte_cad2) == variable_asig:
                if contador4 == 2 and contador3 == 1:
                    time.sleep(1)
                    print("Muy bien! Realizaste la asignacion de una variable de una manera correcta.")
                    time.sleep(4)
                    print(f"Le asignaste a la variable {parte_cad1}, el valor de {parte_cad2}")
                    time.sleep(5)
                    break
                elif contador3 == 1:
                    time.sleep(1)
                    print("Muy bien! Realizaste la asignacion de una variable de una manera correcta.")
                    time.sleep(4)
                    print(f"Le asignaste a la variable {parte_cad1}, el valor de {parte_cad2}")
                    time.sleep(5)
                    break
                else:
                    time.sleep(1)
                    print("Realizaste mal la asignacion, intenta nuevamente.")
                    time.sleep(1)
            else:
                time.sleep(1)
                print("Realizaste mal la asignacion, intenta nuevamente.")
                time.sleep(1)
        else:
            time.sleep(1)
            print("Realizaste mal la asignacion, intenta nuevamente.")
            time.sleep(1)
    os.system("cls")


def ciclo_while():
    """
    Representa la actividad para explicar el ciclo while
    No recibe, no retorna
    """
    contador6 = 0
    time.sleep(1)
    print("Ahora presentaremos el ciclo while. ")
    time.sleep(3)
    print("Podriamos mencionar que while se puede identificar en español como 'mientras' ")
    time.sleep(4)
    print(
        "Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).")
    time.sleep(5)
    print("La sintaxis del bucle while es la siguiente: ")
    time.sleep(3)
    print("while condicion:")
    time.sleep(2)
    print("\tcuerpo del codigo")
    time.sleep(2)
    print("El ciclo while funciona de la siguiente manera: ")
    time.sleep(4)
    print("1. Primeramente, evalua la condicion, devolviendo ya sea True O False ")
    time.sleep(4)
    print("2. Si la condicion es falsa, sale de la sentencia while. ")
    time.sleep(4)
    print(
        "3.Si la condición es verdadera, ejecutar cada una de las sentencias en el cuerpo del bucle while, y luego volver al paso 1.")
    time.sleep(5)
    print("Vamos a mostrar como funcionaria el bucle while. ")
    time.sleep(4)
    print(
        "Primero le vamos a asignar a nuestro contador el valor de 1 y a nuestra variable numero, el valor de 5. Esto lo hacemos de la siguiente forma:")
    time.sleep(4)
    print("contador=1")
    time.sleep(3)
    print("numero=5")
    time.sleep(3)
    print(
        "Ahora, usaremos la sentencia while, para que se imprimima el valor del contador hasta que sea igual al valor del numero.")
    time.sleep(5)
    print("while contador<=numero:")
    time.sleep(3)
    print("\tprint(contador)         ")
    time.sleep(3)
    print("\tcontador=contador+1         ")
    time.sleep(3)
    print("Lo que imprimiria nuestro bucle, seria lo siguiente: ")
    time.sleep(1)
    contador, numero = 1, 5
    while contador <= numero:
        time.sleep(1)
        print(contador)
        contador += 1
    time.sleep(2)
    print("Ahora intentalo tu! Escribe un codigo el cual imprima desde el numero 0 hasta el numero 2.")
    time.sleep(4)
    print("Esto hazlo, asignandole a una variable, el numero 3 y un contador que tenga el numero 0")
    time.sleep(4)
    print("Ademas de ello, usa un simbolo de menor(<) ")
    time.sleep(4)
    print(
        "TIP : El proceso que deberas hacer, es ir sumandole uno al contador. El ciclo se repetira mientras el valor del contador sea menor al valor de la otra variable. ")
    time.sleep(4)
    while True:
        time.sleep(2)
        variables_while = input("Primero, asigna tu primer variable ( la variable, que lleva el numero 3).\n ")
        time.sleep(2)
        variables_while2 = input("Ahora , asigna tu segunda variable (el contador, que lleva el numero 0). \n ")
        time.sleep(2)
        escritura_while = input("Escribe ahora el condicional while \n")
        a = input("\t")
        b = input("\t")
        for i in range(len(variables_while)):
            if variables_while[i] == "=":
                valor1 = i
                contador6 += 1
                num1 = int(variables_while[valor1 + 1:].strip())
        for i in range(len(variables_while2)):
            if variables_while2[i] == "=":
                valor2 = i
                contador6 += 1
                num2 = int(variables_while2[valor2 + 1:].strip())
        lugarw = escritura_while.find("while")
        if lugarw == 0:
            if num1 == 3 and num2 == 0:
                if ("while " + (variables_while2[:valor2]) + "<" + (
                        variables_while[:valor1]) + ":") == escritura_while:
                    if ("print(" + (variables_while2[:valor2]) + ")") == a:
                        if ((variables_while2[:valor2]) + "=" + (variables_while2[:valor2]) + "+1") == b:
                            time.sleep(1)
                            print("Muy bien! Escribiste el codigo de una manera correcta :D ")
                            time.sleep(3)
                            print("Imprimiste los numeros 0,1,2 ")
                            time.sleep(3)
                            break
                        else:
                            time.sleep(1)
                            print(
                                "Ingresa nuevamente los datos, los escribiste erroneamente. Repetiremos las instrucciones.")
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        print(
                            "Ingresa nuevamente los datos, los escribiste erroneamente. Repetiremos las instrucciones.")
                        time.sleep(1)
                else:
                    print(
                        "Ingresa nuevamente los datos, los escribiste erroneamente. Repetiremos las instrucciones.")
            else:
                time.sleep(1)
                print(
                    "Ingresa nuevamente los datos, los escribiste erroneamente. Repetiremos las instrucciones.")
                time.sleep(1)
        else:
            time.sleep(1)
            print("Ingresa nuevamente los datos, los escribiste erroneamente. Repetiremos las instrucciones.")
            time.sleep(1)


def ciclo_for():
    """
    Representa la actividad para explicar el ciclo for.
    No recibe, no retorna
    """
    time.sleep(1)
    print("Ahora trataremos el bucle for. ")
    time.sleep(3)
    print("Un bucle for es un bucle que repite el bloque de instrucciones un número prederminado de veces.")
    time.sleep(4)
    print(
        "El bloque de instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración.")
    time.sleep(5)
    print("La sintaxis del bucle for, seria la siguiente: ")
    time.sleep(3)
    print("for variable in elemento iterable (lista, cadena, range, etc.):")
    time.sleep(4)
    print("\tcuerpo del bucle")
    time.sleep(3)
    print(
        "No es necesario definir la variable de control antes del bucle, aunque se puede utilizar como variable de control una variable ya definida en el programa.")
    time.sleep(5)
    print(
        "Un bucle for puede tener multiples usos como en listas, tuplas, etc. Pero en este caso, presentaremos su funcion de manera breve")
    time.sleep(5)
    print("Vamos a evidenciar un ejemplo, para asi comprender mas a fondo su funcionamiento.")
    time.sleep(4)
    print("Realizaremos un programa que imprimia las letras de una palabra a nuestra eleccion")
    time.sleep(4)
    print("En este caso, sera AMIGO.")
    time.sleep(3)
    print("Primeramente, ubicaremos nuestro for, de la siguiente forma: ")
    time.sleep(3)
    print("for i in 'AMIGO':")
    time.sleep(3)
    print("\tprint(i)")
    time.sleep(3)
    print("De esta forma, nuestro bucle, imprimiria cada una de las letras de la palabra AMIGO. ")
    time.sleep(4)
    print("Imprimiria lo siguiente: ")
    for i in "AMIGO":
        time.sleep(1)
        print(i)
    time.sleep(2)
    print("Ahora intentalo tu! Vamos a imprimir las letras de la palabra PERRO. ")
    time.sleep(3)
    print("TIP: Recuerda usar las comillas simples para las cadenas de caracteres (') ")
    time.sleep(3)

    while True:
        time.sleep(1)
        for1 = input("Escribe primero como se ubicaria el bucle for.\n ")
        time.sleep(1)
        print("Ahora, escribe el cuerpo del bucle")
        for2 = input("\t")
        lugar = (for1.find("in"))
        if for1.find("for i in") == 0:
            for i in range(len(for1)):
                if for1[i] == "r":
                    posf = i
                    break
            if ("for" + for1[i + 1:lugar] + "in 'PERRO':") == for1 and (
                    ("print(" + for1[i + 1:lugar] + ")") == for2 or (
                    "print(" + for1[i + 2:lugar - 1] + ")") == for2):
                time.sleep(1)
                print("Muy bien! :D ")
                time.sleep(2)
                print("Implementaste correctamente el bucle for ")
                time.sleep(3)
                print("Lo que imprimiste por pantalla fue: ")
                time.sleep(3)
                for i in "PERRO":
                    time.sleep(0.5)
                    print(i)
                time.sleep(1.5)
                break
            else:
                time.sleep(1)
                print("Lo escribiste erroneamente, intenta nuevamente. ")
                time.sleep(1)
        else:
            time.sleep(1)
            print("Lo escribiste erroneamente, intenta nuevamente. ")
            time.sleep(1)
    os.system("cls")
    time.sleep(3)
    print("Como pudiste ver, el ciclo for realiza una serie de acciones, un numero determinado de veces.")
    time.sleep(3)
    print("Ahora, vamos a enseñarte otra funcion que es muy util en el ciclo for, la funcion range ")
    time.sleep(4)
    print(
        "Su sintaxis es muy similar a la del for inicial, pero en este caso ubicamos la palabra range, de la siguiente forma: ")
    time.sleep(5)
    print("for variable in range(numero de veces que se ejecuta el bucle):")
    time.sleep(3)
    print("\tcuerpo del bucle")
    time.sleep(3)
    print("Debes saber que range() controla el número de veces que se ejecuta el bucle.")
    time.sleep(3)
    print("Vamos a presentar un ejemplo de la funcion range.")
    time.sleep(3)
    print("Primero escribimos nuestro for, de la siguiente forma: ")
    time.sleep(3)
    print("for i in range(3):")
    time.sleep(3)
    print("Luego, el cuerpo del bucle, el cual imprimiria la palabra 'Hola' ")
    time.sleep(3)
    print("\tprint('Hola')")
    time.sleep(3)
    print("Nuestro programa, imprimiria lo siguiente: ")
    time.sleep(2)
    for i in range(3):
        time.sleep(1)
        print("Hola")
    time.sleep(2)
    print("Ahora vamos a intentarlo! Realiza un programa que imprima la palabra computador, 4 veces")
    while True:
        time.sleep(1.5)
        for3 = input("Escribe primero el bucle for: \n")
        time.sleep(1.5)
        print("Ahora ingresa el cuerpo del codigo. ")
        for4 = input("\t")
        for i in range(len(for3)):
            if for3[i] == "r":
                lugar3 = i
                break
        lugar2 = (for3.find("in"))
        try:
            if ("for" + for3[lugar3 + 1:lugar2] + "in range(4):") == for3 and (("print('computador')") == for4):
                time.sleep(1.5)
                print("Muy bien! Realizaste la implementacion de range de una manera correcta :D")
                time.sleep(3)
                print("Lo que imprimiste fue: ")
                time.sleep(2)
                for i in range(4):
                    time.sleep(1)
                    print('computador')
                    time.sleep(1.5)
                break
            else:
                time.sleep(1.5)
                print("Intentalo nuevamente, lo escribiste mal. Recuerda las comillas simples para las cadenas (') ")
                time.sleep(1)
        except ValueError:
            time.sleep(1.5)
            print("Intentalo nuevamente, lo escribiste mal. Recuerda las comillas simples para las cadenas (') ")
            time.sleep(1)

def main():
    """
    Llama la funcion de pantalla inicial y define avance
    No recibe parametros
    No retorna algun valor
    """
    system('cls')
    avance=0
    pantalla_inicial(avance)
main()
