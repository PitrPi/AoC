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
init_ls_ext <- c(rep("-", 40), init_ls, rep("-", 40))
inst_die <- c()
inst_born  <- c()
for (i in 1:length(inst_ls)) {
    if (grepl("=> #", inst_ls[i])) {
        inst_born <- c(inst_born, strtrim(inst_ls[i], 5))
    } else {
        inst_die <- c(inst_die, strtrim(inst_ls[i], 5))
    }
}

for (i in 1:20) {
    act <- c()
    for (j in 1:(length(init_ls_ext)-4)) {
        act <- c(act, paste(init_ls_ext[j:(j+4)], collapse=""))
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
        init_ls_ext[matches_die[j]] <- "-"
    }
    for (j in 1:length(matches_born)) {
        init_ls_ext[matches_born[j]] <- "#"
    }
}

init_b <- c()
for (i in 1:length(init_ls_ext)) {
    if (init_ls_ext[i] == "#"){
        init_b <- c(init_b, TRUE)
    } else {
        init_b <- c(init_b, FALSE)
    }
}

sum(((1:length(init_b))-41)*init_b)
