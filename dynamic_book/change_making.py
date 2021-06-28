def make_change(coins, amount):
# Handle payment of amount zero.
    if not amount:
        return []
    if amount < 0:
        return None
    optimal_result = None
    for coin in coins: # Solve a subproblem for the rest of the amount.
        partial_result = make_change(coins, amount-coin)
        if partial_result is None:
            continue
        candidate = partial_result + [coin]
        if (optimal_result is None or
                len(candidate) < len(optimal_result)):
            optimal_result = candidate

    return optimal_result

coin=[1,2,5]
print(make_change(coin,9))
def subs(s):
    for left in range(len(s)):
        for right in range(left, len(s)):
            substring = s[left:right+1]
            print(substring)


ss='supraManer'
subs(ss)