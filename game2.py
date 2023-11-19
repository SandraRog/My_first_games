import sys
import time
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((1280,700))

class GameText:
    def __init__(self, text, font_size, color, x, y):
        self.font = pygame.font.SysFont("arial", font_size)
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.surface = self.font.render(self.text, True, self.color)

    def update(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)

    def draw(self, window):
        window.blit(self.surface, (self.x, self.y))
class Player:
    def __init__(self):
        self.x_cord = 100
        self.y_cord = 100
        self.image = pygame.image.load("ludek3.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 20
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self, keys): #wykonuje sie tylko raz na powtorzenie petli (obliczenie polozenia, sterowanie, itp)
        if keys[pygame.K_w]:
            self.y_cord -= self.speed #dwojka zastapiona staerowaniem
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
        if keys[pygame.K_s]:
            self.y_cord += self.speed #idzie w dol wiec zwiekszyamy y
        if keys[pygame.K_d]:
            self.x_cord += self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self): #wyrysowanie gracza na ekranie
        window.blit(self.image, (self.x_cord, self.y_cord))

class Food:
    def __init__(self):
        self.x_cord = randint(0, 1280)
        self.y_cord = randint(0, 700)
        self.image = pygame.image.load("ham.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 1.5
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self): #wysowanie gracza na ekranie
        window.blit(self.image, (self.x_cord, self.y_cord))
def main(): #pętle while zamykamy w funkcji
    run = True
    player = Player() #tworzymy instancje klasy
    clock = 0 #stoper
    score = 0
    foods = [] #lista na kazde jedzenie jakie sie utworzy
    background = pygame.image.load("tlo.png")

    # Dodanie pola tekstowego dla wyniku
    score_text = GameText(f"You eat {score} hamburgers", 40, (0, 0, 0), 10, 10)

    # Dodanie pola tekstowego na gratulacje
    congratulations_text = GameText("", 40, (255, 0, 0), 300, 300)

    # Resetuj czas
    start_czasu = time.time()

    while run:
        clock += pygame.time.Clock().tick(60) / 1000 #czas, jaki wykonuje sie powtorzenie petli, /1000 aby otrzymać sekundy

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #jeżeli gracz zaknie okno
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if clock >= 1:
            clock = 0
            foods.append(Food()) #tworzymy instancje i od razu dodajemy ja do listy

        player.tick(keys)

        for food in foods: #nalezy wywolac fukncje tick dla wszystkich el z listy
            food.tick()

        for food in foods:
            if player.hitbox.colliderect(food.hitbox):
                foods.remove(food)
                score += 1
                score_text.update(f"You eat {score} hamburgers")  # Aktualizacja tekstu wyniku
                congratulations_text.update(f"Congratulations, You eat {score} hamburgers!")

        window.blit(background, (0, 0))
        score_text.draw(window)
        player.draw()
        for food in foods: #to samo co z tick, robimy dla draw
            food.draw()

        pygame.display.update() #grafika oraz polozenie

        # Sprawdzanie czasu
        obecny_czas = time.time()
        czas_grania = obecny_czas - start_czasu
        if czas_grania > 30:
            print("Time ended!")
            run = False  # Zmiana flagi run na False, aby zakończyć pętlę

    # Pętla na wyświetlenie wyniku przed zamknięciem okna
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.blit(background, (0, 0))
        congratulations_text.draw(window)
        pygame.display.update()

        pygame.time.wait(300)

if __name__=="__main__":
    main()
