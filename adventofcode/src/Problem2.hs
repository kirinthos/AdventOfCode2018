module Problem2 where

import Lib

import Data.List

count s = map length $ group $ sort s

hasL l cs = if (length $ filter (==l) cs) > 0 then 1 else 0
hasTwo = hasL 2
hasThree = hasL 3

cc :: (Int, Int) -> [Int] -> (Int, Int)
cc a x = (fst a + (hasTwo x), snd a + (hasThree x))

{- Part 2
 
 i want to compare every two strings
 zip them together, where equal put a 0, where different put a 1
 any pairs that have 1 difference, show all characters besides removed one
-}

strmatch s1 s2 = (s1, s2, sum $ map (\(x, y) -> if x == y then 0 else 1) $ zip s1 s2)


--cmp ss = zip ss (drop 1 ss)

problem2 = do
    putStrLn "Problem 2: counting box IDs"
    doProblem 2 (\s -> do 
            let ss = lines s
            let cs = map count ss
            let sum = foldl cc (0, 0) cs
            putStrLn $ "box ID count: " ++ (show $ (fst sum) * (snd sum))

            let pairs = [ (x, y) | x <- ss, y <- ss, x /= y ]
            let h = map (\(s1, s2, _) -> (s1, s2) $ filter (\(s1, s2, sum) -> sum == 1) $ map (uncurry strmatch) pairs
            putStrLn $ "boxID part 2: " ++ (show h)
        )

    putStrLn "\n"
