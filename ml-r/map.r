my_data <- read_excel("./data/assignment-02-data1.xlsx")

# Q1 Read the data into R
install.packages("readxl")
library(readxl)
str(my_data)

# Q2 Using ggplot2 to show fro each kind of coral and for each site how the bleaching
# varies from year to year
# facet showing the bleaching for one kind of coral at one site across the time period
# The sites should be ordered by latitude
# Fit smoothers to the data
install.packages("ggplot2")
library(ggplot2)

coral <- ggplot(my_data, aes(x = year, y = bleaching)) + geom_jitter()
coral <- coral + facet_grid(latitude + site ~ kind) +  stat_smooth(method = "lm", se = FALSE, col = "red") 
coral

# Q3 Using shiny to create an interactive visualisation.
# Allowing the user to vary the kind of coral display and the choice of smoother
# Read data from xlsx dataset
install.packages("readxl")
library(read)
#my_data = read_excel("/Users/zhengxiao/Documents/TextBooks/2017-S1/FIT5147-Data_exploration_and_visualisation/Assignment/Assignment-03/assignment-02-data.xlsx")

#install.packages("ggplot2")
library(ggplot)
install.packages("shiny")
library(shiny)


# Q4
install.packages("leaflet")
library(leaflet)

library(ggmap)
head(my_data)
mean(my_data$longitude)
mean(my_data$latitude)
corvallis <- c(lon = mean(my_data$longitude), lat = mean(my_data$latitude))
corvallis_map <- get_map(corvallis, zoom = 5, scale = 1)
ggmap(corvallis_map) + geom_point(aes(longitude, latitude), data=my_data)

leaflet(data = my_data) %>% addTiles() %>% 
  addMarkers(~longitude, ~latitude, popup = ~as.character((site)))
