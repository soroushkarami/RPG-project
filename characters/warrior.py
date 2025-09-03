import logging
from .base_character import Character

logger = logging.getLogger(__name__)

class Warrior(Character):
    def __init__(self, name: str, base_health: int, armor: int):
        logger.info(f'__init__ initiated, trying to create warrior {name}')
        super().__init__(name, base_health)
        self._armor = armor
        self._damage = 10
        self._weapon = 'メ Basic Sword メ'
        logger.info(f'Warrior created. Name: {name}, Health+Armor: {base_health+armor}, '
                     f'Weapon: {self._weapon}, Damage: {self._damage}')

    @property
    def armor(self):
        logger.debug(f'Accessing "armor" property: {self._armor}')
        return self._armor

    @armor.setter
    def armor(self, value: int):
        try:
            value = int(value)
        except ValueError as e:
            logger.error(f'Non-int value entered as armor value: {e}')
            raise ValueError(f'Armor defense must be a number!')
        if value < 0:
            logger.error(f'A negative int entered as armor value!')
            raise ValueError(f'Armor defence must be positive!')
        logger.info(f"{value} successfully assigned to {self._name}'s armor!")
        self._armor = value

    @property
    def weapon(self):
        logger.debug(f'Accessing "weapon" property: {self._weapon}')
        return self._weapon

    def take_damage(self, amount: int):
        logger.debug(f'"take_damage" method is called...')
        try:
            amount = int(amount)
        except ValueError as e:
            logger.error(f'Non-int value entered as damage value: {e}')
            raise ValueError(f'Invalid damage input!')
        if amount <= 0:
            logger.error(f'A negative int or 0 entered as damage value!')
            raise ValueError(f'Damage amount must be positive!')
        self._armor -= amount
        logger.info(f'New armor = {self._armor}')
        if self._armor >= 0:
            logger.info(f'{self.name} took {amount} damage! (Health= {self._health}, Armor= {self._armor})')
        else:
            logger.warning(f"{self._name}'s armor is negative, armor set to 0, calculating health...")
            remained_damage = amount + self._armor  # note that _armor is negative here so it will subtract from amount
            self._health -= remained_damage
            self._armor = 0
            if self._health <= 0:
                self._health = 0
                logger.warning(f'{self.name} died!')
            elif self._health < 0.2 * self._max_health:
                logger.warning(f"{self._name}'s health is critical! ({self._health} / {self._max_health})")
            else:
                logger.info(f'{self.name} took {amount} damage! (Health= {self._health}, Armor= {self._armor})')

    def level_up(self):
        logger.debug(f'"level_up" method is called...')
        if self._level < 50:
            logger.info(f'{self._name} can be leveled up...')
            super().level_up()
            self._damage += 10
            logger.info(f'{self._name} leveled up! (level = {self._level}, Max Health = {self._max_health})')
            if self._level == 5:
                self._weapon = '🗡 Iron Sword 🗡'
                logger.warning(f'🗡 Iron Sword 🗡 granted to {self._name}!')
            elif self._level == 15:
                self._weapon = '⚚ Silver Sword ⚚'
                logger.warning(f'⚚ Silver Sword ⚚ granted to {self._name}!')
            elif self._level == 30:
                self._weapon = '⸸༺ Legendary Sword ༻⸸'
                logger.warning(f'⸸༺ Legendary Sword ༻⸸ granted to {self._name}!')
            elif self._level == 50:
                self._weapon = '༺𓆩⚔𓆪༻ Doom Sword ༺𓆩⚔𓆪༻'
                logger.warning(f'༺𓆩⚔𓆪༻ Doom Sword ༺𓆩⚔𓆪༻ granted to {self._name}!')
                logger.warning(f'{self._name} is at max level!')
            logger.info(f'Damage= {self._damage}')
        else:
            logger.warning(f'{self._name} is already at max level! (Damage = {self._damage})')

    def attack(self):
        logger.debug(f'"attack" method is called...')
        attack_power = self._level * self._damage
        logger.info(f"{self._name}'s current attack power: {attack_power}")
        return attack_power

    def display_stats(self):
        logger.debug(f'"display_stats" method is called...')
        previous_info = super().display_stats()
        return f'{previous_info} | Armor: {self._armor}'

    def to_dict(self):
        logger.info(f'"to_dict" method is called...')
        data = super().to_dict()
        data['Armor'] = self._armor
        data['Damage'] = self._damage
        data['Weapon'] = self._weapon
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
        if derived_data['Armor'] < 0:
            logger.warning(f'Invalid armor value for {derived_data['Name']}, '
                           f'setting it to 0...')
            derived_data['Armor'] = 0
        warrior = cls(derived_data['Name'], derived_data['Max Health'], derived_data['Armor'])
        warrior._damage = derived_data['Damage']
        warrior._weapon = derived_data['Weapon']
        logger.info(f"Character's dict successfully converted into {cls} class!")
        return warrior











