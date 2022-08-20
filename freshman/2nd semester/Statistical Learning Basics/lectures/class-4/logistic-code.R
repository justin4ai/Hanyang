install.packages('data.table')

# similar datasets, just use the "Default"
?Credit
?Default

# Always check meaning and domain of data first, to you can recognize inconsistencies.

# balance: The average balance that the customer has remaining on their credit card after making their monthly payment
# default: A factor with levels No and Yes indicating whether the customer defaulted on their debt

# mhm, unconvincing. Search for "default" on the web if it does not ring a bell


# now plot some data and try to model it with linear regression directly:
plot(balance ~ income, Default)
tmp <- subset(Default)#, balance != 0)
plot(balance ~ income, tmp)
plot(balance ~ default, tmp)
plot(income ~ default, tmp)
plot(tmp$balance, as.numeric(tmp$default)-1, ylim=c(-0.3,1.3))

abline(.5, 0, col='red')
abline(lm(I(as.numeric(default)-1) ~ balance, tmp), col="blue")

# no model a logistic regression:
lrmodel <- glm(default ~ balance, tmp, family=binomial)
lines(seq(min(Default$balance), max(Default$balance), len=100),
      predict(lrmodel, newdata=data.frame(balance<-seq(min(Default$balance), max(Default$balance), len=100)), type="response"),
      col='orange')


# how robust are the two approaches to high leverage points?
library(data.table)
tmp <- rbindlist(list(tmp, list("Yes","No",50000.0000000,45000.000)))
#tail(tmp)
abline(lm(as.numeric(default)-1 ~ balance, tmp), col="green")

# ignore warnings: this is due to my strage new values
lrmodel <- glm(default ~ balance, tmp, family=binomial)
lines(seq(min(Default$balance), max(Default$balance), len=100),
      predict(lrmodel, newdata=data.frame(balance<-seq(min(Default$balance), max(Default$balance), len=100)), type="response"),
      col='green')


# here is some illustration of Euler, Binomial distribution and its inverse

exp(1)
x <- seq(-100,100,1)
#plot(x, x/(1+x))
plot(x, exp(1)^x, ylim=c(-1,1))
points(x,exp(1)^x/(1+exp(1)^x), col='blue')
points(x,1/(1+exp(1)^(-x)), col='red')

plot(x,exp(1)^x/(1+exp(1)^x), col='blue', main="relationship of linear regression outputs to probabilities", xlab = "y", ylab='probability')
abline(.5 , 0, col='green')
abline(v=0, col='green')

y <- seq(0,1,0.001)
plot(y, log(y/(1-y)), main="relationship of probabilities to logits", xlab = "probability", ylab='logits')
abline(0 , 0, col='green')
abline(v=0.5, col='green')

x <- seq(-10,10,.1)
p.odds <- exp(1)^x/(1+exp(1)^x)
plot(x,p.odds)
plot(x,p.odds, ylim=c(-6,6))
points(x,log(p.odds/(1-p.odds)), col='red')
# > inverse of the binomial tranform results again in a straight line
