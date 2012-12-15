import System.Environment (getArgs)
import Data.List (transpose)

newtype Matrix a = Matrix [[a]] deriving (Eq, Show)

instance Num a => Num (Matrix a) where
    Matrix as + Matrix bs = Matrix (zipWith (zipWith (+)) as bs)
    Matrix as - Matrix bs = Matrix (zipWith (zipWith (-)) as bs)
    Matrix as * Matrix bs =
        Matrix [[sum $ zipWith (*) a b | b <- transpose bs] | a <- as]
    negate (Matrix as) = Matrix (map (map negate) as)
    fromInteger = const $ Matrix [[]]
    abs = id
    signum = id

fib :: Integer -> Integer
fib n = (\(Matrix m) -> m !! 1 !! 1) $ a ^ n
    where a = Matrix [[0, 1], [1, 1]]

main = do
    x <- getArgs
    print $ fib $ read $ head x
