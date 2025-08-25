from base_character import Character

class Warrior(Character):
    def __init__(self, name, base_health, armor):
        super().__init__(name, base_health)
        self._armor = armor

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        try:
            value = int(value)
        except ValueError as e:
            print(f'{e}: Invalid armor input!')
            raise
        if value <= 0:
            raise ValueError('Armor defence must be positive!')
        self._armor = value

    def take_damage(self, amount):
        try:
            amount = int(amount)
        except ValueError as e:
            print(f'{e}: Invalid damage input!')
            raise
        if amount <= 0:
            raise ValueError('Damage amount must be positive!')
        new_damage = amount - self._armor
        if new_damage > 0:
            self._health -= new_damage
            if self._health <= 0:
                print(f'{self.name} died!')


    def attack(self):
        base_damage = 20
        return self._level * base_damage

    def display_stats(self):
        previous_info = super().display_stats()
        return f'{previous_info} | Armor: {self._armor}'
