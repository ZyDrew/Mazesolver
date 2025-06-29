from graphics import Line, Point

class Cell():

    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True

        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1

        self.visited = False

        self.win = window
    
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.win is None:
            return

        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "Black")
        else:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "White")
        
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "Black")
        else:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "White")
        
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "Black")
        else:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "White")

        if self.has_bot_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "Black")
        else:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "White")

    def draw_move(self, to_cell, undo=False):
        x1 = (self.x1 + self.x2) // 2
        y1 = (self.y1 + self.y2) // 2

        x2 = (to_cell.x1 + to_cell.x2) // 2
        y2 = (to_cell.y1 + to_cell.y2) // 2

        color = "Gray"
        if undo:
            color = "Red"
        
        if self.win is None:
            return
        self.win.draw_line(Line(Point(x1, y1), Point(x2, y2)), color)
        