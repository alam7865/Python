def IsPossible(arr, mid, cow):
    lastCowPos = arr[0]
    cow -= 1
    for x in range(1, len(arr), 1):
        if arr[x] - lastCowPos >= mid:
            cow -= 1
            lastCowPos = arr[x]
        elif cow == 0:
            return True

    return False


def aggressiveCow(arr, k):
    if k > len(arr):
        print("Not Possible")

    n = len(arr)
    low = 0
    high = n - 1

    ans = -1
    while low <= high:
        mid = int(low + (high - low) / 2)

        if IsPossible(arr, mid, k):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print("Result:", ans)


aggressiveCow([1, 2, 4, 8, 9], 3)
