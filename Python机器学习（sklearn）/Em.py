# coding:utf-8

from __future__ import division
import numpy as np
from scipy.stats import norm

if __name__ == "__main__":
    # 第一个高斯分布均值为 0 方差为 1
    mu1 = (1.72)
    cov1 = (0.3)
    data1 = np.random.normal(mu1, cov1, 300)
    # 第二个高斯分布均值为 5 方差为 1
    mu2 = (1.65)
    cov2 = (0.5)
    data2 = np.random.normal(mu2, cov2, 200).T

    # 将两个高斯分布数据拼接到一起
    data = np.hstack((data1, data2))

    '''以下步骤就是 EM 算法了'''

    # 指定初始参数
    pai = 0.5

    mu1hat = np.random.random(size=1) + 1 # 均值 , random() 函数返回一个 [0, 1) 的随机数
    cov1hat = np.random.random(size=1)    # 标准差
    mu2hat = np.random.random(size=1) + 1
    cov2hat = np.random.random(size=1)

    for i in range(100):

        # E 步骤
        norm1 = norm(mu1hat, cov1hat) # 提供均值 , 标准差
        norm2 = norm(mu2hat, cov2hat) # 返回的 norm 函数就能够调用 PDF 函数

        tau1 = pai * norm1.pdf(data)
        tau2 = (1-pai) * norm2.pdf(data)

        gamma1 = tau1/(tau1 + tau2)   # 这里面的 "/" 要使用 from __future__ import division
        gamma2 = tau2/(tau1 + tau2)   # 否则会省略小数部分

        # M 步骤
        N1 = sum(gamma1)
        N2 = sum(gamma2)

        mu1hat = np.dot(gamma1, data.T)/N1
        mu2hat = np.dot(gamma2, data.T)/N2

        cov1hat = np.sqrt(np.dot(gamma1 * (data - mu1hat).T, data - mu1hat)/N1) # 这里返回的是方差 , 所以需要
        cov2hat = np.sqrt(np.dot(gamma2 * (data - mu2hat).T, data - mu2hat)/N2) # np.sqrt() 得到标准差

        pai = N1/len(data)


    print pai
    print mu1hat, mu2hat   # 计算结果能够将两个高斯分布分开
    print cov1hat, cov2hat








