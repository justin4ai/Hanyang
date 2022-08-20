library(ISLR)
Auto
colnames(Auto)
weight <- Auto$weight
horsepower <- Auto$horsepower

h_w.lm <- lm(weight~horsepower, Auto)
summary(h_w.lm)

plot(horsepower, weight)
abline(h_w.lm$coefficients, col = 'red')


####method 1

predict(h_w.lm, newdata=data.frame(horsepower=73))

####method 2
coef(h_w.lm)
print(984.50033 + 19.07816*73)

####confidence
predict(h_w.lm, newdata=data.frame(horsepower=c(73)), interval="confidence")


####prediction
predict(h_w.lm, newdata=data.frame(horsepower=c(73)), interval="prediction")


##plot
plot(horsepower, weight, ylab = 'weight', xlab = 'horsepower')
abline(h_w.lm$coefficients, col = 'red')


par(mfrow=c(2,2))
plot(h_w.lm)
