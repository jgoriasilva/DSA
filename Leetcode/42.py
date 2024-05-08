from typing import *

from typing import *

class Solution:
    def identifyRegions(self, height: List[int]) -> List[List[int]]:
        regions = []
        track = []
        maxLocalHeight = float('-inf')
        i = 0
        while i < len(height) - 1:
            if height[i+1] >= height[i]:
                if len(track):
                    track.append(height[i])
                    maxLocalHeight = max(maxLocalHeight, height[i])
                    while i < len(height) - 1:
                        i+=1
                        track.append(height[i])
                        maxLocalHeight = max(maxLocalHeight, height[i])
                        if i+1 <= len(height) - 1 and height[i] >= maxLocalHeight:
                            track.append(height[i+1])
                            break

                    regions.append(track)
                    track = [height[i]]
                    maxLocalHeight = float('-inf')
            else:
                track.append(height[i])
                maxLocalHeight = max(maxLocalHeight, height[i])
            i += 1
            
        return regions


    def calculateRain(self, region: List[int]) -> int:

        maxHeight = min(region[0], region[-1])
        rain = maxHeight * len(region) - 2*maxHeight
        for h in region[1:-1]:
            rain -= h

        print(rain)
        return rain

    def trap(self, height: List[int]) -> int:
        regions = self.identifyRegions(height)

        print(regions)
        rain = 0
        for region in regions:
            rain += self.calculateRain(region)

        return rain

height = [0,1,0,2,1,0,1,3,2,1,2,1]

rain = Solution().trap(height)

print(rain)