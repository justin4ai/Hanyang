################
# Exerc 1
#
# Calculate manually simple linear regressions and compare to the output of lm
#

library(MASS)

beta <- function(y,x) {
  x_mean <- mean(x)
  y_mean <- mean(y)
  beta_1 <- sum((x-x_mean) * (y-y_mean)) / sum((x-x_mean)^2)
  beta_0 <- y_mean - beta_1*x_mean
  return(c(beta_1, beta_0))
}
  
beta(Boston$medv, Boston$lstat)
beta(Boston$medv, Boston$rm)

lm1 <- lm(medv ~ lstat, Boston)
lm2 <- lm(medv ~ rm, Boston)

lm1$coefficients
lm2$coefficients

plot(medv ~ lstat, Boston)
abline(lm1$coeff, col='red')

plot(medv ~ rm, Boston)
abline(lm2$coeff, col='red')

summary(lm1)
summary(lm2)



################
# Exerc 2
#
#
# calculate confidence intervals

my.confInt <- function(x){
  my.n <- length(x)
  my.mean <- mean(x)
  #my.SE <- sqrt(sum( (x-my.mean)^2 )/(my.n-1))/sqrt(my.n)
  my.SE <- sd(x)/sqrt(my.n)
  #print(my.mean)
  #print(my.SE)
  my.confInt <- c((my.mean-2*my.SE), my.mean, my.mean+2*my.SE)
  return(my.confInt)
}
my.sample <- rnorm(100)

my.confInt(my.sample)

t.test(my.sample)$conf.int
t.test(my.sample)$stderr
t.test(my.sample)$estimate
#
t.test(my.sample)$estimate+2*t.test(my.sample)$stderr
t.test(my.sample)$estimate-2*t.test(my.sample)$stderr

plot(my.confInt(my.sample))



#
# now do it 10 times and plot
#

my.confIntPlot <- function(x){
  my.n <- length(x)
  my.mean <- mean(x)
  my.SE <- sqrt(sum( (x-my.mean)^2 )/(my.n-2))  / sqrt(my.n)
  #my.SE <- sqrt(sum( (x-my.mean)^2 )/(my.n-1))/sqrt(my.n)
  #my.set <- tmp <- t.test(x)$conf.int
  return(c(my.mean, my.SE))
}

#install.packages('psych')
library(psych)


my.means <- c()
my.ses <- c()
for (i in c(1:10)) {
  x <- my.confIntPlot(rnorm(100, mean=0))
  my.means <- c(my.means, x[1])
  my.ses <- c(my.ses, 1.96*x[2])
}
my.stats <- data.frame(mean=my.means,se=my.ses)#,n=rep(100,10))
error.bars(stats=my.stats,main="data with confidence intervals", eyes=FALSE, ylim=c(-1,1), ylab='', xlab='sample no.')
abline(0,0, col='blue')
#points(1,0.01192274, col='red')

################
# Exerc 3
# 
# 
# 
# plot error when using n instead of n-1
ex3 <- function(){
  x <- rnorm(20)
  e <- rnorm(20,m=0, sd=2)
  y <- 2*x+e
  return(data.frame(x,y))
}
currentRSE <- 0
overallRSE <- 0
currentSD <- 0
overallSD <- 0
plot(1, type='n', xlim=c(0,100), ylim=c(1,3), ylab="true standard variation")
abline(2,0, col="red")
for (i in 1:1000) {
  #print(paste(currentRSE,overallRSE,i))
  sampleLM <- lm(y~x, ex3())
  currentRSE <- summary(sampleLM)$sigma 
  overallRSE <- overallRSE*(1-(1/i)) + (1/i)*currentRSE
  currentSD <- sqrt(sum(summary(sampleLM)$resid^2)/20)
  overallSD <- overallSD*(1-(1/i)) + (1/i)*currentSD
  points(i,overallRSE, col="blue")
  points(i,overallSD)
  abline(4,0, col="red")
}



