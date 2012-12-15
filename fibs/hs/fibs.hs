import System.Environment (getArgs)

fib :: Int -> Int
fib 0 = 1
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

main = do
    x <- getArgs
    print $ fib $ read $ head x
