
library(ggplot2)
library(rpart)
#install.packages('rattle')
#install.packages('rpart.plot')
#install.packages('RColorBrewer')
library(rattle)
library(rpart.plot)
library(RColorBrewer)

train <-
  read.csv(file = "../kaggle/house-price/data/train.csv", head = TRUE, sep =
             ",")
test <-
  read.csv(file = "../kaggle/house-price/data/test.csv", head = TRUE, sep =
             ",")

analyseData <- function(){
  str(train)
  # how many NA value for each column
  colSums(sapply(train, is.na))
}

linearRegression <- function() {
  x <- train$LotArea
  y <- train$SalePrice
  relation <- lm(SalePrice ~ LotArea, data = train)
  result <- predict(relation, test)
  
  plot(x, y , abline(lm(y ~ x)))
  return (result)
}

decisionTree <- function() {
  
}
ggplot(train, aes(x=LotArea, y=SalePrice)) + geom_point()
result <- linearRegression()
r <- data.frame(Id = test$Id, SalePrice = result)
write.csv(r, file="~/tmp/house-price.csv", row.names = FALSE)




