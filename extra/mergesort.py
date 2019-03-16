# solves CS 124 problem in directory

# take two sorted arrays and merge
def merge(x, y):
    if not x:
        return y
    elif not y:
        return x

    xlen = len(x)
    ylen = len(y)
    ix = iy = 0
    n = xlen + ylen
    a = []
    while ix < xlen and iy < ylen:
        if x[ix] <= y[iy]:
            a.append(x[ix])
            ix += 1
        else:
            a.append(y[iy])
            iy += 1

    if ix < xlen:
        a.extend(x[ix:])
    else:
        a.extend(y[iy:])
    return a

# sort array with merge sort algo
def mergesort(a):
    alen = len(a)
    if alen <= 1:
        return a

    a1 = a[0:alen//2]
    a2 = a[alen//2:]
    return merge(mergesort(a1), mergesort(a2))

# take user input
arr = map(int, raw_input().split())
n = arr.pop(0)

# sort numbers
arr = mergesort(arr)

# look for two numbers that add to `n` in sorted array
found = False
l = 0
r = len(arr) - 1
while l < r:
    if arr[l] + arr[r] == n:
        print arr[l], arr[r]
        found = True
        break
    elif arr[l] + arr[r] < n:
        l += 1
    else:
        r -= 1

if not found:
    print "False"
