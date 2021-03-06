## ---- include=F-----------------------------------------------------------------------------------------------------------------------------------------
library(here)
library(lubridate)
d <- read_rds(here('rdatos', '00datos.rds')) 


## -------------------------------------------------------------------------------------------------------------------------------------------------------
d %>% 
  mutate(fecha = parse_date_time(fecha, 'ym')) %>% drop_na() %>% 
  kable()


## -------------------------------------------------------------------------------------------------------------------------------------------------------
theme_set(theme_bw())
p <- d %>% 
  filter(sector == 'nacional', sector1 == 'gas84') %>%
  arrange(fecha) %>% 
  mutate(f = year(fecha)) %>% 
  mutate(pb = 101.4928,
         ipc = (ipc/pb)*100) %>% 
  select(-fecha, -sector1, -sector, -pb, -f) %>%
  ts(start = 2010, frequency = 12) 
  
saveRDS(p, here('rdatos', '01ts.rds'))
autoplot(p, facets = T) + ylab("")


## -------------------------------------------------------------------------------------------------------------------------------------------------------
#p %>% View()

Observacion01 <- p[, 1]


d1 <- stl(log(Observacion01), s.window = 'periodic')
d1 %>% autoplot()


## -------------------------------------------------------------------------------------------------------------------------------------------------------
library(forecast)
a1 <- exp(seasadj(d1))

autoplot(cbind(Observacion01, Destacionalizado=a1)) +
  xlab("Anio") + ylab("PIB (miles de milloes)")



## -------------------------------------------------------------------------------------------------------------------------------------------------------
Observacion02 <- p[, 2]


d2 <- stl(log(Observacion02), s.window = 'periodic')
d2 %>% autoplot()


## -------------------------------------------------------------------------------------------------------------------------------------------------------
a2 <- exp(seasadj(d2))

autoplot(cbind(Observacion02, Destacionalizado=a2)) +
  xlab("Anio") + ylab("Consumo electrico (Wh)")



## ---- include=FALSE-------------------------------------------------------------------------------------------------------------------------------------
library(vars)
dat <- cbind(a1, a2, p[, 3:4]) %>% 
  as_tsibble() %>% 
  spread(key, value) %>% 
  rename(pib = 2, 
         consumo = 3, 
         ipc = 4, 
         pob = 5) %>% 
  mutate(pib_p = pib/pob*10^7,
         c_p = consumo/pob*10^4, 
         t_pibp = (pib_p - lag(pib_p))/pib_p*100,
         t_c = (c_p - lag(c_p))/c_p*100) %>% 
  arrange(index) 

dep <- dat[, 7:9] %>% 
  ts(start = 2010, frequency = 12)
dep1 <- dat[, 4]


dat1 <- cbind(dep, dep1) %>% 
  as_tibble() %>% 
  rename(comsumo = 1, tcpbi = 2, tcons = 3, ipc = 4 ) %>% drop_na()

dat1 <- ts(dat1, start = 2010, frequency = 12)
dat1 %>% saveRDS(here('rdatos', '03est.rds'))

VARselect(dat1)
m1 <- VAR(data, p = 2, type = 'const', season = NULL)
m1 %>% summary()

autoplot(dat, facets = T)

