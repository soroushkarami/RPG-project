class Character:
    def __init__(self, name, starting_health):
        self._name = name
        self._health = starting_health
        self._max_health = starting_health
        self._level = 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Name cannot be empty')
        self._name = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        try:
            value = int(value)
        except ValueError as e:
            print(f'{e}: Health must be a number')
        if value <= 0:
            raise ValueError('Health must be positive')
        self._health = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        try:
            value = int(value)
        except ValueError as e:
            print(f'{e}: Level must be a number')
            raise
        if value <= 0:
            raise ValueError('Level must be positive')
        self._level = value

    def level_up(self):
        self._level += 1
        self._max_health += 100
        self._health = self._max_health

    def take_damage(self, amount):
        try:
            amount = int(amount)
        except ValueError as e:
            print(f'{e}: Invalid damage input!')
            raise
        if amount <= 0:
            raise ValueError('Damage amount must be positive!')
        self._health -= amount
        if self._health <= 0:
            print(f'{self.name} died!')

    def heal(self, amount):
        try:
            amount = int(amount)
        except ValueError as e:
            print(f'{e}: Invalid heal input!')
            raise
        if amount <= 0:
            raise ValueError('Heal amount must be positive!')
        new_health = self._health + amount
        if new_health > self._max_health:
            raise ValueError('Health exceeding max health!')
        self._health = new_health

    def attack(self):
        pass        # I want to use it in children

    def display_stats(self):
        return (f'Name: {self._name} | Level: {self._level} | '
                f'Health: {self._health} | Max Health: {self._max_health}')

