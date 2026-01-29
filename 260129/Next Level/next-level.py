user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Program:
    def __init__(self):
        self.id = 'codetree'
        self.level = int(10)
    
    def display(self, user2_id, user2_level):
        print(f'user {self.id} lv {self.level}')
        print(f"user {user2_id} lv {user2_level}")

result = Program()
result.display(user2_id, user2_level)
