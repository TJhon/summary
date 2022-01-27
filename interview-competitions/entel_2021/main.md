
```r
source('code/func.r')
```

# Importar


```r
train <- 
  xl_read(.doc = 'train') %>% 
  vari_td() 
test <- 
  xl_read(.doc = 'test') %>% 
  vari_td()
output <- xl_read(.doc = 'sampleSubmission')
#rm(list = c('costa', 'sierra', 'peru', 'xl_read', 'vari_td'))
```

# Datos

```r


for(i in unique(train$reg)){
  p <- train %>% 
    filter(reg == !!i) %>% 
    ggplot() +
    aes(lat_d, distancia) +
    geom_point() +
    geom_smooth() +
    #scale_y_log10() +
    labs(title = glue(i))
  print(p)
}

```

## Folds

```r
set.seed(55)
train_folds <- vfold_cv(train, 10, 5)
keep_pred <- control_resamples(save_pred = T, save_workflow = T)
set.seed(128)

```


```r
t1 <- initial_split(train, strata = distancia) %>% training()
t2 <- initial_split(train, strata = distancia) %>% testing()
test1 <- 
  test %>% 
  st_as_sf(coords = c('lon', 'lat'), crs = st_crs(peru)) %>% 
    st_intersection(peru) %>% 
    rename(reg = departamen) %>% 
    mutate(
      reg = as_factor(reg)
      , region = 
        case_when(
          reg %in% costa ~ "costa"
          , reg %in% sierra ~ "sierra"
          , T ~ "selva"
        ) %>% as_factor()
    ) %>% 
    st_set_geometry(NULL)

test1 %>% 
  right_join(test) %>% 
  mutate(across(where(is.factor), ~replace_na("No identificado") ))
?write_csv
```





# Modelos

## Workflow

```r

```



```r
lm_model <- linear_reg() %>% set_engine("lm")
metrics_0 <- metric_set(mape, rsq, rmse)
rf_model <- rand_forest(trees = 10) %>% set_engine('ranger') %>% set_mode('regression')
```


## Formulas 

```r
train %>% names()
train %>% head(2)
```


```r
all_model <- list(
  bs_1 <- distancia ~ lon_d + lat_d
, bs_1_d <- distancia ~ lon_d:lat_d
, bs_1_sqr <- distancia ~ I(lon_d^2) + I(lat_d^2)
, bs_2_d <- distancia ~ I(lon_d^2) + I(lat_d^2) + as_factor(dia_sem)
#, bs_2_dn <- distancia ~ I(lon_d^2) + I(lat_d^2) + as_factor(dia)
#, bs_2_dn_d <- distancia ~ I(lon_d^2) + I(lat_d^2) + as_factor(dia) + dia_sem
, bs_2_r <- distancia ~ I(lon_d^2) + I(lat_d^2) + reg
, bs_2_re <- distancia ~ I(lon_d^2) + I(lat_d^2) + region
, bs_2_re_1 <- distancia ~ I(lon_d^2) + I(lat_d^2) + region + reg
, bs_all_1 <- distancia ~ I(lon_d^2) + I(lat_d^2) + region + reg + as_factor(dia_sem)
#, bs_all_2 <- log(distancia) ~ I(lon_d^2) + I(lat_d^2) + region + reg + as_factor(dia) + dia_sem
)


```

```r
set.seed(100)

metrics_mape <- function(.train, .test, .model){
  map(
    .model
    , ~(
      workflow() %>% 
        add_formula(.x) %>% 
        add_model(rf_model) %>% 
    
        fit(data = .train) %>% 
        predict(.test) %>% 
        bind_cols(.test %>% select(distancia)) %>% 
        metrics_0(distancia, .pred)
    )
  )
  
}

metrics_mape(t1, t2, all_model)



```


```r
set.seed(100)


new_test <- 
  workflow() %>% 
  add_formula(bs_1_sqr) %>% 
  add_model(rf_model) %>% 
  fit(data = train) %>% 
  predict(test) %>% 
  rename(distancia = .pred) %>% 
  bind_cols(test %>% select(id))

final <- 
  workflow() %>% 
  add_formula(tiempo ~ distancia) %>% 
  add_model(rf_model) %>% 
  fit(data = train) %>% 
  predict(new_test) %>% 
  rename(tiempo = .pred ) %>% 
  bind_cols(new_test) %>% 
  relocate(id, distancia, tiempo) %>% 
  rename_with(str_to_upper)
```


```r
final %>% write_csv("answer.csv")
```

