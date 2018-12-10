add_marble <- function (marble, circle) {
    if (length(circle) > 2) {
        if ((marble %% 23) != 0) {
            return(list("circle" = c(marble, circle[3:length(circle)], circle[1:2]),
                        "score" = 0))
        } else {
            return(list("circle" = c(circle[(length(circle)-5) : length(circle)],
                                     circle[1:(length(circle)-7)]), 
                        "score" = marble + circle[length(circle)-6]))
        }
    } else if (length(circle) == 2) {
        return(list("circle" = c(2, 1, 0),
                    "score" = 0))
    } else if (length(circle) == 1) {
        return(list("circle" = c(1, 0),
                    "score" = 0))
    } else {
        return(list("circle" = c(0),
                    "score" = 0))
    }
}
num_mar <- 71787 #part1
num_mar <- 7178700 #part2
num_plr <- 463
scr <- rep(0, num_plr)
names(scr) <- 1:num_plr
circle <- c(0)
count <- 0
for (i in 1:num_mar){
    res <- add_marble(i, circle)
    circle <- res[["circle"]]
    scr[((i-1) %% num_plr)+1] <- scr[((i-1) %% num_plr)+1] + res[["score"]]
    if (i %% 10000 == 0) {
        print(i)
        print(Sys.time())
    }
}
print(max(scr))
scr

