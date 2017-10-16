'''
    作者：pythonhan
    功能：弹球游戏
    版本：V1.0
    日期：28/09/2017

'''
import tkinter
import random
import time

tk = tkinter.Tk()
tk.title("pythonhan's game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", -1)
canvas = tkinter.Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

class Ball():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245,100)
        starts = [-3,-2,-1,1,1,2,3,4,6,3,7,9,-5,-4]
        random.shuffle(starts)
        self.x = starts[0]  #从list里面随机抽取一个
        self.y = -3  #-3位y坐标轴移动速度
        self.canvas_height = self.canvas.winfo_height()
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y) #向上运动
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:   #move down
            self.y = 1

        if pos[3] >= self.canvas_height: #move up
            self.y = -1

        # if self.hit_paddle(pos) == 'True':
        #     self.y = -3


class Paddle:
    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

paddle = Paddle(canvas,"blue")
ball=Ball(canvas,"red")
while 1:
    ball.draw() #不断重复绘球
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


def main():
    """
    主程序
    """
    pass

if __name__ == '__main__':
    main()
