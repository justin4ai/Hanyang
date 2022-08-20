library(ISLR)
summary(Hitters)
clean.data <- na.omit(Hitters)
install.packages('leaps')
library(leaps)
subset.fit <- regsubsets(Salary ~ ., clean.data, nvmax=19)
summary(subset.fit)
names(summary(subset.fit)) #AIC는 cp의 일부
plot(subset.fit, scale='Cp')
plot(summary(subset.fit)$cp, ylab='cp', xlab='no. of predictors')
coef(subset.fit, 10)
library(stats)

forward.fit <- regsubsets(Salary ~ ., clean.data, nvmax=19, method='forward')
summary(forward.fit)

test.ind <- sample(nrow(clean.data), nrow(clean.data)/5)

test.data <- clean.data[test.ind,]
train.data <- clean.data[-test.ind,]

forward.fit <- regsubsets(Salary ~ ., train.data, nvmax=19, method='forward')

# predict test for all 19 forward models

test.mat <- model.matrix(Salary ~., data=test.data)
test.mat

mse.list = c()

for (i in 1:19){
  this.coef <- coef(forward.fit, id=i)
  predictions <- test.mat[,names(this.coef)]%*%this.coef
  mse.list <- c(mse.list, (mean(test.data$Salary - predictions)^2))
}

mse.list
which.min(mse.list)
