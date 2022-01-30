Web scraping with R
================

# Librerias

``` r
knitr::opts_chunk$set(
  warning = F
  , message = F
)
```

``` r
if(!require("librarian")) install.packages('librarian')
librarian::shelf(
  tidyverse
  , rvest
)
```

## Wong

``` r
knitr::include_graphics(here::here("fig_sc", "wong.png"))
```

![](C:/Users/Jhon/Documents/me/summary/challenge/fig_sc/wong.png)<!-- -->

### Scraping

``` r
wong <- "https://www.wong.pe/cervezas-vinos-y-licores"

wong_h <- read_html(wong) 
namew <- wong_h %>% 
  html_nodes(".product-item__name") %>% 
  html_text()
price1 <- wong_h %>% 
  html_nodes(".product-prices__value--best-price") %>% 
  html_text()

wong <- list(namew, price1)
wong_dt <- 
  wong %>% 
  map(
    ~enframe(.) %>% 
      mutate(value = str_trim(value)) 
  ) %>% 
  bind_cols() %>% 
  rename(
    id = 1
    , producto = 2
    , precio = 4
    ) %>% 
  select(!3) |> 
  mutate(
    precio = (
      str_remove(precio, "S/.|,") |> parse_number()
    )
  )

wong_dt |> 
  head(10)
```

    ## # A tibble: 10 x 3
    ##       id producto                                                         precio
    ##    <int> <chr>                                                             <dbl>
    ##  1     1 Delonghi Molinillo de Café                                        329  
    ##  2     2 Oster Exprimidor cítricos FPSTJU407W 18W                           99.0
    ##  3     3 Bosch Batidora de Mano MFQ24200                                   179  
    ##  4     4 Nex Horno Eléctrico 9 Lt EO900BX                                   89  
    ##  5     5 Bosch Cocina Empotrable a Gas PCP6A5B90V 4 Hornillas             1599  
    ##  6     6 Imaco Pentacombo: Pequeños Electrodomésticos                      439  
    ##  7     7 Bosch Tostador TAT7S45 4 Rebanadas                                359  
    ##  8     8 Bosch Hervidor Eléctrico Design Line TWK5P480                     259  
    ##  9     9 Combo Imaco: Licuadora BLS5388I + Mini Grill IG2314 + Hervidor ~  369  
    ## 10    10 Imaco Freidora de Aire Digital 4.2 Lt AF5514 1400W                599

``` r
write_csv(wong_dt, here::here("output", "wong_scraping.csv"))
```

## Urbania

``` r
knitr::include_graphics(here::here("fig_sc", "urb.png"))
```

![](C:/Users/Jhon/Documents/me/summary/challenge/fig_sc/urb.png)<!-- -->

### Scraping

``` r
urb <- 
  read_html("http://urbania.pe/buscar/alquiler-de-departamentos?keyword=lima")
elements <- 
  c(
    ".firstPrice"
    , ".postingCardLocationTitle"
    , ".postingCardExpenses"
    , ".postingCardMainFeatures.go-to-posting"
    , ".postingCardLocation.go-to-posting"
    , ".postingCardRow.postingCardDescription.go-to-posting"
  )

urb1 <- 
  map(
  elements
  , ~urb %>% html_nodes(.x) %>% html_text
  )
names(urb1) <- c("price", "Dir1", "Adicional", "Caracteristicas", "dir2", "descr")
urb2 <- 
  urb1 %>% 
  map(str_trim) %>% 
  map(str_remove_all, "[+]|[\n\t]|##|S/") %>% 
  map(enframe) %>% 
  bind_rows(.id = "type") %>% 
  pivot_wider(names_from = type, values_from = value) %>% 
  mutate_all(str_trim) %>% 
  
  separate(Adicional, c( "adicional", "concepto"), sep = " ") %>% 
  separate(Caracteristicas, c("m2", "null", "dorm", "banios", "estac", "otro"), sep = "[m²]|dorm[.]|bañ[o|os]|[s ]estac") %>% 
  relocate(c(price, adicional, m2, dorm, banios, estac)) %>% 
  mutate(across(price:estac, parse_number)) %>% 
  select(!c(name, null, otro)) %>% 
  relocate(Dir1, dir2, price, m2, dorm, banios, estac, adicional, concepto)


write.csv(urb2, here::here("output", "urbania.csv"), row.names = F)
```
