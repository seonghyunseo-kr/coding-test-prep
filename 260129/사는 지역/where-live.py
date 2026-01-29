n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Program:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region 
    
name_list = []
for i in range(n):
    result = Program(name[i], street_address[i], region[i])
    name_list.append(result)

last_name = name_list[0]
for i in range(len(name_list)):
    if name_list[i].name > last_name.name:
        last_name = name_list[i]

print(f"name {last_name.name}")
print(f"addr {last_name.address}")
print(f"city {last_name.region}")