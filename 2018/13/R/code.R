inpt <- readChar("input.txt", file.info("input.txt")$size)
# inpt <- readChar("test.txt", file.info("test.txt")$size)
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
                      "dir" = new_dir))
}

make_a_tick <- function(mat, carts) {
    carts <- order_carts(carts)
    new_carts <- carts[1,]
    for (i in 1:nrow(carts)) {
        new_carts <- rbind(new_carts, make_a_move(mat, carts[i, ]))
    }
    new_carts <- new_carts[2:nrow(new_carts), ]
    if (any(duplicated(new_carts[, c("row", "col")]))) {
        crash <- TRUE
        crash_loc <- new_carts[(duplicated(new_carts[, c("row", "col")])), c("row", "col")]
    } else if (any(apply(new_carts[, c("row", "col")] == carts[, c("row", "col")], 1, all))) {
        crash <- TRUE
        crash_loc <- carts[(any(apply(new_carts[, c("row", "col")] == carts[, c("row", "col")], 1, all))), c("row", "col")]
    }
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
    print(ticker)
}
crash_loc
