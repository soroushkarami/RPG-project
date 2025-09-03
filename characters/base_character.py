import logging

logger = logging.getLogger(__name__)

class Character:
    def __init__(self, name: str, starting_health: int):
        logger.info(f'__init__ initiated, trying to create base character {name}')
        self._name = name
        self._level = 1
        self._health = starting_health
        self._max_health = starting_health
        logger.info(f'Base character created. Name: {name}, Health: {starting_health}')

    @property
    def name(self):
        logger.debug(f'Accessing "name" property: {self._name}')
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            logger.error(f'Empty value entered for name...')
            raise ValueError(f'Name cannot be empty')
        self._name = value
        logger.info(f'{value} successfully assigned as name!')

    @property
    def level(self):
        logger.debug(f'Accessing "level" property...')
        return self._level
    # I am not writing setter for level; because I don't want anyone to be
    # able to change it, you can only read it, it only changes with level_up

    @property
    def health(self):
        logger.debug(f'Accessing "health" property...')
        return self._health

    @health.setter
    def health(self, value: int):
        try:
            value = int(value)
        except ValueError as e:
            logger.error(f'Non-int value entered as health value: {e}')
            raise ValueError(f'Health must be a number!')
        if value < 0:
            logger.error(f'A negative int entered as health value!')
            raise ValueError(f'Health must be positive!')
        self._health = value
        logger.info(f"{value} successfully assigned to {self._name}'s health!")

    @property
    def max_health(self):
        logger.debug(f'Accessing "max_health" property...')
        return self._max_health
    # read-only; no setter!

    @property
    def health_percentage(self):
        logger.debug(f'Accessing "health_percentage" property...')
        return f'{round((self._health / self._max_health) * 100)}%'

    @property
    def is_alive(self):
        logger.debug(f'Accessing "is_alive" property...')
        return self._health > 0

    @property
    def is_dead(self):
        logger.debug(f'Accessing "is_dead" property...')
        return not self.is_alive

    def level_up(self):
        logger.debug(f'"level_up" method is called...')
        self._max_health += 100
        self._level += 1
        self._health = self._max_health
        logger.info(f"{self.name} leveled up to level {self.level}, new max health = {self._max_health}!")

    def take_damage(self, amount: int):
        logger.debug(f'"take_damage" method is called...')
        try:
            amount = int(amount)
        except ValueError as e:
            logger.error(f'Non-int value entered as damage value: {e}')
            raise ValueError(f'Invalid damage input!')
        if amount <= 0:
            logger.error(f'A negative int entered as damage amount!')
            raise ValueError(f'Damage amount must be positive!')
        self._health -= amount
        logger.debug(f'New health = {self._health}')
        if self._health < 0.2 * self._max_health:   # this line is just for the warning logging
            logger.warning(f"{self._name}'s health is critical! ({self._health} / {self._max_health})")
        if self._health <= 0:
            self._health = 0
            logger.warning(f'{self.name} died!')
        else:
            logger.info(f'{self._name} took {amount} damage! (Health= {self._health}')

    def heal(self, amount: int):
        logger.debug(f'"heal" method is called...')
        try:
            amount = int(amount)
        except ValueError as e:
            logger.error(f'Non-int entered as healing amount: {e}')
            raise ValueError(f'Invalid heal input!')
        if amount <= 0:
            logger.error(f'A negative int entered as damage amount!')
            raise ValueError(f'Heal amount must be positive!')
        self._health += amount
        logger.debug(f'New health = {self._health}')
        if self._health > self._max_health:
            logger.warning(f"{self._name}'s health exceeds max health, "
                            f"setting it to max({self._max_health})...")
            self._health = self._max_health
            logger.info(f'{self._name} is fully healed, Health = {self._health}')
        else:
            logger.info(f'{self._name} healed for {amount}! (Health = {self._health})')

    def attack(self):
        pass        # I want to use it in children

    def display_stats(self):
        logger.debug(f'"display_stats" method is called...')
        return (f'Name: {self._name} | Level: {self._level} | '
                f'Health: {self._health} | Max Health: {self._max_health}')

    def to_dict(self):  # to make it ready for file management: writing to json file
        logger.debug(f'"to_dict" method is called...')
        base_dict = {}
        base_dict['Class'] = self.__class__.__name__
        base_dict['Name'] = self._name
        base_dict['Level'] = self._level
        base_dict['Health'] = self._health
        base_dict['Max Health'] = self._max_health
        logger.info(f'Dictionary for {self._name} successfully created!')
        return base_dict

    @classmethod
    def from_dict(cls, derived_data):  # to make it ready for file management: reading from json file
        logger.debug(f'"from_dict" classmethod is called...')
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
        base_character = cls(derived_data['Name'], derived_data['Max Health'])
        base_character._level = derived_data['Level']
        base_character._health = derived_data['Health']
        base_character._max_health = derived_data['Max Health']
        logger.info(f"Character's dict successfully converted into {cls} class!")
        return base_character










