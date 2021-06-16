# -*- coding: utf-8 -*-
"""Assignment7.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W6aaWM2usfKC4xcqSVDoNAx3r8HnYnca
"""

import numpy as np
import math

len = 1000
a = []
b = []
t = []
s = []

for i in range(len):
    x = np.random.normal(0.0 , 1.0)
    y = np.random.normal(0.0 , 1.0)
    a.append(x)
    b.append(y)

# Function to find mean.
def mean(k, n):     
    sum = 0
    for i in range(1, n):
        sum = sum + k[i]     
    return sum / n

# Function to find covariance.
def cov(x, y, n): 
    sum = 0
    for i in range(1, n):
        sum = (sum + (x[i] - mean(x, n)) * (y[i] - mean(y, n)))
    return sum / (n - 1)

p = cov(a , b , len) # p = rho(X , Y)

if (p>-1 and p<1):
      print("Theoritical value of rho(X,Y) : -1<p<1" )
      print("Simulated value of rho(X,Y) = ",p)
      print()

# O = X+Y
# L = X-Y
if (p>-1 and p<1):
  for i in range(len):
      o = np.random.normal(0.0 , 2+2*p)
      l = np.random.normal(0.0 , 2-2*p)
      t.append(o)
      s.append(l)

c = cov(t , s , len) 
d = math.sqrt((2+2*p)*(2-2*p))
q = c / d # q = rho(X+Y ,X-y)

print("Theoritical value of rho(X+Y , X-Y) = 0" )
print("Simulated value of rho(X+Y , X-Y) = ",q)