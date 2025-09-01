from .base_character import Character

class Mage(Character):
    def __init__(self, name: str, base_health: int, mana: int):
        super().__init__(name, base_health)
        self._mana = mana
        self._max_mana = mana

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        try:
            value = int(value)
        except ValueError as e:
            print(f'{e}: Invalid mana input!')
            raise
        if value <= 0:
            raise ValueError(f'Mana value must be positive!')
        self._mana = value

    def level_up(self):
        super().level_up()
        self._max_mana += 50
        self._mana = self._max_mana

    def attack(self):
        base_magic_damage = 10
        level_magic_damage = self._level * base_magic_damage
        self._mana -= (self._level * 5)
        return level_magic_damage

    def cast_spell(self, spell_cost):
        try:
            spell_cost = int(spell_cost)
        except ValueError as e:
            print(f'{e}: Invalid cost!')
            raise
        if spell_cost <= 0:
            raise ValueError(f'Spell cost must be positive!')
        if spell_cost > self._max_mana:
            raise ValueError(f'Spell is locked at this level!')
        self._mana -= spell_cost
        if self._mana <= 0:
            raise ValueError(f'Not enough mana!')

    def display_stats(self):
        previous_info = super().display_stats()
        return f'{previous_info} | Mana: {self._mana} | Max Mana: {self._max_mana}'

    def to_dict(self):
        data = super().to_dict()
        data['Mana'] = self._mana
        data['Max Mana'] = self._max_mana
        return data

    @classmethod
    def from_dict(cls, derived_data):
        mage = cls(derived_data['Name'], derived_data['Max Health'], derived_data['Mana'])
        mage._mana = derived_data['Mana']
        mage._max_mana = derived_data['Mana']
        return mage







