import curses
import invaders as G
import time


def put_object(screen, glyph, column, row):
    screen.addstr(int(row/10), int(40+column/10), glyph)

def main(screen):
    #screen.nodelay(True)
    game = G.Game()
    ch = -1
    while not game.is_over:
        game.update()

        screen.clear()
        if (ch >= 0):
            screen.addstr(0, 60, str(ch)+" "+chr(ch))
        screen.addstr(0,0, str(game.player))
        put_object(screen, "@", game.player.x, game.player.y)
        for enemy in game.enemies:
            put_object(screen, "&", enemy.x, enemy.y)
        for bullet in game.bullets:
            put_object(screen, "\u2022", bullet.x, bullet.y)
        screen.refresh()
 
        ch = screen.getch()
        if ch == 113: break # 'q'

        if 0 <= ch < 128:
            game.last_key = chr(ch)

if __name__=="__main__":
    
    curses.wrapper(main)