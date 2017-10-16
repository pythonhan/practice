'''
    作者：pythonhan
    功能：五角星的绘制,重复绘制出边长不同的五角星（使用turtle模块）
    日期：27/09/2017
    版本号：V2.0
    turtle模块常用函数：
    turtle.forward(distance):向前移动一段距离，X坐标轴的正方向
    turtle.backward(distance):向后移动一段距离，X坐标轴的负方向
    turtle.left(degree):向左旋转一定的角度,从X坐标轴的正方向到Y坐标轴的正方向
    turtle.right(degree):向右旋转一定的角度，从X坐标轴的正方向到Y坐标轴的负方向
    turtle.exitonclick():点击关闭图形窗口
    turtle.penup()抬起画笔，之后移动画笔不绘制形状
    turtle.pendown()落下画笔，之后移动画笔绘制形状
    turtle.pensize()设置画笔宽度
    turtle.pencolor('red')设置画笔颜色，常用的颜色：
    whilte,black,grey,darkgreen,gold,violet,purple
    新增功能：加入循环操作
'''
import turtle

def draw_pentagram(size):
    '''
    绘制五角星
    '''
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1
#         -= *= /=都可以

def main():
    '''
    主函数
    '''
    # 移动笔的初始位置
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor('red')

    size = 50
    while size <= 200:
        # 调用函数
        draw_pentagram(size)
        # size = size + 10
        size += 30
    turtle.penup()
    turtle.exitonclick()

if __name__ == '__main__':
    main()
