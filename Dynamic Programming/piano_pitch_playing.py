import math
from random import randint, seed

memo = {}

seed(0)
notes = [randint(0, 50) for i in range(100)]

def transit(n1, f1, n2, f2):
    note_diff = n2-n1
    finger_diff = f2-f1

    return abs(note_diff - finger_diff)

def DP(i, pinky, n_f, n):
    if i >= n:
        return 0

    if (i, pinky, n_f) in memo:
        return memo[(i, pinky, n_f)]

    if i == 0:
        value = min(DP(i+1, notes[i] - f, n_f, n) for f in range(n_f))
    else:
        value = min(DP(i+1, notes[i] - f, n_f, n) + transit(pinky, 0, notes[i], f) for f in range(n_f))

    memo[(i, pinky, n_f)] = value
    return value

# notes = [0,1,2,3,4,5]
print(*notes)
print(DP(0,0,5,len(notes)))