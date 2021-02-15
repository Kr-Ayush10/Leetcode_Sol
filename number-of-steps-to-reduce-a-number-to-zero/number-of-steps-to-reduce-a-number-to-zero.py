class Solution:
    def numberOfSteps (self, n: int) -> int:
        c = 0
        while n != 0: n, c = n - 1 if n % 2 else n//2, c + 1
        return c