from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, heigh):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=heigh)
        self.__canvas.pack()
        self.__online = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__online = True
        while self.__online == True:
            self.redraw()

    def close(self):
        self.__online = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point_1.x, self.__point_1.y, self.__point_2.x, self.__point_2.y, fill=fill_color, width=2
        )