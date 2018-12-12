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



### 模型表示

$x^{(i)}$ 表示输入变量（输入特征）；$y^{(i)}$ 表示输出变量（目标变量）。

一对（$x^{(i)}$，$y^{(i)}$） 被称为训练样本；多个训练样本（$x^{(i)}$，$y^{(i)}$）;$i=1,...,m$ 被称为训练数据集。

上标 $^{(i)}$ 表示训练数据集中索引为 $i$ 的训练样本，不是指数。

一般情况，我用 $X$  表示输入空间，用 $Y$ 表示输出空间。

对于监督学习问题，我们的目标是，在给定训练集的情况下，学习函数 $h：X→Y$，使得 $h(x)$ 是 $y$ 的对应值预测函数。我们的目标是在假设空间中选取一个最优的模型 $h(x)$ ，所以我们的模型 $h(x)$ 叫假设函数。

> 课程中说 “由于历史原因，该函数h被称为假设。 For historical reasons, this function h is called a hypothesis. ”



### 成本函数（Cost function）

损失函数(Loss function)是定义在**单个训练样本**上的，也就是就算一个样本的误差，用 L 表示。

成本函数(Cost function)，也叫代价函数，是定义在**整个训练集**上面的，也就是所有样本的误差的总和的平均，也就是损失函数的总和的平均。

![1544580074110](C:\Users\Andy_Liu\AppData\Roaming\Typora\typora-user-images\1544580074110.png)

> 这个方程又称“平方误差函数(Squared error function)” 或者“均值平方误差（Mean squared error）”。 “均值”是一半（1/2m），这方便计算计算梯度下降（gradient descent），平方函数的导数将会抵消 (1/2m)。同样是为了计算的方便，把假设函数的常数看成特征值为1的一个特征，所以 θ 为 n+1 维。



### 参数学习

#### 梯度下降

![1544585031516](C:\Users\Andy_Liu\AppData\Roaming\Typora\typora-user-images\1544585031516.png)

