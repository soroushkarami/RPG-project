from characters.base_character import Character
from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue
from utils.file_manager import save, load, empty, delete

my_warrior = Warrior('Bran', 170, 30)
my_mage = Mage('Ron', 150, 20)
my_rogue = Rogue('Ezio', 135, 1)

empty()

save(my_rogue)
save(my_warrior)
save(my_mage)

class_mapping = {
    'Character': Character,
    'Warrior': Warrior,
    'Mage': Mage,
    'Rogue': Rogue
}

derived_chars = load(class_mapping)
counter = 1
for char in derived_chars:
    print(f'Character No.{counter}: {char.name}, a/an {char.__class__.__name__}')
    counter += 1

delete()














