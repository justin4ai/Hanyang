library(MASS)
lm.result <- lm(medv ~ lstat, Boston)
lm(medv ~ rm, Boston)

plot(medv ~ lstat, Boston)
abline(coefficients(lm.result), col='red')
abline(lm.result$coefficients, col='blue')

x <- Boston$lstat
y <- Boston$medv

x_bar <- mean(x)
y_bar <- mean(y)
my_varx <- sum((x-x_bar)^2)/(length(x)-1)

my_slope(x,y)
my_intercept(x,y,-.96)

my_slope <- function(x,y) {
  x_bar <- mean(x)
  y_bar <- mean(y)
  my_varx <- sum((x-x_bar)^2)/(length(x)-1)
  print(paste("var x: ", var(x), my_varx))
  my_vary <- sum((y-y_bar)^2)/(length(y)-1)
  print(paste("var y: ", var(y), my_vary))
  my_numerator <- sum((x-x_bar)*(y-y_bar))
  my_nominator <- sum((x-x_bar)^2)
  print(paste("slope: ", my_numerator / my_nominator))
}
my_intercept <- function(x,y,slope) {
  x_bar <- mean(x)
  y_bar <- mean(y)
  print(paste("intercept: ", y_bar - x_bar*slope))
}
library(MASS)
my_slope(Boston$rm,Boston$medv)
my_intercept(Boston$rm,Boston$medv,9.10210898118031)

# compare to lm()
lm(medv ~ rm, Boston)


library(ISLR)
#http://faculty.marshall.usc.edu/gareth-james/ISL/Advertising.csv
ads_data <- as.data.frame(read.csv('../material/Advertising.csv'))

plot(ads_data$TV, ads_data$sales, ylab="sales", xlab="TV", col="red")
abline(lm(sales ~ TV, ads_data), col="blue")

newInt <- lm(sales ~ I(sqrt(TV)), ads_data)$coeff[1]
newSlope <- lm(sales ~ I(sqrt(TV)), ads_data)$coeff[2]
lines(0:300, newInt+sqrt(0:300)*newSlope, col="orange")


# OLS
plot(ads_data$TV-mean(ads_data$TV), ads_data$sales-mean(ads_data$sales), ylab="sales", xlab="TV", col="red")
plot(ads_data$TV, ads_data$sales, ylab="sales", xlab="TV", col="red")

my_slope <- function(x,y) {
  x_bar <- mean(x)
  y_bar <- mean(y)
  my_varx <- sum((x-x_bar)^2)/(length(x)-1)
  print(paste("var x: ", var(x), my_varx))
  my_vary <- sum((y-y_bar)^2)/(length(y)-1)
  print(paste("var y: ", var(y), my_vary))
  my_numerator <- sum((x-x_bar)*(y-y_bar))
  my_nominator <- sum((x-x_bar)^2)
  print(paste("slope: ", my_numerator / my_nominator))
}
my_intercept <- function(x,y,slope) {
  x_bar <- mean(x)
  y_bar <- mean(y)
  print(paste("intercept: ", y_bar - x_bar*slope))
}
my_slope(ads_data$TV, ads_data$sales)
my_intercept(ads_data$TV, ads_data$sales, 0.0475366404330197)

lm(sales ~ TV, ads_data)$coeff






# assessing accuracy
population <- function(x){
  return(2+3*x+rnorm(length(x), sd=1))
}




samples <- rnorm(100)
sample_y <- population(samples)
plot(samples, sample_y)
abline(2,3, col="red")
abline(lm(sample_y ~ samples, data.frame(sample_y, samples)), col='blue')

samples2 <- rnorm(100)
sample_y2 <- population(samples2)
abline(lm(sample_y2 ~ samples2, data.frame(sample_y2, samples2)), col='blue')


# t and p
x <- seq(-4, 4, length=100)
hx <- dnorm(x)

degf <- c(1, 3, 8, 30)
colors <- c("red", "blue", "darkgreen", "gold", "black")
labels <- c("df=1", "df=3", "df=8", "df=30", "normal")

plot(x, hx, type="l", lty=2, xlab="x value",
     ylab="Density", main="Comparison of t Distributions")

for (i in 1:4){
  lines(x, dt(x,degf[i]), lwd=2, col=colors[i])
}

legend("topright", inset=.05, title="Distributions",
       labels, lwd=2, lty=c(1, 1, 1, 1, 2), col=colors)




summary(lm(sales~TV, ads_data))


