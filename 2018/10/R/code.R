inpt <- readChar("input.txt", file.info("input.txt")$size)
inpt_ls <- strsplit(inpt, "\n")[[1]]
X_start <- sapply(inpt_ls, function(x) {
    regmatches(x, regexpr("-?[0-9]+", x))
})
X_start <- sapply(X_start, strtoi)
inpt_ls <- sapply(inpt_ls, substring, 17)
Y_start <- sapply(inpt_ls, function(x) {
    regmatches(x, regexpr("-?[0-9]+", x))
})
Y_start <- sapply(Y_start, strtoi)
inpt_ls <- sapply(inpt_ls, substring, 10)
X_vel <- sapply(inpt_ls, function(x) {
    regmatches(x, regexpr("-?[0-9]+", x))
})
X_vel <- sapply(X_vel, strtoi)
inpt_ls <- sapply(inpt_ls, substring, 14)
Y_vel <- sapply(inpt_ls, function(x) {
    regmatches(x, regexpr("-?[0-9]+", x))
})
Y_vel <- sapply(Y_vel, strtoi)

min_width <- 1e7
min_height <- 1e7
for (i in 1:100000) {
    X_start <- X_start + X_vel
    Y_start <- Y_start + Y_vel
    mat_size_x <- max(X_start) - min(X_start)
    if (mat_size_x < min_width) {
        min_width <- mat_size_x
        min_width_i <- i
        X_start_best <- X_start
    }
    mat_size_y <- max(Y_start) - min(Y_start)
    if (mat_size_y < min_height) {
        min_height <- mat_size_y
        min_height_i <- i
        Y_start_best <- Y_start
    }
    
}

mat_size_x <- max(X_start_best) - min(X_start_best)
mat_size_y <- max(Y_start_best) - min(Y_start_best)
X_start_best_shift <- X_start_best - min(X_start_best) + 1
Y_start_best_shift <- Y_start_best - min(Y_start_best) + 1
mat <- matrix(".", ncol = mat_size_y + 1, nrow = mat_size_x + 1)
cat("\014") 
for (j in 1:length(X_start_best)) {
    mat[X_start_best_shift[j], Y_start_best_shift[j]] <- "#"
}
mat
# part 2
min_height_i
