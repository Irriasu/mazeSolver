from tkinter import Tk,BOTH,Canvas

class Window:
    def __init__(self,width,height):
        self.root_widget = Tk()
        self.root_widget.title="solver"
        self.canvas = Canvas(self.root_widget,bg='white',height=height,width=width)
        self.canvas.pack()
        self.is_running = False
        self.root_widget.protocol('WM_DELETE_WINDOW',self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running=False

    def draw_line(self,line,fill_color='black'):
        line.draw(self.canvas,fill_color)




class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y =y

class Line:

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2 

    def draw(self,canvas,color='black'):
        canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=color, width=2)


        
        
