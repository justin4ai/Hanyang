library(ISLR)

plot(balance~income, Default)
tmp <- subset(Default, balance != 0)
plot(balance ~ income, tmp)
plot(balance~default, tmp)
plot(income ~ default, tmp)
plot(tmp$balance, as.numeric(tmp$default)-1, ylim=c(-0.3,1.3))

abline(0.5, col='red')
#abline()

exp(1)
x <- seq(-100,100,1)
plot(x, exp(1)^x, ylim=c(-1,1))
points(x, exp(1)^x/(1+exp(1)^x), col = 'blue')
points(x, 1/(1+exp(1)^(-x)), col = 'red')

tmp <- subset(Default, balance != 0)
plot(tmp$balance, as.numeric(tmp$default)-1, ylim=c(-0.3,1.3))

lrmodel <- glm(default ~ balance, tmp, family=binomial)

lines(seq(min(Default$balance), max(Default$balance),len = 100), predict(lrmodel, newdata=data.frame(balance<- seq(min(Default$balance), max(Default$balance)), col = 'orange')

                                                                         
