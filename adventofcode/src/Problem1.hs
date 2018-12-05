module Problem1 where

import Lib

import Data.List
import Data.Maybe
import System.IO

int :: String -> Int
int a = if head a == '+' then read (tail a) else read a

dup [] = True
dup (a:[]) = True
dup (a:as) = isNothing $ dup' as a
    where 
          dup' [] _ = Nothing
          dup' (x:xs) b = if x == b then Just b else dup' xs b


problem1 = do
    putStrLn "Problem 1: calibrating fall frequency"
    doProblem 1 (\s -> do 
            let ints = fmap int (lines s)
            let f = foldl (+) 0 ints
            let g = head $ dropWhile (dup . reverse) (inits $ scanl (+) 0 ints)

            putStrLn $ "Problem 1 answer: " ++ show f
        )

    putStrLn "\n"
