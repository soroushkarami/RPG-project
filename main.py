import logging
from characters.base_character import Character
from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue
from utils.file_manager import save, load, empty, delete

logging.basicConfig(level= logging.DEBUG,
                    format='%(asctime)s | %(levelname)s: %(message)s',  # this only affect root log not the other modules
                    filemode='w')   # 'w' instead of default which is 'a' to clear console each time the program runs
        # Later I may put it on 'a' and instead add timestamp to keep track of history

base_character_handler = logging.FileHandler('base_character.log')
warrior_handler = logging.FileHandler('warrior.log')
mage_handler = logging.FileHandler('mage.log')
rogue_handler = logging.FileHandler('rogue.log')
file_manager_handler = logging.FileHandler('file_manager.log')  # now we have .log for each module separately

formatter = logging.Formatter('%(asctime)s | %(name)s - %(levelname)s: %(message)s')
base_character_handler.setFormatter(formatter)
warrior_handler.setFormatter(formatter)
mage_handler.setFormatter(formatter)
rogue_handler.setFormatter(formatter)
file_manager_handler.setFormatter(formatter)

logging.getLogger('characters.base_character').addHandler(base_character_handler)
logging.getLogger('characters.warrior').addHandler(warrior_handler)
logging.getLogger('characters.mage').addHandler(mage_handler)
logging.getLogger('characters.rogue').addHandler(rogue_handler)
logging.getLogger('utils.file_manager').addHandler(file_manager_handler)

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














