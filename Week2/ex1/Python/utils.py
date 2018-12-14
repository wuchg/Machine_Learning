
# coding: utf-8

# In[ ]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import cm
from numpy.linalg import inv
from pandas import DataFrame
from mpl_toolkits.mplot3d import Axes3D
import scipy.io as sio

def J(X,y,theta):
    m=X.shape[0]
    cv=sum((X*theta-y).T*(X*theta-y))/2/m
    return  np.around(cv,decimals=2)

def gradientDescent(X,y,alpha,iterations):
    theta=np.zeros((X.shape[1],1))
    m=X.shape[0]
    for i in range(0,iterations):
        theta=theta-np.multiply(alpha/m,X.T*(X*theta-y))
    return np.around(theta,decimals=4)

