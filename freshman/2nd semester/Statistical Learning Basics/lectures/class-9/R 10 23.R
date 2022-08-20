install.packages('tree')
library(tree)
library(ISLR)
summary(Carseats)

hist(Carseats$Sales)

High <- ifelse(Carseats$Sales <= 8, "No", "Yes")

newdata <- data.frame(cbind(Carseats, as.factor(High)))

names(newdata)[12] <- 'High'

newdata
nrow(newdata)

tree.carseats <- tree(High ~. -Sales, newdata)

summary(tree.carseats)
plot(tree.carseats) #overfit
text(tree.carseats, pretty=1)


indices <- sample(1:nrow(Carseats), 250)
Carseats.test <- newdata[-indices,]

tree.carseats <- tree(High ~ .-Sales, newdata, subset=indices)

tree.pred <- predict(tree.carseats, Carseats.test, type="class")

#confusion matrix
table(data.frame(pred=tree.pred, true= Carseats.test$High))

?cv.tree
prune.misclass
# prune - 10 fold
cv.carseats <- cv.tree(tree.carseats, FUN=prune.misclass)
cv.carseats

plot(cv.carseats)

# prune the full data tree
prune.carseats <- prune.misclass(tree.carseats, best=15)
plot(prune.carseats)


# do the test data prediction with the pruned model
tree.pred <- predict(prune.carseats, Carseats.test, type = 'class')
table(tree.pred, Carseats.test$High)

