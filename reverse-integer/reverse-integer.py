class Solution:
    def reverse(self, x: int) -> int:
        new = x<0
        x = abs(x)
        revs = 0
        while(x>0):
            ret = x%10
            revs = revs*10+ret
            x = x//10
        
        if revs >= 2** 31 -1 or revs <= -2** 31:
            return 0

        elif new:
            return 0-revs
        else:
            return revs 