library(ISLR)
library(dplyr)
library(e1071)

Smarket

set.seed(1)
x = matrix(rnorm(200*2), ncol=2)
x
x[1:100,] = x[1:100,]+2
x[101:150,] = x[101 : 150,]-2
x
y = c(rep(1,150),rep(2,50))
dat = data.frame(x = x, y = as.factor(y))

dat

plot(x , col=y)

train = sample(200, 100)
svmfit = svm (y~x.1+x.2, data= dat[train,], kernel = 'radial', gamma = 1, cost = 1)
plot(svmfit, dat[train,])

summary(svmfit)

svmfit = svm (y~x.1+x.2, data= dat[train,], kernel = 'radial', gamma = 1, cost = 1e5)
plot(svmfit, dat[train,])

table(true=dat[-train,"y"], pred=predict(svmfit, newdata = dat[-train,]))

?svm
