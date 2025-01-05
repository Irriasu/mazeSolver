from graphics import Window,Line,Point
from cell import Cell
from maze import Maze
import sys


def main():

    num_rows = 3
    num_cols = 3
    margin = 50
    screen_x = 1800
    screen_y = 1600
    cell_size_x = 20
    cell_size_y = 20

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win,0)
    maze.solve()
    
    win.wait_for_close()

main()