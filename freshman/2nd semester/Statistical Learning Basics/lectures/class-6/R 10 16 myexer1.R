library(ISLR)
library(boot)

lm.fit <- lm(mpg~horsepower, data = Auto)
lm.fit$coefficients
true_beta0 <- lm.fit$coefficients[1]
true_beta1 <- lm.fit$coefficients[2]

nrow(Auto)


#draw samples
train <- sample(nrow(Auto), size=100)
forboot.fit <- lm(mpg~horsepower, data=Auto, subset=train)
forboot.fit$coefficients


intercept_sum = c()
slope_sum = list()

for (i in 1:1000){
  train <- sample(nrow(Auto), size=392) # Use same size of the original sample
  forboot.fit <- lm(mpg~horsepower, data=Auto, subset=train)
  intercept_sum <- append(intercept_sum, forboot.fit$coefficients[1])
  slope_sum <- append(slope_sum, forboot.fit$coefficients[2])
}
intercept_mean <- mean(intercept_sum)
slope_mean <- mean(slope_sum)

#about 1000 times manual bootstrap
intercept_mean
slope_mean

#about true values
true_beta0
true_beta1
