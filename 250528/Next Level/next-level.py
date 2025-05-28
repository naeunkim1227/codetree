user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Practice :
    def __init__(self, id = "codetree", level = 10) :
        self.id = id
        self.level = level



p = Practice()
print("user", p.id , "lv", p.level)

p.id = user2_id
p.level = user2_level
print("user", p.id , "lv", p.level)

