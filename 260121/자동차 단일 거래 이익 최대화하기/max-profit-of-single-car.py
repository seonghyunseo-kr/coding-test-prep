n = int(input())
price = list(map(int, input().split()))
profit, curr_max_profit, final_max_profit = 0, None, None

# Please write your code here.
for i in range(n-1):
    curr_price = price[i]
    future_prices = price[i+1:]
    # print(curr_price, future_prices)
    for p in future_prices:
        if p > curr_price:
            profit = p - curr_price
            # print('yes profit', profit)
        else:
            # print('no profit')
            profit = 0 

        if curr_max_profit is None or profit > curr_max_profit:
            curr_max_profit = profit
            # print('curr_max_profit updated', curr_max_profit)

print(curr_max_profit)