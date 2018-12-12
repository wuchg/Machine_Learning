# 机器学习

## 定义

机器学习（统计机器学习）是什么？字面意思就是让机器（计算机程序）学习，通过这一过程，可以使自身更加智能化（特别是对未知数据进行预测）。**Herbert A. Simon**  曾对 “学习”  给出以下定义：“如果一个系统能够通过执行某个过程改进它的性能，这就是学习。”  按照这一观点，机器学习就是计算机程序通过运用数据及统计方法来提高系统性能的过程。



## 分类

In general, any machine learning problem can be assigned to one of two broad classifications: **supervised learning** or **unsupervised learning** .

### 监督学习（supervised learning）

> 从一个给定的训练数据集（training data），假设数据是独立同分布产生的；并且假设要学习的模型属于某个函数的集合，称为假设空间；应用某个评价准则，从假设空间中选取一个最优的模型，使它对已知训练数据及未知数据在给定的评价准则下有最优的预测；最优的模型选取由算法实现。李航的《统计学习方法》

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

Supervised learning problems are categorized into "regression" and "classification" problems.

在回归问题中，我们试图在连续输出中预测结果，这意味着我们正在尝试将输入变量映射到某个连续函数。 例如：预测年龄、预测房价、预测玩具的价格...



在分类问题中，我们试图在离散输出中预测结果。 换句话说，我们试图将输入变量映射到离散类别。例如：银行根据你的年龄，是否结婚、是否有房子等信息来决定是否给你贷款。根据电影中的打斗镜头数、接吻镜头数来判别未分类的电影类型（爱情片 or 动作片）,手写数字识别 ...



### 非监督学习（unsupervised learning）

无监督学习使我们能够在很少或根本不知道我们的结果应该是什么样的情况下处理问题。 我们可以从数据中导出结构，我们不一定知道变量的影响。我们可以通过基于数据中变量之间的关系聚类数据来推导出这种结构。在无监督学习的情况下，没有基于预测结果的反馈。例如：收集1000篇关于美国经济的论文集，并找到一种方法将这些论文自动分组为少数几个相似或相关的不同变量，如词频，句子长度，页数等。