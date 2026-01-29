product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Program:
    def __init__(self):
        self.name = 'codetree'
        self.code = 50 
    
    def display(self, product_name=None, product_code=0):
        print(f"product {self.code} is {self.name}")
        print(f"product {product_code} is {product_name}")

result = Program()
result.display(product_name, product_code)