"""
    作者:pythonhan
    日期：12/10/2017
    功能：赔率小游戏，猜测参与活动的人数回事素数还是合数，如果我坐庄，开出的赔率为素数5.5, 合数1.1， 以素数下注1元为例子：
    若最终人数为素数，则返还5.5元，1元为庄家所有，若最终人数是合数，则无返还，1元为庄家所有
    笔记：
    超参与过拟合，线性回归，高阶拟合
"""
#!/usr/bin/python
# -*- coding:utf-8 -*-


from scipy.integrate import odeint
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def clip(x, path):
    """

    """
    for i in range(len(x)):
        if x[i] >= path:
            x[i] %= path

def main():
    """
    主函数
    """
    path = 5000     # 环形公路长度
    n = 100         # 公路车辆个数
    v0 = 5          # 车辆的初始速度
    p = 0.3         # 随机减速概率
    Times = 3000

    np.random.seed(0)
    x = np.random.rand(n) * path
    x.sort()
    v = np.tile([v0], n).astype(np.float)

    plt.figure(figsize=(10, 8), facecolor='r')
    for t in range(Times):
        plt.scatter(x, [t]*n, s=1, c='k',alpha=0.5)
        for i in range(n):
            if x[(i + 1) % n] > x[i]:
                d = x[(i + 1) % n] - x[i]
            else:
                d = path - x[i] + x[(i + 1) % n]
            if v[i] < d:
                if np.random.rand() > p:
                    v[i] += 1
                else:
                    v[i] -= 1
            else:
                v[i] = d - 1
        v = v.clip(0, 150)
        x += v
        clip(x, path)
    plt.xlim(0, path)
    plt.ylim(0, Times)
    plt.xlabel(u'车辆位置', fontsize = 16)
    plt.ylabel(u'模拟时间', fontsize = 16)
    plt.title(u'环形车辆堵车模拟', fontsize = 20)
    plt.tight_layout(pad=2)
    plt.show()



    # figure 1
    # s0 = (0., 1., 0.)
    # t = np.arange(0, 30, 0.01)
    # s = odeint(lorenz, s0, t)
    # plt.figure(figsize=(12, 8), facecolor ='w')
    # plt.subplot(121, projection='3d')
    # plt.plot(s[:, 0], s[:, 1], s[:, 2], c='g')
    # plt.title(u'微分方程计算结果', fontsize=16)
    #
    # s = lorenz_trajectory(s0, 40000)
    # plt.subplot(122, projection='3d')
    # plt.plot(s[:, 0], s[:, 1], s[:, 2], c='r')
    # plt.title(u'沿着梯度累加结果', fontsize=16)
    #
    # plt.tight_layout(1, rect=(0,0,1,0.98))
    # plt.suptitle(u'lorenz系数', fontsize=20)
    # plt.show()
    #
    # # figure 2
    # ax = Axes3D(plt.figure(figsize=(8, 8)))
    # s0 = (0., 1., 0.)
    # s1 = lorenz_trajectory(s0, 50000)
    # s0 = (0., 1.0001, 0.)
    # s2 = lorenz_trajectory(s0, 50000)
    #
    # #曲线
    # ax.plot(s1[:, 0], s1[:, 1], s1[:, 2], c='g', lw=0.4)
    # ax.plot(s2[:, 0], s2[:, 1], s2[:, 2], c='r', lw=0.4)
    #
    # # 起点
    # ax.scatter(s1[0, 0], s1[0, 1], s1[0, 2], c='g', s=50, alpha=0.5)
    # ax.scatter(s2[0, 0], s2[0, 1], s2[0, 2], c='r', s=50, alpha=0.5)
    #
    # #终点
    # ax.scatter(s1[-1, 0], s1[-1, 1], s1[-1, 2], c='g', s=100)
    # ax.scatter(s2[-1, 0], s2[-1, 1], s2[-1, 2], c='r', s=100)
    # ax.set_title(u'Lorenz方程与初始条件', fontsize =20)
    # ax.set_xlabel(u'Y')
    # ax.set_ylabel(u'Y')
    # ax.set_zlabel(u'Z')
    # plt.show()

if __name__ == "__main__":
    main()