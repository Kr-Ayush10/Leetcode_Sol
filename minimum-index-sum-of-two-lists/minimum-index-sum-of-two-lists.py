class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        
        length_list1 = len(list1)
        length_list2 = len(list2)
        
        
        list_index_sum = length_list1+length_list2
        
        
        common_items = []
        
        
        index_1 = -1
        for item in list1:
            
            
            index_1 += 1
            
            
            if item in list2:
                
                
                index_2 = list2.index(item)
                
                temp_index_sum = index_1+index_2
                
                
                if temp_index_sum <= list_index_sum:
                    
                    
                    if temp_index_sum == list_index_sum:
                        common_items.append(item)
                    
                    
                    else:
                        common_items = [item]
                        
                    
                    list_index_sum = temp_index_sum
        
        return common_items