import random
class Bullet():
    def __init__(self):
        self.position = random.randint(1,10)
        pass
    def Move(self):
        self.position+=1

bullets = []
for i in range(5):
    b = Bullet()
    print(b.position)
    bullets.append(b)

for item in bullets:
    item.Move()

print("\nPrinting:")
for item in bullets:
    print(item.position)
    



