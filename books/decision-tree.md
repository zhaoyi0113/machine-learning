# Decision Tree

Decision tree is a machine learning algorithm used to classify data into categories. It helps us to explore the data set. This section will use the `kyphosis` data set provided by `gam` package.

## Classification tree 

Below example creates a decision tree on `Kyphosis` from `Age, Number, Start` columns. 

```
# Classification Tree with rpart
library(rpart)

# grow tree 
fit <- rpart(Kyphosis ~ Age + Number + Start,
  	method="class", data=kyphosis)

printcp(fit) # display the results 
plotcp(fit) # visualize cross-validation results 
summary(fit) # detailed summary of splits

# plot tree 
plot(fit, uniform=TRUE, 
  	main="Classification Tree for Kyphosis")
text(fit, use.n=TRUE, all=TRUE, cex=.8)

# create attractive postscript plot of tree 
post(fit, file = "/tmp/tree.ps", 
  	title = "Classification Tree for Kyphosis")
```

## Prune the tree 

```
# prune the tree 
pfit<- prune(fit, cp=   fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"])

# plot the pruned tree 
plot(pfit, uniform=TRUE, 
  	main="Pruned Classification Tree for Kyphosis")
text(pfit, use.n=TRUE, all=TRUE, cex=.8)
post(pfit, file = "~/tmp/ptree.ps", 
  	title = "Pruned Classification Tree for Kyphosis")
```

