#!/usr/bin/env Rscript
library(ggplot2)
library(ggmap)

house <- read.csv(file="./data/Rgraphics/dataSets/landdata-states.csv",head=TRUE,sep=",")

head(house)
nrow(house)

data <- read.csv(file="./data/assignment-02-data.csv")
ggplot(house, aes(Home.Value, Land.Value)) + geom_point()


#Sys.sleep(3)
head(data)
ggplot(data, aes(longitude, longitude, col=site)) + geom_point()

nyc <- c(lon = -123.2620, lat = 44.5646)
nyc_map <- get_map(location=nyc, zoom=10, scale=1)
ggmap(nyc_map)

corvallis <- c(lon = -143.515, lat = -11.5646)

# Get map at zoom level 5: map_5
map_5 <- get_map(corvallis, zoom = 5, scale = 1)

# Plot map at zoom level 5
ggmap(map_5)

# Get map at zoom level 13: corvallis_map
corvallis_map <- get_map(corvallis, zoom = 13, scale = 1)

# Plot map at zoom level 13
ggmap(corvallis_map) + geom_point(aes(longitude, longitude), data=data)

