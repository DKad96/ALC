from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
#import numpy
import random


class Server():
    '''
    Criptografía Asimétrica
        fuente n°1 = https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
        fuente n°2 = https://cryptography.io/en/latest/hazmat/primitives/asymmetric/utils/?highlight=hazmat
    
    
    Criptografía Simétrica
        fuente n°3 = https://cryptography.io/en/latest/fernet/
    '''
    
    def __init__(self):
        self.players = []
        self.ip_players = []
        self.symmetric_keys=[]
        self.llave_publica = None
        self.llave_privada = None
        


    def generar_par_de_claves(self):
        '''
        Ver cómo funciona IKEv2, o sea el órden
        '''
        #El cliente usará la clave pública para enviar la tupla (user, password)
        #Código obtenido de fuente n°1        
        self.llave_privada = rsa.generate_private_key( public_exponent=65537, 
                             key_size=2048, backend=default_backend())
        self.llave_publica = self.llave_privada.public_key()
          

    def generar_llaves_simetricas(self):
        pass
    
    
    def validar_usuario(self, usuario='', psw=''):
        #hacer la consulta correspondiente con la base de datos
        #En este punto los datos YA ESTÁN desencriptados
        pass

    def nuevo_psw(self, usuario='', psw=''):
        #Establecer un nuevo password para el usuario
        #En este punto los datos YA ESTÁN desencriptados
        pass


    def add_player(self, player):
        self.players.append(player)
    

    def elegir_escenario(self, esc=[]):
        if random.random() < 0.5:
            return esc[0]
        else:
            return esc[1]

       
    def enviar_mensaje_encriptado(self, destino, mensaje = ''):
        pass


    def desencriptar_mensaje(self, remitente, mensaje = ''):
        pass
    

def main():
    server = Server()
    
    server.generar_par_de_claves()
    server.generar_llaves_simetricas()
        
    
    #Otras acciones con la base de datos
    #Nuevo usuario/olvide psw
    
    
    #Corroborar autenticidad del usuario


    #Enviar clave simétrica
        
    
    #Enviar si será héroe o corrputo


    #Esperar ambas respuestas de personaje, escenario


    #Elegir un escenario aleatoriamente 


    #Informar a los jugadores del escenario


    #empezar la partida
    



if __name__ == '__main__':
    main()