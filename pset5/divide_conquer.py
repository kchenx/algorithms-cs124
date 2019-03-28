# Uses divide and conquer and recursive median function
# Solves CS 124 programming problem `dividends` in directory

# Recursive compute a good pivot for an array
def select(arr):
    if len(arr) == 1:
        return arr[0]

    i = 0
    size = len(arr)
    medians = []

    while i + 5 < size:
        medians.append(sorted(arr[i:i+5])[2])
        i += 5

    if size - i > 0:
        medians.append(sorted(arr[i:size])[(size-i)//2])

    return select(medians)


# Use divide and conquer to calculate sum
def divide_conquer(arr, l_i, r_i):
    global funds
    global cumulative
    global result

    if not arr:
        return

    # Partition into two subarrays around pivot
    pivot = select(arr)
    larr = []
    rarr = []
    flag = 0
    for x in arr:
        if x < pivot:
            larr.append(x)
        elif x > pivot:
            rarr.append(x)
        # if x == pivot:
        elif flag == 0:
            flag = 1
        else:
            larr.append(x)

    max_val = max_i = 0
    for i in xrange(l_i, r_i):
        if cumulative[i]:
            newfund = cumulative[i][1] + funds[i] * (pivot - i)
            if newfund >= max_val:
                max_val = newfund
                max_i = i

    result += max_val

    if len(larr) >= 1:
        divide_conquer(larr, l_i, max_i + 1)
    if len(rarr) >= 1:
        divide_conquer(rarr, max_i, r_i)

    return


# Get input from user
N, Q = map(int, raw_input().split())
funds = map(int, raw_input().split())
times = map(int, raw_input().split())
times[:] = [time - 1 for time in times]

# Find cumulative funds
cumulative = [None] * N
count = 0
currmax = 0
for i, fund in enumerate(funds):
    count += fund
    if fund > currmax:
        cumulative[i] = [i, count]
        currmax = fund


# Divide and conquer time queries
result = 0
divide_conquer(times, 0, N)
print result

