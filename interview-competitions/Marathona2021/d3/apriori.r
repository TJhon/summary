



df_groceries <- readr::read_csv("https://raw.githubusercontent.com/nupur1492/RProjects/master/MarketBasketAnalysis/Groceries_dataset.csv")


df_sorted <- df_groceries[order(df_groceries$Member_number),]
df_sorted$Member_number <- as.numeric(df_sorted$Member_number)

if(sessionInfo()['basePkgs']=="dplyr" | sessionInfo()['otherPkgs']=="dplyr"){
  detach(package:dplyr, unload=TRUE)
}
library(plyr)

df_itemList <- ddply(df_groceries,c("Member_number","Date"), 
                     function(df1)paste(df1$itemDescription, 
                                        collapse = ","))


df_itemList$Member_number <- NULL
df_itemList$Date <- NULL

#Rename column headers for ease of use
colnames(df_itemList) <- c("itemList")


write.csv(df_itemList, here::here("d3", "ItemList.csv"), quote = FALSE, row.names = TRUE)


library(arules)

txn = read.transactions(file=here::here('d3', "ItemList.csv"), rm.duplicates= F, format="basket",sep=",",cols=1)

txn@itemInfo$labels <- gsub("\"","",txn@itemInfo$labels)

basket_rules <- apriori(txn,parameter = list(sup = 0.01, conf = 0.5,target="rules"))

if(sessionInfo()['basePkgs']=="tm" | sessionInfo()['otherPkgs']=="tm"){
  detach(package:tm, unload=TRUE)
}

inspect(basket_rules)

#Alternative to inspect() is to convert rules to a dataframe and then use View()
df_basket <- as(basket_rules,"data.frame")
View(df_basket)

library(arulesViz)
plot(basket_rules)
plot(basket_rules, method = "grouped", control = list(k = 5))
plot(basket_rules, method="graph", control=list(type="items"))
plot(basket_rules, method="paracoord",  control=list(alpha=.5, reorder=TRUE))
plot(basket_rules,measure=c("support","lift"),shading="confidence",interactive=T)

itemFrequencyPlot(txn, topN = 5)