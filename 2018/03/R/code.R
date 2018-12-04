inpt_ls <- strsplit(inpt, "\n")[[1]]
inpt_parse <- sapply(inpt_ls, gsub, pattern = ".*@ ", replacement = "")
mat_size <- 1001

fit_inpt <- function(inpt_parse, mat_size) {
    mtx <- matrix(0, nrow = mat_size, ncol = mat_size)
    for (i in 1:length(inpt_parse)) {
        coor <- regmatches(inpt_parse[i], regexpr("[0-9]*,[0-9]*", inpt_parse[i]))
        coor <- strtoi(strsplit(coor, ",")[[1]]) 
        coor <- coor + 1 # compensate for R indexing from 0
        if (any(coor == 0)) print(coor)
        size <- regmatches(inpt_parse[i], regexpr("[0-9]*x[0-9]*", inpt_parse[i]))
        size <- strtoi(strsplit(size, "x")[[1]])
        mtx[coor[1]:(coor[1]+size[1]-1), coor[2]:(coor[2]+size[2]-1)] <- mtx[coor[1]:(coor[1]+size[1]-1), coor[2]:(coor[2]+size[2]-1)] + 1 
    }
    mtx
}
output <- fit_inpt(inpt_parse, mat_size)
sum(output > 1)

#part2
fit_inpt2 <- function(inpt_parse, mtx) {
    for (i in 1:length(inpt_parse)) {
        coor <- regmatches(inpt_parse[i], regexpr("[0-9]*,[0-9]*", inpt_parse[i]))
        coor <- strtoi(strsplit(coor, ",")[[1]]) 
        coor <- coor + 1 # compensate for R indexing from 0
        if (any(coor == 0)) print(coor)
        size <- regmatches(inpt_parse[i], regexpr("[0-9]*x[0-9]*", inpt_parse[i]))
        size <- strtoi(strsplit(size, "x")[[1]])
        if (all(mtx[coor[1]:(coor[1]+size[1]-1), coor[2]:(coor[2]+size[2]-1)] == 1)){
            return(i)
        }
    }
}
num <- fit_inpt2(inpt_parse, output)
regmatches(inpt_ls[num], regexpr("#[0-9]*", inpt_ls[num]))
