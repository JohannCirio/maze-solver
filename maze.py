from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)
        self.__reset_cells_visited()
        self.solver(0,0)

    def __create_cells(self):
        matrix = []
        for col in range(self.__num_cols):
            line = []
            for row in range(self.__num_rows):
                x1 = self.__x1 + (self.__cell_size_x * row)
                y1 = self.__y1 + (self.__cell_size_y * col)
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                cell = Cell(x1, y1, x2, y2, self.__window)
                line.append(cell)
                self.__draw_cell(cell)

            matrix.append(line)
        
        self.cells = matrix
        
        
    def __draw_cell(self, cell):
        if self.__window is None:
            return

        cell.draw()
        self.__animate()
    
    def __animate(self):
        self.__window.redraw()
        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        entrance = self.cells[0][0]
        exit = self.cells[-1][-1]

        entrance.has_top_wall = False
        exit.has_botton_wall = False

        self.__draw_cell(entrance)
        self.__draw_cell(exit)
    
    def __break_walls(self, current_x, current_y):
        self.cells[current_x][current_y].visited = True
        
        possible_cells = self.check_possible_cells(current_x, current_y)
        
        while len(possible_cells) > 0:
            next_cell_position = random.choice(possible_cells)

            if current_x - next_cell_position[0] == -1:
                self.cells[current_x][current_y].has_botton_wall = False
                self.cells[next_cell_position[0]][next_cell_position[1]].has_top_wall = False
            elif current_x - next_cell_position[0] == 1:
                self.cells[current_x][current_y].has_top_wall = False
                self.cells[next_cell_position[0]][next_cell_position[1]].has_botton_wall = False
            elif current_y - next_cell_position[1] == -1:
                self.cells[current_x][current_y].has_right_wall = False
                self.cells[next_cell_position[0]][next_cell_position[1]].has_left_wall = False
            else:
                self.cells[current_x][current_y].has_left_wall = False
                self.cells[next_cell_position[0]][next_cell_position[1]].has_right_wall = False
            
            self.__break_walls(next_cell_position[0], next_cell_position[1])
            possible_cells = self.check_possible_cells(current_x, current_y)

        self.__draw_cell(self.cells[current_x][current_y])

    def check_possible_cells(self, current_x, current_y):
        possible_cells = []
        if current_x - 1 >= 0 and self.cells[current_x - 1][current_y].visited != True:
            possible_cells.append((current_x - 1, current_y))
        if current_x + 1 < self.__num_cols and self.cells[current_x + 1][current_y].visited != True:
            possible_cells.append((current_x + 1, current_y))
        if current_y - 1 >= 0 and self.cells[current_x][current_y - 1].visited != True:
            possible_cells.append((current_x, current_y - 1))
        if current_y + 1 < self.__num_rows and self.cells[current_x][current_y + 1].visited != True:
            possible_cells.append((current_x, current_y + 1))
        
        return possible_cells
    
    def __reset_cells_visited(self):
        for line in self.cells:
            for cell in line:
                cell.visited = False
                print(cell.visited)

    def solver(self, current_x, current_y):
        self.cells[current_x][current_y].visited = True

        if current_x == self.__num_cols - 1 and current_y == self.__num_rows -1:
            return True
        
        possible_paths = self.__check_possible_paths(current_x, current_y)

        while len(possible_paths) > 0:
            selected_path = random.choice(possible_paths)
            self.cells[current_x][current_y].draw_move(self.cells[selected_path[0]][selected_path[1]])
            self.__window.redraw()
            time.sleep(0.1)
            if self.solver(selected_path[0], selected_path[1]):
                return True
            
            self.cells[current_x][current_y].draw_move(self.cells[selected_path[0]][selected_path[1]], undo=True)
            possible_paths = self.__check_possible_paths(current_x, current_y)
        
        return False

    
    def __check_possible_paths(self, current_x, current_y):
        possible_paths = []

        if (not self.cells[current_x][current_y].has_left_wall and 
            current_y - 1 >= 0 and 
            not self.cells[current_x][current_y - 1].visited):

            possible_paths.append((current_x, current_y - 1))

        if (not self.cells[current_x][current_y].has_right_wall and 
            current_y + 1 < self.__num_rows and 
            not self.cells[current_x][current_y + 1].visited):

            possible_paths.append((current_x, current_y + 1))

        if (not self.cells[current_x][current_y].has_top_wall and 
            current_x - 1 >= 0 and 
            not self.cells[current_x - 1][current_y].visited):

            possible_paths.append((current_x - 1, current_y))

        if (not self.cells[current_x][current_y].has_botton_wall and 
            current_x + 1 < self.__num_cols and 
            not self.cells[current_x + 1][current_y].visited):

            possible_paths.append((current_x + 1, current_y))
        
        return possible_paths