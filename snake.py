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

fps_controller = pygame.time.Clock()

# Cobra tamanho quadrado
square_size = 20

def init_vars():
    global head_pos, snake_body, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size)) * square_size]
    food_spawn = True
    score = 0

init_vars()

def show_score():
    print("showing score")

#game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if( event.key == pygame.K_UP or event.key == ord("w")
                and direction != "DOWN" ):
                direction = "UP"
            elif( event.key == pygame.K_UP or event.key == ord("s")
                and direction != "UP" ):
                direction = "DOWN"
            elif( event.key == pygame.K_UP or event.key == ord("a")
                and direction != "RIGHT" ):
                direction = "LEFT"
            elif( event.key == pygame.K_UP or event.key == ord("d")
                and direction != "LEFT" ):
                direction = "RIGHT"
    
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

#eating apple

    snake_body.insert(0,list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

#spawn food
    if not food_spawn:
      food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
            random.randrange(1,(frame_size_y // square_size)) * square_size]   

