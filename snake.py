import pyxel
import os
import itertools as tool
from random import randint

class App():

    def __init__(self):
        self.snake_position = [(2,7), (3,7)]
        self.old_snake_position = []
        self.apple_position = [9, 7]
        self.delay = 0
        self.snake_state = ""
        pyxel.init(128, 128, fps=30, title="Snake le meilleur")
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.delay == 1:
            self.delay = 0
            self.old_snake_position = self.snake_position
            if self.snake_state == "up":
                self.old_snake_position.append((self.old_snake_position[-1][0], self.old_snake_position[-1][1]-1))
            elif self.snake_state == "down":
                self.old_snake_position.append((self.old_snake_position[-1][0], self.old_snake_position[-1][1]+1))
            elif self.snake_state == "right":
                self.old_snake_position.append((self.old_snake_position[-1][0]+1, self.old_snake_position[-1][1]))
            elif self.snake_state == "left":
                self.old_snake_position.append((self.old_snake_position[-1][0]-1, self.old_snake_position[-1][1]))
            
            if self.old_snake_position[-1] == (self.apple_position[0], self.apple_position[1]) and self.snake_state != "":
                self.snake_position = self.old_snake_position
                self.apple_position = self.change_apple_coords(self.free_squares())
                self.apple_position = [self.apple_position[0], self.apple_position[1]]
            elif self.snake_state != "":
                self.snake_position = self.old_snake_position[1:]

            if self.snake_position[-1] in self.snake_position[:-1] or self.snake_position[-1][0] not in range(16) or self.snake_position[-1][1] not in range(16):
                print("You lost!")
                pyxel.quit()
        else:
            self.delay += 1

        if pyxel.btnp(pyxel.KEY_UP) and self.snake_state != "down":
            self.snake_state = "up"
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.snake_state != "up":
            self.snake_state = "down"
        elif pyxel.btnp(pyxel.KEY_RIGHT) and self.snake_state != "left":
            self.snake_state = "right"
        elif pyxel.btnp(pyxel.KEY_LEFT) and self.snake_state != "right":
            self.snake_state = "left"
    
    def draw(self):
        pyxel.cls(0)
        for draw_x, draw_y in tool.product(range(16), range(16)):
            if (draw_x, draw_y) in self.snake_position[:-1]:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 1)
            elif (draw_x, draw_y) == self.snake_position[-1]:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 5)
            elif [draw_x, draw_y] == self.apple_position:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 8)
            else:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 11)
    
    def free_squares(self):
        list = []
        for list_x, list_y in tool.product(range(16), range(16)):
            if (list_x, list_y) not in self.snake_position:
                list.append((list_x, list_y))
        if list != []:
            return list
        else:
            print("You won!")
            pyxel.quit()

    def change_apple_coords(self, list):
        new_pos = list[randint(0, len(list)-1)]
        return new_pos

os.system("clear")
App()