import time
import sys
import pygame
from random import randint
from tkinter import messagebox

def TRIQUI():
    """
    Esta funcion inicia el juego del triqui, con las funciones para iniciar el juego
    No recibe
    :return None
    """
    ###########SECCIÓN DE INICIALIZACION DE LA VENTANA.###################
    pygame.init()#Iniciamos pygame
    pygame.display.set_caption("Triqui") #Titulo de la ventana
    tamaño=(1280,700) #Tamaño de nuestra ventana
    ventana=pygame.display.set_mode((tamaño))#Colocamos el tamaño determinado
    logo = pygame.image.load("../recursor/icono.ico")
    pygame.display.set_icon(logo)
    equis=pygame.image.load("../recursor/Imagenes juegos/EQUIS.png")#Cargamos las imagenes y ajustamos sus tamaños
    equis= pygame.transform.scale(equis, (100, 100))
    circulo=pygame.image.load("../recursor/Imagenes juegos/CIRCULO.png")
    circulo= pygame.transform.scale(circulo, (100, 100))
    titulo0=pygame.image.load("../recursor/Imagenes juegos/Titulo0.png")
    titulo1=pygame.image.load("../recursor/Imagenes juegos/Titulo1.png")
    tituloPLAYTHON=pygame.image.load("../recursor/Imagenes juegos/TITULOPLAYTHON.png")
    victoriasp1=pygame.image.load("../recursor/Imagenes juegos/0.png")
    victoriaspc=pygame.image.load("../recursor/Imagenes juegos/1.png")
    derrotasp1=pygame.image.load("../recursor/Imagenes juegos/2.png")
    derrotaspc=pygame.image.load("../recursor/Imagenes juegos/3.png")
    tituloempate=pygame.image.load("../recursor/Imagenes juegos/4.png")
    pygame.display.set_caption("Triqui")#Ajustamos su tamaño
    PLAYTHON_IMG = pygame.image.load("../recursor/Imagenes juegos/playthontriqui.png")#Cargamos la imagen del logo

    color_azul=pygame.Color(135,206,250)#Definimos los colores usados
    color_blanco=pygame.Color(255,255,255)

    fuente_contenido=pygame.font.SysFont("comicsansms",30)#Definimos las fuentes usadas
    fuente_titulo=pygame.font.SysFont("comicsansms",42)

    seleccion_jugador1=fuente_titulo.render("X",1,color_blanco)
    seleccion_jugador2=fuente_contenido.render("ó",1,color_blanco)
    seleccion_jugador3=fuente_titulo.render("O",1,color_blanco)
    ######################################################################################

    def reiniciojuego():
        """
        Esta función, sirve para reiniciar el juego, una vez este llena la pizarra.
        No recibe
        :return None
        """
        global turnosiguiente, turno_actual, pizarra
        pizarra=["a","a","a","a","a","a","a","a","a"]
        turnosiguiente=0
        turno_actual=0

    def menuprincipal():
        """
        Esta funcion, genera nuestro menu principal, en el cual se elijen las fichas.
        Ademas de ello, en esta se encuentran diferentes textos, como el titulo principal, etc
        No recibe
        :return None
        """
        ventana.blit(titulo0,(340,15))
        ventana.blit(titulo1,(450,100))
        ventana.blit(seleccion_jugador1,(570,150))
        ventana.blit(seleccion_jugador2,(640,150))
        ventana.blit(seleccion_jugador3,(700,150))
        ventana.blit(tituloPLAYTHON,(380,430))
        ventana.blit(PLAYTHON_IMG, (500, 230))

    def comprobador_victoria(player):
        """
        Esta funcion, determina los posibles movimientos con los cuales se puede generar el triqui
        :param string player: Almacena el juegador que puede generar el triqui, ya sea el jugador o la PC
        No recibe
        Retorna un booleano
        """
        if comprobador_linea(player,3,6,0):
            return True
        if comprobador_linea(player,3,5,4):
            return True
        if comprobador_linea(player,8,0,4):
            return True
        if comprobador_linea(player,0,2,1):
            return True
        if comprobador_linea(player,8,2,5):
            return True
        if comprobador_linea(player,4,7,1):
            return True
        if comprobador_linea(player,7,8,6):
            return True
        if comprobador_linea(player,2,4,6):
            return True


    def revisarposicion(escala,valorenequis,valorenye):
        """
        Esta funcion, coloca las fichas segun donde se clickee.
        :param string escala: Determina si se encuentra en el menu o en el juego
        :param int valorenequis: Determina presionado en el eje x
        :param int valorenye: Determina presionado en el eje y
        Retorna la posicion
        """
        posicion=0
        if valorenequis>=580 and valorenequis<=740 and valorenye >= 395 and valorenye <= 535 and escala == "juego":
            posicion = 7
            return posicion
        elif valorenequis>=430 and valorenequis<=580 and valorenye >= 395 and valorenye <= 535 and escala == "juego":
            posicion = 6
            return posicion
        elif valorenequis>=740 and valorenequis<=900 and valorenye >= 395 and valorenye <= 535 and escala == "juego":
            posicion = 8
            return posicion
        elif valorenequis>=740 and valorenequis<=900 and valorenye >= 245 and valorenye <= 385 and escala == "juego":
            posicion = 5
            return posicion
        elif valorenequis>=430 and valorenequis<=580 and valorenye >= 245 and valorenye <= 385 and escala == "juego":
            posicion = 3
            return posicion
        elif valorenequis>=580 and valorenequis<=740 and valorenye >= 245 and valorenye <= 385 and escala == "juego":
            posicion = 4
            return posicion
        elif valorenequis>=570 and valorenequis<=620 and valorenye>=150 and valorenye<=200 and escala=="menu":
            posicion = 9
            return posicion
        elif valorenequis >= 430 and valorenequis <= 580 and valorenye >= 90 and valorenye <= 235 and escala == "juego":
            return posicion
        elif valorenequis >= 740 and valorenequis <= 900 and valorenye >= 90 and valorenye <= 235 and escala == "juego":
            posicion = 2
            return posicion
        elif valorenequis >= 580 and valorenequis <= 740 and valorenye >= 90 and valorenye <= 235 and escala == "juego":
            posicion = 1
            return posicion
        elif valorenequis>=700 and valorenequis<=750 and valorenye>=150 and valorenye<=200 and escala=="menu":
            posicion = 10
            return posicion
        else:
            posicion = 11
            return posicion

    def espaciovacio(posicion):
        """
        Esta funcion, determina si un lugar se encunetra vacio, en base a la posicion
        :param int posicion: Se refiere a la posicion clickeada.
        Retorna un booleano
        """
        if not posicion==9:
            if pizarra[posicion]=="X" or pizarra[posicion]=="O":
                return True

    def movimiento_computador():
        """
        Esta funcion, genera la seleccion de movimiento del computador
        No recibe
        :return None
        """
        global turno_actual,turnosiguiente
        time.sleep(0.19)
        seleccion=randint(0,8)
        if not espaciovacio(seleccion):
            turnosiguiente+=1
            turno_actual=0
            pizarra[seleccion]=computador
        else:
            movimiento_computador()

    def crearcuadrados():
        """
        Esta funcion, genera los cuadrados de nuestro triqui
        No recibe
        :return None
        """
        longitudx,ancho,longitudy,alto =420,151,90,151
        contador=0
        for i in range(9):
            pygame.draw.rect(ventana,color_blanco,(longitudx,longitudy,ancho,alto),1)
            contador+=1
            longitudx+=151
            if contador==3:
                longitudy+=151
                longitudx=420
            if contador==6:
                longitudy+=151
                longitudx=420

    def dibujar_fichas():
        """
        Esta funcion, dibuja las fichas, segun se clickee en el tablero
        No recibe
        :return None
        """
        valor0,valor1,valor2=0,1,2
        if pizarra[2] == "O":
            ventana.blit(circulo, (Xlugar[valor2], Ylugar[valor0]))
        elif pizarra[2] == "X":
            ventana.blit(equis, (Xlugar[valor2], Ylugar[valor0]))
        if pizarra[7] == "O":
            ventana.blit(circulo, (Xlugar[valor1], Ylugar[valor2]))
        elif pizarra[7] == "X":
            ventana.blit(equis, (Xlugar[valor1], Ylugar[valor2]))
        if pizarra[1]=="O":
            ventana.blit(circulo,(Xlugar[valor1],Ylugar[valor0]))
        elif pizarra[1]=="X":
            ventana.blit(equis,(Xlugar[valor1], Ylugar[valor0]))
        if pizarra[6]=="O":
            ventana.blit(circulo,(Xlugar[valor0],Ylugar[valor2]))
        elif pizarra[6]=="X":
            ventana.blit(equis,(Xlugar[valor0], Ylugar[valor2]))
        if pizarra[0]=="O":
            ventana.blit(circulo,(Xlugar[valor0],Ylugar[valor0]))
        elif pizarra[0]=="X":
            ventana.blit(equis,(Xlugar[valor0], Ylugar[valor0]))
        if pizarra[5]=="O":
            ventana.blit(circulo,(Xlugar[valor2],Ylugar[valor1]))
        elif pizarra[5]=="X":
            ventana.blit(equis,(Xlugar[valor2], Ylugar[valor1]))
        if pizarra[3]=="O":
            ventana.blit(circulo,(Xlugar[valor0],Ylugar[valor1]))
        elif pizarra[3]=="X":
            ventana.blit(equis,(Xlugar[valor0], Ylugar[valor1]))
        if pizarra[8]=="O":
            ventana.blit(circulo,(Xlugar[valor2],Ylugar[valor2]))
        elif pizarra[8]=="X":
            ventana.blit(equis,(Xlugar[valor2], Ylugar[valor2]))
        if pizarra[4]=="O":
            ventana.blit(circulo,(Xlugar[valor1],Ylugar[valor1]))
        elif pizarra[4]=="X":
            ventana.blit(equis,(Xlugar[valor1], Ylugar[valor1]))

    def dibujar_puntajes(jugadorvic,jugadorderr,compvic,compderr,empate):
        """
        Esta funcion, dibuja cada uno de los puntajes en la pantalla del juego
        :param string jugadorvic: Se refiere a las victorias del jugador
        :param string jugadorderr: Se refiere a las derrotas del juegador
        :param string compvic: Se refiere a las victorias del PC.
        :param string compderr: Se refiere a las derrotas del PC.
        :param string empate: Se refiere a los empates
        :return None
        """
        jugadorvic=fuente_contenido.render(str(jugadorvic),1,color_blanco)
        jugadorderr = fuente_contenido.render(str(jugadorderr), 1, color_blanco)
        empate=fuente_contenido.render(str(empate),1,color_blanco)
        compvic=fuente_contenido.render(str(compvic),1,color_blanco)
        compderr = fuente_contenido.render(str(compderr), 1, color_blanco)
        ventana.blit(victoriasp1, (65, 120))
        ventana.blit(jugadorvic, (180, 215))
        ventana.blit(derrotasp1, (65, 335))
        ventana.blit(jugadorderr, (180, 430))
        ventana.blit(tituloempate, (510, 520))
        ventana.blit(empate, (650,615))
        ventana.blit(victoriaspc, (950, 120))
        ventana.blit(compvic, (1080, 215))
        ventana.blit(derrotaspc, (950, 335))
        ventana.blit(compderr, (1080, 430))

    def comprobador_linea(jugador00,lugar1,lugar2,lugar3):
        """
        Esta funcion, determina si hay una linea con tres en linea, ya sea diagonal, en la fila o en una columna
        :param string jugador00: Se refiere al jugador que este segun las fichas, ya sea el jugador o el PC
        :param int lugar1: Se refiere a la primera posicion que buscamos determinar
        :param int lugar2: Se refiere a la segunda posicion que buscamos determinar.
        :param int lugar3: Se refiere a la tercera posicion que buscamos determinar.
        :Retorna un booleano
        """
        if pizarra[lugar3]==jugador00 and pizarra[lugar1]==jugador00 and pizarra[lugar2]==jugador00:
            return True


    def main():
        """
        Funcion principal del programa
        :return None
        """
        global empate,movimiento,turno_actual,turnosiguiente,pizarra,Xlugar,Ylugar,computador
        #########################################INICIO Y LLAMADA DE LAS FUNCIONES EN EL JUEGO#######################
        quitar_ventana = pygame.QUIT
        mouse = pygame.MOUSEBUTTONUP
        Xlugar, Ylugar = [445, 595, 745], [110, 265, 415]
        puntajeJugador, puntajeComputador, empate = [0, 0], [0, 0], 0
        pizarra = ["a", "a", "a", "a", "a", "a", "a", "a", "a"]
        turno_actual, turnosiguiente, valor0, valor1 = 0, 0, 0, 1
        ciclo_menu, ciclo_juego = True, False
        Estado_juego = 1
        jugador, computador = "", ""
        while ciclo_menu:
            for movimiento in pygame.event.get():
                if mouse == movimiento.type:
                    posicion_mouse = pygame.mouse.get_pos()
                    lugar1 = revisarposicion("menu", posicion_mouse[0], posicion_mouse[1])
                    if lugar1 == 10 or lugar1 == 9:
                        if lugar1 == 10:
                            jugador = "O"
                            computador = "X"
                            ciclo_juego = True
                            ciclo_menu = False
                        else:
                            jugador = "X"
                            computador = "O"
                            ciclo_juego = True
                            ciclo_menu = False
            ventana.fill(color_azul)
            menuprincipal()
            pygame.display.flip()
            if quitar_ventana == movimiento.type:
                pygame.quit()
                sys.exit()
        while ciclo_juego:
            if comprobador_victoria("O"):
                time.sleep(0.6)
                if jugador=="O":
                    puntajeComputador[valor1]+=1
                    puntajeJugador[valor0]+=1
                    if puntajeJugador[valor0]==4:
                        ganador = pygame.image.load('../recursor/Imagenes juegos/Winnertriqui.png')
                        ventana.blit(ganador, (420,90))
                        pygame.display.update()
                        time.sleep(2)
                        pygame.quit()
                        break
                    reiniciojuego()
                else:
                    puntajeComputador[valor0]+=1
                    puntajeJugador[valor1]+=1
                    reiniciojuego()
            elif comprobador_victoria("X"):
                time.sleep(0.6)
                if jugador=="X":
                    puntajeComputador[valor1]+=1
                    puntajeJugador[valor0]+=1
                    if puntajeJugador[valor0]==4:
                        ganador = pygame.image.load('../recursor/Imagenes juegos/Ganadorgg0000.png')
                        ventana.blit(ganador, (420, 90))
                        pygame.display.update()
                        time.sleep(2)
                        pygame.quit()
                        break
                    reiniciojuego()
                else:
                    puntajeComputador[valor0]+=1
                    puntajeJugador[valor1]+=1
                    reiniciojuego()
            if turnosiguiente>8:
                time.sleep(0.6)
                empate+=1
                reiniciojuego()
            if turno_actual==1:
                movimiento_computador()
            for movimiento in pygame.event.get():
                if mouse ==movimiento.type:
                    if turno_actual==0:
                        posicion_mouse=pygame.mouse.get_pos()
                        lugar1=revisarposicion("juego",(posicion_mouse[valor0]),(posicion_mouse[valor1]))
                        try:
                            if lugar1<9 and not espaciovacio(lugar1):
                                pizarra[lugar1]=jugador
                                turnosiguiente+=1
                                turno_actual=1

                        except IndexError:
                            messagebox.showwarning('PRECAUCIÓN',"Selecciona una casilla adecuada.")

            ventana.fill(color_azul)
            ventana.blit(titulo0,(340,10))
            dibujar_puntajes(puntajeJugador[valor0], puntajeJugador[valor1], puntajeComputador[valor0], puntajeComputador[valor1], empate)
            crearcuadrados()
            dibujar_fichas()
            pygame.display.flip()
            if movimiento.type ==quitar_ventana:
                pygame.quit()
                sys.exit()
    main()
