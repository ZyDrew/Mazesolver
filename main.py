from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_right_wall = False
    c.has_left_wall = False
    c.draw(1, 1, 50, 50)
    
    c2 = Cell(win)
    c2.has_bot_wall = False
    c2.has_left_wall = False
    c2.draw(50, 1, 100, 50)

    c.draw_move(c2, True)
    
    win.wait_for_close()

    

main()