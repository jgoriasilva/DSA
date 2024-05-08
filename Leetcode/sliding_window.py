

def max_sum_subarray(arr: list[int], size: int) -> list[int]:
    l = 0
    max_sum = float('-inf')
    while l <= len(arr) - size:
        r = l + size
        sub_arr = arr[l : r]
        sum_sub_arr = sum(sub_arr)
        if sum_sub_arr >= max_sum:
            max_arr = sub_arr
            max_sum = sum_sub_arr
        l += 1
    return max_sum, max_arr


def max_seq_ones(arr: list[int], k: int) -> list[int]:
    l = 0
    r = l + k - 1
    max_arr = []
    while l < len(arr) and r < len(arr):
        sub_arr = arr[l : r+1]
        count_zeros = len(sub_arr) - sum(sub_arr)
        if count_zeros <= k: 
            if len(sub_arr) >= len(max_arr): max_arr = sub_arr
            r += 1
        else: l += 1
    return max_arr


def add_up_to_num(arr: list[int], num: int) -> list[list[int]]:
    res = []
    l, r = 0, 0
    while l < len(arr) and r < len(arr):
        sub_arr = arr[l : r+1]
        sum_sub_arr = sum(sub_arr)
        if sum_sub_arr == num: 
            res.append(sub_arr)
            l += 1
        elif sum_sub_arr > num:
            l += 1
        else: r += 1
    return res

def shortest_sub_all_char(string: str, chars: list[str]) -> str:
    # l = 0
    # r = l + len(chars) - 1
    # while l < len(string) and r < len(string):
    #     sub_string = string[l : r+1]
    #     if not all([char in sub_string for char in chars]): r += 1
    #     else:
    #         else:
    raise NotImplementedError


def main() -> None:
    # l, r = 0, 1
    # sub_arr = [1]
    # arr = [8, 7, 4, 3, 1, 2, 1, 5, 1]
    # res = max_sum_subarray(arr, size)
    # res = add_up_to_num(arr, 7)
    arr = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0]
    res = max_seq_ones(arr, 4)

    print(res)


if __name__ == '__main__':
    main()