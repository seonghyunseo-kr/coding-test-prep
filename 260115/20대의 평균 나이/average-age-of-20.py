sum_age = 0 
cnt = 0 
while True:
    age = int(input())
    if age < 20 or age > 29:
        break
    else:
        sum_age += age 
        cnt += 1
    
mean_age = sum_age / cnt 
print(f"{mean_age:.2f}")