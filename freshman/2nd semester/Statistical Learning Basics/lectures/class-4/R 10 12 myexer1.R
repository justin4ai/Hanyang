library(ISLR)
library(dplyr)
glimpse(Smarket)

cor(Smarket[,-9])
plot(Year~Direction,Smarket)
plot(Today~Direction,Smarket)
plot(Volume~Direction,Smarket)

tmp <- subset(Smarket, Today != 0)

plot(tmp$Today, as.numeric(tmp$Direction)-1, ylim = c(-0.3, 1.3))
lrmodel_1 <- glm(Direction ~ Lag1, family=binomial, data=Smarket)
step(lrmodel_1, direction = "backward")

lrmodel$coef
lrmodel$coef[0]
lrmodel$coef[2]
X <- c(factor(Smarket$Volume))
print(X)


training <- subset(Smarket, Year < 2005)
test <- Smarket

lrmodel_2 <- glm(Direction ~ Volume+Lag1+Lag2+Lag3+Lag4+Lag5, family=binomial, data=training)
step(lrmodel_2, direction = "backward")



lrmodel_1$coef

Y <- lrmodel$coef[1] + X*lrmodel$coef[2]
print(Y)
probs <- exp(Y)/(1+exp(Y))

print(length(X))
probs
plot(X, probs, ylim=c(0,1), type = "l", lwd=3, lty=2)
