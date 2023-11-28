def sorted_squares(arr: []) -> []:
    l, r = 0, len(arr) - 1
    res = [0] * len(arr)
    pos = len(arr) - 1
    while l <= r:
        s_r = arr[r] * arr[r]
        s_l = arr[l] * arr[l]
        if s_r >= s_l:
            res[pos] = s_r
            r -= 1
        else:
            res[pos] = s_l
            l += 1
        pos -= 1
    return res

print(sorted_squares([-3, 2, 4]))
