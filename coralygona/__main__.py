from escape_the_rato import escapeTheRato,scale,load,TELA,TAMANHO
from pygame.mixer import Sound
from pygame import QUIT, quit, display , event, KEYDOWN

APRESENTACAO_ESCAPETHERATO = scale(load("assets/escape-the-rato.png"),TAMANHO)
NAO_FOI_DESSA_VEZ = Sound("assets/nao_foi_dessavez.mp3")
DOLL_MUSIC =  Sound("assets/doll.mp3")

while True:
    for evento in event.get():
        if evento.type == QUIT:
            quit()
            break
        elif evento.type == KEYDOWN:
            if evento.key == 13:
                NAO_FOI_DESSA_VEZ.stop()
                if escapeTheRato() == "Morreu":
                    NAO_FOI_DESSA_VEZ.play()
                    
                else:
                    DOLL_MUSIC.play()

    TELA.blit(APRESENTACAO_ESCAPETHERATO,(0,0))
    display.update()

#escapeTheRato()