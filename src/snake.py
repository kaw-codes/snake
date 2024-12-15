# snake.py

from config import *

class Snake:
    def __init__(self, canva):
        self.canva = canva
        self.body_part = 0
        self.coordinates = []
        self.squares = []
        self.color = '#00FF00'

        initial_coords = [(1,1), (2,1), (3,1)]
        for (x, y) in initial_coords:
            self.add_body_part((x, y))
    
    def add_body_part(self, new_part:tuple[int,int]):
        self.coordinates.insert(0, new_part)
        x, y = new_part
        square = self.canva.create_rectangle(x * CELL_SIZE,
                                             y * CELL_SIZE,
                                             x * CELL_SIZE + CELL_SIZE,
                                             y * CELL_SIZE + CELL_SIZE,
                                             fill=self.color,
                                             tag='snake')
        self.squares.insert(0, square)