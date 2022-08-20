
# comment

# check out help pages for commands
?plot
help(plot)
example(plot)
apropos("plot")

# check out vignettes
vignette()
vignette("grid")
browseVignettes()

ls()
a <- 3
a
b <- c(a, 2, 7, 5)
ls()

b
b[2]
b[2:3]
b[c(2,4)]

newmat <- matrix(data=c(1,2,3,4), nrow=2, ncol=2)
newmat
newmat[2,1]
sqrt(newmat)
newmat[,2]
newmat[,2, drop=F]

mean(b)
var(b)





my_mean <- function(value_list) {
  x <- 0
  for (i in 1:length(value_list)) {
    #print(i)
    x <- x + value_list[i]
  }
  return(x/length(value_list))
} 

my_mean(b)

my_mean

plot

methods(plot)
plot.default


plot(density(rnorm(20, mean=5, sd=1)), ylim=c(0,0.5), xlim=c(1,9))
curve(dnorm(x, mean=5, sd=1), add=TRUE, col='red')

plot(density(rchisq(100, 7)), ylim=c(0,0.2))
curve(dchisq(x, df = 7), from = 0, to = 25, add=TRUE, col='red')

x <- c()
for (i in 1:1000) {
  x <- c(x, mean(rchisq(100, 7)))
}
plot(density(x))     
curve(dnorm(x, mean=7, sd=.35), add=TRUE, col='red')


x <- seq(1,10)
y <- seq(11,20)
plot(x,y)

#z <- outer(x,y,function (x,y)cos(y)/(1+x^2))
#contour(x,y,z)
#fa=(z-t(z))/2
#contour(x,y,fa)
#image(x,y,fa)
#persp(x,y,fa)

library(ISLR)
?Wage

summary(Wage)
is.data.frame(Wage)
names(Wage)
?data.frame

Wage$race
Wage$year
Wage$education

#lm(wage~year+age,data=Wage)
#lm_wage <- lm(wage ~ age, data = Wage)
#new <- data.frame(age = c(40, 60, 70))
#wage_pred <- predict(lm_wage, new)
plot(Wage$wage ~ Wage$age)
#points(c(40, 60, 70), wage_pred, col = "red", pch=20, cex=2)
plot(Wage$wage ~ Wage$year)
#abline(lm(wage~year,data=Wage)$coefficients, col='blue')
abline(lm(wage~year,data=Wage), col='blue')
plot(Wage$wage ~ Wage$education, col=rainbow(5))
boxplot(Wage$wage ~ Wage$education, col=rainbow(5))
boxplot(Wage$wage ~ Wage$education, col=rainbow(5), ylab="wages", xlab="education")
?boxplot
?par
par(mfrow=c(2,1))
hist(Wage$wage)
boxplot(Wage$wage ~ Wage$education, col=rainbow(5), ylab="wages", xlab="education")
par(mfrow=c(1,1))

# median
# upper/lower extreme whisker
# outliers

# exercises
plot(Wage$wage, Wage$age)
plot(Wage$wage, Wage$age, col=c("red","blue","green","yellow","black")[Wage$education])
legend(x="topright", legend = levels(Wage$education), col=c("red","blue","green","yellow","black"), pch=1)
