class Character:
    def __init__(self, name: str, starting_health: int):
        self._name = name
        self._level = 1
        self._health = starting_health
        self._max_health = starting_health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError(f'Name cannot be empty')
        self._name = value

    @property
    def level(self):
        return self._level
    # I am not writing setter for level; because I don't want anyone to be
    # able to change it, you can only read it, it only changes with level_up

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f'Health must be a number')
        if value < 0:
            raise ValueError(f'Health must be positive')
        self._health = value

    @property
    def max_health(self):
        return self._max_health
    # read-only; no setter!

    @property
    def health_percentage(self):
        return f'{round((self._health / self._max_health) * 100)}%'

    @property
    def is_alive(self):
        return self._health > 0

    @property
    def is_dead(self):
        return not self.is_alive

    def level_up(self):
        self._level += 1
        self._max_health += 100
        self._health = self._max_health
        print(f"{self.name} leveled up to level {self.level}!")

    def take_damage(self, amount: int):
        try:
            amount = int(amount)
        except ValueError:
            raise ValueError(f'Invalid damage input!')
        if amount <= 0:
            raise ValueError(f'Damage amount must be positive!')
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            print(f'{self.name} died!')
        else:
            print(f'{self._name} took {amount} damage! (Health= {self._health}')

    def heal(self, amount: int):
        try:
            amount = int(amount)
        except ValueError as e:
            raise ValueError(f'Invalid heal input!')
        if amount <= 0:
            raise ValueError(f'Heal amount must be positive!')
        self._health += amount
        if self._health > self._max_health:
            self._health = self._max_health
            print(f'{self._name} is fully healed!')
        else:
            print(f'{self._name} healed for {amount}! (Health= {self._health})')

    def attack(self):
        pass        # I want to use it in children

    def display_stats(self):
        return (f'Name: {self._name} | Level: {self._level} | '
                f'Health: {self._health} | Max Health: {self._max_health}')
