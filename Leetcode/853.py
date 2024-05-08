from typing import *

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        arrived = 0
        while True:

            new_hashmap = {}
            for p, s in zip(position, speed):
                if p in hashmap: s = min(s, hashmap[p])
                new_hashmap[p] = s
            hashmap = new_hashmap

            new_hashmap = {}
            for p, s in hashmap.items():
                new_p = p
                for _ in range(s):
                    new_p += 1
                    if new_p in hashmap:
                        new_s = min(s, hashmap[new_p])
                        if new_p == target: arrived += 1
                        else: new_hashmap[new_p] = new_s
                        break
                # if new_p == target: arrived += 1
                # else: new_hashmap[new_p] = s
                new_hashmap[new_p] = s
            hashmap = new_hashmap

            if len(hashmap) == 0: break

def will_catch_up(car1: Tuple[int, int], car2: Tuple[int, int], limit: int):
    position1, speed1 = car1
    position2, speed2 = car2

    if position1 > position2: return True
    if speed2 > speed1: return False
    if limit < (speed1/speed2*limit - speed1/speed2*position2 + position1): return True
    return False

def main() -> None:
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    cars = [(p, s) for p, s in zip(position, speed)]

    res = will_catch_up(cars[1], cars[0], 100)
    print(res)

if __name__ == '__main__':
    main()