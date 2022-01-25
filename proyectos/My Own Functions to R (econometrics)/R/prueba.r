
## Var

library(vars)
library(magrittr)
data("Canada")
Canada %>% 
  as_data_frame()

plot(Canada)

my_ur_var <- function(df, variable, periodo = 12){
  library(vars)
  ur.df(df[, variable], type = "none", lags = periodo) %>% 
    summary()
}

ur.df(Canada[, "prod"], type = "none", lags = 2) %>% 
  summary

ur.df(Canada[, "prod"], type = "drift", lags = 1) %>% 
  summary

VARselect(Canada, lag.max = 8, type = "both")

cnd <- Canada[, c("prod", "e", "U", "rw")]

s1 <- VAR(cnd, p = 1, type = "both")

summary(s1, equation = "e")

plot(s1, names = "e")

serial.test(s1, lags.pt = 16, type ="PT.asymptotic") %$% 
  serial
  
  