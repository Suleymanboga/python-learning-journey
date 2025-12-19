"""Class and constructor updated"""
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
class SuperBot(CyberBot):
    def heal(self):
        self.health += 50
        print(f"{self.name} repaired itself! New hp: {self.health}")

bot1 = CyberBot("edward", 100, 10)
bot2 = CyberBot("anna", 200, 5)
bot3 = SuperBot("william", 150, 15)

bot1.attack(bot2)
bot2.attack(bot1)
bot3.attack(bot1)
bot3.attack(bot2)
bot3.heal()
print("-" * 20)

bot1.status_report()
bot2.status_report()
bot3.status_report()
