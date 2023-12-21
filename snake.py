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
        self.chosen_delay = 1000
        self.freeze = False
        self.cheat_code_var = False
        self.snake_state = ""
        pyxel.init(128, 128, fps=3000, title="Snake le meilleur")
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.freeze:
            if pyxel.btnp(pyxel.KEY_C):
                self.cheat_code_var = True
            if pyxel.btn(pyxel.KEY_P) and self.chosen_delay != 2999:
                self.chosen_delay += 1
                self.delay = 0
                os.system("clear")
                print(self.chosen_delay)
            elif pyxel.btn(pyxel.KEY_M) and self.chosen_delay != 1:
                self.chosen_delay += -1
                os.system("clear")
                self.delay = 0
                print(self.chosen_delay)
            if self.delay == self.chosen_delay:
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
                    self.free_squares_list = self.free_squares()
                    if not self.freeze:
                        self.apple_position = self.change_apple_coords(self.free_squares_list)
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

            if self.cheat_code_var:
                self.cheat_code()

    def draw(self):
        pyxel.cls(0)
        for draw_x, draw_y in tool.product(range(16), range(16)):
            if (draw_x, draw_y) in self.snake_position[:-1]:
                if self.snake_position.index((draw_x, draw_y))%2 == 0:
                    pyxel.rect(draw_x*8, draw_y*8, 8, 8, 12)
                else:
                    pyxel.rect(draw_x*8, draw_y*8, 8, 8, 6)
            elif (draw_x, draw_y) == self.snake_position[-1]:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 5)
            elif [draw_x, draw_y] == self.apple_position:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 8)
            elif (draw_x + draw_y)%2 == 0:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 3)
            else:
                pyxel.rect(draw_x*8, draw_y*8, 8, 8, 11)
    
    def cheat_code(self):
        if self.snake_position[-1] in [(test_x, 1) for test_x in range(0, 15, 2)] or self.snake_position[-1] == (0,0):
            self.snake_state = "down"
        elif self.snake_position[-1] in [(test_x, 1) for test_x in range(1, 15, 2)] or self.snake_position[-1] in [(test_x, 15) for test_x in range(0, 15, 2)]:
            self.snake_state = "right"
        elif self.snake_position[-1] in [(test_x, 15) for test_x in range(1, 17, 2)]:
            self.snake_state = "up"
        elif self.snake_position[-1] == (15, 0):
            self.snake_state = "left"

    def free_squares(self):
        list = []
        for list_x, list_y in tool.product(range(16), range(16)):
            if (list_x, list_y) not in self.snake_position:
                list.append((list_x, list_y))
        if list != []:
            return list
        else:
            print("You won!")
            self.freeze = True

    def change_apple_coords(self, list):
        new_pos = list[randint(0, len(list)-1)]
        return new_pos

os.system("clear")
App()
