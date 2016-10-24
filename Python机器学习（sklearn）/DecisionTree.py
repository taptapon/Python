# coding:utf-8

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

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

    # 划分训练集 测试集的时候 不能写成如下形式
    # train_test_split(x) train_test_split(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    '''sklearn  决策树 分类树'''

    # criterion    分类树使用什么方式算法？ID3 算法使用信息熵、C4.5 算法使用信息增益、CART 算法使用基尼系数
    # max_depth=30 分类树的最大深度为 30
    # min_samples_leaf=10  如果结点通过某特征划分后 , 每个叶子结点包含样本数目大于 10 则划分 否则不划分
    # min_samples_split=10 如果结点包含样本数目大于 10 , 有可能通过某特征划分该结点
	# 这三个参数是预剪枝的限定条件
    dt_clf = DecisionTreeClassifier(criterion="entropy", max_depth=10)
    dt_clf.fit(x_train, y_train)
    y_test_hat = dt_clf.predict(x_test)

    print float(np.count_nonzero(y_test_hat==y_test))/len(y_test)
    print np.round(float(np.count_nonzero(y_test_hat==y_test))/len(y_test), 4) * 100