library('ggplot2')

weather <- read.csv("./data/Beijing_2016_HourlyPM25_created20170201.csv", header = TRUE)
weather <- weather[-c(1)]
weather <- weather[-(1:2),]
colnames(weather) <- as.character(unlist(weather[1,]))
weather <- weather[-(1),]

weather <- transform(weather, D = paste(weather$Year,weather$Day, weather$Hour))
head(weather)

ggplot(weather, aes(Value, Year)) + geom_area()

