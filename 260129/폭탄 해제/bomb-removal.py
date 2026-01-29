unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Program:
    def __init__(self, unlock_code, wire_color, seconds):
        self.code = unlock_code
        self.color = wire_color
        self.seconds = seconds
    def display(self):
        print(f"code : {self.code}")
        print(f"color : {self.color}")
        print(f"second : {self.seconds}")

    
result = Program(unlock_code, wire_color, seconds)
result.display()