library(here)
library(tidyverse)
library(readxl)
library(purrr)
library(lubridate)

# consumo de combustible

rm(list = ls())

dem <- read_rds(here("datos", "rds", "dem1.rds")) # datos cada treinta minutos 

dem %>% transmute(fecha = dmy_hm(FECHA), anio = year(fecha),
                  mes = month(fecha), dia = day(fecha), consumo = EJECUTADO) %>% 
  group_by(anio, mes) %>% 
  summarise(consumo_men = sum(consumo, na.rm = T)) %>% 
  arrange(desc(anio)) %>% saveRDS(here("rdatos", "consumo.rds"))


# crecimiento 
rm(list = ls())
##pib_re <- read_xlsx(here("datos", "excel", "crecimiento", "pib_inei_2007.csv")) #datos similares a los de la siguiente linea

pib_na <- read_xlsx(here("datos", "excel", "crecimiento", "pib_inei_2007_total.xlsx")) %>% 
  drop_na() %>%
  select(-`...2`, -`...3`) %>% 
  rename(pib = 1) %>% 
  gather('anio', 'valor', -1) %>% spread(pib, valor) %>%
  rename(anio_mes = 2, 
         pib = 3) %>% 
    select(-1) %>% 
  mutate(pib = parse_number(pib),
         sector = 'nacional')



## Sectores

pib_cons <- read_xlsx(here("datos", "excel", "crecimiento", "sect", "constr.xlsx"))%>% 
  drop_na() %>%
  select(-`...2`, -`...3`) %>% 
  rename(pib = 1) %>% 
  gather('anio', 'valor', -1) %>% spread(pib, valor) %>%
  rename(anio_mes = 2, 
         pib = 3) %>% 
  select(-1) %>% 
  mutate(pib = parse_number(pib),
         sector = 'construccion')

pib_manu <- read_xlsx(here("datos", "excel", "crecimiento", "sect", "manufac.xlsx"))%>% 
  drop_na() %>%
  select(-`...2`, -`...3`) %>% 
  rename(pib = 1) %>% 
  gather('anio', 'valor', -1) %>% spread(pib, valor) %>%
  rename(anio_mes = 2, 
         pib = 3) %>% 
  select(-1) %>% 
  mutate(pib = parse_number(pib) ,
         sector = 'manufactura')

pib_min <- read_xlsx(here("datos", "excel", "crecimiento", "sect", "mineria.xlsx"))%>% 
  drop_na() %>%
  select(-`...2`, -`...3`) %>% 
  rename(pib = 1) %>% 
  gather('anio', 'valor', -1) %>% spread(pib, valor) %>%
  rename(anio_mes = 2, 
         pib = 3) %>% 
  select(-1) %>% 
  mutate(pib = parse_number(pib),
         sector = 'mineria')

pib_otrs <- read_xlsx(here("datos", "excel", "crecimiento", "sect", "otros.xlsx"))%>% 
  drop_na() %>%
  select(-`...2`, -`...3`) %>% 
  rename(pib = 1) %>% 
  gather('anio', 'valor', -1) %>% spread(pib, valor) %>%
  rename(anio_mes = 2, 
         pib = 3) %>% 
  select(-1) %>% 
  mutate(pib = parse_number(pib),
         sector = 'otros servicios')


## union de los datos 

bind_rows(pib_cons, pib_manu, pib_min, pib_na, pib_otrs) %>% 
  saveRDS(here('rdatos', 'pib.rds'))


# poblacion 
rm(list = ls())

pob <- read_xlsx(here("datos", "excel", "pobla", "pob.xlsx")) %>% 
  filter(Indicador == "Población Total Estimada",
         Departamento != "Total Nacional",
         Departamento != "Callao"
         ) %>% select(-Indicador) %>% 
  gather("anio", "pob", -1) %>% 
  mutate(pob = parse_integer(pob))

saveRDS(pob, here('rdatos', 'pob.rds'))

# precios tarifas ipc 

rm(list = ls())

p_gas <- read_xlsx(here("datos", "excel", "pre_traf_ipc", "gas.xlsx")) %>%  
  drop_na() %>%
  select(-`...2`, -`...3`) %>% 
  rename(pib = 1) %>% 
  gather('anio', 'valor', -1) %>% spread(pib, valor) %>%
  rename(anio_mes = 2, 
         ipc = 3) %>% 
  select(-1) %>% 
  mutate(ipc = parse_number(ipc) ,
         sector = 'pgas') %>% 
  separate(anio_mes, c('anio', 'mes1')) %>% 
  mutate(mes1 = parse_integer(mes1),
         anio = parse_number(anio)) %>% 
  filter(anio != 2020) 

  

t_inds <- read_xlsx(here("datos", "excel", "pre_traf_ipc", "t_elec_inds.xlsx")) %>% drop_na() %>% 
  rename(mes_anio = 1, 
         ipc = 2) %>% 
  mutate(sector = "industrial")

t_reis <- read_xlsx(here("datos", "excel", "pre_traf_ipc", "t_elec_resid.xlsx")) %>% drop_na() %>% 
  rename(mes_anio = 1, 
         ipc = 2) %>% 
  mutate(sector = "residencial")

p_gas84 <- read_xlsx(here("datos", "excel", "pre_traf_ipc", "p_gas84.xlsx")) %>% drop_na() %>% 
  rename(mes_anio = 1, 
         ipc = 2) %>% 
  mutate(sector = "gas84")

ipc1 <- bind_rows(t_inds, t_reis, p_gas84) %>% 
  separate(mes_anio, c("mes", "anio"), "(?<=[a-z])(?=[0-9])") %>% 
  mutate(anio1 = "20") %>% 
  select(anio1, anio, everything()) %>% 
  unite(anio, anio1:anio, sep = "") %>% 

  filter(anio != "2020") %>% 
  mutate(mes1 = rep(1:12, 30)) %>% 
  select(-mes) %>% 
  mutate(anio = parse_number(anio),
         ipc = parse_number(ipc))

bind_rows(ipc1, p_gas) %>% saveRDS(here('rdatos', 'ipc.rds'))

# datos terminados 

## script
