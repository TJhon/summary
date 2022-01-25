library(tidyverse)
library(lubridate)
library(here)
library(tsibble)

pib <- read_rds(here('rdatos', 'pib.rds')) %>%
  mutate(variable = "pib", 
         id = 'PIB') %>% 
  mutate(fecha = parse_date_time(anio_mes, 'ym')) %>% 
  select(-anio_mes) %>% 
  rename(valor = pib)

con <- read_rds(here('rdatos', 'consumo.rds')) %>% 
  mutate(variable = "consumo", 
         sector = "percapita", 
         id = 'elect') %>% 
  unite('fecha', anio:mes) %>% 
  rename(valor = consumo_men) %>% 
  mutate(fecha = parse_date_time(fecha, 'ym'))

ipc <- read_rds(here('rdatos', 'ipc.rds')) %>% 
  select(anio, mes1, everything()) %>% 
  unite('fecha', anio:mes1, sep = '-') %>% 
  mutate(fecha = parse_date_time(fecha, 'ym'),
         variable = "ipc", id = 'id') %>% #
  rename(valor = ipc)

pob <- read_rds(here('rdatos', 'pob.rds')) %>% 
  group_by(anio) %>% 
  summarise(valor = sum(pob)) %>% 
  mutate(sector = 'pea', Variable = "pob", 
         mes = 1) %>% 
  select(anio, mes, everything()) %>% 
  unite('fecha', anio:mes) %>% 
  mutate(fecha = parse_date_time(fecha, 'ym'))


ggplot(pob, aes(fecha, valor)) +geom_point()


datos <- bind_rows(pib, con, ipc, pob) %>% spread(variable, valor) %>% 
  mutate(mes = yearmonth(fecha)) %>% as_tibble()
  

theme_set(theme_minimal())

datos %>% filter(sector == 'nacional') %>% 
  ggplot(aes(fecha, pib)) + geom_line()

datos %>% filter(sector == 'percapita') %>% 
  ggplot(aes(pib, consumo)) + geom_line()

datos %>% filter(sector == 'nacional') %>% 
  ggplot(aes(mes)) + 
  geom_line(aes(y = log(pib))) +
  geom_line(aes(y = log(consumo))) 


ipc %>% #filter(sector == 'residencial') %>% 
  ggplot(aes(fecha, valor, color = sector)) + geom_line()+
  geom_jitter()

datos %>% filter(id == 'consumo') %>% 
  ggplot(aes(fecha, consumo)) + geom_point()
