import math


def IsPossible(arr, mid, k):
    lastPlace = arr[0]
    k -= 1

    for x in range(1, len(arr)):  # include last element
        if arr[x] - lastPlace >= mid:
            lastPlace = arr[x]
            k -= 1
        if k == 0:
            return True
    return False


def minimizeDiff(arr, k):
    arr.sort()
    ans = -1
    low = 0
    n = len(arr)

    max = arr[n - 1]
    min = arr[0]
    high = max - min
    while low <= high:
        mid = low + (high - low) // 2

        if IsPossible(arr, mid, k):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print("Result", ans)


arr = [1, 4, 9, 0, 2, 13, 3]
k = 4

minimizeDiff(arr, k)
