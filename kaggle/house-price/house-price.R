
library(ggplot2)
library(rpart)
#install.packages('rattle')
#install.packages('rpart.plot')
#install.packages('RColorBrewer')
if(!require('e1071')){
  install.packages('e1071')
}
if(!require('corrplot')){
  install.packages('corrplot')
}
library(rattle)
library(rpart.plot)
library(RColorBrewer)
library(dplyr)
library(e1071)    
library(corrplot)
#load.libraries <- c('data.table', 'testthat', 'gridExtra', 'corrplot', 'GGally', 'ggplot2', 'e1071', 'dplyr')
#install.lib <- load.libraries[!load.libraries %in% installed.packages()]
#for(libs in install.lib) install.packages(libs, dependences = TRUE)
#sapply(load.libraries, require, character = TRUE)

if(!require('data.table')){
  install.packages('data.table')
}
library(data.table)


train <- fread('../kaggle/house-price/data/train.csv',colClasses=c('MiscFeature' = "character", 'PoolQC' = 'character', 'Alley' = 'character'))
test <- fread('../kaggle/house-price/data/test.csv' ,colClasses=c('MiscFeature' = "character", 'PoolQC' = 'character', 'Alley' = 'character'))



linearRegression <- function() {
  x <- train$LotArea
  y <- train$SalePrice
  relation <- lm(SalePrice ~ LotArea, data = train)
  result <- predict(relation, test)
  
  plot(x, y , abline(lm(y ~ x)))
  return (result)
}

analysisData <- function(){
  #str(train);
  colSums(sapply(train, is.na)); # show NA count for each column
  cat('Train has', dim(train)[1], 'rows and', dim(train)[2], 'columns.\n')
  cat('Test has', dim(test)[1], 'rows and', dim(test)[2], ' columns.\n')
  # The percentage of data missing in train.
  sum(is.na(train)) / (nrow(train) *ncol(train))
  # The percentage of data missing in test.
  sum(is.na(test)) / (nrow(test) * ncol(test))
  # Check for duplicated rows.
  cat("The number of duplicated rows are", nrow(train) - nrow(unique(train)))
  
  cat_var <- names(train)[which(sapply(train, is.character))]
  cat_car <- c(cat_var, 'BedroomAbvGr', 'HalfBath', ' KitchenAbvGr','BsmtFullBath', 'BsmtHalfBath', 'MSSubClass')
  
  ####Convert character to factors 
  train[,(cat_var) := lapply(.SD, as.factor), .SDcols = cat_var]
  train_cat <- train[,.SD, .SDcols = cat_var]
  numeric_var <- names(train)[which(sapply(train, is.numeric))]
  train_cont <- train[,.SD,.SDcols = numeric_var]
  doPlots(train_cat, fun = plotHist, ii = 1:4, ncol = 2)
  doPlots(train_cat, fun = plotHist, ii  = 4:8, ncol = 2)
  doPlots(train_cat, fun = plotHist, ii = 8:12, ncol = 2)
  doPlots(train_cat, fun = plotHist, ii = 13:18, ncol = 2)
  doPlots(train_cat, fun = plotHist, ii = 18:22, ncol = 2)
  
  train %>% select(LandSlope, Neighborhood, SalePrice) %>% 
    filter(LandSlope == c('Sev', 'Mod')) %>% arrange(Neighborhood) %>% 
    group_by(Neighborhood, LandSlope) %>% summarize(Count = n()) %>% 
    ggplot(aes(Neighborhood, Count)) + geom_bar(aes(fill = LandSlope), position = 'dodge', stat = 'identity') + theme_light() +theme(axis.text.x = element_text(angle = 90, hjust =1))
  
  train %>% select(Neighborhood, SalePrice) %>% 
    ggplot(aes(factor(Neighborhood), SalePrice)) + 
    geom_boxplot() + theme(axis.text.x = element_text(angle = 90, hjust =1)) + 
    xlab('Neighborhoods')
  
  doPlots(train_cont, fun = plotDen, ii = 2:6, ncol = 2)
  doPlots(train_cont, fun = plotDen, ii = 7:12, ncol = 2)
  doPlots(train_cont, fun = plotDen, ii = 13:17, ncol = 2)
  doPlots(train_cont, fun = plotHist, ii = 18:23, ncol = 2)
  
  
  exploreCorrelation(train_cont);
}

exploreCorrelation <- function(train_cont){
  # Explore the correlation
  correlations <- cor(na.omit(train_cont[,-1, with = FALSE]))
  
  # correlations
  row_indic <- apply(correlations, 1, function(x) sum(x > 0.3 | x < -0.3) > 1)
  
  correlations<- correlations[row_indic ,row_indic ]
  corrplot(correlations, method="square")
}

plot_Missing <- function(data_in, title = NULL){
  temp_df <- as.data.frame(ifelse(is.na(data_in), 0, 1))
  temp_df <- temp_df[,order(colSums(temp_df))]
  data_temp <- expand.grid(list(x = 1:nrow(temp_df), y = colnames(temp_df)))
  data_temp$m <- as.vector(as.matrix(temp_df))
  data_temp <- data.frame(x = unlist(data_temp$x), y = unlist(data_temp$y), m = unlist(data_temp$m))
  ggplot(data_temp) + geom_tile(aes(x=x, y=y, fill=factor(m))) + scale_fill_manual(values=c("white", "black"), name="Missing\n(0=Yes, 1=No)") + theme_light() + ylab("") + xlab("") + ggtitle(title)
}

plotHist <- function(data_in, i) {
  data <- data.frame(x=data_in[[i]])
  p <- ggplot(data=data, aes(x=factor(x))) + stat_count() + xlab(colnames(data_in)[i]) + theme_light() + 
    theme(axis.text.x = element_text(angle = 90, hjust =1))
  return (p)
}

doPlots <- function(data_in, fun, ii, ncol=3) {
  pp <- list()
  for (i in ii) {
    p <- fun(data_in=data_in, i=i)
    pp <- c(pp, list(p))
  }
  do.call("grid.arrange", c(pp, ncol=ncol))
}


plotDen <- function(data_in, i){
  data <- data.frame(x=data_in[[i]], SalePrice = data_in$SalePrice)
  p <- ggplot(data= data) + geom_line(aes(x = x), stat = 'density', size = 1,alpha = 1.0) +
    xlab(paste0((colnames(data_in)[i]), '\n', 'Skewness: ',round(skewness(data_in[[i]], na.rm = TRUE), 2))) + theme_light() 
  return(p)
}

ggplot(train, aes(x=LotArea, y=SalePrice)) + geom_point()
result <- linearRegression()
r <- data.frame(Id = test$Id, SalePrice = result)
#write.csv(r, file="~/tmp/house-price.csv", row.names = FALSE)

plot_Missing(train[,colSums(is.na(train)) > 0, with=FALSE])
# draw remoded hourse and non-remoded hourse
train %>% select(YearBuilt, YearRemodAdd) %>% mutate(Remodeled = as.integer(YearBuilt != YearRemodAdd)) %>% ggplot(aes(x= factor(x = Remodeled, labels = c( 'No','Yes')))) + geom_bar() + xlab('Remodeled') + theme_light()

analysisData()
