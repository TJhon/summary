library(tidyverse)


set.seed(12)

bin <- c(0, 1)

dt <- 
  tibble(
  x1 = rnorm(100, 0, 1)
  , x2 = rnorm(100, 0, 1)
  , y = sample(bin, 100, replace = T) |> factor()
)  

dt


glm_filt <- glm(y ~ ., data = dt, family = binomial)



zero_one <- predict(glm_filt, type = 'response') 

dt$.predict <- zero_one
dt1 <- 
  dt |> 
  mutate(.predict = ifelse(.predict < 0.5, 0, 1) |> factor()) 
dt1 |> 
  yardstick::accuracy(y, .predict)

dt1 |> 
  pivot_longer(!c(x1, x2)) |> 
  ggplot() +
  aes(x1, x2, color = value) +
  geom_jitter() +
  facet_wrap(~name)
