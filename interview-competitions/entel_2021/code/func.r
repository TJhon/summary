if(!require(librarian)) install.packages('librarian')
options(scipen = 999)
librarian::shelf(
  tidyverse
  , lubridate
  , sf
  , here
  , glue
  , janitor
  , tidymodels
  )

costa <- c(
"Tumbes"
, "Piura"
, "Lambayeque"
, "La libertad"
, "Ancash"
, "Lima"
, "Ica"
, "Arequipa"
, "Moquegua"
, "Tacna"
, "Callao"
) %>% str_to_lower()



sierra <- c(
"Ayacucho"
, "Junin"
, "Cusco"
, "Apurímac"
, "San Martin"
, "Cajamarca"
, "Huancavelica"
, "Huanuco"
, "Puno"
) %>% str_to_lower()

peru <- 
  here('data', 'map', 'dep', 'DEPARTAMENTOS.shp') %>% 
  sf::read_sf() %>% 
  clean_names() %>% 
  select(departamen, geometry) %>% 
  mutate(across(where(is.character), str_to_lower)) %>% 
  mutate(across(where(is.character), str_trim))  



xl_read <- function(.data = 'data', .doc, .type = '.csv'){
  .name <- 
    glue("{.doc}{.type}")
  .file <- 
    here(.data, .name) %>% 
    readr::read_csv(col_types = cols()) %>% 
    clean_names() %>% 
    arrange(1)
  return(.file)
}

vari_td <- function(.data){
  .data1 <-
    .data %>% 
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
      # Implementar la region (regiones de costa tienen mayor rapidez  que los de sierra y selva)
    ) %>% 
    select(!anio) %>% 
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
  .data3 <- 
    .data1 %>% 
    right_join(.data) %>% 
    mutate(across(where(is.factor), ~replace_na("No identificado") ))
}


round_df <- function(.data, .n = 2){
  .data %>% 
    mutate(
      across(
        where(
          is.numeric
        )
        , round
        , .n
      )
    )
}


tbl <- function(.model_dist, .model_time, .new_data = test){
  id <- 
    .new_data %>% 
    select(id)
  ls_1 <- 
    list("distancia" = .model_dist, "tiempo" = .model_time)
  d_t <- 
    ls_1 %>% 
    map(predict, .new_data) %>% 
    bind_cols()
  bind_cols(id, d_t) %>% 
    rename_with(str_to_upper)
}

predic_time <- function(.model_time, .new_data = test){
  .model_time %>% 
    predict(.new_data) %>% 
    enframe() %>% 
    bind_cols((.new_data %>% select(id)))
}


predic_dis <- function(.model_dis, .new_data = test){
  .model_dis %>% 
    predict(.new_data) %>% 
    enframe() %>% 
    bind_cols((.new_data %>% select(id)))
}


