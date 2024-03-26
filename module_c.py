import itertools
import random



class MinesweeperAI():


    def __init__(self, height=16, width=16):

        self.height = height
        self.width = width

        self.moves_made = set()

        self.mines = set()
        self.safes = set()

        self.knowledge = []

    def mark_mine(self, cell):

        #when a cell is marked as mine ,update the self.mines set
        #for every sentence in the knowledge list, mark the cell as mine, if the cell is present in the unrvealed cells of the sentence

        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):

        #when a cell is marked as safe ,update the self.safes set
        #for every sentence in the knowledge list, mark the cell as safe, if the cell is present in the unrvealed cells of the sentence

        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):

        self.moves_made.add(cell)

        self.mark_safe(cell)

        cells = set()

        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                if (i, j) == cell:
                    continue

                if 0 <= i < self.height and 0 <= j < self.width:
                    if (i, j) not in self.moves_made and (i, j) not in self.mines:
                        cells.add((i, j))

                    elif (i, j) in self.mines:
                        count -= 1
        self.knowledge.append(Sentence(cells, count))

        for sentence in self.knowledge:
            safes = sentence.known_safes()
            if safes:
                for cell in safes.copy():
                    self.mark_safe(cell)
            mines = sentence.known_mines()
            if mines:
                for cell in mines.copy():
                    self.mark_mine(cell)

        for sentence1 in self.knowledge:
            for sentence2 in self.knowledge:
                if sentence1 is sentence2:
                    continue
                if sentence1 == sentence2:
                    self.knowledge.remove(sentence2)
                elif sentence1.cells.issubset(sentence2.cells):
                    new_knowledge = Sentence(
                        sentence2.cells - sentence1.cells,
                        sentence2.count - sentence1.count)
                    if new_knowledge not in self.knowledge:
                        self.knowledge.append(new_knowledge)

    def make_safe_move(self):

        available_steps = self.safes - self.moves_made
        if available_steps:
            return random.choice(tuple(available_steps))
        return None

    def make_random_move(self):

        if len(self.mines) + len(self.moves_made) == self.height * self.width:
            return None

        while True:
            i = random.randrange(self.height)
            j = random.randrange(self.width)
            if (i, j) not in self.moves_made and (i, j) not in self.mines:
                return (i, j)
