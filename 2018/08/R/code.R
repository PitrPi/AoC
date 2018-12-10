inpt <- read.table("input.txt", sep="\n", stringsAsFactors = FALSE)
inpt_c <- strsplit(inpt[1,1], " ")[[1]]
inpt_c <- strtoi(inpt_c)
num_child <- inpt_c[1]
num_metad <- inpt_c[2]
meta_all <- c()
get_meta <- function(data) {
    num_child <- data[1]
    num_metad <- data[2]
    data <- data[3:length(data)]
    while (num_child > 0) {
        data <- get_meta(data)
        num_child <- num_child - 1
    }
        meta_all <<- c(meta_all, data[1:num_metad])
        return(data[(1+num_metad):length(data)])
}
get_meta(inpt_c)
sum(meta_all)

#part 2
inpt <- read.table("input.txt", sep="\n", stringsAsFactors = FALSE)
inpt_c <- strsplit(inpt[1,1], " ")[[1]]
inpt_c <- strtoi(inpt_c)
num_child <- inpt_c[1]
num_metad <- inpt_c[2]
get_meta <- function(data) {
    num_child <- data[1]
    num_metad <- data[2]
    data <- data[3:length(data)]
    if (num_child == 0){
        return(list(data[(1+num_metad):length(data)], sum(data[1:num_metad])))
    } else {
        child_value <- c()
        for (i in 1:num_child) {
            data_both <- get_meta(data)
            data <- data_both[[1]]
            value <- data_both[[2]]
            child_value <- c(child_value, value)
        }
    }
    my_value <- c(0)
    for (j in 1:num_metad) {
        if (data[j] <= num_child){
            my_value <- my_value + child_value[data[j]]
        }
    }
    return(list(data[(1+num_metad):length(data)], my_value))
}
out <- get_meta(inpt_c)
out[[2]]

