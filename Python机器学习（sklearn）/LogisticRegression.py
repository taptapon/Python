# coding:utf-8

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split

if __name__ == "__main__":
    path = "C:/Users/JYL-Family/Documents/iris.data"

    '''通过 pandas 库读入数据'''

    # 注意这里 header=None 代表数据没有表头
    data = pd.read_csv(path, header=None)

    '''通过 sklearn 库数据预处理'''

    # 取输入变量 ndarray
    # 第一个 : 代表取所有的行
    # 第二个 : 代表取所有的列 , 从第 1 列开始直到最后 1 列但不包括最后 1 列
    x = data.values[:, :-1]
    # 取输出变量 ndarray
    y = data.values[:, -1]

    # 下面这三行代码实现了将 'Iris-setosa' , 'Iris-versicolor' , 'Iris-virginica' 编码为 0 1 2
    le = LabelEncoder()
    le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    y = le.transform(y)

    '''sklearn logistic 回归'''

    # 数据预处理得到的 x , y 数据集都作为训练集
    x_train, x_test, y_train, y_test = train_test_split(x, y, \
                                                        test_size=0.4, random_state=1)

    logReg = LogisticRegression()
    logReg.fit(x_train, y_train.ravel())

    y_test_hat = logReg.predict(x_test)
    accuratearray = y_test_hat == y_test
    accuraterate = np.count_nonzero(accuratearray)/len(accuratearray)
    print accuraterate, '\n'

    # StandardScaler() 应该怎么使用？下面报了错 , 不知道怎么解决
    # logReg = Pipeline([('sc', StandardScaler()), ('clf', LogisticRegression())])
    # logReg.fit(x_train, y_train.ravel())
    # y_test_hat = logReg.predict(x_test)
    # accuratearray = y_test_hat == y_test
    # accuraterate = np.count_nonzero(accuratearray)/len(accuratearray)
    # print accuraterate, '\n'


'''
    sklearn logistic 回归 数据可视化
    # 可视化只能用前两个特征训练 LR 模型
    logReg2 = LogisticRegression()
    print logReg2.fit(x_train[:, :2], y_train)

    # 为画图方便 , 取 x_train 前两列分别作为 x 轴变量与 y 轴变量
    x_train = x_train[:, :2]
    # x_train 第一列作为 x 轴变量 x_min, x_max 分别为 x 轴变量的范围
    x_min, x_max = x_train[:, 0].min(), x_train[:, 0].max()
    # x_train 第一列作为 y 轴变量 y_min, y_max 分别为 y 轴变量的范围
    y_min, y_max = x_train[:, 1].min(), x_train[:, 1].max()

    # 生成 500 个数字 以 x_min 开始 x_max 结束的等差数列
    t1 = np.linspace(x_min, x_max, 2000)
    # 生成 500 个数字 以 y_min 开始 y_max 结束的等差数列
    t2 = np.linspace(y_min, y_max, 2000)

    x1, x2 = np.meshgrid(t1, t2)
    print t1, '\n', t2
    print x1, '\n', x2
    x_test = np.stack((x1.flat, x2.flat), axis=1)

    y_test_hat = logReg2.predict(x_test)
    y_test_hat = y_test_hat.reshape(x1.shape)
    plt.pcolormesh(x1, x2,\
                   y_test_hat,\
                   cmap=plt.cm.Spectral,\
                   alpha=0.1)
    # c color 这里 c=y_train 类似 R 语言中 color=定性变量
    # edgecolors='k' 圆圈边界是黑色
    # cmap=plt.cm.prism 使用 plt.cm.prism 调色版？
    plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, \
                edgecolors='k', cmap=plt.cm.prism)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid()
    plt.show()
'''
