from graphics import Window, Line, Point
from maze import Maze

def main():
    win = Window(800, 600)
    
    m = Maze(5, 5, 10, 10, 20, 20, win)
    
    win.wait_for_close()

    

main()