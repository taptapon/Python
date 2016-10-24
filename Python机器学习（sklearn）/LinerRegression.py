# coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 用于十字交叉验证
from sklearn.cross_validation import train_test_split
# 用于线性回归
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    path = "C:/Users/JYL-Family/Documents/Advertising.csv"

    '''通过 numpy 库读入 .csv 数据'''
    # 提供路径、文件用逗号分隔、跳过第一行
    # 返回 ndarray 对象
    p = np.loadtxt(path,\
                   delimiter=',',\
                   skiprows=1)
    print p

    '''通过 pandas 库读入 .csv 数据'''
    # 只提供路径即可
    data = pd.read_csv(path)
    # 取 TV、Radio、Newspaper 这三列
    print data[['TV', 'Radio', 'Newspaper']]

    '''数据可视化-1'''
    # plt.plot(x变量, y变量, 形状, 标签)
    # 形状这里还是很形象的 ,
    #     ro 代表 red 圆形
    #     g^ 代表 green 尖儿朝上的三角
    #     bv 代表 blue 尖儿朝下的三角
    plt.plot(data[['TV']],\
             data[['Sales']],\
             'ro',\
             label='TV')
    plt.plot(data[['Radio']], \
             data[['Sales']], \
             'g^', \
             label='Radio')
    plt.plot(data[['Newspaper']], \
             data[['Sales']], \
             'bv', \
             label='Newspaper')
    # 图例在图的右下方显示
    plt.legend(loc='lower right')
    # 图包含虚线网格
    plt.grid()
    # 图显示
    plt.show()

    '''数据可视化-2：分面'''
    # 确定画布大小 , 这步可以省略
    plt.figure(figsize=(9 , 12))
    # 311 代表一共绘制 3×1 幅图 , 现在绘制第一幅
    plt.subplot(311)
    plt.plot(data[['TV']],\
             data[['Sales']],\
             'ro')
    plt.title('TV')
    plt.grid() # 每幅图都要有
    # 同上 现在绘制第二幅
    plt.subplot(312)
    plt.plot(data[['Radio']],\
             data[['Sales']],\
             'g^')
    plt.title('Radio')
    plt.grid() # 每幅图都要有
    # 同上 现在绘制第三幅
    plt.subplot(313)
    plt.plot(data[['Newspaper']],\
             data[['Sales']],\
             'bv')
    plt.title('Newspaper')
    plt.grid() # 每幅图都要有
    plt.show()

    '''sklearn 线性回归'''

    # 生成测试集、训练集
    # random_state 代表随机数种子类似 R 语言中得 set.seed() 设定相同数字 , 保证下次得到的训练集、测试集相同
    # test_size 测试集占总数据集的比例
    x_train, x_test, y_train, y_test = train_test_split(data[['TV', 'Radio']],\
                                                        data[['Sales']], test_size=0.4, random_state=1)
    print len(x_train)
    print len(x_test)
    # 通过训练集生成 θ0、θ1、θ2、θ3
    linReg = LinearRegression()
    model = linReg.fit(x_train, y_train)
    # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    # copy_X=True True 表示对数据集 x_train、y_train 是拷贝后再使用
    # fit_intercept=True True 表示提供的数据集没有全 1 那一列 , False 表示提供的数据集已经有全 1 的那一列了
    # n_jobs=1 在一个 cpu 上计算
    # normalize=False 不正则化
    print model
    # 计算 θ1、θ2、θ3
    print linReg.coef_
    # 计算 θ0
    print linReg.intercept_

    # 训练好的模型 linReg 在测试集上做预测 , 得到 x_test 的预测值 y_hat
    y_hat = linReg.predict(np.array(x_test))
    # 误差平方的平均值 均方误差
    mse = np.average((y_hat - np.array(y_test))** 2)
    # 误差平方的平均值再开根号 均方误差开根号
    print mse, np.sqrt(mse)

    '''sklearn 线性回归 数据可视化'''
    x = np.arange(len(x_test))
    # 预测测试数据
    plt.plot(x,\
             y_hat,\
             'r-',\
             linewidth=2,\
             label='predict')
    # 测试真实数据
    plt.plot(x, \
             y_test, \
             'g-', \
             linewidth=2, \
             label='predict')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()



