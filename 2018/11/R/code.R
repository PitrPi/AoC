mat <- matrix(0, ncol=400, nrow=400) 
for (i in 1:400) {
    for (j in 1:400) {
        mat[i, j] <- floor(((i+10)*j+9306)*(i+10)/100)%%10-5
    }
}
mat_res <- matrix(0, ncol=398, nrow=398)
for (i in 1:398) {
    for (j in 1:398) {
        mat_res[i, j] <- sum(mat[i:(i+2), j:(j+2)])
    }
}
res <- which(mat_res == max(mat_res), arr.ind = FALSE)
print(ceiling(res/398))
print(res %% 398)
res <- which(mat_res == max(mat_res), arr.ind = TRUE)
res

# part2
mat <- matrix(0, ncol=400, nrow=400) 
for (i in 1:400) {
    for (j in 1:400) {
        mat[i, j] <- floor(((i+10)*j+18)*(i+10)/100)%%10-5
    }
}
k <- 16

best_for_k <- rep(0, 300)
for (k in 0:299) {
    mat_res <- matrix(0, ncol=400-k, nrow=400-k)
    for (i in 1:(400-k)) {
        for (j in 1:(400-k)) {
            mat_res[i, j] <- sum(mat[i:(i+k), j:(j+k)])
        }
    }
    best_for_k[k+1] <- max(mat_res)
    # names(best_for_k)[k+1] <- paste(which(mat_res == max(mat_res), arr.ind = TRUE))
    print(k)
}

k <- which(best_for_k == max(best_for_k))
mat_res <- matrix(0, ncol=400-k, nrow=400-k)
for (i in 1:(400-k)) {
    for (j in 1:(400-k)) {
        mat_res[i, j] <- sum(mat[i:(i+k), j:(j+k)])
    }
}

# names(best_for_k)[k+1] <- paste(which(mat_res == max(mat_res), arr.ind = TRUE))
print(k)
dim(mat_res)
res <- which(mat_res == max(mat_res), arr.ind = TRUE)
res
k <- 13
mat_res[232,144]
mat_res[233,144]
i <- 90
j <- 269

