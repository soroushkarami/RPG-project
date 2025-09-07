import logging
import json
import os

logger = logging.getLogger(__name__)

# TODO: ADD THESE
#    Configuration Management
#    Backup System
#    Atomic Operations
#    File Locking
#    Validation


path = os.path.join(os.path.dirname(__file__), 'utils', 'characters.json')      # creating a relative path
def save(character):
    logger.debug(f'"save" method is called for {character}...')
    if os.path.exists(path):
        with open(path, 'r', encoding= 'utf-8') as file:
            logger.info(f'Json file found! Opening to read...')
            try:
                logger.debug(f'Trying to load the data from json file...')
                first_list = json.load(file)
            except json.JSONDecodeError:      # this is an error happens when json file is broken
                logger.error(f'Json file corrupted! Starting with an empty list...')
                first_list = []
            logger.info(f'Data loaded from json file successfully!')
    else:
        logger.warning(f'Json file not found! Starting with an empty list...')
        first_list = []
    ready_char = character.to_dict()
    if first_list:      # this section is to avoid adding repetitive characters
        for char in first_list:
            if not isinstance(char, dict):      # because json might contain 'null'
                logger.warning(f'A non-dictionary data found, skipping...')
                continue
            if ready_char.get('Name') == char.get('Name'):
                logger.warning(f'{char.get('Name')} is already in the list!')
                return
    first_list.append(ready_char)      # we first turn class into a dict and then append the dict
    logger.info(f'{ready_char.get('Name')} added to the updated list!')
    # now we overwrite the list into the json file
    with open(path, 'w', encoding= 'utf-8') as file:
        logger.debug(f'Trying to write the updated list into the json file...')
        json.dump(first_list, file, indent= 4, ensure_ascii= False)     # ensure_ascii False make it recognize emojis and doesn't turn them into letters
    logger.info(f"{ready_char.get('Name')} added to the json file successfully!")


def load(classes):
    logger.debug(f'"load" method is called with specified class-mapping...')
    if not os.path.exists(path):
        print(f'Json file not found! Nothing loaded...')
        return []
    with open(path, 'r', encoding= 'utf-8') as file:
        logger.info(f'Json file found! Opening to read...')
        try:
            logger.debug(f'Trying to load the data from json file...')
            data = json.load(file)
        except json.JSONDecodeError:    # this is an error happens when json file is broken
            logger.error(f'Json file corrupted! Nothing loaded...')
            return []
    logger.info(f'Data loaded from json file successfully!')
    ready_char = []
    for character_data in data:     # character_data is a dict / data is a list of dicts
        duplicated = False
        if not isinstance(character_data, dict):
            logger.warning(f'A non-dictionary data found, skipping...')
            continue
        for char in ready_char:   # to avoid loading repetitive characters
            if character_data.get('Name') == char.name:     # NOTE: char here is an object not a dict!
                logger.warning(f'{character_data.get('Name')} is already loaded, skipping...')
                duplicated = True
        if duplicated:
            logger.debug(f'skipping character because of duplication...')
            continue
        logger.debug(f'Trying to find the suitable class for {character_data.get('Name')}...')
        if character_data.get('Class') in classes.keys():
            the_class = classes[character_data.get('Class')]
            the_object = the_class.from_dict(character_data)    # here we turned dict into class
        else:
            logger.warning(f"Loading {character_data.get('Name')} failed! Invalid class: {character_data.get('Class')}, skipping...")
            continue
        ready_char.append(the_object)
        logger.info(f'Success! {character_data['Name']} loaded as {character_data['Class']} class.')
    logger.info(f'Returning all the loaded characters...')
    return ready_char


def empty():
    logger.debug(f'"empty" method is called...')
    try:
        with open(path, 'w'):
            if not os.path.exists(path):
                logger.warning(f'Json file not found! New empty file created!')
            else:
                logger.info(f'Done! Json file is empty!')
        logger.info(f'Emptying process ended...')
        return True
    except Exception as e:
        logger.error(f'Error emptying the json file "{path}": {e}')
        return False


def delete():
    logger.debug(f'"delete" method is called...')
    if os.path.exists(path):
        logger.info(f'Json file found!')
        while True:
            logger.debug(f'Waiting for user confirmation...')
            confirm = input(f"Are you sure you want to delete characters' database?(Y/N) ").upper()
            if confirm == 'Y':
                os.remove(path)
                logger.info(f"Done! Json file is deleted!")
                break
            elif confirm == 'N':
                logger.info(f"Deleting process canceled!")
                break
            else:
                logger.error(f'Invalid input from user!')
                continue
        logger.info(f'Deleting process ended...')
        return True
    else:
        logger.error(f'Json file not found!')
        return False







































