module Lib where

import System.IO

problemNameFromInt :: Int -> String
problemNameFromInt a = "problem" ++ (show a) ++ ".input"

doProblem :: Int -> (String -> IO a) -> IO a
doProblem a f = do
    withFile ("problems/" ++ filename) ReadMode (\h -> do
        s <- hGetContents h
        f s)
    where filename = problemNameFromInt a
