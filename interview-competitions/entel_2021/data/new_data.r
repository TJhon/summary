source('code/func.r')
train <- 
  xl_read(.doc = 'train') 

train_reg <- 
  train %>% 
  mutate(
    lat_d = latitud_destino - latitud_origen
    , lon_d = longitud_destino - longitud_origen
    , lat = latitud_destino
    , lon = longitud_destino
    , anio = year(fecha)
    , mes = month(fecha)
    #, dia = day(fecha)
    , dia_sem = wday(fecha)
    , dia = case_when(
      dia_sem < 6 ~ "l-v"
      , T ~ "s-d"
    )
  ) %>% 
  select(!anio) %>% 
  st_as_sf(coords = c('lon', 'lat'), crs = st_crs(peru)) %>% 
  st_intersection(peru) %>% 
  st_set_geometry(NULL) %>% 
  rename(reg = departamen) %>% 
  mutate(
    reg = as_factor(reg)
    , region = 
      case_when(
        reg %in% costa ~ "costa"
        , reg %in% sierra ~ "sierra"
        , T ~ "selva"
      ) %>% as_factor()
  ) 


