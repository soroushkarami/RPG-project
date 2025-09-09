from pickletools import bytes_types

from characters.base_character import Character
from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue
import logging
import tkinter as tk
from tkinter import messagebox

# todo:
#    bring next butt out of all frames
#    create back butt
#    write loggings
#    position everything better + improve UI (fonts, colors...)
#    write PlayGUI


class HomeGUI:
    def __init__(self, root):
        self.root = root

        # class choice
        self.warrior = tk.Button(root, text='Warrior', command=self.warrior_frame)
        self.mage = tk.Button(root, text='Mage', command=self.mage_frame)
        self.rogue = tk.Button(root, text='Rogue', command=self.rogue_frame)

        # frame creation
        self.base_frame = tk.Frame(root)
        self.w_frame = tk.Frame(root)
        self.m_frame = tk.Frame(root)
        self.r_frame = tk.Frame(root)

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

        # base_frame location
        self.name_lbl.grid(row=0, column=0, padx=20)
        self.name.grid(row=0, column=1)
        self.health_lbl.grid(row=1, column=0, pady=15)
        self.health.grid(row=1, column=1, pady=15)

    def next(self, cls, first, second, third):
        first_getter = first.get()
        if not first_getter:
            messagebox.showerror(f'Value Error', f'Name cannot be empty!')
            raise ValueError
        try:
            conv_sec = int(second.get())
            conv_thi = int(third.get())
        except ValueError as e:
            messagebox.showerror(f'Type Error', f'Non-int input entered as class attributes: {e}')
            raise ValueError
        if conv_sec <= 0 or conv_thi <= 0:
            messagebox.showerror(f'Value Error', f'Values must be positive!')
            raise ValueError
        if cls == 'Warrior':
            self.warrior_class(name=first_getter, health=conv_sec, armor=conv_thi)
        elif cls == 'Mage':
            self.mage_class(name=first_getter, health=conv_sec, mana=conv_thi)
        elif cls == 'Rogue':
            self.rogue_class(name=first_getter, health=conv_sec, stealth_lvl=conv_thi)
        self.deleter(first, second, third)      # to empty the entries on gui after the character is created

    def frame_grid(self, first, second, next_butt):
        first.grid(row=0, column=0, padx=20)
        second.grid(row=0, column=1)
        next_butt.grid(row=1, column=1, pady=15)

    def deleter(self, first, second, third):
        first.delete(0, tk.END)
        second.delete(0, tk.END)
        third.delete(0, tk.END)

    def warrior_frame(self):
        name_lbl, name, health_lbl, health = self.name_lbl, self.name, self.health_lbl, self.health
        armor_lbl = tk.Label(self.w_frame, text='Armor')
        armor = tk.Entry(self.w_frame)
        next_butt = tk.Button(self.w_frame, text='Next',
                              command=lambda : self.next('Warrior', name, health, armor))

        self.frame_grid(armor_lbl, armor, next_butt)

        self.warrior.grid_forget()
        self.mage.grid_forget()
        self.rogue.grid_forget()
        self.status.config(text='Warrior class chosen!')
        self.m_frame.grid_forget()
        self.r_frame.grid_forget()
        self.w_frame.grid(row=3, column=1)

    def warrior_class(self, name, health, armor):
        self.status.config(text=f'Warrior "{name}" successfully created!')
        return Warrior(name, health, armor)

    def mage_frame(self):
        name_lbl, name, health_lbl, health = self.name_lbl, self.name, self.health_lbl, self.health
        mana_lbl = tk.Label(self.m_frame, text='Mana')
        mana = tk.Entry(self.m_frame)
        next_butt = tk.Button(self.m_frame, text='Next',
                              command=lambda : self.next('Mage', name, health, mana))

        self.frame_grid(mana_lbl, mana, next_butt)

        self.warrior.grid_forget()
        self.mage.grid_forget()
        self.rogue.grid_forget()
        self.status.config(text='Mage class chosen!')
        self.r_frame.grid_forget()
        self.w_frame.grid_forget()
        self.m_frame.grid(row=3, column=1)

    def mage_class(self, name, health, mana):
        self.status.config(text=f'Mage "{name}" successfully created!')
        return Mage(name, health, mana)

    def rogue_frame(self):
        name_lbl, name, health_lbl, health = self.name_lbl, self.name, self.health_lbl, self.health
        stealth_lvl_lbl = tk.Label(self.r_frame, text='Stealth Level')
        stealth_lvl = tk.Entry(self.r_frame)
        next_butt = tk.Button(self.r_frame, text='Next',
                              command=lambda : self.next('Rogue', name, health, stealth_lvl))

        self.frame_grid(stealth_lvl_lbl, stealth_lvl, next_butt)

        self.warrior.grid_forget()
        self.mage.grid_forget()
        self.rogue.grid_forget()
        self.status.config(text='Rogue class chosen!')
        self.m_frame.grid_forget()
        self.w_frame.grid_forget()
        self.r_frame.grid(row=3, column=1)

    def rogue_class(self, name, health, stealth_lvl):
        self.status.config(text=f'Rogue "{name}" successfully created!')
        return Rogue(name, health, stealth_lvl)

