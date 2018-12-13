inpt <- readChar("input.txt", file.info("input.txt")$size)
# inpt <- readChar("test2.txt", file.info("test2.txt")$size)
# inpt <- readChar("test3.txt", file.info("test3.txt")$size)
inpt_ls <- strsplit(inpt, "\n")[[1]] #load input
ncols <- nchar(inpt_ls[1])
inpt <- gsub("\n", "", inpt)
inpt_ls <- strsplit(inpt, c())[[1]] #load input
# regmatches(x, regexpr("-?[0-9]+", x))

mat <- matrix(inpt_ls, ncol = ncols, byrow = TRUE)
carts <- which(mat == "<" | mat == "^" | mat == "v" | mat == ">" , arr.ind = TRUE)
carts <- data.frame(carts)
carts$names <- LETTERS[1:nrow(carts)]
carts$turn <- rep("L", nrow(carts))
carts$dir <- diag(mat[carts$row, carts$col])

order_carts <- function(carts){
    carts[order(carts$row, carts$col), ]
}


make_a_move <- function(mat, cart) {
    if (cart$dir == "<") {
        new_row <- cart$row
        new_col <- cart$col - 1
    } else if (cart$dir == "^") {
        new_row <- cart$row - 1
        new_col <- cart$col 
    } else if (cart$dir == ">") {
        new_row <- cart$row
        new_col <- cart$col + 1
    } else if (cart$dir == "v") {
        new_row <- cart$row + 1
        new_col <- cart$col
    }
    if (mat[new_row, new_col] == "\\") {
        if (cart$dir == "v") {
            new_dir <- ">"
            new_turn <- cart$turn
        } else if (cart$dir == "<") {
            new_dir <- "^"
            new_turn <- cart$turn
        } else if (cart$dir == "^") {
            new_dir <- "<"
            new_turn <- cart$turn
        } else if (cart$dir == ">") {
            new_dir <- "v"
            new_turn <- cart$turn
        }
    } else if (mat[new_row, new_col] == "/") {
        if (cart$dir == "v") {
            new_dir <- "<"
            new_turn <- cart$turn
        } else if (cart$dir == "<") {
            new_dir <- "v"
            new_turn <- cart$turn
        } else if (cart$dir == "^") {
            new_dir <- ">"
            new_turn <- cart$turn
        } else if (cart$dir == ">") {
            new_dir <- "^"
            new_turn <- cart$turn
        }
    } else if (mat[new_row, new_col] == "+") {
        if (cart$dir == "v") {
            if (cart$turn == "L") {
                new_dir <- ">"
                new_turn <- "S"
            } else if (cart$turn == "S") {
                new_dir <- "v"
                new_turn <- "R"
            } else if (cart$turn == "R") {
                new_dir <- "<"
                new_turn <- "L"
            }
        } else if (cart$dir == "<") {
            if (cart$turn == "L") {
                new_dir <- "v"
                new_turn <- "S"
            } else if (cart$turn == "S") {
                new_dir <- "<"
                new_turn <- "R"
            } else if (cart$turn == "R") {
                new_dir <- "^"
                new_turn <- "L"
            }
        } else if (cart$dir == "^") {
            if (cart$turn == "L") {
                new_dir <- "<"
                new_turn <- "S"
            } else if (cart$turn == "S") {
                new_dir <- "^"
                new_turn <- "R"
            } else if (cart$turn == "R") {
                new_dir <- ">"
                new_turn <- "L"
            }
        } else if (cart$dir == ">") {
            if (cart$turn == "L") {
                new_dir <- "^"
                new_turn <- "S"
            } else if (cart$turn == "S") {
                new_dir <- ">"
                new_turn <- "R"
            } else if (cart$turn == "R") {
                new_dir <- "v"
                new_turn <- "L"
            }
        }
    } else {
        new_dir <- cart$dir
        new_turn <- cart$turn
    }
    return(data.frame("row" = new_row,
                      "col" = new_col,
                      "names" = cart$names,
                      "turn" = new_turn,
                      "dir" = new_dir,
                      "crashed" = cart$crashed))
}

rows_in_frame <- function(df1, df2) {
    keep <- apply(df1, 1, function(x) {
        ifelse(any(x[1] == df2$row & x[2] == df2$col), FALSE, TRUE)}
    )
    return(df1[keep, ])
}
make_a_tick <- function(mat, carts) {
    carts <- order_carts(carts)
    carts$crashed <- FALSE
    new_carts <- carts[1,]
    new_carts$row <- -1
    new_carts$col <- -1
    new_carts$crashed <- TRUE
    # new_carts$crashed <- TRUE
    for (i in 1:nrow(carts)) {
        new_carts <- rbind(new_carts, make_a_move(mat, carts[i, ]))
        if (paste(new_carts[i+1, "col"], new_carts[i+1, "row"]) %in%
            (paste(new_carts[1:i, "col"], new_carts[1:i, "row"]))) {
            new_carts[i+1, "crashed"] <- TRUE
            new_carts[new_carts$col == new_carts$col[i+1] &
                          new_carts$row == new_carts$row[i+1], "crashed"] <- TRUE
        }
        if (paste(new_carts[i+1, "col"], new_carts[i+1, "row"]) %in%
            (paste(carts[i+1:nrow(carts), "col"], carts[i+1:nrow(carts), "row"]))) {
            new_carts[i+1, "crashed"] <- TRUE
            carts[carts$col == carts$col[i+1] &
                      carts$row == carts$row[i+1], "crashed"] <- TRUE
        }
    }

    carts_no_crash <- new_carts[!new_carts$crashed, ]
    crash_loc <- NULL
    if (nrow(carts_no_crash) < 2) {
        crash <-  TRUE
        crash_loc <- carts_no_crash[,c("row", "col")]
    }
    new_carts <- carts_no_crash[, 1:5]
    return(list("crash" = crash, "crash_loc" = crash_loc, "carts" = new_carts))
}
ticker <- 0
crash <- FALSE
while (!isTRUE(crash)) {
    out <- make_a_tick(mat, carts)
    ticker <- ticker + 1
    crash <- out[["crash"]]
    carts <- out[["carts"]]
    crash_loc <- out[["crash_loc"]]
    if (ticker %% 100 == 0) {
        print(ticker)
        print(nrow(carts))
    }
}
crash_loc
