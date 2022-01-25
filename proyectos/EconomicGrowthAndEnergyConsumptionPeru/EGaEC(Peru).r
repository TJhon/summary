## ----setup, echo=FALSE, warning=FALSE, include=TRUE-----------------------------------------------------------------------------------------------------
# import code  
# libreris necesarias 
#library(tidyverse)
#library(kableExtra)
sable <- function(x, escape = T, booktabs = T, caption = "", longtable = T, optio  = c("stripted", "hold_position"), full = T) {
  kable(x, escape = escape, booktabs = T, caption = caption, longtable = longtable) %>%
    kable_styling(latex_options =  optio, full_width = full, position = "center")
}




## ----resumen, child = 'rmd/01resumen.rmd'---------------------------------------------------------------------------------------------------------------




## ----introduccion, child = 'rmd/02intro.rmd'------------------------------------------------------------------------------------------------------------

## ---- echo = FALSE, include=FALSE, warning=FALSE--------------------------------------------------------------------------------------------------------
library(here)
library(tidyverse)
library(readr)
library(glue)
library(tsibble)
theme_set(theme_minimal())
knitr::opts_chunk$set(fig.pos = "H", # Fijar posicion de las figuras 
                      echo = F, # si es FALSE Correr el codigo pero mostrarlo
                      message = F, # si es FALSE Mensajes omitidos
                      warning = F, # si es FALSE Advertencias omitidas
                      include = T, # si es FALSE 
                      out.extra = "", 
                      cache = F,# 
                      fig.align='center'
                      ) 

options(knitr.duplicate.label = "allow", # permitir Chunk names repetidos
        knitr.table.format = function() { # funcione de acuerdo a la salida del texto
  if (knitr::is_latex_output()) 'latex' else 'pandoc'
}, digits = 4, 
kableExtra.auto_format = FALSE
)
datos <- read_rds(here('rdatos', '00datos.rds'))



## ----teoria, child = 'rmd/03ant_teo.rmd'----------------------------------------------------------------------------------------------------------------

## ----<chunk-label>, echo = FALSE, fig.cap = 'Relacion entre el consumo electrico y el crecimiento econónico'--------------------------------------------
knitr::include_graphics(here('code', 'make.jpeg'))



## ----hecho, child = 'rmd/05hechos.rmd'------------------------------------------------------------------------------------------------------------------

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



## ----modelo, child = 'rmd/06model.rmd'------------------------------------------------------------------------------------------------------------------




## ----hipotesis, child = 'rmd/07hipo.rmd'----------------------------------------------------------------------------------------------------------------




## ----metodologia, child = 'rmd/08method.rmd'------------------------------------------------------------------------------------------------------------




## ----resultados, child = 'rmd/09resul.rmd'--------------------------------------------------------------------------------------------------------------

## -------------------------------------------------------------------------------------------------------------------------------------------------------
library(tidyverse)
library(here)
library(GGally)
library(kableExtra)
library(broom)


serie <- read_rds(here('rdatos' , 'desestacionalizado.rds'))
data <- read_rds(here('rdatos', '03est.rds')) %>% 
  dplyr::select(-tcons)

data1 <- data %>% as_tibble() %>% 
  mutate(comsumo = log(comsumo))

describir <- serie %>% as_tibble() %>% 
  rename("PIB per capita" = 1, "Consumo electrico per capita" = 2) %>% 
  gather(variable, v1) %>%
  mutate(v1 = v1*10^3) %>% 
  group_by(variable) %>% 
  summarise(n = n(), 
            Minimo = min(v1),
            Maximo = max(v1),
            Suma = sum(v1), 
            Promedio = mean(v1), 
            SD = sd(v1), 
            Curtosis = e1071::kurtosis(v1)) 

sable(describir, caption = "Estadisticas descriptivas /n del PIB per-capita y el consumo electrico per-capita, series mensuales 2010.1 - 2019.12")



## ----pib-fig, fig.dim=c(5, 3), fig.cap='Correlaciones', fig.subcap=c('Niveles', 'Primera diferencia'), out.width='50%', fig.ncol=2, fig.align='center'----

serie %>% exp %>%  
  as_tibble() %>% 
  rename("PIB per capita" = 1, 'Consumo electrico per capita' = 2) %>% 
   ggpairs() + labs(title = "Tranforma")

serie %>% diff %>% 
  as_tibble() %>% 
  rename("PIB per capita" = 1, 'Consumo electrico per capita' = 2) %>% 
  ggpairs() 



## ---- raiz----------------------------------------------------------------------------------------------------------------------------------------------
read_rds(here('rdatos', 'raiz.rds')) %>% 
  sable(caption = 'Augmented Dickey–Fuller - Prueba de raiz unitaria ') %>% 
  pack_rows("Transformacion logaritmica", 1, 2) %>%
  pack_rows("Primera diferencia", 3, 4)



## -------------------------------------------------------------------------------------------------------------------------------------------------------
library(magrittr)
orden_p <- serie %>%  diff %>%  vars::VARselect(lag.max = 12)# %$% #%$% criteria  %>% glimpse()
tibble("Criterio" = c("AIC", "HQ", "SC", "FPE"), 
  "Orden p" = c(3, 1 ,1 ,3)) %>% sable(caption = 'Lag selection', full = F) 


## ---- results = 'asis'----------------------------------------------------------------------------------------------------------------------------------

#acf(serie[,1] %>% diff)

m1 <- serie %>% diff %>% vars::VAR(., p = 1) 

m3 <- serie %>% diff %>% vars::VAR(., p = 3) 


#summary(m1)
#summary(m3)
stargazer::stargazer(m1$varresult$pib_d,
m1$varresult$cons_d, 
m3$varresult$cons_d, 
m3$varresult$pib_d,
#type = 'text', 
title = "Estimaciones VAR(1), VAR(3)",
column.labels = c("PIB", "Consumo", "PIB", "Consumo"), 
header = F, 
single.row=TRUE,
table.placement = '!h',
column.sep.width = "2pt",
#float.env = "sidewaystable",
no.space = F
)
#dep.var.labels = c(''), 
#align = T, 
#covariate.labels = c('Producto percapita(-1)', 'Consumo electrico(-1)', 'Producto percapita(-2)', #'Consumo electrico(-2)', 'Producto #percapita(-3)', 'Consumo electrico(-3)', 'Constante'), 



## ----varest, fig.cap='Estabilidad de los modelos', fig.subcap=c('VAR(1)', 'VAR(3)'), out.width='50%', fig.ncol=2, fig.align='center', fig.pos="H"-------

#vars::serial.test(m3, lags.pt = 12, type = 'PT.asymptotic')
#vars::arch.test(m1, lags.multi = 12, multivariate.only = T)
#vars::normality.test(m1, multivariate.only = T)

vars::stability(m1, type = 'OLS-CUSUM') %>% plot
vars::stability(m3, type = 'OLS-CUSUM') %>% plot


## -------------------------------------------------------------------------------------------------------------------------------------------------------
dserie <- diff(serie)

gran <- tibble(
gran1 = c(lmtest::grangertest(dserie[, 1] ~ dserie[,2], orden  = 1)),
gran2 = c(lmtest::grangertest(dserie[, 2] ~ dserie[,1], orden  = 1))
)

tibble(
  Hipotesis = c("H0 = El Crecimiento económico no causa en el sentido de Granger al consumo electrico","H0 = El Consumo electrico no causa en el sentido de Granger al Crecimiento económico"),
  `F-test` = c(gran$gran1$F[3], gran$gran2$F[3]),
  `P-valor` = c(gran$gran1$`Pr(>F)`[3], gran$gran2$`Pr(>F)`[3])
) %>% sable(caption = 'Test de Causalidad en el sentido de Granger')



## ---- fig.cap='Impulso respuesta', fig.subcap=c('Producto percapita', 'Consumo percapita'), out.width='50%', fig.ncol=2, fig.align='center'-------------
vars::irf(m1, impulse = 'cons_d', response = 'pib_d', n.ahead = 20, boot =T) %>% plot
vars::irf(m1, impulse = 'pib_d', response = 'cons_d', n.ahead = 10, boot =T) %>% plot




## ----fila, child = 'rmd/10final.rmd'--------------------------------------------------------------------------------------------------------------------



