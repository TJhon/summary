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

