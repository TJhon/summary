
# data librerias

librarian::shelf(
  tidyverse
  , arules 
)

#reacsv <- function(url){read_csv(url) |> janitor::clean_names()}

invest <-read_csv("https://raw.githubusercontent.com/maratonadev/desafio-3-2021/main/assets/data/InvestmentBankCDE.csv")  

reatail <- read_csv("https://raw.githubusercontent.com/maratonadev/desafio-3-2021/main/assets/data/RetailBankEFG.csv")

insurage <- read_csv("https://raw.githubusercontent.com/maratonadev/desafio-3-2021/main/assets/data/InsuranceCompanyABC.csv")

answ <- read_csv("https://raw.githubusercontent.com/maratonadev/desafio-3-2021/main/assets/data/ANSWERS.csv")
answ1 <- answ |> janitor::clean_names()

# full data apriori rules

full_data <- reduce(list(invest, reatail, insurage), full_join) |> 
  mutate(across(where(is.logical), as.numeric)) |> 
  select(!c(ID, Renda, Idade, Regiao))

rm(list = c('invest', 'reatail', 'insurage', "reacsv"))

reglas <- arules::apriori(as.matrix(full_data))


recomend <- 
  reglas |> as("data.frame") |> 
  arrange(desc(confidence), count) |> 
  select(-c(support, coverage, lift, count)) |> 
  as_tibble() |> 
  separate(rules, c("name", "recomend"), sep = "=>") |> 
  mutate(rule = row_number()) |> 
  as_tibble() |> 
  separate_rows(name, sep = ",") |> 
  mutate(across(where(is.character), ~str_remove_all(., "[{]|[}]") |> str_trim())) |> 
  filter(recomend != 'genero')

full_data_list <- 
  mutate(full_data, id = row_number()) |> 
  pivot_longer(!id) |>
  mutate(value = as.logical(value)) |> 
  filter(value) |> 
  select(!value)

# predecir reglas
# 
#
## try with full data

left_join(recomend, full_data_list) |> 
  group_by(id) |> 
  arrange(id) |> 
  distinct(recomend, .keep_all = T) |> 
  arrange(confidence) |> 
  slice(1:3) |> 
  mutate(
    rango = row_number()
    , confidence = round(confidence, 5)
    , rec = paste("re", rango)
    , con = paste("co", rango)
    ) |> 
  select(!c(name, rule, rango)) |> 
  pivot_wider(id_cols = id, names_from = c(rec, con), values_from = c(recomend, confidence)) |> 
  full_join((mutate(full_data, id = row_number())), by = 'id', ) |> 
  arrange(id)


## 
## 
## 

answ_list_t <- 
  answ |> 
  select(!c(Idade, Renda, Regiao)) |> 
  mutate_all(as.numeric) |> 
  pivot_longer(!ID) |> 
  filter(value == 1) |> 
  select(!value)
  


rec_4_asnw <- 
  left_join(recomend, answ_list_t) |> 
  rename(id = ID) |> 
  group_by(id) |> 
  arrange(id) |> 
  distinct(recomend, .keep_all = T) |> 
  arrange(desc(confidence)) |> 
  slice(1:3) |> 
  mutate(
    rango = row_number()
    , confidence = round(confidence, 5) |> as.character()
    , rec = paste("re", rango)
    , con = paste("co", rango)
  ) |> 
  select(!c(name, rule, rango)) |> 
  pivot_wider(id_cols = id, names_from = c(rec, con), values_from = c(recomend, confidence), values_fill = "False") |> 
  relocate(1, 2, 5, 3, 6, 4, 7) 


names(rec_4_asnw) <- c("ID", names(answ)[26:31])
left_join((answ |> select(!contains(c("recomm", "conf")))), rec_4_asnw) |> 
  mutate(across(contains("confidence"), as.numeric)) |> 
  mutate(across(contains("confidence"), ~replace_na(., "False"))) |> 
  mutate(across(contains("recomm"), ~replace_na(., "False"))) |> 
  write.csv("d3/d3.csv", row.names = F)
