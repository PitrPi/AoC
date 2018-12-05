inpt <- read.table("input.txt", stringsAsFactors = FALSE)
inpt <- inpt[1,1]
asci <- utf8ToInt(inpt)
chng <- TRUE
rem <- c()
react <- function(asci) {
    while (chng) {
        chng <- FALSE
        rem <- c(0) # non empty c for if on line 12. 0 does not do anything
        if (length(asci) >= 2) {
            for (i in 2:length(asci)) {
                if (rem[length(rem)]+1 == i) next
                if (abs((asci[i] - asci[i-1])) == 32) {
                    rem <- c(rem, i-1, i)
                }
            }
            if (length(rem) > 1) {
                asci <- asci[setdiff(1:length(asci), rem)]
                chng <- TRUE
                # print(paste("removed", length(rem)-1))
            }
        }
    }
    length(asci)
}
react(asci)
# part 2
final <- c()
for (l in LETTERS) {
    big <- which(asci == utf8ToInt(l))
    sml <- which(asci == utf8ToInt(l)+32)
    rem <- c(big, sml)
    final[l] <- react(asci[setdiff(1:length(asci), rem)])
}

final[which(final == min(final))]
