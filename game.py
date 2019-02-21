import pygame
from pantalla import *

class ScreenManager:
    instancia = None
    
    @classmethod
    def get_instance(cls): # Metodo de clase
        if cls.instancia == None:
            cls.instancia = ScreenManager()
        return cls.instancia
    
    def reproducir_sonido(self, musica) #musica es el archivo del background 2
        pygame.mixer.music.stop()
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play(-1)   

    def __init__(self):
        pygame.init()
        #img_background = "Background"
        #self._pantalla_actual = EjemploPantalla(canvas)
        self.clock = pygame.time.Clock()
        #backdrop = pygame.image.load("images/fondos/" + img_background + ".png").convert()
        #backdropbox = canvas.get_rect()
        self.pantalla = []
        self.indice_actual = -1
        
        

    def cambiar_pantalla(self,nueva_pantalla):
        #condicion de prueba
        self.condicion = 0
        self.aux = True
        self.pantalla.append(nueva_pantalla)
        self.indice_actual += 1
        self._pantalla_actual = self.pantalla[self.indice_actual]

    def condicion_pantalla(self):

        #CONDICION DE PRUEBA
        if self.condicion < 100:
            self.aux = True
        else:
            self.aux = False

    def run(self):
        
        background1 = "foo.mp3" #insertar archivo de primer background
        pygame.mixer.music.load(background1)
        pygame.mixer.music.play(-1)

        while self.aux == True:
            self._pantalla_actual.handle_events()
            self._pantalla_actual.update()
            self._pantalla_actual.render()
            self.clock.tick(60)
            self.condicion_pantalla()
            self.condicion += 1

def main():
    manager = ScreenManager.get_instance()
    
    pantalla1 = Pantalla1()     
    manager.cambiar_pantalla(pantalla1)
    manager.run()
    
    pantalla2 = Pantalla2()
    manager.cambiar_pantalla(pantalla2)
    manager.run()
    

if __name__ == "__main__":
    main()