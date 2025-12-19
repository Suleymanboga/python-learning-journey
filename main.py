"""Studying modules and imports"""

from bot_army import CyberBot, SuperBot

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
