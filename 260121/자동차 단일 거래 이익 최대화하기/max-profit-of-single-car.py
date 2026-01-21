n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
curr_price = price[n-1]
print('curr_price:', curr_price)
min_price, max_price = 0, 0 
for p in price:
    print('p:', p)
    if p != curr_price:
        if p < curr_price:
            min_price = p
        else:
            max_price = p
        print('curr_price, p, min_price, max_price:', curr_price, p, min_price, max_price)


    # min_profit = curr_price - min_price
    # max_profit = max_price - curr_price

    # print(min_profit, max_profit)