install.packages("RGtk2")
install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')

library(rpart)
library(rpart.plot)
library(RColorBrewer)

data <- read.csv("../titanic/data/train.csv")
summary(data)

summary(data$Sex)

str(data)

prop.table(table(data$Survived))

table(data$Survived)
prop.table(table(data$Survived),1)

table(data$Sex, data$Survived)
prop.table(table(data$Sex, data$Survived),1)

fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
             data=data,
             method="class")

fancyRpartPlot(fit)
