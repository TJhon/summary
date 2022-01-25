# Seleccionar todo y dar click en `RUN`, 

# Esta en la parte superior derecha de este panel


zcon <- c("tidyverse", "kableExtra", "here", "readr", "glue" , "tsibble", "e1071", "ggfortify", "ggplottimeseries", 
          "GGally", "lubridate", "vars", "Stargazer", "lmtest")


if(!require(zcon)) install.packages(zcon, dependencies = T)