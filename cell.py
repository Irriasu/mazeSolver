from graphics import Line,Point

class Cell: 
    def __init__(self,win):
        self.has_left_wall =True
        self.has_right_wall =True
        self.has_top_wall =True
        self.has_bottom_wall =True
        self.x1= None
        self.x2= None
        self.y1= None
        self.y2= None 
        self.win = win

    def draw(self,x1,x2,y1,y2):
        self.x1= x1
        self.x2= x2
        self.y1= y1
        self.y2= y2 
        
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self.win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self.win.draw_line(line)
        
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self.win.draw_line(line)
        
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self.win.draw_line(line)

    def draw_move(self,to_cell,undo=False):
        if self.win is None:
            return
        half_length = abs(self.x2 - self.x1) // 2
        x_center = half_length + self.x1
        y_center = half_length + self.y1

        half_length2 = abs(to_cell.x2 - to_cell.x1) // 2
        x_center2 = half_length2 + to_cell.x1
        y_center2 = half_length2 + to_cell.y1

        color = 'red'
        if undo:
            color='gray'

        line = Line(Point(x_center,y_center),Point(x_center2,y_center2))
        self.win.draw_line(line,color)
