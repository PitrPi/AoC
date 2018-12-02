library(stringdist)
inpt_ls <- strsplit(inpt, "\n")

a <- 0
b <- 0
for (i in 1:length(inpt_ls[[1]])){
    tmp <- strsplit(inpt_ls[[1]][i], split=c())
    tbl <- table(tmp)
    if (2 %in% tbl) {
        a <- a+1
    }
    if (3 %in% tbl) {
        b <- b+1
    }
}


print(a*b)

levenshtein <- stringdistmatrix(inpt_ls[[1]])
mtx <- as.matrix(levenshtein)

coor1 <- ceiling(which(mtx == 1)[1]/dim(mtx)[1])
coor2<- (which(mtx == 1)[1] %% dim(mtx)[1])
coor1str <- strsplit(inpt_ls[[1]][coor1], split=c())[[1]]
coor2str <- strsplit(inpt_ls[[1]][coor2], split=c())[[1]]
out <- c()
for (i in 1:length(coor1str)){
    if (coor1str[i] == coor2str[i]) {
        out <- c(out, coor1str[i])
    }
}
paste0(out, collapse = "")
