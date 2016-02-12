from Attack import *
from tkinter import *
from Pokedex import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        # Assigning string variables for user text entry
        self.userStrVar = StringVar()
        self.userStrVar.set("")

        self.cpuStrVar = StringVar()
        self.cpuStrVar.set("")

        self.moveStrVar1 = StringVar()
        self.moveStrVar1.set("")

        self.moveStrVar2 = StringVar()
        self.moveStrVar2.set("")

        # WIDGETS
        # Buttons
        self.pokedexBtn = Button(self, text="See All Pokemon", command=self.seePokedex)
        self.pokedexBtn.grid(row=0, column=1)

        self.checkBtn = Button(self, text="Lock In", command=self.checkPokemon)
        self.checkBtn.grid(row=1, column=1)

        self.battleBtn = Button(self, text="Begin Battle", state=DISABLED, command=self.beginBattle)
        self.battleBtn.grid(row=2, column=1)

        self.moveBtn1 = Button(self, text="Select Move", state=DISABLED, command=self.selectMove1)
        self.moveBtn1.grid(row=7, column=0)

        self.moveBtn2 = Button(self, text="Select Move", state=DISABLED, command=self.selectMove2)
        self.moveBtn2.grid(row=7, column=2)

        self.restartBtn = Button(self, text="Restart?", state=DISABLED, command=self.restart)
        self.restartBtn.grid(row=7, column=1)

        # Labels, Entry fields, and Text Boxes
        self.entLabel1 = Label(self, text="Choose your Pokemon: ")
        self.entLabel1.grid(row=0, column=0)

        self.entName1 = Entry(self, textvariable=self.userStrVar)  # Pokemon name entry
        self.entName1.grid(row=1, column=0, rowspan=2)

        self.moveText1 = Text(self, width=20, height=8, state=DISABLED)  # Text box with moveset and HP
        self.moveText1.grid(row=5, column=0, sticky=S)

        self.entLabel2 = Label(self, text="Choose your opponent: ")
        self.entLabel2.grid(row=0, column=2)

        self.entName2 = Entry(self, textvariable=self.cpuStrVar)  # Pokemon name entry
        self.entName2.grid(row=1, column=2, rowspan=2)

        self.moveText2 = Text(self, width=20, height=8, state=DISABLED)  # Text box with moveset and HP
        self.moveText2.grid(row=5, column=2, sticky=S)

        self.txtStats = Text(self, width=50, height=10, state=DISABLED)  # Main text box
        self.txtStats.grid(row=3, column=1)

        self.moveEnt1 = Entry(self, textvariable=self.moveStrVar1, state=DISABLED)  # Move entry field 1
        self.moveEnt1.grid(row=6,column=0)

        self.moveEnt2 = Entry(self, textvariable=self.moveStrVar2, state=DISABLED)  # Move entry field 2
        self.moveEnt2.grid(row=6, column=2)

        # Sprites
        tempImg = PhotoImage(file="Sprites/white.gif")  # first putting a blank image for each sprite, will replace later after pressing "Begin Battle"

        # Creating an image label object for each sprite
        self.sprite1Label = Label(self, image=tempImg)
        self.sprite1Label.image = tempImg
        self.sprite1Label.grid(row=3, column=0)

        self.sprite2Label = Label(self, image=tempImg)
        self.sprite2Label.image = tempImg
        self.sprite2Label.grid(row=3, column=2)


        # Pokemon Objects
        # Blank until the user enters which Pokemon they want
        self.userPokemon = None
        self.cpuPokemon = None

    # Creating a method to print the list of all Pokemon
    def seePokedex(self):
        self.txtStats.config(state=NORMAL)
        self.txtStats.delete(0.0, END)
        for pokemon in pokedex:
            self.txtStats.insert(END, "\n" + pokemon)
        self.txtStats.config(state=DISABLED)

    # Creating a method to check if the Pokemon are valid and actually usable
    # Returns an error message if the Pokemon are not usable
    def checkPokemon(self):
        if self.userStrVar != "" and self.cpuStrVar != "":
            if self.userStrVar.get().lower() in pokedex and self.cpuStrVar.get().lower() in pokedex:
                self.txtStats.config(state=NORMAL)
                self.txtStats.delete(0.0, END)
                self.txtStats.insert(0.0, "You are ready to battle.")
                self.txtStats.config(state=DISABLED)

                self.checkBtn.config(state=DISABLED)
                self.entName1.config(state=DISABLED)
                self.entName2.config(state=DISABLED)
                self.pokedexBtn.config(state=DISABLED)
                self.battleBtn.config(state=NORMAL)

                self.userPokemon = Pokemon(self.userStrVar.get())
                self.cpuPokemon = Pokemon(self.cpuStrVar.get())

            # Returning an error message if Pokemon are not valid
            else:
                self.txtStats.config(state=NORMAL)
                self.txtStats.delete(0.0, END)
                self.txtStats.insert(0.0, "Please make sure the Pokemon you've entered are in the Pokedex")
                self.txtStats.config(state=DISABLED)
                self.battleBtn.config(state=DISABLED)

    # Creating a method to actually start the battle
    def beginBattle(self):
        # Replacing the blank image with the actual sprites of the appropriate Pokemon
        # Using the user-input string to determine which sprite image to use
        self.sprite1 = PhotoImage(file="Sprites/" + self.userStrVar.get().lower() + ".gif")
        self.sprite1Label.configure(image=self.sprite1)
        self.sprite1Label.image = self.sprite1

        self.sprite2 = PhotoImage(file="Sprites/" + self.cpuStrVar.get().lower() + ".gif")
        self.sprite2Label.configure(image=self.sprite2)
        self.sprite2Label.image = self.sprite2

        # Printing each Pokemon's HP and moveset to its respective box
        self.moveText1.config(state=NORMAL)
        self.moveText2.config(state=NORMAL)
        self.moveText1.delete(0.0, END)
        self.moveText2.delete(0.0, END)
        self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
        self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
        self.moveText1.config(state=DISABLED)
        self.moveText2.config(state=DISABLED)

        # Deciding which Pokemon to enable first based on the speed (battleSpeed) stat
        if self.userPokemon.isAlive() and self.cpuPokemon.isAlive():
            if self.userPokemon.battleSpeed >= self.cpuPokemon.battleSpeed:
                self.moveEnt1.config(state=NORMAL)
                self.moveBtn1.config(state=NORMAL)
            elif self.cpuPokemon.battleSpeed > self.userPokemon.battleSpeed:
                self.moveEnt2.config(state=NORMAL)
                self.moveBtn2.config(state=NORMAL)
        self.battleBtn.config(state=DISABLED)

    # Method takes the user-inputted string and plugs it into the attack function
    # Prints the result of the attack function to the center text box
    def selectMove1(self):
        if self.moveStrVar1.get().lower() in self.userPokemon.moveList:
            self.txtStats.config(state=NORMAL)
            self.txtStats.delete(0.0, END)
            self.txtStats.insert(0.0, attack(self.moveStrVar1.get(), self.userPokemon, self.cpuPokemon))
            self.txtStats.config(state=DISABLED)

            # Updating the info for both Pokemon after the move has been used
            self.moveText1.config(state=NORMAL)
            self.moveText2.config(state=NORMAL)
            self.moveText1.delete(0.0, END)
            self.moveText2.delete(0.0, END)
            self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
            self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
            self.moveText1.config(state=DISABLED)
            self.moveText2.config(state=DISABLED)

            # If one of the Pokemon faints, this method will end the battle by disabling all other buttons/fields except
            # for the Restart button
            if not self.cpuPokemon.isAlive():
                self.txtStats.config(state=NORMAL)
                self.txtStats.insert(END, "\n" + self.cpuPokemon.faint())
                self.txtStats.insert(END, "\nPlay again?")
                self.txtStats.config(state=DISABLED)
                self.moveEnt1.delete(0, END)
                self.restartBtn.config(state=NORMAL)
                self.moveBtn1.config(state=DISABLED)
                self.moveEnt1.config(state=DISABLED)
                self.battleBtn.config(state=DISABLED)

            # If both Pokemon are alive, this method will disable the current Pokemon and enable the opposing Pokemon so
            # it can make its move as well
            else:
                self.moveEnt1.delete(0, END)
                self.moveEnt1.config(state=DISABLED)
                self.moveBtn1.config(state=DISABLED)
                self.moveEnt2.config(state=NORMAL)
                self.moveBtn2.config(state=NORMAL)

    # Does the same thing as selectMove1() just with respect to the other Pokemon
    def selectMove2(self):
        if self.moveStrVar2.get().lower() in self.cpuPokemon.moveList:
            self.txtStats.config(state=NORMAL)
            self.txtStats.delete(0.0, END)
            self.txtStats.insert(0.0, attack(self.moveStrVar2.get(), self.cpuPokemon, self.userPokemon))
            self.txtStats.config(state=DISABLED)

            # Updating the info for the other Pokemon
            self.moveText1.config(state=NORMAL)
            self.moveText2.config(state=NORMAL)
            self.moveText1.delete(0.0, END)
            self.moveText2.delete(0.0, END)
            self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
            self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
            self.moveText1.config(state=DISABLED)
            self.moveText2.config(state=DISABLED)

            if not self.userPokemon.isAlive():
                self.txtStats.config(state=NORMAL)
                self.txtStats.insert(END, "\n" + self.userPokemon.faint())
                self.txtStats.insert(END, "\nPlay again?")
                self.txtStats.config(state=DISABLED)
                self.moveEnt2.delete(0, END)
                self.restartBtn.config(state=NORMAL)
                self.moveText1.config(state=DISABLED)
                self.moveText2.config(state=DISABLED)
                self.moveEnt2.config(state=DISABLED)
                self.moveBtn2.config(state=DISABLED)
                self.battleBtn.config(state=DISABLED)

            else:
                self.moveEnt2.delete(0, END)
                self.moveEnt2.config(state=DISABLED)
                self.moveBtn2.config(state=DISABLED)
                self.moveEnt1.config(state=NORMAL)
                self.moveBtn1.config(state=NORMAL)

    # Completely clears and resets all text fields, buttons, and images to their original state
    def restart(self):
        # Resetting the Pokemon objects
        self.userPokemon = None
        self.cpuPokemon = None

        # Resetting all the widgets
        self.txtStats.config(state=NORMAL)
        self.moveText1.config(state=NORMAL)
        self.moveText2.config(state=NORMAL)

        self.txtStats.delete(0.0, END)
        self.moveText1.delete(0.0, END)
        self.moveText2.delete(0.0, END)
        self.moveEnt1.delete(0, END)
        self.moveEnt2.delete(0, END)

        self.txtStats.config(state=DISABLED)
        self.moveText1.config(state=DISABLED)
        self.moveText2.config(state=DISABLED)

        # Enabling widgets so the window returns to its original state
        self.entName1.config(state=NORMAL)
        self.entName1.delete(0, END)

        self.entName2.config(state=NORMAL)
        self.entName2.delete(0, END)

        self.checkBtn.config(state=NORMAL)
        self.pokedexBtn.config(state=NORMAL)

        # Disabling the restart button so the user can't constantly restart the game
        self.restartBtn.config(state=DISABLED)

        # Resetting the Sprites
        tempImg = PhotoImage(file="Sprites/white.gif")
        self.sprite1Label.configure(image=tempImg)
        self.sprite1Label.image = tempImg

        self.sprite2Label.configure(image=tempImg)
        self.sprite2Label.image = tempImg





