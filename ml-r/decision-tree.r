if(!require("RGtk2")){
  install.packages("RGtk2", repos="http://cran.us.r-project.org")
}
#
if(!require("rattle")){
  install.packages('rattle', repos="http://cran.us.r-project.org")
}
#
if(!require("rpart.plot")){
  install.packages('rpart.plot', repos="http://cran.us.r-project.org")
}
#
if(!require("RColorBrewer")){
  install.packages('RColorBrewer', repos="http://cran.us.r-project.org")
}
#

library(RGtk2)
library(rattle)
library(rpart)
library(rpart.plot)
library(RColorBrewer)

data <- read.csv("../titanic/data/train.csv")
summary(data)

summary(data$Sex)

str(data)

prop.table(table(data$Survived))

table(data$Survived)
prop.table(table(data$Survived), 1)

table(data$Sex, data$Survived)
prop.table(table(data$Sex, data$Survived), 1)

fit <- rpart(Survived ~ Pclass +
    Sex +
    Age +
    SibSp +
    Parch +
    Fare +
    Embarked,
data = data,
method = "class")

fancyRpartPlot(fit)
