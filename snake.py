#pygame -> Pygame é um wrapper python para SDL , escrito por Pete Shinners.
#  O que isso significa é que, usando pygame, você pode escrever jogos 
# ou outros aplicativos multimídia em Python que serão executados
#  inalterados em qualquer uma das plataformas suportadas pelo SDL
# https://www.pygame.org/docs/tut/newbieguide.html

#sys -> Este módulo fornece acesso a algumas variáveis ​​usadas ou mantidas pelo 
# interpretador e a funções que interagem fortemente com o interpretador. 
# Está sempre disponível.
# https://docs.python.org/3/library/sys.html

#time -> Este módulo fornece várias funções relacionadas ao tempo.
# https://docs.python.org/3/library/time.html

#random - > Este módulo implementa geradores de números pseudo-aleatórios para 
# várias distribuições.
# Para inteiros, há seleção uniforme de um intervalo. Para sequências, há seleção
# uniforme de um elemento aleatório, uma função para gerar uma permutação aleatória
# de uma lista no local e uma função para amostragem aleatória sem reposição.

################################------------------------################################

import pygame, sys, time, random

speed = 15

#windows size

frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()

#Conditional

if(check_errors[1] > 0):
    print("Erro " + check_errors[1])
else:
    print("Sucesso ao inicializar o jogo ")

#Initialise game window

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode(frame_size_x,frame_size_y)

#colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red   = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue  = pygame.Color(0,0,255)





