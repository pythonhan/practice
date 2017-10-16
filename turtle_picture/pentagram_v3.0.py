'''
    作者：pythonhan
    功能：五角星的绘制,重复绘制出边长不同的五角星（使用turtle模块）
    日期：27/09/2017
    版本号：V3.0
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
    新增功能：使用递归函数迭代绘制：内部自己调用自己，完成很好的封装，不需要关注细节
    每次函数会临时存储变量，要设置终止条件，跳出迭代
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

def draw_recursive_pentagram(size):
    '''
    递归绘制五角星
    '''
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1
    # 五角星绘制完成，更新参数
    size += 10
    if size <= 100:
        draw_recursive_pentagram(size)

def main():
    '''
    主函数
    '''
    # 移动笔的初始位置
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('red')

    size = 50
    draw_recursive_pentagram(size)
    turtle.exitonclick()



if __name__ == '__main__':
    main()
