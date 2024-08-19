from graphics import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
        self.__top_left_point = Point(x1, y1)
        self.__top_right_point = Point(x2, y1)
        self.__bott_left_point = Point(x1, y2)
        self.__bott_right_point = Point(x2, y2)
        self.center_point = Point((x2 + x1) / 2, (y2 + y1) / 2)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_botton_wall = True
        self.__window = window
        self.visited = False

    def __str__(self):
        return f"{self.__top_left_point.x}, {self.__top_left_point.y} --- {self.__bott_right_point.x}, {self.__bott_right_point.y}"

    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(self.__top_left_point, self.__bott_left_point), "black")
        else:
            self.__window.draw_line(Line(self.__top_left_point, self.__bott_left_point), "white")

        if self.has_top_wall:
            self.__window.draw_line(Line(self.__top_left_point, self.__top_right_point), "black")
        else:
            self.__window.draw_line(Line(self.__top_left_point, self.__top_right_point), "white")

        if self.has_right_wall:
            self.__window.draw_line(Line(self.__top_right_point, self.__bott_right_point), "black")
        else:
            self.__window.draw_line(Line(self.__top_right_point, self.__bott_right_point), "white")
        
        if self.has_botton_wall:
            self.__window.draw_line(Line(self.__bott_left_point, self.__bott_right_point), "black")
        else:
            self.__window.draw_line(Line(self.__bott_left_point, self.__bott_right_point), "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        self.__window.draw_line(Line(self.center_point, to_cell.center_point), color)
        

    