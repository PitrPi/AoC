rec <- c(3, 7)
pos1 = 1
pos2 = 2
new_rec <- function(rec, pos1, pos2) {
    add <- rec[(pos1-1 %% length(rec))+1] + rec[(pos2-1 %% length(rec))+1]
    add_ls <- strsplit(as.character(add), c())[[1]]
    add_ls <- strtoi(add_ls)
    rec <- c(rec, add_ls)
    pos1 <- (pos1 + rec[pos1]) %% length(rec) + 1
    pos2 <- (pos2 + rec[pos2]) %% length(rec) + 1
    return (list(rec, pos1, pos2))
}
num_rep <- 702831
for (i in 1:(num_rep-1+10)) {
    out <- new_rec(rec, pos1, pos2)
    rec <- out[[1]]
    pos1 <- out[[2]]
    pos2 <- out[[3]]
}
print(paste0(rec[(num_rep+1):(num_rep+10)], collapse = ""))
