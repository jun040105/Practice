valid_triangle :: Int -> Int -> Int -> Bool

valid_triangle a b c = a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a  