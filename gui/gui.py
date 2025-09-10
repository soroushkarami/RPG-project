from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue
import logging
import tkinter as tk
from tkinter import messagebox

# todo:
#    position everything better + improve UI (fonts, colors...)
#    write PlayGUI

logger = logging.getLogger(__name__)

class HomeGUI:
    def __init__(self, root):
        logger.debug(f'init method is called...')
        self.root = root

        # buttons
        self.warrior = tk.Button(root, text='Warrior', command=self.warrior_frame)
        self.mage = tk.Button(root, text='Mage', command=self.mage_frame)
        self.rogue = tk.Button(root, text='Rogue', command=self.rogue_frame)
        self.nextbutt = tk.Button(root, text='Next')
        self.backbutt = tk.Button(root, text='Back', command=self.back)
        logger.debug(f'Buttons created successfully!')

        # frame creation
        self.base_frame = tk.Frame(root)
        self.w_frame = tk.Frame(root)
        self.m_frame = tk.Frame(root)
        self.r_frame = tk.Frame(root)
        logger.debug(f'Frames created successfully!')

        self.name_lbl = tk.Label(self.base_frame, text='Name')
        self.name = tk.Entry(self.base_frame)
        self.health_lbl = tk.Label(self.base_frame, text='Health')
        self.health = tk.Entry(self.base_frame)

        self.status = tk.Label(root, text='Choose your class', font=('Ariel', 12))

        # root location
        self.status.grid(row=0, column=1, pady=10)
        self.warrior.grid(row=1, column=0, padx=20, pady=15)
        self.mage.grid(row=1, column=1, padx=10)
        self.rogue.grid(row=1, column=2, padx=30)
        self.base_frame.grid(row=2, column=1)
        self.backbutt.grid(row=4, column=0)
        self.nextbutt.grid(row=4, column=1)

        # base_frame location
        self.name_lbl.grid(row=0, column=0, padx=20)
        self.name.grid(row=0, column=1)
        self.health_lbl.grid(row=1, column=0, pady=15)
        self.health.grid(row=1, column=1, pady=15)
        logger.debug(f'Positioning of the objects set successfully!')

    def back(self):
        logger.info(f'method "back" is called...')
        self.clear_frame_obj()
        self.w_frame.grid_forget()
        self.r_frame.grid_forget()
        self.m_frame.grid_forget()
        self.status.config(text = 'Choose your class')
        self.status.grid(row=0, column=1, pady=10)
        self.warrior.grid(row=1, column=0, padx=20, pady=15)
        self.mage.grid(row=1, column=1, padx=10)
        self.rogue.grid(row=1, column=2, padx=30)
        self.base_frame.grid(row=2, column=1)

    def next(self, cls, first, second, third):
        logger.info(f'method "next" is called...')
        first_getter = first.get()
        if not first_getter:
            messagebox.showerror(f'Value Error', f'Name cannot be empty!')
            logger.warning(f'User left name section empty!')
            return
        try:
            logger.info(f'Trying to convert entered values into integer...')
            conv_sec = int(second.get())
            conv_thi = int(third.get())
        except ValueError as e:
            messagebox.showerror(f'Type Error', f'Non-int input entered as class attributes: {e}')
            logger.warning(f'User entered non-int value(s): {e}')
            return
        if conv_sec <= 0 or conv_thi <= 0:
            messagebox.showerror(f'Value Error', f'Values must be positive!')
            logger.warning(f'User entered non-positive value(s)!')
            return
        if cls == 'Warrior':
            self.warrior_class(name=first_getter, health=conv_sec, armor=conv_thi)
            logger.info(f'Valid inputs, trying to call warrior_class method...')
        elif cls == 'Mage':
            self.mage_class(name=first_getter, health=conv_sec, mana=conv_thi)
            logger.info(f'Valid inputs, trying to call mage_class method...')
        elif cls == 'Rogue':
            self.rogue_class(name=first_getter, health=conv_sec, stealth_lvl=conv_thi)
            logger.info(f'Valid inputs, trying to call rogue_class method...')
        self.deleter(first, second, third)      # to empty the entries on gui after the character is created

    def deleter(self, first, second, third):
        logger.debug(f'method "deleter" is called...')
        first.delete(0, tk.END)
        second.delete(0, tk.END)
        third.delete(0, tk.END)

    def clear_frame_obj(self):
        """
        because in each frame I create new sets of tk objects, first i need to delete the
        already created objects before creating new ones so that they don't stack on top of each other
        """
        logger.debug(f'method "clear_frame_obj" is called...')
        for frame in (self.w_frame, self.m_frame, self.r_frame):
            for obj in frame.winfo_children():
                obj.destroy()
            frame.grid_forget()

    def warrior_frame(self):
        logger.debug(f'method "warrior_frame" is called...')
        self.clear_frame_obj()
        name_lbl, name, health_lbl, health = self.name_lbl, self.name, self.health_lbl, self.health
        armor_lbl = tk.Label(self.w_frame, text='Armor')
        armor = tk.Entry(self.w_frame)
        logger.info(f'name, health, armor are received, jumping into "next" method...')
        self.nextbutt.config(command=lambda : self.next('Warrior', name, health, armor))

        armor_lbl.grid(row=0, column=0, padx=20)
        armor.grid(row=0, column=1)

        self.warrior.grid_forget()
        self.mage.grid_forget()
        self.rogue.grid_forget()
        self.status.config(text='Warrior class chosen!')
        self.m_frame.grid_forget()
        self.r_frame.grid_forget()
        self.w_frame.grid(row=3, column=1)
        self.nextbutt.grid(pady=20)
        self.backbutt.grid(pady=20)
        logger.debug(f'Visibility and positioning of the frames set successfully!')

    def warrior_class(self, name, health, armor):
        logger.debug(f'method "warrior_class" is called...')
        char = Warrior(name, health, armor)
        self.status.config(text=f'Warrior "{name}" successfully created!')
        logger.info(f'Warrior {name} successfully created and returned...')
        return char

    def mage_frame(self):
        logger.debug(f'method "mage_frame" is called...')
        self.clear_frame_obj()
        name_lbl, name, health_lbl, health = self.name_lbl, self.name, self.health_lbl, self.health
        mana_lbl = tk.Label(self.m_frame, text='Mana')
        mana = tk.Entry(self.m_frame)
        logger.info(f'name, health, mana are received, jumping into "next" method...')
        self.nextbutt.config(command=lambda : self.next('Mage', name, health, mana))

        mana_lbl.grid(row=0, column=0, padx=20)
        mana.grid(row=0, column=1)

        self.warrior.grid_forget()
        self.mage.grid_forget()
        self.rogue.grid_forget()
        self.status.config(text='Mage class chosen!')
        self.r_frame.grid_forget()
        self.w_frame.grid_forget()
        self.m_frame.grid(row=3, column=1)
        self.nextbutt.grid(pady=20)
        self.backbutt.grid(pady=20)
        logger.debug(f'Visibility and positioning of the frames set successfully!')

    def mage_class(self, name, health, mana):
        logger.debug(f'method "mage_class" is called...')
        char = Mage(name, health, mana)
        self.status.config(text=f'Mage "{name}" successfully created!')
        logger.info(f'Mage {name} successfully created and returned...')
        return char

    def rogue_frame(self):
        logger.debug(f'method "rogue_frame" is called...')
        self.clear_frame_obj()
        name_lbl, name, health_lbl, health = self.name_lbl, self.name, self.health_lbl, self.health
        stealth_lvl_lbl = tk.Label(self.r_frame, text='Stealth Level')
        stealth_lvl = tk.Entry(self.r_frame)
        logger.info(f'name, health, stealth level are received, jumping into "next" method...')
        self.nextbutt.config(command=lambda : self.next('Rogue', name, health, stealth_lvl))

        stealth_lvl_lbl.grid(row=0, column=0, padx=20)
        stealth_lvl.grid(row=0, column=1)

        self.warrior.grid_forget()
        self.mage.grid_forget()
        self.rogue.grid_forget()
        self.status.config(text='Rogue class chosen!')
        self.m_frame.grid_forget()
        self.w_frame.grid_forget()
        self.r_frame.grid(row=3, column=1)
        self.nextbutt.grid(pady=20)
        self.backbutt.grid(pady=20)
        logger.info(f'Visibility and positioning of the frames set successfully!')

    def rogue_class(self, name, health, stealth_lvl):
        logger.debug(f'method "rogue_class" is called...')
        char = Rogue(name, health, stealth_lvl)
        self.status.config(text=f'Rogue "{name}" successfully created!')
        logger.warning(f'Rogue {name} successfully created and returned...')
        return char

