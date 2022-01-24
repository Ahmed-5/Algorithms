from itertools import permutations as per

memo = {}

def winner(house, player, i):

    # print("house: {}, player: {}, iter: {}".format(house, player, i))

    if house == player or (house>21 and player>21):
        return 0
    elif house > 21:
        return 1
    elif player > 21:
        return -1
    elif house > player:
        return -1
    else:
        return 1

def DP(i):
    if i>= 48:
        return 0
    if i in memo:
        return memo[i]
    else:
        c = 4
        s_p = 0 # player
        s_h = 0 # house
        for j in range(4):
            if j%2==0:
                s_p += deck[i+j]
            if j%2==1:
                s_h += deck[i+j]

        value = -1
        ch = -1
        shh = 0
        if s_h <= 16:
            while s_h + shh <= 16:
                if ch + i + c + 1 < 52:
                    ch += 1
                    shh += deck[i+c + ch]
                else:
                    break
            w1 = winner(s_h + shh, s_p, i)
            value = max(value, DP(i+c+ch+1) + w1)
        else:
            w1 = winner(s_h, s_p, i)
            value = max(value, DP(i+c) + w1)

        while s_p <= 21:
            s_p += deck[i+c]
            c += 1
            ch = -1
            shh = 0
            if s_h <= 16:
                while s_h + shh <= 16:
                    if ch + i + c + 1 < 52:
                        ch += 1
                        shh += deck[i+c + ch]
                    else:
                        break
                w1 = winner(s_h + shh, s_p, i)
                value = max(value, DP(i+c+ch+1) + w1)
            else:
                w1 = winner(s_h, s_p, i)
                value = max(value, DP(i+c) + w1)

        memo[i] = value
        return(value)


def suffle():
    arr = []
    for i in range(4):
        for j in range(2, 11):
            arr.append(j)
        arr.extend([10, 10, 10, 11])

    for i in per(arr, 52):
        return i

deck = suffle()
# print(deck)
DP(0)
for i in range(52):
    print(i, 0 if not i in memo else memo[i])