## -------------------------------------------------------------------------------------------------------------------------------------------------------
librarian::shelf(
  tidyverse
  , readxl
  , here
  , janitor
  , lubridate
)


## -------------------------------------------------------------------------------------------------------------------------------------------------------
knitr::include_graphics(here("fig_sc", "sbs.png"))


## -------------------------------------------------------------------------------------------------------------------------------------------------------
sbs_zona <- read_excel(here("data", "sbs", "B-zona.csv"))
head(sbs_zona, 10)


## -------------------------------------------------------------------------------------------------------------------------------------------------------
sbs_clean <- 
  sbs_zona |> 
  clean_names() |> 
  fill(x1) |> 
  select(!fuente_anexo_10_depositos_colocaciones_y_personal_por_oficinas) |> 
  rename(
    reg = 1
    , prov = 2
    , dist = 3
  ) |> 
  filter(!str_detect(reg, "[Tt]otal|Dep")) |> 
  fill(prov) |> 
  mutate(
    date1 = as.numeric(reg) |> as_date(origin = "1899-12-30")
    ) |> 
  fill(date1) |> 
  drop_na(x5) |> 
  mutate(
    year_date = year(date1)
    , month_date = month(date1)
         ) |> 
  relocate(date1, year_date, month_date, reg, prov, dist) |> 
  rename(
    cred_direc = x6
    , dep_vis = x9
    , dep_aho = x12
    , dep_pla = x15
    , dep_tot = x18
  ) |> 
  select(!contains("X")) |> 
  mutate(
    across(contains(c("dep", "cre"))
      , as.numeric)
    )


## -------------------------------------------------------------------------------------------------------------------------------------------------------
sbs_clean <- function(sbs_data) {
  sbs_data |> 
    clean_names() |> 
    fill(x1) |> 
    #select(!fuente_anexo_10_depositos_colocaciones_y_personal_por_oficinas) |> 
    rename(
      reg = 1
      , prov = 2
      , dist = 3
    ) |> 
    filter(!str_detect(reg, "[Tt]otal|Dep")) |> 
    fill(prov) |> 
    mutate(
      date1 = as.numeric(reg) |> as_date(origin = "1899-12-30")
      ) |> 
    fill(date1) |> 
    drop_na(x5) |> 
    mutate(
      year_date = year(date1)
      , month_date = month(date1)
           ) |> 
    relocate(date1, year_date, month_date, reg, prov, dist) |> 
    rename(
      cred_direc = x6
      , dep_vis = x9
      , dep_aho = x12
      , dep_pla = x15
      , dep_tot = x18
    ) |> 
    select(!contains("X")) |> 
    mutate(
      across(contains(c("dep", "cre"))
        , as.numeric)
      )
  
}


## -------------------------------------------------------------------------------------------------------------------------------------------------------
all_sbs <- dir(here("data", "sbs"), full.names = T) |> 
  map_df(read_excel, range = "A1:R286")

## -------------------------------------------------------------------------------------------------------------------------------------------------------
all_sbs_clean <- 
  all_sbs |> 
  sbs_clean() |> 
  select(!cuadro_no_2) 

write.csv(all_sbs_clean, here("output", "sbs.clean.csv"), row.names = F)


