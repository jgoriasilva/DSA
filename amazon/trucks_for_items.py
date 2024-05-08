"""
Extracted from here: https://leetcode.com/discuss/interview-question/4819993/Amazon-SDE-2-or-Interview-Loop-or-2024-(Rejected)/

trucks = [4, 5, 7, 2]
items = [1, 2, 5]

"""


def getTrucksForItems(trucks: list[int], items: list[int]) -> None:
    trucks = sorted([(truck, i) for i, truck in enumerate(trucks)], key=lambda x: x[0])
    
    def binary_search(trucks: list[int], item: int) -> int:
        l, r = 0, len(trucks) - 1
        while l <= r:
            m = (l+r) // 2
            if trucks[m][0] > item:
                r = m-1
            else:
                l = m+1
        if l < len(trucks): return trucks[l][1]
        return -1

    res = []
    for item in items:
        res.append(binary_search(trucks, item))

    return res
        

# trucks = [4, 5, 7, 2]
trucks = [5, 3, 8, 1]
# items = [1, 2, 5]
items = [6, 10]

res = getTrucksForItems(trucks, items)
print(res)