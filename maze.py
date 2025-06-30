from cell import Cell
import time, random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

        if seed:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_visited_cells()
    
    def create_cells(self):

        for _ in range(0, self.num_cols):
            row_cells = []
            for _ in range(0, self.num_rows):
                row_cells.append(Cell(self.win))
            self.cells.append(row_cells)

        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.draw_cell(i, j)
    
    def draw_cell(self, i, j):
        if self.win is None:
            return
        
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self.cells[i][j].draw(x1, y1, x2, y2)
        self.animate()
    
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.02)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[-1][-1].has_bot_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls_r(self, i , j):
        self.cells[i][j].visited = True

        while True:
            to_visit = []

            #Check cells that can be visited
            #Left
            if i > 0 and self.cells[i - 1][j].visited == False:
                to_visit.append((i-1, j))
            
            #Right
            if i < self.num_cols - 1 and self.cells[i+1][j].visited == False:
                to_visit.append((i+1, j))
            
            #Top
            if j > 0 and self.cells[i][j-1].visited == False:
                to_visit.append((i, j-1))
            
            #Bot
            if j < self.num_rows - 1 and self.cells[i][j+1].visited == False:
                to_visit.append((i, j+1))

            #No cell to visit available
            if not to_visit:
                self.draw_cell(i, j)
                return

            cell_to_visit = to_visit[random.randrange(len(to_visit))]

            #Break the wall between the 2 cells
            #Left
            if cell_to_visit[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
            
            #Right
            if cell_to_visit[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False

            #Top
            if cell_to_visit[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bot_wall = False
            
            #Bottom
            if cell_to_visit[1] == j + 1:
                self.cells[i][j].has_bot_wall = False
                self.cells[i][j+1].has_top_wall = False

            #Recall function with next cell
            self.break_walls_r(cell_to_visit[0], cell_to_visit[1])

    def reset_visited_cells(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.cells[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)
    
    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True

        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        #Left
        if i - 1 >= 0 and not self.cells[i-1][j].has_right_wall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j], True)
            result = self.solve_r(i-1, j)
            if result:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j])
        
        #Right
        if i + 1 < self.num_cols and not self.cells[i+1][j].has_left_wall and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j], True)
            result = self.solve_r(i+1, j)
            if result:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j])

        #Top
        if j - 1 >= 0 and not self.cells[i][j-1].has_bot_wall and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1], True)
            result = self.solve_r(i, j-1)
            if result:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1])

        #Bot
        if j + 1 < self.num_rows and not self.cells[i][j+1].has_top_wall and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1], True)
            result = self.solve_r(i, j+1)
            if result:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1])

        return False

        