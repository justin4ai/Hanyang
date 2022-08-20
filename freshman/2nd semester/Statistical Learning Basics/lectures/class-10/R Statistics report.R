library(olsrr)
library(MASS)
library(boot)
library(dplyr)
library(leaps)
glimpse(Boston)
attach(Boston)



ncol(Boston)
regfit.full = regsubsets(medv~., Boston, nvmax = 13)
summary(regfit.full)
reg.summary = summary(regfit.full)
names(reg.summary)
reg.summary$rsq
par(mfrow = c(2,2))
plot(reg.summary$rss , xlab = "Number of Variables" , ylab = "RSS", type="l")
plot(reg.summary$adjr2, xlab="Number of Variables", ylab = "Adjusted RSq", type = "l")
plot(reg.summary$cp , xlab = "Number of Variables" , ylab = "Cp", type="l")
plot(reg.summary$bic, xlab="Number of Variables", ylab = "BIC", type = "l")


which.max(reg.summary$adjr2)
which.min(reg.summary$rss)
which.min(reg.summary$cp)
which.min(reg.summary$bic)


points(11,reg.summary$adjr2[11], col='red', cex=2, pch = 20)
points(13,reg.summary$rss[13], col='red', cex=2, pch = 20)
points(11,reg.summary$cp[11], col='red', cex=2, pch = 20)
points(11,reg.summary$bic[11], col='red', cex=2, pch = 20)

plot(regfit.full, scale="adjr2")
coef(regfit.full, 7)



predict.regsubsets=function(object,newdata,id,...){
  form=as.formula(object$call[[2]])
  mat=model.matrix(form,newdata)
  coefi=coef(object,id=id)
  xvars=names(coefi)
  mat[,xvars]%*%coefi
}



#10 fold validation

k=10
set.seed(1)
folds=sample(1:k,nrow(Boston),replace=TRUE)
cv.errors = matrix(NA,k,13, dimnames = list(NULL, paste(1:13)))




for(j in 1:k){
  best.fit = regsubsets(medv ~ ., data = Boston[folds!=j,], nvmax=13)
  for (i in 1:13){
    pred = predict(best.fit, Boston[folds==j,], id=i)
    cv.errors[j,i]=mean( (Boston$medv[folds==j] - pred)^2)
  }
}

cv.errors

# (i, j)는 i번째 교차검증 fold와 최고의 j 변수 모델에 대한 검정 MSE
mean.cv.errors = apply(cv.errors,2,mean)
mean.cv.errors
par(mfrow=c(1,1))
plot(mean.cv.errors,type='b')

reg.best = regsubsets(medv~. , data= Boston, nvmax=13)
reg.best
reg.summary = summary(reg.best)
reg.summary$adjr2
reg.summary$adjr2[11]
#0.7348

###### glm 모델
glm.fit <- glm(medv~.,data=Boston)
summary(glm.fit)
##### indus랑 age 제외

step(glm.fit,direction = 'backward')

stepfit.glm <- glm(formula = medv ~ crim + zn + chas + nox + rm + dis + rad + 
00                   tax + ptratio + black + lstat, data = Boston)
summary(stepfit.glm)
#0.7348

?regsubsets
?r2



