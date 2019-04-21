# Solves CS 124 programming problem in directory using Rabin-Karp hashing

_p = 2038074743        # prime number for hash
_b = 300               # _b for hash

def hashed(word):
    """ Hashing function, not used for efficiency """
    hashval = 0
    index = len(word) - 1
    for i in xrange(len(word)):
        hashval = (hashval + (ord(word[i]) - ord('A') + 1) * bexp[index - i]) % _p
    return hashval

# Get user input
N, B = map(int, raw_input().split())
bug = raw_input()

# Store powers of _b, mod _p
bexp = [1, _b, _b**2]
indicators = {}

# Store bug indicator length and hash
maxlen = 0
for i in xrange(B):
    indicator = raw_input()
    lenindicator = len(indicator)
    index = lenindicator - 1

    # Ensure enough powers of _b mod _p are stored
    blast = len(bexp)
    while index >= blast:
        bexp.append((bexp[blast - 1] * _b) % _p)
        blast += 1

    # Hash the indicator
    hashval = 0
    for i in xrange(len(indicator)):
        hashval = (hashval + (ord(indicator[i]) - ord('A') + 1) * bexp[index - i]) % _p

    if index not in indicators.keys():
        indicators[index] = {hashval: 1}
    elif hashval not in indicators[index]:
        indicators[index][hashval] = 1
    else:
        indicators[index][hashval] += 1


# Compare hashes in bug with indicators
answer = 0
for i in indicators.keys():
    j = 0
    hashval = 0
    while j + i < N:
        if i == 0:
            hashval = ord(bug[j]) - ord('A') + 1
        elif j == 0:
            for k in xrange(i+1):
                hashval += (ord(bug[k]) - ord('A') + 1) * bexp[i - k]
            hashval %= _p

        elif j > 0:
            hashval = ((hashval - ((ord(bug[j-1]) - ord('A') + 1) * bexp[i])) * _b
                       + (ord(bug[j + i]) - ord('A') + 1) ) % _p
 
        if hashval in indicators[i]:
            answer += indicators[i][hashval]

        j += 1

print answer
