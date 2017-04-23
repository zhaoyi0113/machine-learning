library(dplyr)
library(tidyr)

date <- data.frame('YEAR', 'JAN', 'FEB', 'MAR', 'APR', 
                   'MAY','JUN','JUL','AUG', 'SEP','OCT','NOV','DEC', stringsAsFactors = F)

colnames(date) <- c('YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')

date[1,] <- c(1992, 146913, 147270, 146831, 148082, 149015, 149821, 150809, 151064, 152595 ,153577, 153605, 155504)
#date[2,] <- c(1993, 157525, 156292, 154774, 158996, 160624, 160171, 162832, 162491, 163285, 164711, 166593, 168101)
#date[3,] <- c(1994, 167504, 169652, 172775, 173099, 172340, 174307, 174801, 177289, 178776, 180569, 180695, 181492)

gatheredDate <- gather(date, month, amount, -YEAR)

gatheredDate

restored <- spread(gatheredDate, month, amount)

restored
