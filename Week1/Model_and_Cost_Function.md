# 模型表示、参数学习

### 模型

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

![1544585031516](C:\Users\Andy_Liu\AppData\Roaming\Typora\typora-user-images\1544585031516.png)

