# get the XML for the 2 offline downloads

library(XML)
brexit90d <- xmlToDataFrame("Analysis/brexit_20190322_90d.xml")
brexit24h <- xmlToDataFrame("Analysis/brexit_20190322_24h.xml")

# getting it from the API directly is different
library(httr)
library(jsonlite)
library(dplyr)
foo <- GET("https://www.predictit.org/api/Public/GetMarketChartData/4672?timespan=24h&maxContracts=6&showHidden=true")
foo$status_code
bar <- foo$content %>%
  rawToChar() %>%
  fromJSON()

setdiff(tolower(names(brexit90d)), tolower(names(bar)))
names(bar)
