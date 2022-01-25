library(plm)
library(punitroots)
library(broom)
options(scipen = 999)


panel_1_variable <- function(df, variable = NULL){
  df %>% 
    select(1:2, variable) %>% 
    pivot_wider(values_from = variable, names_from = reg) %>% 
    select(!anio) %>% 
    ts(start = 2007, frequency = 1) %>% 
    window() %>% 
    as.matrix()
}

#panel_unit_test <- funfunction(ts1_object, )
 # diff %>% 
  #autoplot()

library(magrittr)

tabla_raiz <- function(ts_df, variable = NULL){
  n <- c()
  test1 <- c("levinlin", "ips", "madwu")
  n[["levinlin"]] <- ts_df %>% 
    purtest(test = "levinlin", exo = "intercept", lag = "AIC", pmax = 2) %$%
    statistic %>% tidy
  n[["ips"]] <- ts_df %>% 
    purtest(test = "ips", exo = "intercept", lag = "AIC", pmax = 2) %$%
    statistic %>% tidy
  n[["madwu"]] <- ts_df %>% 
    purtest(test = "madwu", exo = "intercept", lag = "AIC", pmax = 2) %$%
    statistic %>% tidy
  invoke(bind_rows, n) %>% 
    select(!c(alternative, parameter)) %>% 
    mutate(Variable = variable) %>% 
    mutate(across(is.numeric, round, 4)) %>% 
    relocate(Variable, method) %>% 
    rename(Test = method) %>% 
    mutate(Test = case_when(
      str_detect(Test, "Levin") ~ "Levin Lin y Chu",
      str_detect(Test, "Pesaran") ~ "Im Pesaran Shin",
      str_detect(Test, "Wu") ~ "Maddala Wu"
    )) %>% 
    rename("Puebas de raíz unitaria de datos de panel" = Test)
}

ph_tidy <- function(x, ...){
  x %>% 
    tidy %>% 
    select(!any_of(c("parameter", "alternative", "df1", "df2"))) %>% 
    relocate(method, statistic, p.value) %>% 
    mutate(across(is.numeric, round, 4)) %>% 
    mutate(method = case_when( 
      str_detect(method, "individual") ~ "Efectos individuales",
      str_detect(method, "time effects") ~ "Multiplicadores de Lagrange | Breusch - Pagan (Efectos temporales)",
      str_detect(method, "(Breusch-Pagan)") ~ "Multiplicadores de Lagrange | Breusch - Pagan",
      str_detect(method, "correlation") ~ "Breusch-Godfrey/Wooldridge (Correlación serial)",
      str_detect(method, "Hausman") ~ "Hausman"
    )) %>% 
    mutate("Conclusión" = case_when(
      p.value < .05  && str_detect(method, "Hausman")~ "Efectos Fijos", 
      p.value >= .05 && str_detect(method, "Hausman")~ "Efectos aleatorios",
      p.value < .05  && str_detect(method, "individuales")~ "Efectos individuales", 
      p.value >= .05 && str_detect(method, "individuales")~ "No hay efectos individuales",
      p.value < .05  && str_detect(method, "temporales")~ "Efectos temporales", 
      p.value >= .05 && str_detect(method, "temporales")~ "No hay efectos temporales",
      p.value < .05  && str_detect(method, "Breusch - Pagan")~ "Diferencia cruzada entre individuos", 
      p.value >= .05 && str_detect(method, "Breusch - Pagan")~ "No hay diferencia entre individuos (se puede usar MCO)",
      p.value < .05  && str_detect(method, "Wooldridge")~ "Correlación serial", 
      p.value >= .05 && str_detect(method, "Wooldridge")~ "No hay correlación serial"
      )) %>% 
    rename(Test = method, Estadistico = statistic) 
    #kableExtra::kable()
}

#phtest(agri_d_fix, agri_d_ran) %>% 
#  ph_tidy()
#pFtest(agri_d_fixed, agri_d_fix) %>% 
#  tidy
#plmtest(agri_d_fixed, c("time"), type = ("bp")) %>% 
 # tidy
#plmtest(agri_d_pool, type = "bp") %>% 
#  ph_tidy
#pbgtest(agri_d_fixed) %>% 
#  ph_tidy
#panel_1_variable(df1, "banco") %>%
  #log %>% 
 # diff %>% 
  #tabla_raiz( "Banco") 
  
#none <- c()
#names1 <- names(df1)[3:length(df1)]
#for(i in names1){
#  none[[i]] <- panel_1_variable(df1, i) %>% 
#    tabla_raiz(i)
#}

#df1 %>% 
#  group_by(reg) %>% 
#  mutate(across(is.numeric, log))
#
#invoke(bind_rows, none)
