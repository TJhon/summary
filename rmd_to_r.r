#install.packages("librarian")

librarian::shelf(
  tidyverse
  , here
  , fs
  , knitr
)


full_path <- 
  here() |> 
  dir(recursive = T, full.names = T, pattern = ".rmd") |> 
  str_subset("README|lang|summary.rmd", negate = T) 



full_path_output <- 
  full_path |> 
  str_replace_all(".rmd$", ".r")

walk2(full_path, full_path_output, knitr::purl)
