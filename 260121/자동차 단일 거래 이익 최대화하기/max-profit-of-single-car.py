n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
buy_price = price[n-1]
min_price, max_price = buy_price, buy_price
curr_min, curr_max = buy_price, buy_price

for p in price:
    if p != buy_price:
        if p < buy_price:
            curr_min = p
        else:
            curr_max = p 

        if curr_min < min_price:
            min_price = curr_min
            
        if curr_max > max_price:
            max_price = curr_max 
    else:
        continue

if buy_price > min_price:
    min_profit = buy_price - min_price
    print(min_profit)
else:
    print(0)