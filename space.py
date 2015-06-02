import pygame
import os, sys
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)


def player():
    os.system('omxplayer -o local Pioneering.mp4')
    
def picture(img,w,h):
    pic = pygame.image.load(img)
    background = (255, 64, 64)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    screen.blit(pic,(0,0))
    pygame.display.flip()
    sleep(10)
    pygame.display.quit()
    pygame.quit()

def picture_with_audio(img,w,h,audio):
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(1)
    screen = pygame.display.set_mode((w,h))
    pic = pygame.image.load(img).convert()
    background = (0, 0, 0)
    screen.fill((background))
    myfont = pygame.font.Font(None, 15)
    info1 = myfont.render("The International Space Station (ISS) is a space station,",1,(0,255,0))
    info2 = myfont.render("or a habitable artificial satellite, in low Earth orbit.",1,(0,255,0))
    info3 = myfont.render("Its first component launched into orbit in 1998,",1,(0,255,0))
    info4 = myfont.render("the ISS is now the largest artificial body in orbit and can often be ",1,(0,255,0))
    info5 = myfont.render("seen with the naked eye from Earth.",1,(0,255,0))
    info6 = myfont.render("Source: Wikipedia.org",1,(0,0,255))
    screen.blit(info1, (0,0))
    screen.blit(info2, (0,20))
    screen.blit(info3, (0,40))
    screen.blit(info4, (0,60))
    screen.blit(info5, (0,80))
    screen.blit(info6, (0,100))
    pygame.display.flip()
    sleep(10)
    screen.blit(pic,(0,0))
    pygame.display.flip()
    sleep(5)
    pygame.display.quit()
    pygame.mixer.music.stop()

while True: 
    #choices = ["Pioneering Space","ISS","Mars","Exit"]
    #selection = 'Blank'
    #selection = eg.buttonbox(title="Movie Player", msg="Choose a movie",choices=(choices))
    if GPIO.input(14) == False:
        player()
    elif GPIO.input(15) == False:
        print("ISS Chosen")
        picture_with_audio('./iss.jpg',640,421,'./eva.mp3')
    elif GPIO.input(18) == False:
        picture('./mars.jpg', 1280,720)
    #elif selection == 'Exit':
        #break
pygame.quit()
