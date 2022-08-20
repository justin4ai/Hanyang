library(ISLR)
advertise <- as.data.frame(read.csv("Advertising.csv"))
colnames(advertise)
sales <- advertise$sales
TV <- advertise$TV
radio <- advertise$TV
newspaper <- advertise$newspaper

plot(sales~TV, advertise)
plot(sales~radio, advertise)
plot(sales~newspaper, advertise)

lm1.fit <- lm(sales~TV, advertise)
summary(lm1.fit)

# Is there a relationship beteen teh response and predictors?

summary(lm(sales~TV+radio+newspaper, advertise))
cor(advertise[,c(2:4)])

# Which predictors are relevant?

step(lm(sales~TV+radio+newspaper, advertise), scope=(sales ~ 1), direction="backward")
step(lm(sales~1, advertise), scope=(sales~TV+radio+newspaper), direction="forward")

# How good is the model predicting the data?
summary(lm(sales~TV+radio, advertise))
summary(lm(sales~TV+radio+newspaper, advertise))

# How accurate is the model?
confint(lm(sales~TV+radio, advertise), level = 0.95)

# Is the relationship linear? A : nonlinear.
plot(TV, sales, ylab='sales', xlab='TV', col='red')
abline(lm(sales ~ TV, advertise), col='blue')
newInt <- lm(sales~I(sqrt(TV)), advertise)$coeff[1]
newSlope <- lm(sales~I(sqrt(TV)), advertise)$coeff[2]
lines(0:300, newInt+sqrt(0:300)*newSlope, col='magenta')

summary(lm(sales~sqrt(TV)+radio, advertise))

# Is there synergy among the advertising media?
summary(lm(sales~TV+radio+TV:radio, advertise))
#short version : summary(lm(sales~TV*radio, advertise))

anova(lm(sales~sqrt(TV)+radio, advertise),
      lm(sales~sqrt(TV)+radio+TV:radio, advertise))

