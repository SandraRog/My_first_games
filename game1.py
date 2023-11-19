import pygame

pygame.init()
window = pygame.display.set_mode((800,600))

#tworzymy gracza=obszar
x = 70
y = 50
player = pygame.rect.Rect(x,y,100,100) #położenie na siatce pikseli (x,y), wielkosc

run=True
while run:
    pygame.time.Clock().tick(60) #max petla wykona se 60x na sek, czyli gra ma 60fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #jeżeli gracz zaknie okno
            run = False

    keys = pygame.key.get_pressed() #do przejecia klawiatury uzytkownika

    speed = 5 #mozemy stworzymy zmienna okreslajaca predkosc

    if keys[pygame.K_RIGHT]: #czy strzalka w prawo jest wcisnieta
        x+= speed
    if keys[pygame.K_LEFT]:
        x-= speed
    if keys[pygame.K_UP]:
        y-= speed
    if keys[pygame.K_DOWN]:
        y+= speed

    player = pygame.rect.Rect(x, y, 100, 100)

    window.fill((24,164,240)) #kolor tła RGB
    pygame.draw.rect(window, (20,200,20), player ) #funkcja do umieszczania prostokatow na ekranie(okienko gdzie chcemy rysowac i kolor w RGB, nasz prostokat)
    pygame.display.update() #jak cos zmieniamy to musimy odswiezyc obraz