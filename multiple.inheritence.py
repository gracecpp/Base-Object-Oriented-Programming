class warrior:
    def __init__(self, name, heal, attack):
        self.name = name
        self.heal = heal
        self.attack = attack

    def attack_power(self):
        return self.attack

class magic_user:
    def __init__(self, name, magic):
        self.name = name
        self.magic = magic

    def magic_power(self):
        return self.magic

class paladin(warrior, magic_user):
    def __init__(self, name, heal, attack, magic):
        warrior.__init__(self, name, heal, attack)
        magic_user.__init__(self, name, magic)

    def total_power(self):
        total = self.attack_power() + self.magic_power() + self.heal
        return total
    
class holy_paladin(paladin):
    def __init__(self, name, heal, attack, magic, holy_power):
        super().__init__(name, heal, attack, magic)
        self.holy_power = holy_power

    def total_power(self):
        return super().total_power() + self.holy_power


P1 = paladin ("Harry Potter", 999, 100, 250)
HP1 = holy_paladin("Voldemort", -10, 345, 900, -123)
PW = warrior("Severus Snape", 300, 1200)
PMS = magic_user("Sora", 900)

print(PW.attack_power())
print(PMS.magic_power())
print(P1.total_power())
print(HP1.total_power())