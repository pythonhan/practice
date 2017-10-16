'''
    作者：pythonhan
    功能：绘制分形树
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
    turtle.pencolor('red')设置画笔颜色，常用的颜色：
    whilte,black,grey,darkgreen,gold,violet,purple
    新增功能：加入循环操作
    新增功能：使用递归函数迭代绘制：内部自己调用自己，完成很好的封装，不需要关注细节
    每次函数会临时存储变量，要设置终止条件，跳出迭代
    新增功能：绘制分形树
'''
import turtle

def draw_branch(branch_length):
    '''
    绘制分形树
    '''
    if branch_length > 5:
        '''绘制右侧树枝'''
        if branch_length > 20:
            turtle.color('red')
        else:
            turtle.color('green')
        turtle.forward(branch_length)
        print('向前：',branch_length)
        turtle.right(20)
        print('右转20')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转40')
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(20)
        print('右转20')
        turtle.backward(branch_length)
        print('向后',branch_length)

def main():
    '''
    主函数
    '''
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    draw_branch(60)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
