import pygame
import numpy as np


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
        self.bowser = None
        self.flor = None
        self.estrella = None
        self.princesa = None
        self.mario = None
        self.salir = False
        self.grid = pasos[paso_actual] if len(pasos) > 0 else grid
        self.pasos = pasos
        self.paso_actual = paso_actual
        # Establecemos el LARGO y ALTO de cada celda de la retícula.
        self.largo = largo
        self.alto = alto
        # Establecemos el margen entre las celdas.
        self.margen = margen
        # Inicializamos pygame
        pygame.init()
        alto_m = len(self.grid)
        largo_m = len(self.grid[0])
        margen_total = ((self.margen * 10) + 5)
        # Establecemos el LARGO y ALTO de la pantalla
        dimension_ventana = [largo_m * margen_total, alto_m * margen_total]
        self.pantalla = pygame.display.set_mode(dimension_ventana)
        # Establecemos el título de la pantalla.
        pygame.display.set_caption("Proyecto 1 IA")
        self.inicializar_imagenes()
        # Lo usamos para establecer cuán rápido de refresca la pantalla.
        self.reloj = pygame.time.Clock()

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

    def set_pos_ant(self):
        pos_ant = list(map(lambda x: x[0], np.where(self.grid == 2)))
        self.grid[pos_ant[0]][pos_ant[1]] = 0
        print("Coordenadas de la retícula anterior: ", pos_ant)

    def loop_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.salir = True
            if evento.type == pygame.MOUSEBUTTONDOWN and len(self.pasos) > 0:
                if self.paso_actual + 1 >= len(self.pasos):
                    self.paso_actual = 0
                else:
                    self.paso_actual += 1

    def dibujar_imagen(self, imagen, columna, fila):
        self.pantalla.blit(
            imagen,
            [
                (self.margen + self.largo) * columna + self.margen,
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
                                 [(self.margen + self.largo) * columna + self.margen,
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

            # Establecemos el fondo de pantalla.
            self.pantalla.fill(self.NEGRO)

            self.draw_loop()

            # Limitamos a 60 fotogramas por segundo.
            self.reloj.tick(60)

            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()

        # Pórtate bien con el IDLE.
        pygame.quit()

    def show_window(self):
        self.main_loop()
