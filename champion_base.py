# Class đại diện cho Tướng trong Liên minh huyền thoại
# Đây là 1 Abstract Class
# Bất kỳ class nào kế thừa class này đều sẽ có 
#   tính chất của 1 tướng trong Liên minh huyền thoại

from abc import ABC

# Đánh dấu đây là 1 Abstract Class bằng cách dùng ABC
class Champion(ABC):
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def attack(self):
        print(self.name, 'thi triển' ,self.skill)