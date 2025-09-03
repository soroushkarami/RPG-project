import logging
from .base_character import Character
import random

logger = logging.getLogger(__name__)

class Rogue(Character):
    def __init__(self, name: str, base_health: int, stealth_level: int):
        logger.info(f'__init__ initiated, trying to create rogue {name}')
        super().__init__(name, base_health)
        self._damage = 10
        self._stealth_level = stealth_level
        logger.info(f'Rogue created. Name: {name}, Health: {base_health}, '
                    f'Damage: {self._damage}')

    @property
    def damage(self):
        logger.debug(f'Accessing "damage" property: {self._damage}')
        return self._damage

    def attack(self):
        logger.debug(f'"attack" method is called...')
        level_damage = self._level * self._damage
        critical_hit = 2 * level_damage
        logger.info(f'{self._name}: Level damage = {level_damage}, Critical damage = {critical_hit}'
                    f'Critical hit chance: 10%')
        logger.debug(f'Evaluating final damage...')
        final_damage = random.choices([critical_hit, level_damage],
                                      weights= [0.1, 0.9],
                                      k=1)[0]
        logger.debug(f'Final damage = {final_damage}')
        return [critical_hit, final_damage]

    def sneak_attack(self):
        logger.debug(f'"sneak_attack" is called...')
        crit = self.attack()[0]  # 100% critical hit !
        logger.warning(f'Sneak attacked launched! (Damage = {crit})')
        return crit

    def display_stats(self):
        logger.debug(f'"display_stats" method is called...')
        previous_info = super().display_stats()
        return f'{previous_info} | Stealth Level: {self._stealth_level}'

    def to_dict(self):
        logger.debug(f'"to_dict" method is called...')
        data = super().to_dict()
        data['Stealth Level'] = self._stealth_level
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
        if derived_data['Damage'] < 10:
            logger.warning(f'Invalid damage for {derived_data['Name']}, '
                           f'setting it to 10...')
            derived_data['Damage'] = 10
        if derived_data['Stealth Level'] <= 0:
            logger.warning(f'Invalid stealth level for {derived_data['Name']}, '
                           f'setting it to 1...')
            derived_data['Stealth Level'] = 1
        rogue = cls(derived_data['Name'], derived_data['Max Health'], derived_data['Stealth Level'])
        rogue._damage = derived_data['Damage']
        logger.info(f"Character's dict successfully converted into {cls} class!")
        return rogue