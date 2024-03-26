import itertools
import random

class Sentence():


    #each sentence object contains information about number of mines around each cell and a set of unrevealed cells
    def __init__(self, cells, count):
        #not sure
        self.cells = set(cells) #unrevealed cells around each cell
        self.count = count    #the number that is revealed when we click on a cell(the number of mine around a cell)

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        if self.count == len(self.cells):
            return self.cells
        return None

    def known_safes(self):


        if not self.count:
            return self.cells
        return None

    def mark_mine(self, cell):

        if cell in self.cells:
            #if a cell is a mine then we remove it from the unrevealed set
            #decrease the mine count by one
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):

        if cell in self.cells:
            #if a cell is a safe then we remove it from the unrevealed set
            self.cells.remove(cell)
