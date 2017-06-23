
flights <- fread("data/flights14.csv")

# Get all the flights with “JFK” as the origin airport in the month of June.
flights[origin == "JFK" & month == 6L]

# Get the first two rows from flights.
flights[1:2]

# Sort flights first by column origin in ascending order, and then by dest in descending order
flights[order(origin, -dest)]

# Select arr_delay column, but return it as a vector.
flights[, arr_delay]

# Select arr_delay column, but return as a data.table instead.
flights[, list(arr_delay)]

# Select both arr_delay and dep_delay columns.
flights[, .(arr_delay, dep_delay)]

# Select both arr_delay and dep_delay columns and rename them to delay_arr and delay_dep.
flights[, .(delay_arr = arr_delay, delay_dep = dep_delay)]

# How many trips have had total delay < 0?
flights[, sum((arr_delay + dep_delay) < 0)]

# Calculate the average arrival and departure delay for all flights with “JFK” as the origin airport in the month of June.
flights[origin == "JFK" & month == 6L, .(m_arr = mean(arr_delay), m_dep = mean(dep_delay))]

# – How many trips have been made in 2014 from “JFK” airport in the month of June?
flights[origin == "JFK" & month == 6L, length(dest)]

#.N is a special in-built variable that holds the number of observations in the current group. 
#It is particularly useful when combined with by as we’ll see in the next section. 
#In the absence of group by operations, it simply returns the number of rows in the subset.
#So we can now accomplish the same task by using .N as follows:
flights[origin == "JFK" & month == 6L, .N]

# Select both arr_delay and dep_delay columns the data.frame way.
flights[, c("arr_delay", "dep_delay"), with = FALSE]

# How can we get the number of trips corresponding to each origin airport?
flights[, .(.N), by = .(origin)]
# or equivalently using a character vector in 'by'
flights[, .(.N), by = "origin"]

# How can we calculate the number of trips for each origin airport for carrier code “AA”?
flights[carrier == "AA", .N, by = origin]

# How can we get the total number of trips for each origin, dest pair for carrier code “AA”?
flights[carrier == "AA", .N, by = .(origin,dest)]

# How can we get the average arrival and departure delay for each orig,dest pair for each month for carrier code “AA”?
flights[carrier == "AA", .(mean(arr_delay), mean(dep_delay)), by = .(origin, dest, month)]
