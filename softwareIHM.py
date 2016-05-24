__author__ = "Jackson Willian Goulart"
import RPi.GPIO as GPIO                    #Importa GPIO   biblioteca
import time                                #Importa time   biblioteca
import pygame                              #Importa pygame biblioteca
from threading import  Thread
GPIO.setmode(GPIO.BCM)                     #Seta GPIO pin numero

TRIG1 = 23                                  #Associa pino 23 ao TRIG
ECHO1 = 24                                  #Associa pino 24 ao ECHO

TRIG2 = 21
ECHO2 = 22


GPIO.setup(TRIG1,GPIO.OUT)                  #Seta pino como GPIO out saida
GPIO.setup(ECHO1,GPIO.IN)                   #Seta pino como GPIO in  entrada


GPIO.setup(TRIG2,GPIO.OUT)                  #Seta pino como GPIO out saida
GPIO.setup(ECHO2,GPIO.IN)                   #Seta pino como GPIO in  entrada


print "Inicializando ..."

#Funcao para carregar audio e executar
def playing(p1,p2,p3):
        pygame.init()
        a = pygame.mixer.Sound('beep.wav')
        if p1 is True:
                channel = a.play()
                channel.set_volume(1, 0)
                time.sleep(1)
        if p2 is True:
                channel = a.play()
                channel.set_volume(0, 1)
                time.sleep(1)
        if p3 is True:
                channel = a.play()
                channel.set_volume(1,1)
                time.sleep(1)

#funcao para tratamento da leitura dos sensores
def tratamento(TRIG, ECHO):

        global distance
        GPIO.output(TRIG, False)
        print "esperando pelo sensor"
        time.sleep(1)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

#funcao que execulta o sensor chamando a funcao de tratamento
# da leitura do sensores e a playing que trata o audio
def sensor1():
        tratamento(TRIG1,ECHO1)
        if distance > 2 and distance < 400:
               # messagem para ferificacao do funcionamento  para testes em desenvolvimento
               print "Distance:",distance - 0.5,"cm"

        #verificacao da distancia
        if distance <  50:
                        playing(True,False, False)
                        time.sleep(0.50)
                        playing(False,True)

        else:
           print " Fora de alcance"


def sensor2():
        tratamento(TRIG2,ECHO2)

        if distance > 2 and distance < 400:

               print "Distance:",distance - 0.5,"cm"


        if distance <  50:
                       playing(False,True,False)

        else:
           print " Fora de alcance"


if __name__ == '__main__':
              Thread(target=sensor1()).start()
              Thread(target=sensor2()).start()



