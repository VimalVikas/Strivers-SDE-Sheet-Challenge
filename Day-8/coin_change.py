def minCoins(coins, m, V):
    if (V == 0):
        return 0
 
    result = 1e9
     
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V-coins[i])

            if (sub_res != 1e9 and sub_res + 1 < result):
                res = sub_res + 1
 
    return result