class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        array = sorted([[arr[i],i] for i in range(0,len(arr))])
        st = []
        count = 0
        for n,i in array:
            if not st or st[-1]<n:
                st.append(n)
                count+=1
                arr[i]=count
            else:
                arr[i] = count
        return arr