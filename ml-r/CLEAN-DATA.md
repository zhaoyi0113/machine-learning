# Clean Data

The first thing you need to consider after collecting a lot of raw data is to make it clean. As the data go bigger, it will defintely include many dirty data. In order to make data analysis job easier, we need to clean the data first. In fact, data clean is a core step in data science and machine learning. Let go through each methods in data clean specifically in R. This chapter will focus on three topics:
    
    * Exploring raw data
    * Tidying data
    * Preparing data for analysis

In the final part of this chapter, it will put everything together to take the wider data from raw to be ready for analysis.

## Exploring Raw Data

1. ```class``` returns the class of an R object
2. ```dim``` retrieve or set the dimension of an object
3. ```names``` View the column names
4. ```str``` check the structure of an data frame
5. ```glimpse``` use dplyr way to retrieve the data structure.
6. ```smmary``` view the summary of an data object.
7. ```head``` show the first 6 rows  of your data. ```head(data, n = 15)``` display the first 15 rows of the data.
8. ```tail``` show the last 6 rows of data.
9. ```hist()``` view histogram of the data.
10. ```plot``` view plot of two variables.

## Exploring Data with Tidy
1. ```gather``` It should be used when you have columns that are not variables and you want to collapse them into key-value pairs. The easiest way to visualize the effect of gather() is that it makes wide datasets long.

I have below data set:

```
>head(bmi)
              Country    Y1980    Y1981    Y1982    Y1983    Y1984    Y1985
1         Afghanistan 21.48678 21.46552 21.45145 21.43822 21.42734 21.41222
2             Albania 25.22533 25.23981 25.25636 25.27176 25.27901 25.28669
3             Algeria 22.25703 22.34745 22.43647 22.52105 22.60633 22.69501
4             Andorra 25.66652 25.70868 25.74681 25.78250 25.81874 25.85236
5              Angola 20.94876 20.94371 20.93754 20.93187 20.93569 20.94857
6 Antigua and Barbuda 23.31424 23.39054 23.45883 23.53735 23.63584 23.73109
     Y1986    Y1987    Y1988    Y1989    Y1990    Y1991    Y1992    Y1993
1 21.40132 21.37679 21.34018 21.29845 21.24818 21.20269 21.14238 21.06376
2 25.29451 25.30217 25.30450 25.31944 25.32357 25.28452 25.23077 25.21192
3 22.76979 22.84096 22.90644 22.97931 23.04600 23.11333 23.18776 23.25764
4 25.89089 25.93414 25.98477 26.04450 26.10936 26.17912 26.24017 26.30356
5 20.96030 20.98025 21.01375 21.05269 21.09007 21.12136 21.14987 21.13938
6 23.83449 23.93649 24.05364 24.16347 24.26782 24.36568 24.45644 24.54096
     Y1994    Y1995    Y1996    Y1997    Y1998    Y1999    Y2000    Y2001
1 20.97987 20.91132 20.85155 20.81307 20.78591 20.75469 20.69521 20.62643
2 25.22115 25.25874 25.31097 25.33988 25.39116 25.46555 25.55835 25.66701
3 23.32273 23.39526 23.46811 23.54160 23.61592 23.69486 23.77659 23.86256
4 26.36793 26.43569 26.50769 26.58255 26.66337 26.75078 26.83179 26.92373
5 21.14186 21.16022 21.19076 21.22621 21.27082 21.31954 21.37480 21.43664
6 24.60945 24.66461 24.72544 24.78714 24.84936 24.91721 24.99158 25.05857
     Y2002    Y2003    Y2004    Y2005    Y2006    Y2007    Y2008
1 20.59848 20.58706 20.57759 20.58084 20.58749 20.60246 20.62058
2 25.77167 25.87274 25.98136 26.08939 26.20867 26.32753 26.44657
3 23.95294 24.05243 24.15957 24.27001 24.38270 24.48846 24.59620
4 27.02525 27.12481 27.23107 27.32827 27.43588 27.53363 27.63048
5 21.51765 21.59924 21.69218 21.80564 21.93881 22.08962 22.25083
6 25.13039 25.20713 25.29898 25.39965 25.51382 25.64247 25.76602
```

```gather``` will give column as key value pair

```
gather(bmi, year, bmi_val, -Country) %>% head()
              Country  year  bmi_val
1         Afghanistan Y1980 21.48678
2             Albania Y1980 25.22533
3             Algeria Y1980 22.25703
4             Andorra Y1980 25.66652
5              Angola Y1980 20.94876
6 Antigua and Barbuda Y1980 23.31424
```

2. The opposite of `gather()` is `spread()` , which takes key-values pairs and spreads them across multiple columns. This is useful when values in a column should actually be column names (i.e. variables). It can also make data more compact and easier to read. The easiest way to visualize the effect of spread() is that it makes long datasets wide.

3. ```separate``` used to split the data set.

4. The opposite of ```separate``` is ```unite()```

## Missing Value

1. `is.na` print whether a data is NA or not
2. `any` ask whether there are any NAs in the data.
3. `summary` gives the total number of NA in the data set.

   Example:
   ```
   # Replace all empty strings in status with NA
    social_df$status[social_df$status == ""] <- NA
   # Use complete.cases() to see which rows have no missing values
    complete.cases(social_df)
   # Use na.omit() to remove all rows with any missing values
    na.omit(social_df)
   ```
   
