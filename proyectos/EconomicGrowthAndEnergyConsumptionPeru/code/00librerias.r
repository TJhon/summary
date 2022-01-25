library(here)

library(tidyverse)
library(readr)
library(glue)
library(tsibble)
library(kableExtra)
library(e1071)
library(ggfotrify)
library(GGally)
library(lubridate)


sable <- function(x, escape = T) {
  kable(x, escape = escape) %>%
    kable_styling("striped", full_width = T)
}


sselect <- function() {
    dplyr::select()
}

sable(head(mtcars, 5))
kable(mtcars)