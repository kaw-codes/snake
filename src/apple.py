# apple.py

import random as rdm
from config import *

class Apple:
    def __init__(self, canva, snake):
        self.snake = snake
        self.coordinates = self.__get_rdm_coord()
        x, y = self.coordinates
        self.color ='#FF0000'
        canva.create_oval(x * CELL_SIZE,
                          y * CELL_SIZE,
                          x * CELL_SIZE + CELL_SIZE,
                          y * CELL_SIZE + CELL_SIZE,
                          fill=self.color,
                          tag='apple')

    def __get_rdm_coord(self):
        while True:
            x = rdm.randint(0, COLUMNS-1)
            y = rdm.randint(0, ROWS-1)
            if (x, y) not in self.snake.coordinates:
                return (x, y)