import json
import os

# TODO: ADD THESE
#    Configuration Management
#    Backup System
#    Atomic Operations
#    File Locking
#    Validation


path = r'F:\python\RPG_Characters\utils\characters.json'
def save(character):
    if os.path.exists(path):
        with open(path, 'r', encoding= 'utf-8') as file:
            try:
                ready_list = json.load(file)
            except json.JSONDecodeError:      # this is an error happens when json file is broken
                print(f'File corrupted; starting with an empty list...')
                ready_list = []
    else:
        ready_list = []
    ready_char = character.to_dict()
    if ready_list:      # this section is to avoid adding repetitive characters
        for char in ready_list:
            if not isinstance(char, dict):      # because json might contain 'null'
                continue
            if ready_char.get('Name') == char.get('Name'):
                print(f'{char.get('Name')} is already in the list!')
                return
    ready_list.append(ready_char)      # we first turn class into a dict and then append the dict
    # now we overwrite the list into the json file
    with open(path, 'w', encoding= 'utf-8') as file:
        json.dump(ready_list, file, indent= 4, ensure_ascii= False)     # ensure_ascii False make it recognize emojis and doesn't turn them into letters
    print(f"{ready_char.get('Name')} added to the database.")


def load(classes):
    if not os.path.exists(path):
        print(f'File not found! Starting with an empty list...')
        return []
    with open(path, 'r', encoding= 'utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:    # this is an error happens when json file is broken
            print(f'File corrupted! Starting with an empty list...')
            return []
    ready_characters = []
    for character_data in data:     # character_data is a dict / data is a list of dicts
        duplicated = False
        if not isinstance(character_data, dict):
            print(f'Non-dict data found, skipping...')
            continue
        for char in ready_characters:   # to avoid loading repetitive characters
            if character_data.get('Name') == char.name:     # NOTE: char here is an object not a dict!
                duplicated = True
        if duplicated:
            continue
        if character_data.get('Class') in classes.keys():
            the_class = classes[character_data.get('Class')]
            the_object = the_class.from_dict(character_data)    # here we turned dict into class
        else:
            print(f"{character_data.get('Name')} skipped...")
            continue
        ready_characters.append(the_object)
    return ready_characters


def empty():
    try:
        with open(path, 'w') as file:
            if not os.path.exists(path):
                print(f'File "characters.json" not found! new empty file created!')
            else:
                print(f'Done, File is empty!')
        return True
    except Exception as e:
        print(f'Error emptying file: {e}')
        return False


def delete():
    if os.path.exists(path):
        while True:
            confirm = input(f"Are you sure you want to delete characters' database?(Y/N) ").upper()
            if confirm == 'Y':
                os.remove(path)
                print(f"Characters' database deleted!")
                break
            elif confirm == 'N':
                break
            else:
                print(f'Invalid input...')
                continue
        return True
    else:
        print(f'File "characters.json" not found!')
        return False







































