library(ISLR) #for the data
library(MASS) #for the classifier

### 
# fit the model
lda.fit <- lda(default ~ balance, Default)
lda.fit
# plot the distributions
plot(lda.fit)

# subset data if you want to split
testset <- subset(Default, Year=2005)
training.index <- 1:25

Default[training.index, -2]


# use prdict on training data to get the predicted classes
lda.pred <- predict(lda.fit)

# plot the results of the discriminative functions by class
plot(lda.pred$posterior[,1], lda.pred$posterior[,2], col=lda.pred$class)

# create a confusion matrix
table(lda.pred$class, Default$default)

## create it with % instead of counts
number.data <- sum(table(lda.pred$class, Default$default))
table(lda.pred$class, Default$default)/number.data*100
#prop.table(table(lda.pred$class, Default$default))

# how is class encoded?
contrasts(Default$default)

# confusion matrix with labels
class.tab <- table(data.frame(pred=lda.pred$class, true=Default$default))
class.tab

# get F1
precision <- class.tab[2,2] / sum(table(lda.pred$class, Default$default)[2,])
precision
recall <- class.tab[2,2] / sum(table(lda.pred$class, Default$default)[,2])
recall 

F.score <- 2*precision*recall/(precision+recall)
F.score
mean(c(precision,recall))
###


