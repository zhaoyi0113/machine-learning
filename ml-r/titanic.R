library(rpart)
install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)

train <- read.csv(file="../titanic/data/train.csv",head=TRUE,sep=",")
nrow(train)
head(train)
str(train)
train$Survived
table(train$Survived)
prop.table(table(train$Survived))

prop.table(table(train$Sex, train$Survived))
prop.table(table(train$Sex, train$Survived),1)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
             data=train,
             method="class")
plot(fit)
text(fit)
fancyRpartPlot(fit)

test <- read.csv(file="../titanic/data/test.csv")

Predition <- predict(fit, test, type = "class")
submit <- data.frame(PassengerId = test$PassengerId, Survived = Predition)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
             data=train,
             method="class", 
             control=rpart.control(minsplit=2, cp=0))
Predition <- predict(fit, test, type = "class")
submit <- data.frame(PassengerId = test$PassengerId, Survived = Predition)


test$Survived <- rep(0, 418)
test$Survived[test$Sex == 'female'] <- 1


aggregate(Survived ~ Child + Sex, data=test, FUN=sum)

train$Fare2 <- '30+'
train$Fare2[train$Fare < 30 & train$Fare >= 20] <- '20-30'
train$Fare2[train$Fare < 20 & train$Fare >= 10] <- '10-20'
train$Fare2[train$Fare < 10] <- '<10'

aggregate(Survived ~ Fare2 + Pclass + Sex, data=train, FUN=function(x) {sum(x)/length(x)})

test$Survived <- 0
test$Survived[test$Sex == 'female'] <- 1
test$Survived[test$Sex == 'female' & test$Pclass == 3 & test$Fare >= 20] <- 0



submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived)
write.csv(submit, file = "~/tmp/theyallperish.csv", row.names = FALSE)
