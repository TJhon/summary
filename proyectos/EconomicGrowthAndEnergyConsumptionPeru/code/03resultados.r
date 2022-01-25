library(here)
library(tidyverse)
library(lubridate)
library(tsibble)
library(forecast)

s1 <- read_rds(here('rdatos', '01ts.rds'))
s1

s2 <- s1 %>% as_tsibble() %>% 
  spread(key, value) %>% 
  transmute(cons_per = consumo/pob*10^5, 
            pib_per = pib/pob*10^7) %>% as_tibble()

data <- s2 %>% select(2, 3) %>% 
  ts(start = 2010, frequency = 12)

# Componentes

pib <- data[, 2] %>% stl(log(), s.window = 'periodic')
cons <- data[, 1] %>% stl(log(), s.window = 'periodic')


# Descestacionalizado 

pib_d <-  seasadj(pib) %>% log()
cons_d <-  seasadj(cons) %>% log()


cbind(pib_d, cons_d) %>% 
  saveRDS(here('rdatos', 'desestacionalizado.rds'))

# Raiz unitaria 

## Niveles

### Augument dickey fuller

adf_pib <- adf.test(pib_d)
adf_cons <- adf.test(cons_d)

#pp_pib_pib_d <- kpss.test(pib_d)
#pp_pib_consd <- pp.test(cons_d)

## 1 diferencia

### Augument dickey fuller

adf_pib_d <- pib_d %>% diff %>% adf.test()
adf_cons_d<- cons_d %>% diff %>% adf.test()


## tabla
### t. test adf nivelec

tibble(
variable = rep(c('PIB percapita - log', 'Consumo Percapita - log'), 2),  

t_estadistico = c(
adf_pib$statistic[[1]],
adf_cons$statistic[[1]],
adf_pib_d$statistic[[1]],
adf_cons_d$statistic[[1]]
), 

### p_value
p_valor = c(
adf_pib$p.value[[1]],
adf_cons$p.value[[1]],
adf_pib_d$p.value[[1]],
adf_cons_d$p.value[[1]]
)
) %>% saveRDS(here('rdatos', 'raiz.rds'))

## Modelo Var


# Estacionalidad


PP.test(pib_d)
pp.test(pib_d, lag = 1)
ndiffs(pib_d)
ndiffs(cons_d)






