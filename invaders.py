"a simple game from a more enlightened age"
from typing import TypeVar
import random
import time

TOS = 0
BOS = 220

class Player:
    def __init__(self):
        self.x = 0
        self.y = BOS - 10
        self.lives = 3
    
    def __str__(self):
        lives = "<3 " * self.lives
        return f"Player @({self.x},{self.y}) {lives}"
    
    def move(self, direction):
        if direction > 0:
            self.x += 10
        if direction < 0:
            self.x -= 10
    
    def shoot(self):
        return Bullet(self.x, self.y - 10, True)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Invader @({self.x},{self.y})"
    
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

class Bullet:
    def __init__(self, x, y, is_player_bullet:bool):
        self.x = x
        self.y = y
        self.is_player_bullet = is_player_bullet
        self.v = 1

    def __str__(self):
        glyph = "x"
        if self.is_player_bullet:
            glyph = "z"
        return f"{glyph} @({self.x},{self.y})"
    
    def move(self):
        if self.is_player_bullet:
            self.y -= self.v
        else:
            self.y += self.v

T = TypeVar('T', Player, Enemy, Bullet)
def collision(a:T, b:T) -> bool:
    return abs(a.x - b.x) < 1 and abs(a.y - b.y) < 1

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = [Enemy(-10, 180)]
        self.bullets = []
        self.last_key = None

    @property
    def is_over(self):
        return self.player.lives < 1
    
    def update(self):
        if self.last_key is not None:
            if self.last_key == "d": self.player.move(+1)
            if self.last_key == "a": self.player.move(-1)
            if self.last_key == "s":
                if sum([bullet.is_player_bullet for bullet in self.bullets]) < 2:
                    self.bullets.append(self.player.shoot())
            self.last_key = None

        for bullet in self.bullets:
            bullet.move()
            if collision(bullet, self.player):
                self.player.take_hit()
        self.bullets = [bullet for bullet in self.bullets if TOS <= bullet.y <= BOS]

def trace(game: Game):
    
    print(game.player)
    for enemy in game.enemies:
        print(enemy)
    for bullet in game.bullets:
        print(bullet)
    print()

if __name__=="__main__":
    game = Game()
    while game.player.lives > 0:
        if random.random() < 0.5:
            game.last_key = random.choice("asdqwe")
        game.update()
        trace(game)
        time.sleep(1.0)

