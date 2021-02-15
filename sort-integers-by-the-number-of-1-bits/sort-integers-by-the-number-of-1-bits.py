class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()          
        arr2 = []           
						
        for i in arr:
            arr2.append([bin(i).count('1'), i])
        arr2.sort()        
        arr3 = []
        for i in range(len(arr2)):       
            arr3.append(arr2[i][1])
        return arr3