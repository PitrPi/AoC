inpt_split <- strsplit(inpt, "\n")
a<-inpt_split[[1]]
b<-0
freq <- c(0)
en <- TRUE
while(en) {
for (i in 1:length(a)){
    if (grepl("-", a[i])){
        b <- b - strtoi(substr(a[i], 2, nchar(a[i])))
    } else {
        b <- b + strtoi(substr(a[i], 2, nchar(a[i])))
    }
    if (b %in% freq) {
        print(b)
        en <- FALSE
        break
    }
    freq <- c(freq, b)
}
}