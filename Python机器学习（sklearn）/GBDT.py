# coding:utf-8

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

def show_accuracy(y_test, y_test_hat):
    acc_number = sum(y_test == y_test_hat)
    acc_rate = float(acc_number)/len(y_test)
    return np.round(acc_rate, 2)

def load_data():
    # 读数据
    df = pd.read_csv("C:/Users/JYL-Family/Titanic_train.csv")


    # Sex 性别特征处理 , 由 female、male 变为 0、1 sklearn 才能够处理
    df.Sex = df.Sex.map({'female': 0, 'male': 1}).astype(int)


    # Fare 船票价格特征处理 , 用相同舱位船票价格的中位数代替
    if sum(df.Fare.isnull()) > 0: # 如果船票价格有缺失值
        fare = np.zeros(3)
        # 计算三个仓位船票价格的中位数 , 存储到 fare 列表中
        for f in range(0, 3):
            fare[f] = df.loc[df.Pclass == f + 1, 'Fare'].dropna().median()
        # 循环将 fare 列表中的船票价格添加到相应舱位的、 船票价格缺失的
        for f in range(0, 3):
            df.loc[(df.Fare.isnull()) & (df.Pclass == f + 1), 'Fare'] = fare[f]


    # Age 年龄特征处理 , 使用随机森林策略预测年龄
    df_for_age = df[['Age', 'Survived', 'Fare', 'Parch', 'SibSp', 'Pclass']]
    age_exist = df_for_age.loc[(df.Age.notnull())]   # 年龄不缺失的数据 , 作为训练集
    age_null = df_for_age.loc[(df.Age.isnull())]     # 年龄缺失的数据 , 作为真实的输入数据
    
    x = age_exist.values[:, 1:] # 训练集输入变量
    y = age_exist.values[:, 0]  # 训练集输出变量
    
    rfr = RandomForestRegressor(n_estimators=1000) # 生成 1000 棵树的随机森林对年龄进行预测
    rfr.fit(x, y) 
    age_hat = rfr.predict(age_null.values[:, 1:])

    df.loc[(df.Age.isnull()), 'Age'] = age_hat


    # Embarked 出发城市特征处理 , 使用众数填充出发城市缺失值后将
    df.loc[(df.Embarked.isnull()), 'Embarked'] = \
        df.loc[df.Embarked.notnull(), 'Embarked'].mode().get_values() # …….mode() 返回的是 Series 对象,要使用 get_values()
    
    embarked_df = pd.get_dummies(df.Embarked) 
    embarked_df = embarked_df.rename(columns=lambda x: 'Embarked_' + str(x))
    df = pd.concat([df, embarked_df], axis=1)

    x = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S']]
    y = df['Survived']


    # 扩大数据集数量（变相增加了训练集数目） , x 数据集复制 3 倍 , y 数据集复制 3 倍
    x = np.array(x)
    y = np.array(y)
    x = np.tile(x, (3, 1)) # 列不复制 , 每行复制 3 次
    y = np.tile(y, (3, ))  # 列不复制 , 每行复制 3 次


    return x, y


if __name__ == "__main__":
    
    # 数据录入
    x, y = load_data()

    # 划分训练集 、测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=1)
    
    # 使用 LR 预测 Survived
    lr = LogisticRegression(penalty='l2')
    lr.fit(x_train, y_train)
    y_test_hat = lr.predict(x_test)
    lr_rate = show_accuracy(y_test, y_test_hat)
    
    
    # 使用 RF 预测 Survived
    rfc = RandomForestClassifier(n_estimators=1000)
    rfc.fit(x_train, y_train)
    y_test_hat = rfc.predict(x_test)
    rfc_rate = show_accuracy(y_test, y_test_hat)
    
    # 使用 GBDT 预测 Survived
    gbc = GradientBoostingClassifier()
    gbc.fit(x_train, y_train)
    y_test_hat = gbc.predict(x_test)
    gbc_rate = show_accuracy(y_test, y_test_hat)

    print 'Logistic回归：%f' % lr_rate
    print '随机森林：%f' % rfc_rate
    print 'GBDT：%f' % gbc_rate