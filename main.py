from graphics import Window,Line,Point

def main():
    win = Window(800,800)
    win.draw_line(Line(Point(),Point(50,100))) 
    win.wait_for_close()

main()