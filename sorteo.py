import random
from pygame import mixer
puntuacion=0
vidas=3

while(vidas!=0):
    coleccion=int (random.randint(1,100))
    valor=int(input('Introduce un valor entre 1 y 100: '))
    if valor>100 or valor<0:
        print('Introduzca un valor en el rango establecido por favor')
    else:    
        if valor==coleccion:
            puntuacion+=1
            print('¡Increible has acertado!, tienes: ',puntuacion,' pts')
            mixer.init()
            mixer.music.load('victoria.mp3')
            mixer.music.play()
        
        else: 
            vidas-=1
            print('Has fallado vuelve a intentarlo te quedan: ', vidas ,' vidas y tienes: ',puntuacion,' pts')    

print('Lo siento has perdido T_T, obtuviste una puntuacion de: ',puntuacion,' pts')