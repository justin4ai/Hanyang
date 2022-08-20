# Multiple linear regression!

plot(sales~TV, ads_data)
plot(sales~radio, ads_data)
plot(sales~newspaper, ads_data)

lm1.fit <- lm(sales~TV, ads_data)
summary(lm1.fit)

summary(lm(sales~TV, ads_data))
summary(lm(sales~radio, ads_data))
summary(lm(sales~newspaper, ads_data))

# 1. Is there a relationship between the response and predictors?
  
summary(lm(sales~TV+radio+newspaper, ads_data))
cor(ads_data[,c(2:4)])

# 2. Which predictors are relevant?
step(lm(sales~TV+radio+newspaper, ads_data), scope=(sales ~ 1), direction="backward")
step(lm(sales~1, ads_data), scope=(sales ~ TV+radio+newspaper), direction="forward")

# 3. How good is the model predicting the data?
summary(lm(sales~TV+radio, ads_data))
summary(lm(sales~TV+radio+newspaper, ads_data))

# 4. How accurate is the model
confint(lm(sales~TV+radio, ads_data), level=0.95)

# 5. Is the relationship linear?
plot(ads_data$TV, ads_data$sales, ylab="sales", xlab="TV", col="red")
abline(lm(sales ~ TV, ads_data), col="blue")
newInt <- lm(sales ~ I(sqrt(TV)), ads_data)$coeff[1]
newSlope <- lm(sales ~ I(sqrt(TV)), ads_data)$coeff[2]
lines(0:300, newInt+sqrt(0:300)*newSlope, col="brown")

summary(lm(sales~sqrt(TV)+radio, ads_data))



# 6. Is there synergy among the advertising media?
#summary(lm(sales~TV+radio+TV:radio, ads_data))
#summary(lm(sales~TV*radio, ads_data))


summary(lm(sales~sqrt(TV)+radio+TV:radio, ads_data))

anova(lm(sales~sqrt(TV)+radio, ads_data),
      lm(sales~sqrt(TV)+radio+TV:radio, ads_data))




# nonlinearity
plot(ads_data$TV, ads_data$sales, ylab="sales", xlab="TV", col="red")
abline(lm(sales ~ TV, ads_data), col="blue")
#
newInt <- lm(sales ~ I(sqrt(TV)), ads_data)$coeff[1]
newSlope <- lm(sales ~ I(sqrt(TV)), ads_data)$coeff[2]
lines(0:300, newInt+sqrt(0:300)*newSlope, col="brown")


library(ISLR)

plot(mpg~horsepower, Auto)
abline(lm(mpg~horsepower, Auto), col="orange")

minMax = range(Auto$horsepower)
xVals = seq(minMax[1], minMax[2], len = 100)
lines(xVals,predict(lm(mpg~horsepower+I(horsepower^2), Auto), newdata = data.frame(horsepower = xVals)), col="blue")
lines(xVals,predict(lm(mpg~horsepower+I(horsepower^2)+I(horsepower^3)+I(horsepower^4)+I(horsepower^5), Auto), newdata = data.frame(horsepower = xVals)), col="green")

anova(lm(mpg~horsepower, Auto),
      lm(mpg~horsepower+I(horsepower^2), Auto), 
      lm(mpg~horsepower+I(horsepower^2)+I(horsepower^3)+I(horsepower^4)+I(horsepower^5), Auto)
)




# non-linearity
plot(lm(mpg~horsepower, Auto))
plot(lm(mpg~horsepower+I(horsepower^2), Auto))


fit4 <- lm(mpg ~ cylinders + horsepower + weight, Auto)
plot(fit4$fitted.values, Auto$mpg)

# plot multiple lines for categorical variables

