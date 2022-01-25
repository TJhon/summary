## --------------------------------------------------------
librarian::shelf(
  tidyverse
  , janitor
  , tidymodels
)
sonda <- "https://raw.githubusercontent.com/maratonadev/desafio-5-2021/main/assets/data/dataset.csv" |> read_csv() |> janitor::clean_names()
answ <- answ1 <- read_csv("https://raw.githubusercontent.com/maratonadev/desafio-5-2021/main/assets/data/ANSWERS.csv") 
 


## --------------------------------------------------------
sonda |> count(seniorcitizen)


## --------------------------------------------------------

cln <- function(.data) {
  .data |> 
    janitor::clean_names() |> 
    drop_na(gender, paymentmethod, contract, seniorcitizen) |> 
    transmute(
      churn = factor(churn)
      , totalcharges
      , monthlycharges
      , seniorcitizen = factor(seniorcitizen)
      , internetservice = ifelse(is.na(internetservice), "No", internetservice)
      , streamingmovies = ifelse(str_detect(streamingmovies, "No") | is.na(streamingmovies), "No", "Yes")
      , contract
    ) |> 
    mutate(across(where(is.numeric), ~log(., + 0.1)))
}

sonda1 <- cln(sonda)



logt <- glm(churn ~ totalcharges + monthlycharges + seniorcitizen + internetservice + streamingmovies + contract , data = sonda1, family = binomial) 






## --------------------------------------------------------
library(tidymodels)


## --------------------------------------------------------
set.seed(12)
d_split <- initial_split(sonda1, 0.7, strata = churn)
train <- training(d_split)
test <- testing(d_split)


## --------------------------------------------------------
logt <- glm(churn ~ totalcharges + monthlycharges + internetservice + streamingmovies + seniorcitizen, data = train, family = binomial) 

#broom::tidy(logt) |> filter(p.value < 0.1)

add_column(test, ".predict" = predict(logt, test,  type = 'response')) |> 
  mutate(.predict = ifelse(.predict < 0.5, "No", "Yes") |> factor()) |> 
  f_meas(churn, .predict)



## --------------------------------------------------------



add_column(answ, ".predict" = predict(logt, cln(answ), type = "response")) |> 
  mutate(.predict = ifelse(.predict < 0.5, "No", "Yes"))  |> 
  select(!CHURN) |> 
  rename(CHURN = .predict) |> 
  write.csv('d5.csv', row.names = F)

