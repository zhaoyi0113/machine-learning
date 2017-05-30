# How to calculate mean value of two list for each row

If there are two lists defined as below code:

```
l1 <- list(a=1, b=2, c=3)
l2 <- list(a=4, b=5, c=6)
```

what if I want to get the mean value of them for each row as below expected results:

```
l3 <- mean(l1, l2)
```

There are a couple of ways to do that,

- use cbind
```
> apply(cbind(do.call(rbind,l1),do.call(rbind,l2)),1, mean)
a   b   c 
2.5 3.5 4.5 

```
- use map
```
> Map(function(x,y) mean(c(x,y)), l1, l2)
$a
[1] 2.5

$b
[1] 3.5

$c
[1] 4.5
```
- use map2 from `purrr`
```
> purrr::map2(l1, l2, ~ mean(c(.x, .y)))
$a
[1] 2.5

$b
[1] 3.5

$c
[1] 4.5
```
- use relist
```
> relist((unlist(l1) + unlist(l2))/2, skeleton= l1)
$a
[1] 2.5

$b
[1] 3.5

$c
[1] 4.5
```
- use colMeans
```
> colMeans(do.call(rbind.data.frame, list(l1,l2)))
  a   b   c 
2.5 3.5 4.5 
```