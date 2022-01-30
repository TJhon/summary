Clean Data SBS
================

``` r
knitr::opts_chunk$set(
  warning = F
  , message = F
)
```

``` r
librarian::shelf(
  tidyverse
  , readxl
  , here
  , janitor
  , lubridate
)
```

# Overview

``` r
knitr::include_graphics(here::here("fig_sc", "sbs.png"))
```

![](../fig_sc/sbs.png)<!-- -->

It is curious that the SBS database is not recognized as reading .csv or
.xlsx, so I crossed the function and it worked.

Only MN

``` r
sbs_zona <- read_excel(here("data", "sbs", "B-zona.csv"))
head(sbs_zona, 10)
```

    ## # A tibble: 10 x 19
    ##    ...1  ...2  ...3  ...4  ...5  ...6  ...7  ...8  ...9  ...10 ...11 ...12 ...13
    ##    <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr>
    ##  1 Créd~ <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA> 
    ##  2 43861 <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA> 
    ##  3 <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  (En ~ <NA>  <NA>  <NA>  <NA>  <NA> 
    ##  4 <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA> 
    ##  5 <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA>  <NA> 
    ##  6 Depa~ Prov~ Dist~ Créd~ <NA>  <NA>  Depó~ <NA>  <NA>  Depó~ <NA>  <NA>  Depó~
    ##  7 <NA>  Dist~ Dist~ MN    ME    Total MN    ME    Total MN    ME    Total MN   
    ##  8 Amaz~ Bagua Bagua 5027~ 44.8~ 5031~ 3120~ 29.7~ 3150~ 2006~ 1090~ 2115~ 2460~
    ##  9 <NA>  Chac~ Chac~ 1073~ 302.~ 1076~ 2585~ 1134~ 2698~ 3581~ 5914~ 4173~ 4792~
    ## 10 <NA>  Utcu~ Bagu~ 1231~ 62.6~ 1231~ 1382~ 2881~ 1670~ 2924~ 1815~ 3106~ 4340~
    ## # ... with 6 more variables: ...14 <chr>, ...15 <chr>, ...16 <chr>,
    ## #   ...17 <chr>, ...18 <chr>,
    ## #   Fuente: Anexo 10 Depósitos, Colocaciones y Personal por oficinas <chr>

# Try

``` r
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
```

## All data base

``` r
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
```

``` r
all_sbs <- dir(here("data", "sbs"), full.names = T) |> 
  map_df(read_excel, range = "A1:R286")
```

``` r
all_sbs_clean <- 
  all_sbs |> 
  sbs_clean() |> 
  select(!cuadro_no_2) 

write.csv(all_sbs_clean, here("output", "sbs.clean.csv"), row.names = F)
```
