## -------------------------------------------------------------------------------------------------------------------------------------------------------
library(here)
library(tidyverse)
library(kableExtra)
library(e1071)   
library(ggfortify)
library(GGally)
library(tsibble)
library(lubridate)
datos <- read_rds(here('rdatos', '00datos.rds'))
# import code  
# libreris necesarias 
#library(tidyverse)
#library(kableExtra)
sable <- function(x, escape = T, booktabs = T, caption = "", longtable = T, optio  = c("stripted", "hold_position"), full = T) {
  kable(x, escape = escape, booktabs = T, caption = caption, longtable = longtable) %>%
    kable_styling(latex_options =  optio, full_width = full, position = "center")
}



## ----pib, fig.dim=c(5, 3), fig.cap='Comportamiento Temporal de las variables', fig.subcap=c('PIB nacional', 'PIB sectorial', 'Variaciones anuales'), out.width='50%', fig.ncol=2, fig.align='center'----
datos %>% 
 filter(sector == 'nacional') %>% 
 ggplot(aes(fecha, pib)) + geom_line()

datos %>% 
 filter(sector != 'nacional') %>% 
 ggplot(aes(fecha, log(pib), color = factor(sector))) + geom_line(size = 0.8)
datos %>%
  mutate(fecha = year(fecha)) %>% 
  group_by(sector, fecha) %>% 
  summarise(pib = mean(pib)) %>% 
  mutate(diff = pib - lag(pib),  
    t_crecimiento = (diff / pib)*100)  %>% drop_na() %>% 
  ggplot(aes(fecha, t_crecimiento, color = sector)) + geom_line() + geom_hline(yintercept = 0)



## -------------------------------------------------------------------------------------------------------------------------------------------------------
h1 <- datos %>%# filter(sector != 'construccion') %>% 
  group_by(sector, fecha) %>% 
  #group_by(fecha) %>% 
  mutate(fecha = year(fecha)) %>% 
  summarise(pib = mean(pib)) %>% 
  mutate(diff = pib - lag(pib),  
    t_crecimiento = (diff / pib)*100)  %>% drop_na() %>% 
   mutate(diff = pib - lag(pib),  
    t_crecimiento = (diff / pib)*100,
         int = ifelse(fecha >= 2007 & fecha <= 2011, '2007-2011',
                      ifelse(fecha > 2011 & fecha <= 2015, '2012-2015',
                             ifelse(fecha > 2015 & fecha < 2020, '2015-2019', '2020.1 - 2020.4')))) %>% 
  group_by(sector, int) %>% 
  summarise(promedio = mean(t_crecimiento, na.rm = T)) %>% 
  spread(int, promedio) %>% 
  rename(Sector = 1) %>% 
  arrange(5)


sable(h1, caption = "Tasa de crecimiento")


## ---- fig.cap='Comportamiento Temporal del consumo electrico', out.width='50%'--------------------------------------------------------------------------
datos %>%  
  mutate(f = year(fecha)) %>% 
  filter(f >= 2007) %>%
  ggplot(aes(fecha, consumo)) + geom_line()


## -------------------------------------------------------------------------------------------------------------------------------------------------------
h1 <- datos %>%
  mutate(f = year(fecha)) %>% 
  group_by(f) %>%
  filter(f >= 2006) %>%
  summarise(consumo = mean(consumo)) %>% 
  mutate(d = consumo - lag(consumo),  
    t_crecimiento = (d / consumo)*100,
    nt = ifelse(f >= 2007 & f <= 2011, '2007-2011',
                      ifelse(f > 2011 & f <= 2015, '2012-2015',
                             ifelse(f > 2015 & f < 2020, '2015-2019', '2020.1 - 2020.4'))) )  %>% drop_na() %>% 
  group_by(nt) %>% 
  summarise(promedio = mean(t_crecimiento, na.rm = T)) %>% 
  spread(nt, promedio) %>% 
  mutate(variable = 'Crecimiento % del consumo') %>% 
  dplyr::select(variable, everything())

sable(h1)



## ---- fig.cap='IPC', out.width='50%'--------------------------------------------------------------------------------------------------------------------
datos %>% filter(sector1 == 'gas84') %>% 
  ggplot(aes(fecha, ipc)) + geom_line()


## -------------------------------------------------------------------------------------------------------------------------------------------------------
h1 <- datos %>%
  mutate(f = year(fecha)) %>% 
  group_by(f) %>%
  filter(f >= 2006) %>%
  summarise(ipc = mean(ipc)) %>% 
  mutate(d = ipc - lag(ipc),  
    t_crecimiento = (d / ipc)*100,
    nt = ifelse(f >= 2007 & f <= 2011, '2007-2011',
                      ifelse(f > 2011 & f <= 2015, '2012-2015',
                             ifelse(f > 2015 & f < 2020, '2015-2019', '2020.1 - 2020.4'))) )  %>% drop_na() %>% 
  group_by(nt) %>% 
  summarise(promedio = mean(t_crecimiento, na.rm = T)) %>% 
  spread(nt, promedio) %>% 
  mutate(variable = 'Crecimiento % del IPC') 

h1 %>% kable()

