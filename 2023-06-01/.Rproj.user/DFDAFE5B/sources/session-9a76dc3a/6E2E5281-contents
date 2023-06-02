# import alice in wonderland
text <- base::readRDS(url("https://slcladal.github.io/data/alice.rda", "rb"))

text <- text %>%
  # collapse lines into a single  text
  paste0(collapse = " ") %>%
  # remove superfluous white spaces
  str_squish()

mykwic <- quanteda::kwic(
  # define text
  quanteda::tokens(text), 
  # define search pattern
  pattern = "Alice") %>%
  # make it a data frame
  as.data.frame()

mykwic_longer <- kwic(
  # define text
  text, 
  # define search pattern
  pattern = "alice", 
  # define context window size
  window = 10) %>%
  # make it a data frame
  as.data.frame()