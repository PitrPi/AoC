inpt <- readChar("input.txt", file.info("input.txt")$size)
nchar(inpt)
#part 1
inpt1 <- gsub("\n\n\n.*", "", inpt)
inpt2 <- gsub(".*\n\n\n", "", inpt)
inpt2 <- gsub("[^0-9]", ",", inpt2)
inpt2 <- gsub(",+", ",", inpt2)
nchar(inpt1)
inpt1 <- gsub("[^0-9]", ",", inpt1)
inpt1 <- gsub(",+", ",", inpt1)
# regmatches(x, regexpr("-?[0-9]+", x))
inpt_ls <- strsplit(inpt1, ",")[[1]]
inpt_ls <- inpt_ls[2:(length(inpt_ls))]
# inpt_l <- lapply(inpt_ls, strsplit, "\n")
# inpt_l <- gsub("[^0-9]", "", inpt_l)
# inpt_l <- strsplit(inpt_l, c())
# inpt_num <- sapply(inpt_l, strtoi)[,1]
nmatch <- function(x) {
    count <- c()
    before <- strtoi(x[1:4])
    after <- strtoi(x[9:12])
    inst <- strtoi(x[5:8]) + 1 #indexing 1
    if (after[inst[4]] == before[inst[2]] + before[inst[3]]) {
        count <- c(count, 1)
    }
    if (after[inst[4]] == before[inst[2]] + inst[3] - 1) { #+1 
        count <- c(count, 2)
    }
    if (after[inst[4]] == before[inst[2]] * before[inst[3]]) {
        count <- c(count, 3)
    }
    if (after[inst[4]] == before[inst[2]] * inst[3] - 1) { #+1 
        count <- c(count, 4)
    }    
    if (after[inst[4]] == bitwAnd(before[inst[2]],before[inst[3]])) {
        count <- c(count, 5)
    }
    if (after[inst[4]] == bitwAnd(before[inst[2]], (inst[3] - 1))) { #+1 
        count <- c(count, 6)
    }
    if (after[inst[4]] == bitwOr(before[inst[2]], before[inst[3]])) {
        count <- c(count, 7)
    }
    if (after[inst[4]] == bitwOr(before[inst[2]],(inst[3] - 1))) { #+1 
        count <- c(count, 8)
    }    
    if (after[inst[4]] == before[inst[2]]) {
        count <- c(count, 9)
    }
    if (after[inst[4]] == inst[2] - 1) { #+1 
        count <- c(count, 10)
    }    
    if (after[inst[4]] == (before[inst[2]] > before[inst[3]])) {
        count <- c(count, 11)
    }
    if (after[inst[4]] == (before[inst[2]] > (inst[3] - 1))) { #+1 
        count <- c(count, 12)
    }    
    if (after[inst[4]] == ((inst[2] - 1) > before[inst[3]])) {
        count <- c(count, 13)
    }
    if (after[inst[4]] == (before[inst[2]] == (inst[3] - 1))) { #+1 
        count <- c(count, 14)
    }    
    if (after[inst[4]] == (before[inst[2]] == before[inst[3]])) {
        count <- c(count, 15)
    }
    if (after[inst[4]] == ((inst[2] - 1) == before[inst[3]])) { #+1 
        count <- c(count, 16)
    }
    return(count)
}
out <- list()
for (i in 1:(length(inpt_ls)/12)) {
    out[[i]] <- c(inpt_ls[(i-1)*12+5],
                  nmatch(inpt_ls[((i-1)*12+1):((i)*12)]))
}
out[sapply(out, length) == 2]
15 5
# out <- lapply(out, gsub, pattern = "task_15", replacement = "")
# out[sapply(out, length) == 2]
