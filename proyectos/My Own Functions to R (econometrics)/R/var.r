me_irf <- function(var_model, impulso, respuesta = NULL, numero = 20){
  vars::irf(var_model, impulse = impulso, reponse = respuesta, 
            n.ahead = numero, ortho = T, cumulative = F, boot = T, ci = 0.70)
}

extract_varirf <- function(...){
  
  varirf_object <- list(...) #list one or more varirf input objects
  
  get_vec_length <- function(list_item){nrow(list_item[[1]][[1]])}
  
  if (!("varirf" %in% mapply(class, varirf_object))){
    stop("this function only accepts 'varirf' class objects")
  }
  
  if (length(unique(mapply(class, varirf_object)))!=1){
    stop("all input items must be 'varirf' class objects")
  }    
  if (length(unique(mapply(get_vec_length, varirf_object)))!=1){
    stop("all irf vectors must have the same length")   
  }  
  
  period <- as.data.frame(0:(nrow(varirf_object[[1]][[1]][[1]])-1)) 
  names(period) <- "period"
  
  for (l in 1:length(varirf_object)){
    for (i in 1:3){
      for (j in 1:dim(varirf_object[[l]][[i]][[1]])[2]){
        for (k in 1:length(varirf_object[[l]][[1]])){
          temp_colname <- paste(names(varirf_object[[l]][i]), #vector type (irf, lower, or upper)
                                names(varirf_object[[l]][[i]])[k], #impulse name
                                colnames(varirf_object[[l]][[i]][[k]])[j], #response name
                                sep = "-")
          
          temp <- as.data.frame(varirf_object[[l]][[i]][[k]][, j]) #extracts the vector
          
          names(temp) <- temp_colname #add the column name (vectortype_impulse_reponse)
          period <- cbind(period, temp) 
        }
        
      }
    }
  }
  names(period) <- tolower(names(period))
  period %<>% rename(Tiempo = period)
  return(period %>% as_tibble)
}

# para objetos creados por extract_varirf

irf_plot <- function(df, impulso, respuesta){
  variable <- paste0(impulso, "_", respuesta)
  ggplot(df, 
         aes_string("Tiempo", 
                    paste0("irf_", variable),
                    ymin = paste0("lower_", variable),
                    ymax = paste0("upper_", variable))) + 
    geom_ribbon(fill = "grey", alpha = .2, color = "grey", linetype = "dashed") +
    geom_line(color = "#003f5c") +
    geom_hline(yintercept = 0, color = "red") +
    ylab(toupper(respuesta)) + 
    xlab("Trimestre") +
    ggtitle(paste("Respuesta de impulso ortogonal,", impulso, expression("->"), respuesta)) +
    theme(plot.title = element_text(hjust = .5),
          axis.title.y = element_text(size = 11))
}


# para objetos creados por extract_varirf
irf_plot_all <- function(df, Unidad_tiempo = "Trimestre", colores = c("#20603b", "#E46726", "#2b0545", "#045762")){
  color = colores
  rango <- df %>% 
    select(Tiempo, !contains("irf")) %>% 
    pivot_longer(!Tiempo) %>%
    separate(name, c("rango", "causa", "efecto"), sep = "-") %>% 
    pivot_wider(names_from = rango, values_from = value) 
  irf <- 
    df %>% 
    select(Tiempo, contains("irf")) %>% 
    pivot_longer(!Tiempo) %>% 
    separate(name, c("irf", "causa", "efecto"), sep = "-") %>%
    select(!irf) %>% 
    rename(irf = value)
  union1 <- full_join(rango, irf, by = c("Tiempo", "efecto", "causa"))
  plot_irf_all <- 
    union1 %>%   
    ggplot(aes(x = Tiempo, y = irf, fill = efecto, color = efecto)) +
    geom_line(size = 1) + 
    geom_ribbon(aes(ymin = lower, ymax = upper), alpha = .2, color = "grey", linetype = "dashed") +
    geom_hline(yintercept = 0, color = "red") + 
    facet_wrap(~efecto, ncol = 2, scales = "free") +
    theme(legend.position = "none") +
    scale_color_manual(values = color) +
    scale_fill_manual(values = color) + 
    xlab(Unidad_tiempo) + 
    ylab("")
  print(plot_irf_all)
}


## Pruebas
