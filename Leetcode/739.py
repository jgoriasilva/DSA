from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        memory, new_memory, res = {}, {}, []

        for i, temp in enumerate(temperatures):
            new_memory = memory
            for j, temp_j in memory.items():
                if temp > temp_j:
                    res[j] = i-j
                    del memory[j]
                else:
                    break
                    # new_memory[j] = temp_j
            memory = new_memory
            new_memory = 
            memory[i] = temp
            res.append(0)

        return res


temperatures = [73,74,75,71,69,72,76,73]

res = Solution().dailyTemperatures(temperatures)

print(res)