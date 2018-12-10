inpt <- read.table("input.txt", sep="\n", stringsAsFactors = FALSE)
inpt_c <- inpt[,1]
start <- 
sapply(inpt, function(x) {
    regmatches(substr(x, 2, nchar(x)), regexpr("[A-Z]", substr(x, 2, nchar(x))))
})
stop <- 
    sapply(inpt, function(x) {
        regmatches(substr(x, 10, nchar(x)), regexpr("[A-Z]", substr(x, 10, nchar(x))))
    })
steps <- unique(c(start, stop))
done <- c()
free <- c()
while(length(done) < length(steps)) {
    free <- sort(unique(c(free, setdiff(setdiff(steps, unique(stop)), done))))
    done <- c(done, free[1])
    if (length(free) > 1) {
        free <- free[2:length(free)]
    } else {
        free <- c()
    }
    stop <- stop[!start %in% done]
    start <- start[!start %in% done]
    print(length(done))
}
paste0(done, collapse = "")

#part2
inpt <- read.table("input.txt", sep="\n", stringsAsFactors = FALSE)
inpt_c <- inpt[,1]
start <- 
    sapply(inpt_c, function(x) {
        regmatches(substr(x, 2, nchar(x)), regexpr("[A-Z]", substr(x, 2, nchar(x))))
    })
stop <- 
    sapply(inpt_c, function(x) {
        regmatches(substr(x, 10, nchar(x)), regexpr("[A-Z]", substr(x, 10, nchar(x))))
    })
start <- sapply(start, utf8ToInt)
start <- start - 4
stop <- sapply(stop, utf8ToInt)
stop <- stop - 4
steps <- unique(c(start, stop))
done <- c()
free <- c()
working <- c()
timer <- 0
while(length(done) < length(steps)) {
    if (any(working == 0)) {
        done <- c(done, names(working)[working == 0])
        working <- working[working != 0]
    }
    stop <- stop[!start %in% done]
    start <- start[!start %in% done]
    free <- sort(unique(c(free, setdiff(setdiff(steps, unique(stop)), done))))
    free <- free[!free %in% names(working)]
    if (length(working) < 5 & length(free) > 0) {
        new_names <- c(names(working), free[1:(5-length(working))])
        working <- c(working, free[1:(5-length(working))])
        names(working) <- new_names
        working <- working[!is.na(working)]
        free <- free[!free %in% names(working)]
    }
    working <- working - 1
    timer <- timer + 1
    if (timer %% 20 == 0) print(timer)
}
timer - 1

#part2 tst
inpt <- read.table("input.txt", sep="\n", stringsAsFactors = FALSE)
inpt <- "Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."
inpt_c <- inpt[,1]
inpt_c <- strsplit(inpt, "\n")[[1]]
start <- 
    sapply(inpt_c, function(x) {
        regmatches(substr(x, 2, nchar(x)), regexpr("[A-Z]", substr(x, 2, nchar(x))))
    })
stop <- 
    sapply(inpt_c, function(x) {
        regmatches(substr(x, 10, nchar(x)), regexpr("[A-Z]", substr(x, 10, nchar(x))))
    })
start <- sapply(start, utf8ToInt)
start <- start - 4 - 60
stop <- sapply(stop, utf8ToInt)
stop <- stop - 4 - 60
steps <- unique(c(start, stop))
done <- c()
free <- c()
working <- c()
timer <- 0
while(length(done) < length(steps)) {
    if (any(working == 0)) {
        done <- c(done, names(working)[working == 0])
        working <- working[working != 0]
    }
    stop <- stop[!start %in% done]
    start <- start[!start %in% done]
    free <- sort(unique(c(free, setdiff(setdiff(steps, unique(stop)), done))))
    free <- free[!free %in% names(working)]
    if (length(working) < 2 & length(free) > 0) {
        new_names <- c(names(working), free[1:(2-length(working))])
        working <- c(working, free[1:(2-length(working))])
        names(working) <- new_names
        working <- working[!is.na(working)]
        free <- free[!free %in% names(working)]
    }
    working <- working - 1
    timer <- timer + 1
    if (timer %% 20 == 0) print(timer)
}
timer