library(tidyverse)
library(broom)
library(here)
library(magrittr)
library(fpp2)
library(tseries)
library(kableExtra)
theme_set(theme_bw())
options(scipen=999)
m_var <- vars::VAR 
read_rds1 <- function(path){
  readr::read_rds(here(paste0(path, ".rds")))
}
  

leer_y_borrar <- function(carpeta1, carpeta2, tipo = "xlsx", name = "h"){
  library(tidyverse)
  library(here)
  dirc <- here(carpeta1, carpeta2)
  if(tipo == "xlsx"){
    library(readxl)
    a <- read_xlsx(dirc)
  }
  name_direccion <- here(carpeta1, paste0(name, ".rds"))
  
  a %>% 
    saveRDS(name_direccion)
  }

#install.packages("fpp2")

descomponer_ts <- function(df, variable = "NULL", t = "Descomposición ", type = "multiplicative"){
  var <- df[, variable] %>% 
    decompose(type = type) 
  plot <- var %>% 
    autoplot(ts.colour = "#003f5c") +
    xlab("Tiempo") + 
    ggtitle(glue::glue(t, "de la variable {variable}"))
  return(plot)
}



estacional <- function(df){

  consumo <- df[, 1] %>% decompose(type = "multiplicative") %$% trend 
  fact_cons <- df[, 2] %>% decompose(type = "multiplicative") %$% trend 
  canon <- df[, 3] %>% decompose(type = "multiplicative") %$% trend 
  canon_minero <- df[, 4] %>% decompose(type = "multiplicative") %$% trend 
  canon_hidro <- df[, 5] %>% decompose(type = "multiplicative") %$% trend 
 f <- cbind(consumo, fact_cons, canon, canon_minero, canon_hidro)
  return(f)
}



table1 <- function(df){
  num <- colnames(df)
  
  for(i in 1:length(num)){
    varr <- paste("r", i, sep = ".")
    ldf <- df[, i] %>% log10() %>% adf.test()
    
    #dldf <- ldf[, i] %>% diff() %>% adf.test()
    #ddldf <- dldf[, i] %>% diff() %>% adf.test()
    alv <- list(ldf)#, ldf, dldf, ddldf)
  }
  return(alv)
}

round_df <- function(df, num){
  df %>% 
    mutate(across(is.numeric, round, num))
}


plot.armaroots <- function(x, xlab="Real", ylab="Imaginary",
                           main=paste("Inverse roots of", x$type,
                                      "characteristic polynomial"),
                           ...)
{
  oldpar <- par(pty='s')
  on.exit(par(oldpar))
  plot(c(-1,1), c(-1,1), xlab=xlab, ylab=ylab,
       type="n", bty="n", xaxt="n", yaxt="n", main=main, ...)
  axis(1, at=c(-1,0,1), line=0.5, tck=-0.025)
  axis(2, at=c(-1,0,1), label=c("-i","0","i"),
       line=0.5, tck=-0.025)
  circx <- seq(-1,1,l=501)
  circy <- sqrt(1-circx^2)
  lines(c(circx,circx), c(circy,-circy), col='gray')
  lines(c(-2,2), c(0,0), col='gray')
  lines(c(0,0), c(-2,2), col='gray')
  if(length(x$roots) > 0)
  {
    inside <- abs(x$roots) > 1
    points(1/x$roots[inside], pch=19, col='black')
    if(sum(!inside) > 0)
      points(1/x$roots[!inside], pch=19, col='red')
  }
}