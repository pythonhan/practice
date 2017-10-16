'''
    作者：pythonhan
    功能：五角星的绘制（使用turtle模块）
    日期：27/09/2017
    版本号：V1.0
    turtle模块常用函数：
    turtle.forward(distance):向前移动一段距离，X坐标轴的正方向
    turtle.backward(distance):向后移动一段距离，X坐标轴的负方向
    turtle.left(degree):向左旋转一定的角度,从X坐标轴的正方向到Y坐标轴的正方向
    turtle.right(degree):向右旋转一定的角度，从X坐标轴的正方向到Y坐标轴的负方向
    turtle.exitonclick():点击关闭图形窗口
    turtle.penup()抬起画笔，之后移动画笔不绘制形状
    turtle.pendown()落下画笔，之后移动画笔绘制形状
    turtle.pensize()设置画笔宽度
    turtle.pencolor()设置画笔颜色，常用的颜色：
    whilte,black,grey,darkgreen,gold,violet,purple
'''
import turtle


def main():
    '''
    主函数
    '''
    count = 1
    # 向前移动50个像素
    while count <=5:
        turtle.forward(80)
        turtle.right(144)
        count = count + 1

    # # 向右旋转144度,用for循环来代替画出剩下的四条边
    # for i in range(4):
    #     turtle.right(144)
    #     turtle.forward(80)
    # 让图形窗口保留
    turtle.exitonclick()

if __name__ == '__main__':
    main()
