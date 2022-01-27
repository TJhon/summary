
``` r
if(!require(librarian)){install.packages("librarian")}
```

    ## Loading required package: librarian

``` r
librarian::shelf(tidyverse, janitor)
```

    ## 
    ##   The 'cran_repo' argument in shelf() was not set, so it will use
    ##   cran_repo = 'https://cran.r-project.org' by default.
    ## 
    ##   To avoid this message, set the 'cran_repo' argument to a CRAN
    ##   mirror URL (see https://cran.r-project.org/mirrors.html) or set
    ##   'quiet = TRUE'.

``` r
fs::file_delete(dir(here::here("output"), full.names = T))
```

# Replacement Workflow/Basic Data Cleaning

``` r
ipa_01 <- 
  c(
    "hhid" # label
    , "read"
    , "write" # numeric
    , 'head_gender' #0  female
    , "head_education"
    , "size"
  )
ipa_01_out <- here::here("output", "hh_round1_clean.dta")
```

``` r
ipa_d_01 <- 
  here::here('input', "hh_round1.dta") %>% haven::read_dta() %>% 
  relocate(ipa_01)
```

    ## Note: Using an external vector in selections is ambiguous.
    ## i Use `all_of(ipa_01)` instead of `ipa_01` to silence this message.
    ## i See <https://tidyselect.r-lib.org/reference/faq-external-vector.html>.
    ## This message is displayed once per session.

``` r
names(ipa_d_01)
```

    ##  [1] "hhid"           "read"           "write"          "head_gender"   
    ##  [5] "head_education" "size"           "village"        "enumid"        
    ##  [9] "head_age"       "head_marital"   "m0_5"           "f0_5"          
    ## [13] "m6_16"          "f6_16"          "m17_39"         "f17_39"        
    ## [17] "m40"            "f40"            "cropl_1"        "cropl_2"       
    ## [21] "cropl_3"        "cropl_4"        "cropl_5"        "cropl_6"       
    ## [25] "cropl_9"        "div_mon"        "div_gen"        "div_age"       
    ## [29] "div_rel"        "div_eth"        "div_edu"        "div_pol"       
    ## [33] "give_new"       "comm_wealth"

``` r
ipa_d_01 %>% 
  distinct(head_education) %>% 
  mutate(
    lab = head_education %>% haven::as_factor("labels")
    , num = head_education %>% haven::as_factor("values")
    , lab1 = paste(lab, "=", num)
  ) %>% 
  arrange(num) %>% 
  pull(lab1)
```

    ##  [1] "none = 0"                 "nursery/ pre-unit = 1"   
    ##  [3] "std 1 = 2"                "std 2 = 3"               
    ##  [5] "std 3 = 4"                "std 4 = 5"               
    ##  [7] "std 5 = 6"                "std 6 = 7"               
    ##  [9] "std 7 = 8"                "std 8 = 9"               
    ## [11] "form 1 = 10"              "form 2 = 11"             
    ## [13] "form 3 = 12"              "form 4 = 13"             
    ## [15] "form 5 = 14"              "form 6 = 15"             
    ## [17] "uni. 1 = 16"              " uni. 2 = 17"            
    ## [19] " uni. 3 = 18"             "uni. 4 = 19"             
    ## [21] "uni. 5 = 20"              "vocational training = 21"
    ## [23] "adult education = 22"     "other = 23"              
    ## [25] "not indicated = 98"       "rta = 99"                
    ## [27] "NA = NA"

``` r
head_education_labels <- c(
 none = 0                
 ,"nursery/ pre-unit" = 1   
 ,'std 1' = 2               
 ,'std 2' = 3               
 ,'std 3' = 4               
 ,'std 4' = 5               
 ,'std 5' = 6               
 ,'std 6' = 7               
 ,'std 7' = 8               
 ,'std 8' = 9               
 ,'form 1' = 10             
 ,'form 2' = 11             
 ,'form 3' = 12             
 ,'form 4' = 13             
 ,'form 5' = 14             
 ,'form 6' = 15             
 ,'uni. 1' = 16             
 ,'uni. 2' = 17            
 ,'uni. 3' = 18            
 ,'uni. 4' = 19             
 ,'uni. 5' = 20             
 ,"vocational training" = 2
 ,"adult education" = 22    
 ,"not indicated" = 98      
 ,other = 23              
 ,rta = 99                
 ,"NA" = NA
)
```

``` r
ipa_out <- ipa_d_01 %>% 
  mutate(
    across(.cols = c(read, write, head_gender, head_education), as.numeric)
    , hhid1 = str_sub(hhid, 2, -1) %>% as.numeric()
    , head_gender = ifelse(hhid1 == 15064, 0, head_gender)
    , head_gender = (ifelse(head_gender == 2, 0, 1)) %>% haven::labelled(c(Female = 0, Male = 1)) 
    , head_education = (ifelse(hhid1 == 29038, 0, head_education))
    , read = ifelse(hhid1 == 53024, 3, read)
    ) %>% 
  rename(hh_size = size) %>% 
  select(!hhid1)
    
ipa_out  
```

    ## # A tibble: 2,107 x 34
    ##    hhid    read write head_gender head_education hh_size village enumid head_age
    ##    <chr>  <dbl> <dbl>   <dbl+lbl>          <dbl>   <dbl>   <dbl>  <dbl>    <dbl>
    ##  1 10000~     2     2  0 [Female]             13       2       1      6       53
    ##  2 10000~     1     1  1 [Male]               13       1       6      5       31
    ##  3 10000~     2     2  1 [Male]                9       3       9      3       40
    ##  4 10000~     6     6  1 [Male]               20       6       4      1       64
    ##  5 10000~     4     4  0 [Female]              8       5       5      6       57
    ##  6 10000~     4     4  1 [Male]               21       5      10      2       33
    ##  7 10000~     7     7  1 [Male]                8       7       4      6       45
    ##  8 10000~     3     3  1 [Male]                8       3       4      9       68
    ##  9 10000~     3     3  1 [Male]               21       5       3      4       31
    ## 10 10000~     3     3  1 [Male]               21       5       5      6       31
    ## # ... with 2,097 more rows, and 25 more variables: head_marital <dbl+lbl>,
    ## #   m0_5 <dbl>, f0_5 <dbl>, m6_16 <dbl>, f6_16 <dbl>, m17_39 <dbl>,
    ## #   f17_39 <dbl>, m40 <dbl>, f40 <dbl>, cropl_1 <dbl>, cropl_2 <dbl>,
    ## #   cropl_3 <dbl>, cropl_4 <dbl>, cropl_5 <dbl>, cropl_6 <dbl>, cropl_9 <dbl>,
    ## #   div_mon <dbl+lbl>, div_gen <dbl+lbl>, div_age <dbl+lbl>, div_rel <dbl+lbl>,
    ## #   div_eth <dbl+lbl>, div_edu <dbl+lbl>, div_pol <dbl+lbl>, give_new <dbl>,
    ## #   comm_wealth <dbl+lbl>

2.  What percent of respondents have a female head of household?
3.  The Principal Investigator wants to see if there is a relationship
    between household head gender and household size. Find the average
    household size by household head gender.

``` r
percent <- 
  ipa_out %>% 
  count(head_gender) %>% 
  mutate(
    head_gender = haven::as_factor(head_gender, "labels")
    , n = (((n / sum(n)) * 100) %>% round(2) ) %>% paste("%")
  ) %>% 
  rename(
    "%" = 2
  )
percent
```

    ## # A tibble: 2 x 2
    ##   head_gender `%`   
    ##   <fct>       <chr> 
    ## 1 Female      23.4 %
    ## 2 Male        76.6 %

Respuesta: 23.4 %

``` r
ipa_out %>% mutate(
  
    head_gender = haven::as_factor(head_gender, "labels")
) %>% 
  select(hh_size, head_gender) %>% 
  group_by(head_gender) %>% 
  summarise(hh_size_mean = mean(hh_size)) 
```

    ## # A tibble: 2 x 2
    ##   head_gender hh_size_mean
    ##   <fct>              <dbl>
    ## 1 Female              3.63
    ## 2 Male                4.46

``` r
ipa_out %>% haven::write_dta(ipa_01_out)
```

``` r
rm(list = ls())
```

# Import and Export Excel

``` r
excel_out <- here::here("output", "excel_dup.xlsx")
```

``` r
ipa_02 <- 
  readxl::read_xlsx(here::here("input", "round2.xlsx"), sheet = 2, skip = 2) %>% 
  mutate(hhid = as.character(hhid))
```

``` r
dup <- 
  ipa_02 %>% 
  count(hhid) %>% 
  filter(n > 1) 
```

``` r
ipa_02_1 <- 
  ipa_02 %>% 
  filter(hhid %in% pull(dup, hhid))
```

``` r
ipa_02_2 <- 
  ipa_02 %>% 
  pull(hhid)
```

``` r
xlsx::write.xlsx(
  ipa_02_1
  , file = excel_out
  , sheetName = "duplicados"
  , append =  T
)
xlsx::write.xlsx(
  ipa_02_2
  , file = excel_out
  , sheetName = "duplicados_list"
  , append =  T
)
```

``` r
rm(list = ls())
```

# Survey Design Reconciliation

``` r
join1 <- here::here("input", "hh_nr_round1.dta") %>% haven::read_dta()
join2 <- here::here("input", "hh_round1.dta") %>% haven::read_dta()
```

## Formato largo

``` r
join1_1 <- 
  join1 %>% 
  separate_rows(crop_l, convert = T) %>% 
  rename(cropl = crop_l)
join1_1
```

    ## # A tibble: 929 x 3
    ##    hhid           village cropl
    ##    <chr>            <dbl> <int>
    ##  1 10000001030863      11     5
    ##  2 10000001030863      11     2
    ##  3 10000001030863      11     7
    ##  4 10000001030863      11     4
    ##  5 10000001030863      11     1
    ##  6 10000001202258      11     5
    ##  7 10000001202258      11     3
    ##  8 10000001202258      11     6
    ##  9 10000001248177      11     5
    ## 10 10000001248177      11     2
    ## # ... with 919 more rows

``` r
join2_1 <- 
  join2 %>% 
  pivot_longer(contains("cropl")) %>% 
  filter(value > 0) %>% 
  relocate(name) %>% 
  select(!value) %>% 
  rename(cropl = name) %>% 
  mutate(
    cropl = parse_number(cropl)
  )
join2_1
```

    ## # A tibble: 3,240 x 28
    ##    cropl hhid          village enumid  size head_age head_gender    head_marital
    ##    <dbl> <chr>           <dbl>  <dbl> <dbl>    <dbl>   <dbl+lbl>       <dbl+lbl>
    ##  1     5 1000000002022       1      6     2       53  2 [female] 1 [single/ nev~
    ##  2     4 1000000002033       6      5     1       31  1 [male]   1 [single/ nev~
    ##  3     5 1000000002033       6      5     1       31  1 [male]   1 [single/ nev~
    ##  4     1 1000000002054       9      3     3       40  1 [male]   3 [monogamousl~
    ##  5     4 1000000002097       4      1     6       64  1 [male]   3 [monogamousl~
    ##  6     1 1000000007020       5      6     5       57  2 [female] 6 [widowed]    
    ##  7     2 1000000007020       5      6     5       57  2 [female] 6 [widowed]    
    ##  8     2 1000000007036      10      2     5       33  1 [male]   3 [monogamousl~
    ##  9     3 1000000007036      10      2     5       33  1 [male]   3 [monogamousl~
    ## 10     3 1000000007053       4      6     7       45  1 [male]   3 [monogamousl~
    ## # ... with 3,230 more rows, and 20 more variables: head_education <dbl+lbl>,
    ## #   read <chr>, write <chr>, m0_5 <dbl>, f0_5 <dbl>, m6_16 <dbl>, f6_16 <dbl>,
    ## #   m17_39 <dbl>, f17_39 <dbl>, m40 <dbl>, f40 <dbl>, div_mon <dbl+lbl>,
    ## #   div_gen <dbl+lbl>, div_age <dbl+lbl>, div_rel <dbl+lbl>, div_eth <dbl+lbl>,
    ## #   div_edu <dbl+lbl>, div_pol <dbl+lbl>, give_new <dbl>, comm_wealth <dbl+lbl>

``` r
full_join(join2_1, join1_1) %>% 
  mutate(
    cropl = haven::labelled(
      cropl
      , c(
            "Rice" = 1
            , "Cassava" = 2
            , "Millet" = 3
            , "Groundnut" = 4
            , "Sweet Potato" = 5
            , "Wheat" = 6
            , "Sorghum" = 7
      )
    )
  ) %>% 
  mutate(
    across(.cols = c(read, write, head_gender, head_education), as.numeric)
    , hhid1 = str_sub(hhid, 2, -1) %>% as.numeric()
    , head_gender = ifelse(hhid1 == 15064, 0, head_gender)
    , head_gender = (ifelse(head_gender == 2, 0, 1)) %>% haven::labelled(c(Female = 0, Male = 1)) 
    , head_education = (ifelse(hhid1 == 29038, 0, head_education))
    , read = ifelse(hhid1 == 53024, 3, read)
    ) %>% 
  rename(hh_size = size) %>% 
  select(!hhid1) %>% 
  haven::write_dta(here::here("output", "hh_round1_longer.dta"))
```

    ## Joining, by = c("cropl", "hhid", "village")
