inpt_ls <- strsplit(inpt, "\n")[[1]] #load input
inpt2 <- sapply(inpt_ls, strsplit, ", ")
inpt2 <- sapply(inpt2, strtoi)
inpt_mat <- t(inpt2)
inpt_mat_shift <- inpt_mat + 200

matr <- matrix("0", nrow = 400, ncol = 400)
for (i in 1:400) {
    for (j in 1:400) {
        dist <- 10000000
        closest <- 0
        for (k in 1:nrow(inpt_mat)) {
            if (abs(inpt_mat[k,1]-i) + abs(inpt_mat[k,2]-j) < dist) {
                dist <- abs(inpt_mat[k,1]-i) + abs(inpt_mat[k,2]-j)
                closest <- k
            } else if ((abs(inpt_mat[k,1]-i) + abs(inpt_mat[k,2]-j) == dist)) {
                closest <- 0
                next
            }
        }
        matr[i,j] <- closest
    }
}
out <- sort(table(matr))
infinit <- (unique(c(matr[1, 1:400], matr[1:400, 400], matr[1:400, 1], matr[400, 1:400])))
#infinit <- sort(strtoi(infinit))
out[setdiff(names(out), infinit)]

inpt_ls <- strsplit(inpt, "\n")[[1]]
inpt2 <- sapply(inpt_ls, strsplit, ", ")
inpt2 <- sapply(inpt2, strtoi)
inpt_mat <- t(inpt2)
inpt_mat <- inpt_mat + 1
inpt_mat_example <- matrix(c(2,2,2,7,4,5,6,6,9,4,9,10), ncol = 2, byrow = TRUE)
matr <- matrix(0, nrow = 401, ncol = 401)
for (i in 1:401) {
    for (j in 1:401) {
        for (k in 1:nrow(inpt_mat)) {
                dist <- abs(inpt_mat[k,1]-i) + abs(inpt_mat[k,2]-j)
                matr[i,j] <- matr[i,j] + dist 
        }
    }
}
matr_t <- matr < 10000
table(matr < 10000)
write.csv2(matr, "mat.csv")
out <- sort(table(matr))
infinit <- (unique(c(matr[1, 1:400], matr[1:400, 400], matr[1:400, 1], matr[400, 1:400])))
#infinit <- sort(strtoi(infinit))
out[setdiff(names(out), infinit)]
