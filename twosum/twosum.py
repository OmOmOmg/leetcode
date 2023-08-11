def twoSum(self, nums: List[int], target: int) -> List[int]:

        temp_array = nums.copy()
        
        for i in nums:       
            
            temp_array.remove(i)

            e = nums.index(i)
            f = nums.index(i)+1

            for j in temp_array:
                        
                if i + j == target:                             
                    return [e,f]
                f+=1
