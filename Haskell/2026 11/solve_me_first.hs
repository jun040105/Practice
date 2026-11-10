solve_me_first a b = a + b

main = do
    a <- readLn
    b <- readLn
    let x = solve_me_first a b
    print x