# Glom The Ugly Creature
# Programmer: Dylan Yankee
# Purpose: Eat the candies before you explode!

## Make sure you have Python, TKinter, and PyGame installed.
# To run the program, these are the commands:
#   Linux           (Bash): ./br.sh
#   Windows   (Powershell): ./br   (or)   ./br.ps1

import os
import eatable
import entity
import level1
import movement
import soundload
import spawners
import texload
import util

menus = os.path.join("menus.py")
os.system(f"python {menus}")