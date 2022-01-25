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


