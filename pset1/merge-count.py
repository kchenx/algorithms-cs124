# Merge sort to count inversions
# Solves CS 124 programming problem in directory

import sys

counter = 0



def merge(s, t):
    """ Merge algorithm for merge sort

    Takes two already sorted arrays and sorts elements
    Counts number of inversions in the array
    """

    global counter

    if not s:
        return t
    elif not t:
        return s

    u = []
    i = j = 0
    slen = len(s)
    tlen = len(t)

    # add elements in order to new array
    while i < slen and j < tlen:
        if s[i] <= t[j]:
            u.append(s[i])
            i += 1
        else:
            u.append(t[j])
            j += 1
            # number of inversions are elements remaining in `s`
            counter += slen - i

    # add remainder of `s` or `t`
    if i < slen:
        u.extend(s[i:])
    else:
        u.extend(t[j:])
    return u



def mergesort(s):
    """ Merge sort algorithm

    Sorts an array using merge sort
    """

    global counter

    slen = len(s)

    if slen <= 1:
        return s

    s1 = s[0:slen//2]
    s2 = s[slen//2:]
    return merge(mergesort(s1), mergesort(s2))



# get input from user
N, M = map(int, raw_input().split())

tenacity = map(int, raw_input().split())
major = map(int, raw_input().split())

# sort tenacity into list by major
people = [[] for i in xrange(M)]
for i in xrange(N):
    people[major[i] - 1].append(tenacity[i])

# count number of inversions
mergesort(tenacity)
total = counter
counter = 0

# subtract double counting inversions from people with same major
for i in xrange(M):
    mergesort(people[i])
    total -= counter
    counter = 0

print(total)
