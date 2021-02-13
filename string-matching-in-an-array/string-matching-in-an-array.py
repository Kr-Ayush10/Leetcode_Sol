class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = words.copy()
        answer = []
        
        for i in words:
            for j in arr:
                if i in j:
                    answer.append(i)
        
        sol = []
         
        for i in answer:
            if answer.count(i)>=2:
                sol.append(i) 
        
        
        return list(set(sol)) 