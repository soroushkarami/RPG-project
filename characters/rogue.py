from base_character import Character
import random

class Rogue(Character):
    def __init__(self, name: str, base_health: int, stealth_level: int):
        super().__init__(name, base_health)
        self._stealth_level = stealth_level

    def attack(self):
        base_damage = 10
        level_damage = self._level * base_damage
        critical_hit = 2 * level_damage
        critical_hit_chance = self._level * 0.1
        final_damage = random.choices([critical_hit, level_damage],
                                      weights= [critical_hit_chance, 1-critical_hit_chance],
                                      k=1)[0]
        return [critical_hit, final_damage]

    def sneak_attack(self):
        return self.attack()[0]     # 100% critical hit !

    def display_stats(self):
        previous_info = super().display_stats()
        return f'{previous_info} | Stealth Level: {self._stealth_level}'
