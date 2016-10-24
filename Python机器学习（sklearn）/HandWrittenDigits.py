#coding:utf-8

import pandas as pd
from sklearn import svm

def load_train_data():
    df = pd.read_csv("C:/Users/JYL-Family/optdigits.tra", header=None)
    x = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]

    return x, y

def load_test_data():
    df = pd.read_csv("C:/Users/JYL-Family/optdigits.tes", header=None)
    x = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]

    return x, y

def get_wrong_test_input(x_test, y_test, y_test_hat):
    df = x_test.loc[y_test != y_test_hat]
    return df

def get_wrong_test_output(x_test, y_test, y_test_hat):
    y_test = y_test.ravel()
    y_test_hat = y_test_hat.ravel()
    df_1 = y_test[y_test != y_test_hat]
    df_2 = y_test_hat[y_test != y_test_hat]
    return df_1, df_2


if __name__ == "__main__":
    x_train, y_train = load_train_data()
    x_test, y_test = load_test_data()

    clf_l = svm.SVC(C=0.8, kernel='linear', decision_function_shape='ovr')            # 使用线性核函数
    clf_r = svm.SVC(C=0.8, kernel='rbf', gamma=0.001, decision_function_shape='ovr')  # 使用高斯核函数

    # 这里注意一下
    clf_l.fit(x_train, y_train.ravel())
    clf_r.fit(x_train, y_train.ravel())

    print clf_l.score(x_test, y_test)
    print clf_r.score(x_test, y_test)

    print get_wrong_test_input(x_test, y_test, clf_l.predict(x_test)) # 返回 clf_l 分类器预测错误的输入变量（64 个灰度值）
    true_output, wrong_output = get_wrong_test_output(x_test, y_test, clf_l.predict(x_test))
    print "----预测错误----"
    print "真实值", true_output
    print "预测值", wrong_output