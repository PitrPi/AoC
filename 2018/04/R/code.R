inpt_ls <- strsplit(inpt, "\n")[[1]]
inpt_tm <- c()
inpt_ac <- c()
for (i in 1:length(inpt_ls)) {
    inpt_tm <- c(inpt_tm, substr(inpt_ls[i], 2, 17)) 
    inpt_ac <- c(inpt_ac, substring(inpt_ls[i], 20))
}
inpt_tm_sorted <- sort(inpt_tm)
inpt_tm_strip <- sapply(inpt_tm_sorted, substr, 15, 16)
inpt_ac_sorted <- inpt_ac[order(inpt_tm)]
inpt_parse <- c()
for (i in 1:length(inpt_ac_sorted)) {
    if (substr(inpt_ac_sorted[i], 1, 1) == "G") {
        inpt_parse <- c(inpt_parse, gsub("[^0-9]", "", inpt_ac_sorted[i]))
    } else if (substr(inpt_ac_sorted[i], 1, 1) == "f") {
        inpt_parse <- c(inpt_parse, "+")
    } else {
        inpt_parse <- c(inpt_parse, "-")
    }
}
final <- list()
grnum <- 0
for (i in 1:length(inpt_parse)) {
    if (inpt_parse[i] != "+" & inpt_parse[i] != "-") {
        grnum <- inpt_parse[i]
        if (is.null(final[grnum][[1]])) {
            final[grnum][[1]] <- matrix(rep(0, 60), nrow=1)
        } else {
            final[grnum][[1]] <- rbind(rep(0, 60), final[grnum][[1]])
        }
    } else {
        if (inpt_parse[i] == "+") {
            final[grnum][[1]][1, inpt_tm_strip[i]:60] <- 1
        } else {
            final[grnum][[1]][1, inpt_tm_strip[i]:60] <- 0
        }
    }
}
guard <- names(which(sapply(final, sum) == max(sapply(final, sum))))
which(apply(final[[guard]], 2, sum) == max(apply(final[[guard]], 2, sum))) * strtoi(guard)

# part 2
pt2 <- as.matrix(sapply(final, apply, 2, sum))
ans <- which(sapply(final, apply, 2, sum)==max(sapply(final, apply, 2, sum)), arr.ind = TRUE)
strtoi(names(final)[ans[1,2]]) * ans[1,1]
