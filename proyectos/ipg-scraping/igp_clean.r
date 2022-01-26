librarian::shelf(
    tidyverse
    , readxl
    , janitor
    , lubridate
)

igp_begin <- read_excel("data/IGP_datos_sismicos.xlsx") |> clean_names()
igp_scrapped <- read_csv("data/igp_2022.csv", show_col_types = F) |> clean_names()
head(igp_scrapped)
igp_scrapped_clean <- 
    igp_scrapped |> 
    separate(date, c("date", "hour"), sep = "-") |> 
    mutate(
        across(
            where(is.character), str_trim
        ),
        m = parse_number(m)
        , date = dmy(date)
        , hour = hms(hour)
           ) |> 
    relocate(m, .after = prof) |> 
    rename(magn = m, intensi_km = prof) |> 
    arrange(desc(date))

colnames(igp_begin) <- names(igp_scrapped_clean)
igp_begin_cl <- 
    igp_begin |> 
    mutate(
        date = dmy(date)
        , hour = hms(hour)
        , across(where(is.character), as.numeric)
    ) |> 
    arrange(desc(date))

bind_rows(igp_scrapped_clean, igp_begin_cl) |> 
    mutate(
        alert = case_when(
            magn < 4.5 ~ "Green"
            , magn > 6.0 ~ "Red"
            , T ~ "Yellow"
        )
    ) |> 
    write.csv("output/igp.csv", row.names = F)
