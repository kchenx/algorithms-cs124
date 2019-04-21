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

    # Store bug hashes. Dict of dicts: bug length -> hash -> frequency of hash
    if index not in indicators.keys():
        indicators[index] = {hashval: 1}
    elif hashval not in indicators[index]:
        indicators[index][hashval] = 1
    else:
        indicators[index][hashval] += 1


answer = 0
# Iterate over log per distinct bug length
for i in indicators.keys():
    j = 0
    hashval = 0
    while j + i < N:
        # If examining single character
        if i == 0:
            hashval = ord(bug[j]) - ord('A') + 1
        # If examining log for a new length
        elif j == 0:
            for k in xrange(i+1):
                hashval += (ord(bug[k]) - ord('A') + 1) * bexp[i - k]
            hashval %= _p

        # Sliding to next frame in 
        elif j > 0:
            hashval = ((hashval - ((ord(bug[j-1]) - ord('A') + 1) * bexp[i])) * _b
                       + (ord(bug[j + i]) - ord('A') + 1) ) % _p
 
        # Check if bug has indicator
        if hashval in indicators[i]:
            answer += indicators[i][hashval]

        j += 1

print answer
