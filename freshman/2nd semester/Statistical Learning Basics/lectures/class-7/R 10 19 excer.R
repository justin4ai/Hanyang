library(ISLR)
library(dplyr)
glimpse(Hitters)
names(Hitters)
dim(Hitters)
mydata <- na.omit(Hitters)

library(leaps)
regfit.full = regsubsets(Salary ~ . , mydata)
summary(regfit.full)
regfit.full = regsubsets(Salary~., data=mydata, nvmax=19)
reg.summary = summary(regfit.full)
names(reg.summary)
reg.summary$rsq ##R squared

par(mfrow=c(2,2))

###RSS와 Adjusted R2의 그래프 및 최대값
plot(reg.summary$rss, xlab="Number of Variables", ylab="RSS", type="l")
plot(reg.summary$adjr2, xlab="Number of Variables", ylab="adjr2", type="l")

which.max(reg.summary$adjr2)
points(11, reg.summary$adjr2[11], col='red', cex=2,pch=20)
###

###Cp랑 BIC도 그래프 및 최소값 똑같이 구할 수 있음.

plot(regfit.full)

par(mfrow=c(2,2))
plot(regfit.full, scale='r2')
plot(regfit.full, scale='adjr2')
plot(regfit.full, scale='Cp')
plot(regfit.full, scale='bic')
### 각 그래프의 맨 위쪽 행은 최적의 모델을 따라 선택된 각 변수에 대한 검은색 사각형
### 예를 들어, 몇 개의 모델은 -150에 가까운 BIC 가짐. 하지만 가장 낮은 BIC는 6변수 모델델

coef(regfit.full, 6)

regfit.fwd = regsubsets(Salary~.,data=mydata,nvmax=19,method='forward')
regfit.bwd = regsubsets(Salary~.,data=mydata,nvmax=19,method='backward')
summary(regfit.bwd)

coef(regfit.full,7)
coef(regfit.fwd,7)
coef(regfit.bwd,7)



#####Validation (and cross validation)
set.seed(1)
train=sample(c(TRUE,FALSE), nrow(mydata),rep=TRUE)
test=(!train)

#훈련셋에 적용하여 최상의 서브셋 선택

regfit.best=regsubsets(Salary~.,data=mydata[train,],nvmax=19)
#검정 데이터로부터 모델 행렬
test.mat=model.matrix(Salary~.,data=mydata[test,])

val.errors = rep(NA,19)
#크기 i의 최고 모델에 대한 계수를 .best에서 추출하고 검정모델 행렬의 적절한 열에
#곱하여 예측값 구한 뒤 검정 MSE 계산산
for(i in 1:19){
  coefi=coef(regfit.best,id=1)
  pred=test.mat[,names(coefi)]%*%coefi
  val.errors[i]=mean((mydata$Salary[test]-pred)^2)
}

val.errors
which.min(val.errors)
coef(regfit.best,1)

#나중을 위하여
predict.regsubsets = function(object,newdata,id,...){
  form=as.formula(object$call[[2]])
  mat=model.matrix(form,newdata)
  coefi=coef(object,id=id)
  xvars=names(coefi)
  mat[,xvars]%*%coefi
}

#이번엔 훈련셋 아닌 전체자료에서 뽑기
regfit.best = regsubsets(Salary~.,data=mydata,nvmax=19)
coef(regfit.best,1)


k=10
set.seed(2)
folds=sample(1:k,nrow(mydata),replace=TRUE)
cv.errors=matrix(NA,k,19, dimnames=list(NULL, paste(1:19)))

for(j in 1:k){
  best.fit=regsubsets(Salary~.,data=mydata[folds!=j,],nvmax=19)
  for(i in 1:19){
    pred=predict(best.fit,mydata[folds==j,],id=i)
    cv.errors[j,i]=mean((mydata$Salary[folds==j]-pred)^2)
  }
}

#10 X 19행렬 나오는데, 원소 (i,j)는 i번째 cross fold와 최고의 j변수 모델에 대한 검정 MSE

mean.cv.errors = apply(cv.errors,2,mean)
mean.cv.errors
par(mfrow=c(1,1))
plot(mean.cv.errors,type='b')

reg.best=regsubsets(Salary~.,data=mydata,nvmax=19)
coef(reg.best,10)
