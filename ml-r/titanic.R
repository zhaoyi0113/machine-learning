library(rpart)
install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)

train <- read.csv(file="../titanic/data/train.csv",head=TRUE,sep=",")
head(train)
str(train)
train$Survived
table(train$Survived)
prop.table(table(train$Survived))
fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
             data=train,
             method="class")
plot(fit)
text(fit)
fancyRpartPlot(fit)
