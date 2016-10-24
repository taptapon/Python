# coding:utf-8

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn import svm


def show_accuracy(y_test, y_test_hat):
    # 通过这两行保证 y_test 与 y_test_hat 都是行向量 , 否则有可能 y_test 是列向量而
    # y_test_hat 是行向量无法比较
    y_test = y_test.ravel()
    y_test_hat = y_test_hat.ravel()

    acc_number = sum(y_test == y_test_hat)
    acc_rate = float(acc_number)/len(y_test)

    return acc_rate

def load_data():
    df = pd.read_csv("C:/Users/JYL-Family/Iris.csv")
    df.columns = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species'] # 数据不含列名 , 添加上

    x = df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']] # 输入变量
    y = df[['Species']] # 输入变量

    # 下面这三行代码实现了将 'Iris-setosa' , 'Iris-versicolor' , 'Iris-virginica' 编码为 0 1 2
    le = LabelEncoder()
    le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    y = le.transform(y)

    return x, y

if __name__ == "__main__":
    x, y =  load_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # SVC 是 svm 用来分类的方法 , 一般情况下我们说到 svm 都是 SVC
    # 还有 SVR svm 用作回归


    clf_l = svm.SVC(C=0.8, kernel='linear', decision_function_shape='ovr')           # 使用线性核函数
    clf_r = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')    # 使用高斯核函数

    clf_l.fit(x_train, y_train.ravel())
    clf_r.fit(x_train, y_train.ravel())

    # clf.score() SVC 函数自带的计算正确率的方法 , 输入 ( 测试集输入变量 , 测试集输出变量)
    print clf_l.score(x_test, y_test) # 这里线性核函数效果远远好于高斯核函数
    print clf_r.score(x_test, y_test)