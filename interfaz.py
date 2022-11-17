import pygame
import numpy as np
from busqueda import Busqueda
import time


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def updatecursor(self):
        (self.left, self.top) = pygame.mouse.get_pos()


class Button(pygame.sprite.Sprite):

    def __init__(self, image1, image2, x=0, y=10):
        self.imagen_normal = image1
        self.imagen_seleccion = image2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

    def update(self, pantalla, cursor, show):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        if show:
            self.rect.left, self.rect.top = (self.x, self.y)
            pantalla.blit(self.imagen_actual, self.rect)
        else:
            self.rect.left, self.rect.top = (-100, -100)


class Interfaz:
    # Definimos algunos colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    ROJO = (255, 0, 0)
    AMARILLO = (231, 242, 0)
    CAFE = (172, 76, 13)
    ROSADO = (249, 128, 186)

    def __init__(self, grid=[], pasos=[], paso_actual=0, largo=50, alto=50, margen=5):
        # Inicializamos pygame
        pygame.init()
        # variables
        self.salir = False
        self.grid = pasos[paso_actual] if len(pasos) > 0 else grid
        self.grid_inicial = self.grid
        self.pasos = pasos
        self.paso_actual = paso_actual
        # Establecemos el LARGO y ALTO de cada celda de la retícula.
        self.largo = largo
        self.alto = alto
        # Establecemos el margen entre las celdas.
        self.margen = margen
        alto_m = len(self.grid)
        largo_m = len(self.grid[0])
        margen_total = ((self.margen * 10) + 5)
        # Establecemos el LARGO y ALTO de la pantalla
        flags = pygame.RESIZABLE | pygame.SCALED
        self.dimension_ventana = [
            400 + (largo_m * margen_total), 200 + (alto_m * margen_total)]
        self.pantalla = pygame.display.set_mode(self.dimension_ventana, flags)
        # Establecemos el título de la pantalla.
        pygame.display.set_caption("Proyecto 1 IA")
        # Lo usamos para establecer cuán rápido de refresca la pantalla.
        self.reloj = pygame.time.Clock()
        # Se usa para saber que botones se muestran
        self.estado_interfaz = 0
        # Texto informes
        self.fuente = pygame.font.SysFont("Gabriola", 27)
        self.textos = ["Tiempo de cómputo: ",
                       "Profundidad del árbol: ", "Nodos expandidos: "]
        self.resultados = ["", "", ""]
        # Inicializamos imagenes
        self.bowser = None
        self.flor = None
        self.estrella = None
        self.princesa = None
        self.mario = None
        self.img_busq_no_inf = None
        self.img_busq_no_inf_2 = None
        self.img_busq_inf = None
        self.img_busq_inf_2 = None
        self.img_amplitud = None
        self.img_amplitud_2 = None
        self.img_costo_u = None
        self.img_costo_u_2 = None
        self.img_profundidad = None
        self.img_profundidad_2 = None
        self.img_avara = None
        self.img_avara_2 = None
        self.img_a_est = None
        self.img_a_est_2 = None
        self.img_atras = None
        self.img_atras_2 = None
        self.inicializar_imagenes()
        # cursor
        self.cursor = Cursor()
        # Botones
        self.atras = None
        self.busqueda_no_inf = None
        self.busqueda_inf = None
        self.amplitud = None
        self.costo = None
        self.profundidad = None
        self.avara = None
        self.a_estrella = None
        self.inicializar_botones()
        self.busqueda = Busqueda(self.grid_inicial)
        self.mostrar = False

    def inicializar_imagenes(self):
        self.mario = pygame.image.load("img/mario.png").convert()
        self.mario.set_colorkey(self.NEGRO)
        self.princesa = pygame.image.load("img/princesa.png").convert()
        self.princesa.set_colorkey(self.NEGRO)
        self.estrella = pygame.image.load("img/estrella.png").convert()
        self.estrella.set_colorkey(self.NEGRO)
        self.flor = pygame.image.load("img/flor.png").convert()
        self.flor.set_colorkey(self.NEGRO)
        self.bowser = pygame.image.load("img/bowser.png").convert()
        self.bowser.set_colorkey(self.NEGRO)
        self.img_busq_no_inf = pygame.image.load("img/boton1.png").convert()
        self.img_busq_no_inf.set_colorkey(self.NEGRO)
        self.img_busq_no_inf_2 = pygame.image.load(
            "img/boton1_2.png").convert()
        self.img_busq_no_inf_2.set_colorkey(self.NEGRO)
        self.img_busq_inf = pygame.image.load("img/boton2.png").convert()
        self.img_busq_inf.set_colorkey(self.NEGRO)
        self.img_busq_inf_2 = pygame.image.load("img/boton2_2.png").convert()
        self.img_busq_inf_2.set_colorkey(self.NEGRO)
        self.img_amplitud = pygame.image.load("img/boton3.png").convert()
        self.img_amplitud.set_colorkey(self.NEGRO)
        self.img_amplitud_2 = pygame.image.load("img/boton3_2.png").convert()
        self.img_amplitud_2.set_colorkey(self.NEGRO)
        self.img_costo_u = pygame.image.load("img/boton4.png").convert()
        self.img_costo_u.set_colorkey(self.NEGRO)
        self.img_costo_u_2 = pygame.image.load("img/boton4_2.png").convert()
        self.img_costo_u_2.set_colorkey(self.NEGRO)
        self.img_profundidad = pygame.image.load("img/boton5.png").convert()
        self.img_profundidad.set_colorkey(self.NEGRO)
        self.img_profundidad_2 = pygame.image.load(
            "img/boton5_2.png").convert()
        self.img_profundidad_2.set_colorkey(self.NEGRO)
        self.img_avara = pygame.image.load("img/boton6.png").convert()
        self.img_avara.set_colorkey(self.NEGRO)
        self.img_avara_2 = pygame.image.load("img/boton6_2.png").convert()
        self.img_avara_2.set_colorkey(self.NEGRO)
        self.img_a_est = pygame.image.load("img/boton7.png").convert()
        self.img_a_est.set_colorkey(self.NEGRO)
        self.img_a_est_2 = pygame.image.load("img/boton7_2.png").convert()
        self.img_a_est_2.set_colorkey(self.NEGRO)
        self.img_atras = pygame.image.load("img/boton8.png").convert()
        self.img_atras.set_colorkey(self.NEGRO)
        self.img_atras_2 = pygame.image.load("img/boton8_2.png").convert()
        self.img_atras_2.set_colorkey(self.NEGRO)

    def inicializar_botones(self):
        # Botones
        self.atras = Button(self.img_atras, self.img_atras_2,
                            self.dimension_ventana[0] - 200, (self.dimension_ventana[1]/2) - 50)
        pos_y_img = (self.margen * 10) * ((len(self.grid) / 2) - 1)
        self.busqueda_no_inf = Button(
            self.img_busq_no_inf, self.img_busq_no_inf_2, 0, pos_y_img)
        self.busqueda_inf = Button(
            self.img_busq_inf, self.img_busq_inf_2, 0, pos_y_img + 80)
        # --------------------------------------------
        self.avara = Button(self.img_avara, self.img_avara_2, 0, pos_y_img)
        self.a_estrella = Button(
            self.img_a_est, self.img_a_est_2, 0, pos_y_img + 80)
        # --------------------------------------------
        pos_y_img = (self.margen * 10) * (len(self.grid) / 3)
        self.amplitud = Button(
            self.img_amplitud, self.img_amplitud_2, 0, pos_y_img)
        self.costo = Button(
            self.img_costo_u, self.img_costo_u_2, 0, pos_y_img + 80)
        self.profundidad = Button(
            self.img_profundidad, self.img_profundidad_2, 0, pos_y_img + 160)

    def set_pos_ant(self):
        pos_ant = list(map(lambda x: x[0], np.where(self.grid == 2)))
        self.grid[pos_ant[0]][pos_ant[1]] = 0

    def update_pos_pasos(self, paso):
        op = self.paso_actual + paso
        if op >= len(self.pasos):
            self.paso_actual = 0
            self.mostrar = False
        elif op < 0:
            self.paso_actual = len(self.pasos) - 1
        else:
            self.paso_actual = op

    def post_search(self, info, tiempo):
        self.pasos = info['pasos']
        self.busqueda.reset_result()
        self.pasos.reverse()
        self.mostrar = True

        self.grid = self.pasos[0]
        self.resultados[0] = f"{round(tiempo, 3)}Seg"
        self.resultados[1] = info['profundidad']
        self.resultados[2] = info['cant_nodos_expandidos']

    def loop_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.salir = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if self.cursor.colliderect(self.atras):
                        self.estado_interfaz = 0
                        self.pasos = []
                        self.grid = self.grid_inicial
                        self.resultados = ["", "", ""]
                        self.busqueda.reset_result()
                    if self.cursor.colliderect(self.busqueda_no_inf):
                        self.estado_interfaz = 1
                    if self.cursor.colliderect(self.busqueda_inf):
                        self.estado_interfaz = 2
                    if self.cursor.colliderect(self.amplitud):
                        self.paso_actual = 0
                        inicio = time.time()
                        info = self.busqueda.bfs()
                        fin = time.time()
                        self.post_search(info, fin - inicio)

                    if self.cursor.colliderect(self.costo):
                        self.paso_actual = 0
                        inicio = time.time()
                        info = self.busqueda.ucs()
                        fin = time.time()
                        self.post_search(info, fin - inicio)

                    if self.cursor.colliderect(self.profundidad):
                        self.paso_actual = 0
                        inicio = time.time()
                        info = self.busqueda.dfs()
                        fin = time.time()
                        self.post_search(info, fin - inicio)

                    if self.cursor.colliderect(self.avara):
                        self.paso_actual = 0
                        inicio = time.time()
                        info = self.busqueda.avara()
                        fin = time.time()
                        self.post_search(info, fin - inicio)

                    if self.cursor.colliderect(self.a_estrella):
                        self.paso_actual = 0
                        inicio = time.time()
                        info = self.busqueda.a_estrella()
                        fin = time.time()
                        self.post_search(info, fin - inicio)


            if evento.type == pygame.KEYDOWN:
                if len(self.pasos) > 0:
                    if evento.key == pygame.K_RIGHT:
                        self.update_pos_pasos(1)
                    if evento.key == pygame.K_LEFT:
                        self.update_pos_pasos(-1)

    def dibujar_imagen(self, imagen, columna, fila):
        self.pantalla.blit(
            imagen,
            [
                (self.margen + self.largo) * columna + self.margen + 200,
                (self.margen + self.alto) * fila + self.margen
            ]
        )

    def set_grid(self):
        if len(self.pasos) > 0:
            if self.paso_actual == 0:
                self.grid = self.pasos[0]
            else:
                self.grid = self.pasos[self.paso_actual]

    def draw_loop(self):
        # Dibujamos la retícula
        self.set_grid()
        for fila in range(len(self.grid)):
            for columna in range(len(self.grid[0])):
                color = self.BLANCO
                if self.grid[fila][columna] == 1:
                    color = self.CAFE

                pygame.draw.rect(self.pantalla,
                                 color,
                                 [(self.margen + self.largo) * columna + self.margen + 200,
                                  (self.margen + self.alto) *
                                  fila + self.margen,
                                  self.largo,
                                  self.alto])

                # pintar imagenes
                if self.grid[fila][columna] == 2:
                    self.dibujar_imagen(self.mario, columna, fila)
                if self.grid[fila][columna] == 3:
                    self.dibujar_imagen(self.estrella, columna, fila)
                if self.grid[fila][columna] == 4:
                    self.dibujar_imagen(self.flor, columna, fila)
                if self.grid[fila][columna] == 5:
                    self.dibujar_imagen(self.bowser, columna, fila)
                if self.grid[fila][columna] == 6:
                    self.dibujar_imagen(self.princesa, columna, fila)

    def main_loop(self):
        # -------- Bucle Principal del Programa-----------
        while not self.salir:
            self.loop_events()

            if self.mostrar:
                self.update_pos_pasos(1)
                self.reloj.tick(4)
            else:
                # Limitamos a 60 fotogramas por segundo.
                self.reloj.tick(60)

            # Establecemos el fondo de pantalla.
            self.pantalla.fill(self.NEGRO)

            self.draw_loop()

            # actualizar rectangulo de cursor
            self.cursor.updatecursor()
            self.busqueda_no_inf.update(
                self.pantalla, self.cursor, self.estado_interfaz == 0)
            self.busqueda_inf.update(
                self.pantalla, self.cursor, self.estado_interfaz == 0)
            self.atras.update(self.pantalla, self.cursor,
                              self.estado_interfaz != 0)
            self.amplitud.update(self.pantalla, self.cursor,
                                 self.estado_interfaz == 1)
            self.costo.update(self.pantalla, self.cursor,
                              self.estado_interfaz == 1)
            self.profundidad.update(
                self.pantalla, self.cursor, self.estado_interfaz == 1)
            self.avara.update(self.pantalla, self.cursor,
                              self.estado_interfaz == 2)
            self.a_estrella.update(
                self.pantalla, self.cursor, self.estado_interfaz == 2)
            pos_x = 0
            for index, texto in enumerate(self.textos):
                if index == 1:
                    pos_x = (self.dimension_ventana[0] / 2) - 90
                if index == 2:
                    pos_x = self.dimension_ventana[0] - 200

                self.pantalla.blit(
                    self.fuente.render(
                        texto + str(self.resultados[index]), 0, self.BLANCO),
                    (pos_x, self.dimension_ventana[1] - 50)
                )

            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()

        # Pórtate bien con el IDLE.
        pygame.quit()

    def show_window(self):
        self.main_loop()


grid = np.loadtxt('entorno.txt', dtype=int)
Interfaz(grid=grid).show_window()
