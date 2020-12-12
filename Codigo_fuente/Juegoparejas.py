import pygame,sys,random
from pygame import *
import tkinter as tk
import time
def JUEGOPAREJAS():
    """
    Esta funcion genera el juego de encontrar las parejas, con las funciones necesarios para el funcionamiento
    dle juego
    No recibe
    :return None
    """
    cuadrados=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    ##############Primeramente, definimos los cuadrados de nuestra pizarra##############
    Cuadrado1=Rect(420,140,100,100)
    Cuadrado2=Rect(520,140,100,100)
    Cuadrado3=Rect(620,140,100,100)
    Cuadrado4=Rect(720,140,100,100)
    Cuadrado5=Rect(420,240,100,100)
    Cuadrado6=Rect(520,240,100,100)
    Cuadrado7=Rect(620,240,100,100)
    Cuadrado8=Rect(720,240,100,100)
    Cuadrado9=Rect(420,340,100,100)
    Cuadrado10=Rect(520,340,100,100)
    Cuadrado11=Rect(620,340,100,100)
    Cuadrado12=Rect(720,340,100,100)
    Cuadrado13=Rect(420,440,100,100)
    Cuadrado14=Rect(520,440,100,100)
    Cuadrado15=Rect(620,440,100,100)
    Cuadrado16=Rect(720,440,100,100)

    Totalcuadrados=(Cuadrado1,Cuadrado2,Cuadrado3,Cuadrado4,Cuadrado5,Cuadrado6,Cuadrado7,Cuadrado8,Cuadrado9,Cuadrado10,Cuadrado11,Cuadrado12,Cuadrado13,Cuadrado14,Cuadrado15,Cuadrado16)
    listafiguras=[]
    def ventanaprincipal():
        """"
        Esta funcion, genera la ventana principal de nuestro juego de parejas. Contiene
        cada uno de los titulos e imagenes del juego.
        :return None
        """
        titulo_principal=pygame.image.load("../recursor/Imagenes juegos/parejas_1.png")
        ventana.blit(titulo_principal, (405,0))
        logo_plaython=pygame.image.load("../recursor/Imagenes juegos/plaython.png")#Cargamos la imagen del logo
        imagen_decoracion=pygame.image.load("../recursor/Imagenes juegos/imagenpc.png")
        imagen_decoracion = pygame.transform.scale(imagen_decoracion, (210, 210))
        ventana.blit(logo_plaython, (900, 180))
        ventana.blit(imagen_decoracion,(100,240))
        titulo_plaython = pygame.image.load("../recursor/Imagenes juegos/TITULOPLAYTHON.png")
        titulo_plaython = pygame.transform.scale(titulo_plaython, (240, 150))
        ventana.blit(titulo_plaython, (505, 550))

    def dibujarcirculos(x,color):
        """
        Esta funcion, dibuja cada uno de las figuras de forma circular del juego en base a su generacion aleatoria.
        :param int x: Representa la casilla elegida, y en base a este valor, se dibuja un cuadrado en determinado lugar
        :param tuple  color: Representa un color determinado, el cual se encuentra escrito en base a sus valores RGB
        :return None
        """
        if x==1:
            pygame.draw.circle(ventana,color,(470,190),30)
        elif x==2:
            pygame.draw.circle(ventana,color,(570,190),30)
        elif x==3:
            pygame.draw.circle(ventana,color,(670,190),30)
        elif x==4:
            pygame.draw.circle(ventana,color,(770,190),30)
        elif x==5:
            pygame.draw.circle(ventana,color,(470,290),30)
        elif x==6:
            pygame.draw.circle(ventana,color,(570,290),30)
        elif x==7:
            pygame.draw.circle(ventana,color,(670,290),30)
        elif x==8:
            pygame.draw.circle(ventana,color,(770,290),30)
        elif x==9:
            pygame.draw.circle(ventana,color,(470,390),30)
        elif x==10:
            pygame.draw.circle(ventana,color,(570,390),30)
        elif x==11:
            pygame.draw.circle(ventana,color,(670,390),30)
        elif x==12:
           pygame.draw.circle(ventana,color,(770,390),30)
        elif x==13:
            pygame.draw.circle(ventana,color,(470,490),30)
        elif x==14:
            pygame.draw.circle(ventana,color,(570,490),30)
        elif x==15:
            pygame.draw.circle(ventana,color,(670,490),30)
        elif x==16:
            pygame.draw.circle(ventana,color,(770,490),30)

    def dibujarcuadrados(x,color):
        """
        Esta funcion, dibuja cada uno de las figuras de forma cuadrada del juego en base a su generacion aleatoria.
        :param int x: Representa la casilla elegida, y en base a este valor, se dibuja un cuadrado en determinado lugar
        :param tuple  color: Representa un color determinado, el cual se encuentra escrito en base a sus valores RGB
        :return None
        """
        if x==1:
            pygame.draw.rect(ventana,color,Rect(440,160,60,60))
        elif x==2:
            pygame.draw.rect(ventana,color,Rect(540,160,60,60))
        elif x==3:
            pygame.draw.rect(ventana,color,Rect(640,160,60,60))
        elif x==4:
            pygame.draw.rect(ventana,color,Rect(740,160,60,60))
        elif x==5:
            pygame.draw.rect(ventana,color,Rect(440,260,60,60))
        elif x==6:
            pygame.draw.rect(ventana,color,Rect(540,260,60,60))
        elif x==7:
            pygame.draw.rect(ventana,color,Rect(640,260,60,60))
        elif x==8:
            pygame.draw.rect(ventana,color,Rect(740,260,60,60))
        elif x==9:
            pygame.draw.rect(ventana,color,Rect(440,360,60,60))
        elif x==10:
            pygame.draw.rect(ventana,color,Rect(540,360,60,60))
        elif x==11:
            pygame.draw.rect(ventana,color,Rect(640,360,60,60))
        elif x==12:
            pygame.draw.rect(ventana,color,Rect(740,360,60,60))
        elif x==13:
            pygame.draw.rect(ventana,color,Rect(440,460,60,60))
        elif x==14:
            pygame.draw.rect(ventana,color,Rect(540,460,60,60))
        elif x==15:
            pygame.draw.rect(ventana,color,Rect(640,460,60,60))
        elif x==16:
            pygame.draw.rect(ventana,color,Rect(740,460,60,60))

    def dibujardiamantes(x,color):
        """
        Esta funcion, dibuja cada uno de las figuras de forma de diamante del juego en base a su generacion aleatoria.
        :param int x: Representa la casilla elegida, y en base a este valor, se dibuja un cuadrado en determinado lugar
        :param tuple  color: Representa un color determinado, el cual se encuentra escrito en base a sus valores RGB
        :return None
        """
        if x==1:
            pygame.draw.polygon(ventana,color,( (430,190),(470,160),(510,190),(470,220)))
        elif x==2:
            pygame.draw.polygon(ventana,color,( (530,190),(570,160),(610,190),(570,220) ))
        elif x==3:
            pygame.draw.polygon(ventana,color,( (630,190),(670,160),(710,190),(670,220) ))
        elif x==4:
            pygame.draw.polygon(ventana,color,( (730,190),(770,160),(810,190),(770,220) ))
        elif x==5:
            pygame.draw.polygon(ventana,color,( (430,290),(470,260),(510,290),(470,320) ))
        elif x==6:
            pygame.draw.polygon(ventana,color,( (530,290),(570,260),(610,290),(570,320) ))
        elif x==7:
            pygame.draw.polygon(ventana,color,( (630,290),(670,260),(710,290),(670,320) ))
        elif x==8:
            pygame.draw.polygon(ventana,color,( (730,290),(770,260),(810,290),(770,320) ))
        elif x==9:
            pygame.draw.polygon(ventana,color,( (430,390),(470,360),(510,390),(470,420) ))
        elif x==10:
            pygame.draw.polygon(ventana,color,( (530,390),(570,360),(610,390),(570,420) ))
        elif x==11:
            pygame.draw.polygon(ventana,color,( (630,390),(670,360),(710,390),(670,420) ))
        elif x==12:
           pygame.draw.polygon(ventana,color,( (730,390),(770,360),(810,390),(770,420) ))
        elif x==13:
            pygame.draw.polygon(ventana,color,( (430,490),(470,460),(510,490),(470,520) ))
        elif x==14:
            pygame.draw.polygon(ventana,color,( (530,490),(570,460),(610,490),(570,520) ))
        elif x==15:
            pygame.draw.polygon(ventana,color,( (630,490),(670,460),(710,490),(670,520) ))
        elif x==16:
            pygame.draw.polygon(ventana,color,( (730,490),(770,460),(810,490),(770,520) ))
    def dibujartriangulos(x,color):
        """
        Esta funcion, dibuja cada uno de las figuras de forma triangular del juego en base a su generacion aleatoria.
        :param int x: Representa la casilla elegida, y en base a este valor, se dibuja un cuadrado en determinado lugar
        :param tuple  color: Representa un color determinado, el cual se encuentra escrito en base a sus valores RGB
        :return None
        """
        if x==1:
            pygame.draw.polygon(ventana,color,( (430,160),(510,160),(470,220) ))
        elif x==2:
            pygame.draw.polygon(ventana,color,( (530,160),(610,160),(570,220) ))
        elif x==3:
            pygame.draw.polygon(ventana,color,( (630,160),(710,160),(670,220) ))
        elif x==4:
            pygame.draw.polygon(ventana,color,( (730,160),(810,160),(770,220) ))
        elif x==5:
            pygame.draw.polygon(ventana,color,( (430,260),(510,260),(470,320)))
        elif x==6:
            pygame.draw.polygon(ventana,color,( (530,260),(610,260),(570,320) ))
        elif x==7:
            pygame.draw.polygon(ventana,color,( (630,260),(710,260),(670,320) ))
        elif x==8:
            pygame.draw.polygon(ventana,color,( (730,260),(810,260),(770,320) ))
        elif x==9:
            pygame.draw.polygon(ventana,color,( (430,360),(510,360),(470,420) ))
        elif x==10:
            pygame.draw.polygon(ventana,color,( (530,360),(610,360),(570,420) ))
        elif x==11:
            pygame.draw.polygon(ventana,color,( (630,360),(710,360),(670,420) ))
        elif x==12:
           pygame.draw.polygon(ventana,color,( (730,360),(810,360),(770,420) ))
        elif x==13:
            pygame.draw.polygon(ventana,color,( (430,460),(510,460),(470,520) ))
        elif x==14:
            pygame.draw.polygon(ventana,color,( (530,460),(610,460),(570,520) ))
        elif x==15:
            pygame.draw.polygon(ventana,color,( (630,460),(710,460),(670,520) ))
        elif x==16:
            pygame.draw.polygon(ventana,color,( (730,460),(810,460),(770,520) ))

    def iniciarjuego():
        """"
        Esta funcion, crea cuatro figuras de cada una de las posibles, dos de ellas con diferente color de las otras dos.
        """
        for i in range(4):
            if i == 1 or i == 0:
                color = (250,208,120,98)
            else:
                color = (159, 250, 120,98)
            x = random.choice(cuadrados)
            listafiguras.append(x)
            dibujarcuadrados(x, color)
            cuadrados.remove(x)

        for i in range(4):
            if i == 0 or i == 1:
                color = (195, 139, 255,100)
            else:
                color = (250, 242, 120,98)
            x = random.choice(cuadrados)
            listafiguras.append(x)
            dibujarcirculos(x, color)
            cuadrados.remove(x)

        for i in range(4):
            if i == 0 or i == 1:
                color = (250, 145, 137,98)
            else:
                color = (126, 139, 250,98)
            x = random.choice(cuadrados)
            listafiguras.append(x)
            dibujartriangulos(x, color)
            cuadrados.remove(x)

        for i in range(4):
            if i == 0 or i == 1:
                color = (176, 255, 237,100)
            else:
                color = (255, 176, 228,100)
            x = random.choice(cuadrados)
            listafiguras.append(x)
            dibujardiamantes(x, color)
            cuadrados.remove(x)

    def mostrar(posicion_del_mouse):
        """
        Esta funcion muestra segun la casilla que clickee el jugador.
        :param tuple posicion_del_mouse: Este parametro representa segun clickee el jugador (posicion en x y y).
        """
        numerodecuadrado = numerocuadrado(posicion_del_mouse)
        ubicaciondelcuadrado=ubicacion_cuadrado(posicion_del_mouse)
        if ubicaciondelcuadrado==0 or ubicaciondelcuadrado==1:
            color = (250,208,120,98)
            dibujarcuadrados(numerodecuadrado,color)
        elif ubicaciondelcuadrado==2 or ubicaciondelcuadrado==3:
            color = (159, 250, 120,98)
            dibujarcuadrados(numerodecuadrado,color)
        elif ubicaciondelcuadrado==4 or ubicaciondelcuadrado==5:
            color = (195, 139, 255,100)
            dibujarcirculos(numerodecuadrado,color)
        elif ubicaciondelcuadrado==6 or ubicaciondelcuadrado==7:
            color = (250, 242, 120,98)
            dibujarcirculos(numerodecuadrado,color)
        elif ubicaciondelcuadrado==8 or ubicaciondelcuadrado==9:
            color = (250, 145, 137,98)
            dibujartriangulos(numerodecuadrado,color)
        elif ubicaciondelcuadrado==10 or ubicaciondelcuadrado==11:
            color = (126, 139, 250,98)
            dibujartriangulos(numerodecuadrado,color)
        elif ubicaciondelcuadrado==12 or ubicaciondelcuadrado==13:
            color = (176, 255, 237,100)
            dibujardiamantes(numerodecuadrado,color)
        elif ubicaciondelcuadrado==14 or ubicaciondelcuadrado==15:
            color = (255, 176, 228,100)
            dibujardiamantes(numerodecuadrado,color)

    def esconderfichas(posicion_del_mouse):
        """"
        Esta funcion, esconde las fichas, si la seleccion del usuario no es la correcta.
        :param tuple posicion_del_mouse: :param tuple primeraeleccion: Representa la posicion de donde clickeo el jugador (tanto en el ejex como en el eje y).
        """
        numerodecuadrado=numerocuadrado(posicion_del_mouse)
        for j in range(16):
            if numerodecuadrado==j+1:
                pygame.draw.rect(ventana,(135,206,250),Totalcuadrados[j].inflate(-10,-10))

    def encontrarparejas(primeraeleccion,segundaeleccion):
        """
        Esta funcion determina si se encontro una pareja.
        :param tuple primeraeleccion: Representa la posicion de donde clickeo el jugador (tanto en el ejex como en el eje y).
        :param tuple segundaeleccion: Representa la segunda posicion de donde clickeo el jugador (tanto en el ejex como en el eje y).
        Retorna un booleano
        """
        x=ubicacion_cuadrado(primeraeleccion)
        y=ubicacion_cuadrado(segundaeleccion)
        if (x==0 and y==1 or x==1 and y==0)\
            or (x == 2 and y == 3 or x == 3 and y == 2) \
            or (x == 4 and y == 5 or x == 5 and y == 4)\
            or (x == 6 and y == 7 or x == 7 and y == 6)\
            or (x == 8 and y == 9 or x == 9 and y == 8) \
            or (x==10 and y==11 or x==11 and y==10)\
            or (x==12 and y==13 or x==13 and y==12)\
            or (x==14 and y==15 or x==15 and y==14):
                return True

    def ubicacion_cuadrado(posicion_del_mouse):
        """
        Esta funcion, retorna la figura que se encuentra en determinado indice segun se clickee.
        :param tuple posicion_del_mouse: Representa la posicion de donde clickeo el jugador (tanto en el ejex como en el eje y).
        Retorna la figura de determinado indice
        """
        for j in range(16):
            if Totalcuadrados[j].collidepoint(posicion_del_mouse):
                return listafiguras.index(j+1)

    def dibujartablero():
        """"
        Esta funcion, dibuja los cuadrados que hacen nuestro tablero.
        :return None
        """
        ventana.fill((135,206,250)) #colocamos el color de fondo de nuestra pantalla
        for j in range(16): #iteramos entre los cuadrados ya diseñados, eligiendo parametros como el color y el grueso de sus lineas.
            pygame.draw.rect(ventana,(255,255,255),Totalcuadrados[j],10)

    def numerocuadrado(posicion_del_mouse):
        """
        Esta funcion, retorna el indice de determinado cuadrado segun se clickee.
        :param tuple posicion_del_mouse: Representa la posicion de donde clickeo el jugador (tanto en el ejex como en el eje y).
        Retorna el indice de terminada posicion
        """

        for j in range(16):
            if Totalcuadrados[j].collidepoint(posicion_del_mouse):
                return j+1

    def main():
        """"
        Funcion proncipal del juego.
        :return None
        """
        pygame.init()
        global ventana
        ventana= pygame.display.set_mode((1280,700))
        ventana.fill((135,206,250))
        pygame.display.set_caption('Encuentra las parejas')
        logo = pygame.image.load("../recursor/icono.ico")
        pygame.display.set_icon(logo)
        pygame.display.update()
        dibujartablero()
        iniciarjuego()
        titulo_principal=pygame.image.load("../recursor/Imagenes juegos/parejas_2.png")
        ventana.blit(titulo_principal, (405,0))
        pygame.display.update()
        pygame.time.wait(3000)
        dibujartablero()
        ventanaprincipal()
        pygame.display.update()
        prueba=0
        eleccioncorrecta=[]
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.MOUSEBUTTONUP:
                    posicion_del_mouse=pygame.mouse.get_pos()
                    mostrar(posicion_del_mouse)
                    pygame.display.update()
                    if prueba==0:
                        primeraeleccion=posicion_del_mouse
                        if numerocuadrado(primeraeleccion) in eleccioncorrecta:
                            prueba=0
                        else:
                            prueba=1
                    else:
                        segundaeleccion=posicion_del_mouse
                        if numerocuadrado(segundaeleccion) in eleccioncorrecta:
                            prueba=1
                        else:
                            prueba=0
                        if not (numerocuadrado(primeraeleccion) in eleccioncorrecta) and not numerocuadrado(segundaeleccion) in eleccioncorrecta:
                            if encontrarparejas(primeraeleccion,segundaeleccion):
                                eleccioncorrecta.append(numerocuadrado(primeraeleccion))
                                eleccioncorrecta.append(numerocuadrado(segundaeleccion))
                            else:
                                pygame.time.wait(1000)
                                esconderfichas(primeraeleccion)
                                esconderfichas(segundaeleccion)
                                pygame.display.update()

            if len(eleccioncorrecta)==16:
                ganador=pygame.image.load('../recursor/Imagenes juegos/Ganadorgg0000.png')
                ventana.blit(ganador,(420, 140))
                pygame.display.update()
                time.sleep(4)
                pygame.quit()
                break

    main()
