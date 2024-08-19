from graphics import Window
from maze import Maze
window = Window(1800, 1200)

maze = Maze(10, 10, 30, 30, 30, 30, window)

window.wait_for_close()