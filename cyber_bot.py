"""Class and constructor study"""
class CyberBot:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, other_bot):
        other_bot.health -= self.damage
        print(f"{self.name} attacked {other_bot.name}.")
    def status_report(self):
        print(f"Now {self.name} remaining hp is {self.health}")

bot1 = CyberBot("edward", 100, 10)
bot2 = CyberBot("anna", 200, 5)

bot1.attack(bot2)
bot2.attack(bot1)

print("-" * 20)

bot1.status_report()
bot2.status_report()
