init <- "##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#."
inst <- "..#.. => .
..#.# => .
#.#.. => .
.#..# => .
#.... => .
....# => .
.#.#. => #
#.### => .
####. => .
..... => .
.#... => #
##### => #
.#### => .
#..#. => #
#...# => #
.###. => .
###.# => #
...## => #
#.##. => #
.#.## => #
##.#. => #
...#. => .
..### => #
###.. => #
##... => .
..##. => .
.##.# => .
##.## => .
.##.. => .
##..# => #
#.#.# => .
#..## => #"
init <- gsub("\\.", "-", init)
inst <- gsub("\\.", "-", inst)
inst_ls <- strsplit(inst, "\n")[[1]]
init_ls <- strsplit(init, c())[[1]]

inst_die <- c()
inst_born  <- c()
for (i in 1:length(inst_ls)) {
    if (grepl("=> #", inst_ls[i])) {
        inst_born <- c(inst_born, strtrim(inst_ls[i], 5))
    } else {
        inst_die <- c(inst_die, strtrim(inst_ls[i], 5))
    }
}
init_ls_trim <- init_ls
states <- c()
cont <- TRUE
ticker <- 0
trimmed_left <- 0
while (cont) {
    init_ls_padded <- c(rep("-", 5), init_ls_trim, rep("-", 5)) #pad with -
    trimmed_left <- trimmed_left - 5
    act <- c()
    for (j in 1:(length(init_ls_padded)-4)) {
        act <- c(act, paste(init_ls_padded[j:(j+4)], collapse=""))
    }
    matches_die <- list()
    matches_born <- list()
    for (j in 1:length(inst_born)){
        matches_born[[j]] <- grep(inst_born[j], act) + 2
    }
    for (j in 1:length(inst_die)){
        matches_die[[j]] <- grep(inst_die[j], act) + 2
    }
    matches_born  <- unlist(matches_born)
    matches_die <- unlist(matches_die)
    for (j in 1:length(matches_die)) {
        init_ls_padded[matches_die[j]] <- "-"
    }
    for (j in 1:length(matches_born)) {
        init_ls_padded[matches_born[j]] <- "#"
    }
    hashes <- which(init_ls_padded == "#")
    trimmed_left <- trimmed_left + hashes[1] - 1
    init_ls_trim <- init_ls_padded[hashes[1]:hashes[length(hashes)]]
    init_ls_paste <- paste0(init_ls_trim, collapse = "")
    if (init_ls_paste %in% states | ticker > 5E9) {
        cont <- FALSE
    }
    states <- c(states, init_ls_paste)
    ticker <- ticker + 1
    print(trimmed_left)
    if (ticker %% 1000 == 0) print(ticker)
}

init_b <- c()
for (i in 1:length(init_ls_trim)) {
    if (init_ls_trim[i] == "#"){
        init_b <- c(init_b, TRUE)
    } else {
        init_b <- c(init_b, FALSE)
    }
}

final_shift <- 50000000000 - ticker + trimmed_left - 1
options(scipen=999)
sum(((1:length(init_b))+final_shift)*init_b)
