library(dplyr)
require(dplyr)

employee <- c('John Doe','Peter Gynn','Jolie Hope')
salary <- c(21000, 23400, 26800)
startdate <- as.Date(c('2010-11-1','2008-3-25','2007-3-14'))

employ <- data.frame(employee, salary, startdate)

head(employ)

# add a new column
employ['Dep'] <- c('1','1','1')
head(employ)
# print total salary for each department
group_by(employ, Dep) %>% summarise(salary = max(salary))
