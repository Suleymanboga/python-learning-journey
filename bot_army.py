"""Studying modules and imports
Main execution script for bot_army
"""
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