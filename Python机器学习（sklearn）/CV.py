# coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVR

def load_data():
    df = pd.read_csv("C:/Users/JYL-Family/Advertising.csv")
    x = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']

    return x, y

if __name__ == "__main__":
    x, y = load_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    ''' 使用线性回归预测 '''

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    lr_y_test_hat = lr.predict(x_test)
    lr_mse = np.average(((lr_y_test_hat - y_test)**2))

    ''' 使用高斯核函数预测 '''

#    svr_rbf = SVR(kernel='rbf', gamma=0.001, C=10)
#    svr_rbf.fit(x_train, y_train)
#    svr_y_test_hat = svr_rbf.predict(x_test)
#    svr_rbf_mse = np.average(((svr_y_test_hat - y_test) ** 2))

    model = SVR(kernel='rbf')
    c_can = np.logspace(-5, 5, 5)  #
    gamma_can = np.logspace(-5, 5, 5)

    # GridSearchCV() 交叉验证函数
    # param_grid={'C':c_can, 'gamma':gamma_can} 参数 C 从 c_can 中取得 参数 gamma 从 gamma_can 中取得
    # cv = 10 代表作 10 折交叉验证 Cross-validation
    svr_rbf = GridSearchCV(model, param_grid={'C':c_can, 'gamma':gamma_can}, cv = 10)
    svr_rbf.fit(x_train, y_train)
    print "最佳参数：", svr_rbf.best_params_ # 最佳参数要训练过之后才能给出 fit 之后

    svr_y_test_hat = svr_rbf.predict(x_test)
    svr_rbf_mse = np.average(((svr_y_test_hat - y_test) ** 2))

    ''' sklearn 线性回归 数据可视化 '''

    x = np.arange(len(x_test))

    # 线性回归预测测试数据
    plt.plot(x,\
             lr_y_test_hat,\
             'r-',\
             linewidth=2,\
             label='linearregression predict')

    # svr 预测测试数据
    plt.plot(x, \
             svr_y_test_hat,\
             'b-',\
             linewidth=2,\
             label='svr predict')

    # 测试真实数据
    plt.plot(x, \
             y_test, \
             'g-', \
             linewidth=1, \
             label='predict')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()

    print lr_mse
    print svr_rbf_mse