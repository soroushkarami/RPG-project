from base_character import Character

class Warrior(Character):
    def __init__(self, name: str, base_health: int, armor: int):
        super().__init__(name, base_health)
        self._armor = armor
        self._damage = 10
        self._weapon = 'メ Basic Sword メ'

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value: int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f'Invalid armor input!')
        if value < 0:
            raise ValueError(f'Armor defence must be positive!')
        self._armor = value

    @property
    def weapon(self):
        return self._weapon

    def take_damage(self, amount: int):
        try:
            amount = int(amount)
        except ValueError as e:
            raise ValueError(f'Invalid damage input!')
        if amount <= 0:
            raise ValueError(f'Damage amount must be positive!')
        self._armor -= amount
        if self._armor >= 0:
            print(f'{self.name} took {amount} damage! (Health= {self._health}, Armor= {self._armor})')
        else:
            remained_damage = amount + self._armor  # note that _armor is negative here so it will subtract from amount
            self._health -= remained_damage
            self._armor = 0
            if self._health <= 0:
                self._health = 0
                print(f'{self.name} died!')
            else:
                print(f'{self.name} took {amount} damage! (Health= {self._health}, Armor= {self._armor})')

    def level_up(self):
        if self._level < 50:
            super().level_up()
            self._damage += 10
            if self._level == 5:
                self._weapon = '🗡 Iron Sword 🗡'
                print('🗡 Iron Sword 🗡 granted!')
                self._damage += 10
            elif self._level == 15:
                self._weapon = '⚚ Silver Sword ⚚'
                print('⚚ Silver Sword ⚚ granted!')
                self._damage += 15
            elif self._level == 30:
                self._weapon = '⸸༺ Legendary Sword ༻⸸'
                print('⸸༺ Legendary Sword ༻⸸ granted!')
                self._damage += 20
            elif self._level == 50:
                self._weapon = '༺𓆩⚔𓆪༻ Doom Sword ༺𓆩⚔𓆪༻'
                print('༺𓆩⚔𓆪༻ Doom Sword ༺𓆩⚔𓆪༻ granted!')
                self._damage += 25
                print(f'{self._name} is at max level! (Damage= {self._damage})')
            print(f'Damage= {self._damage}')
        else:
            print(f'{self._name} is at max level! (Damage= {self._damage})')

    def attack(self):
        return self._level * self._damage

    def display_stats(self):
        previous_info = super().display_stats()
        return f'{previous_info} | Armor: {self._armor}'
