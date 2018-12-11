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
res <- which(mat_res == max(mat_res), arr.ind = TRUE)
print(ceiling(res/398))
print(res %% 398)
floor(((i+10)*j+8)*(i+10)/100)%%10-5
