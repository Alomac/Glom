import tkinter as tk
import os

def runGame():
    Level_1 = os.path.join("level1.py")
    os.system(f"python {Level_1}")
    #windowIn.destroy

#Launcher window
def launchWin():
    window = tk.Tk()
    window.geometry("480x445+500+150")
    window.title("Glom Game Launcher")
    #window.wm_iconphoto(False, "resources/glom.ico")
    frameA = tk.Frame(master=window, width=400, height=400)

    frameA.pack()

    frameB = tk.Frame(master=window, width=400, height=400, borderwidth=5, relief="sunken")
    frameB.pack(side=tk.BOTTOM)

    name = tk.Label(master=frameA, text="Glom The Ugly Creature", width=60, height=20, bg="green")
    name.pack()

    play = tk.Button(master=frameB, text="Play", padx=20, pady=5, borderwidth=3, command=runGame)
    play.pack(side=tk.LEFT)

    # levels = tk.Button(master=frameB, text="Levels", padx=20, pady=5, borderwidth=3)
    # levels.pack(side=tk.LEFT)

    helpg = tk.Button(master=frameB, text="Help", padx=20, pady=5, borderwidth=3, command=helpWin)
    helpg.pack(side=tk.LEFT)

    quitg = tk.Button(master=frameB, text="Quit", padx=20, pady=5, borderwidth=3, command=window.destroy)
    quitg.pack(side=tk.LEFT)

    window.mainloop()

#Help window that shows the rules
def helpWin():
    window = tk.Tk()
    window.geometry("480x300+525+150")
    window.title("Glom Help")
    frameA = tk.Frame(master=window, width=400, height=400)

    frameA.pack()

    frameB = tk.Frame(master=window, width=400, height=400, borderwidth=5, relief="sunken")
    frameB.pack(side=tk.BOTTOM)

    name = tk.Label(master=frameA, text="@___Help___@", width=60, height=3, bg="green")
    name.pack()

    txthldr = (
        "You are Glom The Ugly Creature.\n"
        "You must eat as many candies as possible before \n"
        "Your timer runs out, or you will explode.\n"
        "There is a troll trying to eat you and your candies.\n"
        "If you are bigger than the troll you can eat it, but \n"
        "if the troll is bigger than you it can eat you.\n"
        "If you eat the troll, you win!\n\n"
        "Chocolate makes your time go down, and you get smaller.\n"
        "Peppermint makes your time go down a little, but you get bigger."
    )
    maintxt = tk.Label(master=frameA, text=txthldr)
    maintxt.pack(side=tk.BOTTOM)

    quitg = tk.Button(master=frameB, text=" <-- Back", padx=20, pady=5, borderwidth=3, command=window.destroy)
    quitg.pack(side=tk.LEFT)

    window.mainloop()

launchWin()
