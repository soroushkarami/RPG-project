import logging
from .base_character import Character

logger = logging.getLogger(__name__)

class Mage(Character):
    def __init__(self, name: str, base_health: int, mana: int):
        logger.info(f'__init__ initiated, trying to create mage {name}')
        super().__init__(name, base_health)
        self._mana = mana
        self._max_mana = mana
        self._magic_damage = 10
        logger.info(f'Mage created. Name: {name}, Health: {base_health}, '
                    f'Mana: {mana}, Magic Damage: {self._magic_damage}')

    @property
    def mana(self):
        logger.debug(f'Accessing "mana" property: {self._mana}')
        return self._mana

    @mana.setter
    def mana(self, value):
        try:
            value = int(value)
        except ValueError as e:
            logger.error(f'Non-int value entered as mana value: {e}')
            raise ValueError(f'Armor defense must be a number!')
        if value <= 0:
            logger.error(f'A negative int entered as mana value!')
            raise ValueError(f'Mana must be positive!')
        logger.info(f"{value} successfully assigned to {self._name}'s mana amount!")
        self._mana = value

    @property
    def magic_damage(self):
        logger.debug(f'Accessing "magic_damage" property: {self._magic_damage}')
        return self._magic_damage

    def level_up(self):
        logger.debug(f'"level_up" method is called...')
        if self._level < 50:
            logger.info(f'{self._name} can be leveled up...')
            super().level_up()
            self._max_mana += 50
            self._mana = self._max_mana
            logger.info(f'{self._name} leveled up! (level = {self._level}, '
                        f'Max Health = {self._max_health}, Max Mana = {self._max_mana})')
        else:
            logger.warning(f'{self._name} is already at max level! (Mana = {self._mana})')

    def attack(self):
        logger.debug(f'"attack" method is called...')
        level_magic_damage = self._level * self._damage
        logger.info(f"{self._name}'s current magic attack power: {level_magic_damage}")
        if self._mana == 0:
            logger.error(f'Failure! {self._name} does not have any mana!')
            raise Exception(f'Insufficient mana!')
        self._mana -= (self._level * 5)
        if self._mana < 0:
            logger.warning(f"{self._name}'s mana is over, setting it to 0...")
            self._mana = 0
        logger.info(f"{self._name}'s mana after launching magic attack = {self._mana}")
        return level_magic_damage

    def cast_spell(self, spell_cost):
        try:
            spell_cost = int(spell_cost)
        except ValueError as e:
            logger.error(f'Non-int value entered as mana cost: {e}')
            raise ValueError(f'Spell cost must be a number!')
        if spell_cost <= 0:
            logger.error(f'A negative value entered as mana cost!')
            raise ValueError(f'Spell cost must be positive!')
        if spell_cost > self._max_mana:
            logger.error(f"Failure! Spell cost exceeds {self._name}'s max mana!")
            raise ValueError(f'Spell is locked at this level!')
        if self._mana == 0:
            logger.error(f'Failure! {self._name} does not have any mana!')
            raise Exception(f'Insufficient mana!')
        self._mana -= spell_cost
        if self._mana < 0:
            logger.warning(f"{self._name}'s mana is over, setting it to 0...")
            self._mana = 0
        return self._mana

    def display_stats(self):
        logger.debug(f'"display_stats" method is called...')
        previous_info = super().display_stats()
        return f'{previous_info} | Mana: {self._mana} | Max Mana: {self._max_mana}'

    def to_dict(self):
        logger.info(f'"to_dict" method is called...')
        data = super().to_dict()
        data['Mana'] = self._mana
        data['Max Mana'] = self._max_mana
        data['Magic Damage'] = self._magic_damage
        logger.info(f'Dictionary for {self._name} successfully created!')
        return data

    @classmethod
    def from_dict(cls, derived_data):
        logger.info(f'"from_dict" classmethod is called...')
        if derived_data['Level'] < 1:
            logger.warning(f'Invalid level for {derived_data['Name']}, setting it to 1...')
            derived_data['Level'] = 1
        if derived_data['Level'] > 50:
            logger.warning(f'Derived level for {derived_data['Name']} exceeds max level, '
                            f'setting it to max(50)...')
            derived_data['Level'] = 50
        if derived_data['Max Health'] > 0 and derived_data['Health'] < 0:
            logger.warning(f'Invalid health for {derived_data['Name']}, '
                            f'setting it to max({derived_data['Max Health']})...')
            derived_data['Health'] = derived_data['Max Health']
        if derived_data['Health'] > derived_data['Max Health']:
            logger.warning(f'Derived health for {derived_data['Name']} exceeds max health, '
                            f'setting it to max health({derived_data['Max Health']}...')
            derived_data['Health'] = derived_data['Max Health']
        if derived_data['Magic Damage'] < 10:
            logger.warning(f'Invalid magic damage for {derived_data['Name']}, '
                           f'setting it to 10...')
            derived_data['Magic Damage'] = 10
        if derived_data['Mana'] < 0:
            logger.warning(f'Invalid mana value for {derived_data['Name']}, '
                           f'setting it to 10...')
            derived_data['Mana'] = 10
        mage = cls(derived_data['Name'], derived_data['Max Health'], derived_data['Mana'])
        mage._max_mana = derived_data['Max Mana']
        mage._magic_damage = derived_data['Magic Damage']
        return mage



