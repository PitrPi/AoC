inpt <- readChar("input.txt", file.info("input.txt")$size)
nchar(inpt)
#part 1
inpt1 <- gsub("\n\n\n.*", "", inpt)
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
    count <- 0
    before <- strtoi(x[1:4])
    after <- strtoi(x[9:12])
    inst <- strtoi(x[5:8]) + 1 #indexing 1
    if (after[inst[4]] == before[inst[2]] + before[inst[3]]) {
        count <- count + 1
    }
    if (after[inst[4]] == before[inst[2]] + inst[3] - 1) { #+1 
        count <- count + 1
    }
    if (after[inst[4]] == before[inst[2]] * before[inst[3]]) {
        count <- count + 1
    }
    if (after[inst[4]] == before[inst[2]] * inst[3] - 1) { #+1 
            count <- count + 1
    }    
    if (after[inst[4]] == bitwAnd(before[inst[2]],before[inst[3]])) {
        count <- count + 1
    }
    if (after[inst[4]] == bitwAnd(before[inst[2]], (inst[3] - 1))) { #+1 
            count <- count + 1
    }
    if (after[inst[4]] == bitwOr(before[inst[2]], before[inst[3]])) {
        count <- count + 1
    }
    if (after[inst[4]] == bitwOr(before[inst[2]],(inst[3] - 1))) { #+1 
            count <- count + 1
    }    
    if (after[inst[4]] == before[inst[2]]) {
        count <- count + 1
    }
    if (after[inst[4]] == inst[2] - 1) { #+1 
            count <- count + 1
    }    
    if (after[inst[4]] == (before[inst[2]] > before[inst[3]])) {
        count <- count + 1
    }
    if (after[inst[4]] == (before[inst[2]] > (inst[3] - 1))) { #+1 
            count <- count + 1
    }    
    if (after[inst[4]] == ((inst[2] - 1) > before[inst[3]])) {
        count <- count + 1
    }
    if (after[inst[4]] == (before[inst[2]] == (inst[3] - 1))) { #+1 
            count <- count + 1
    }    
    if (after[inst[4]] == (before[inst[2]] == before[inst[3]])) {
        count <- count + 1
    }
    if (after[inst[4]] == ((inst[2] - 1) == before[inst[3]])) { #+1 
            count <- count + 1
    }
    return(count)
}
count3 <- 0
for (i in 1:(length(inpt_ls)/12)) {
    if (nmatch(inpt_ls[((i-1)*12+1):((i)*12)]) >= 3) {
        count3 <- count3 + 1
    }
}
