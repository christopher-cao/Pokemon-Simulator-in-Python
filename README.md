Pokemon Battle Simulator

Christopher Cao 
ITP 115 

OVERVIEW
This program is a simple Pokemon battle simulator using the 150 Pokemon from the first generation of Pokemon games. 

Running the Program
Make sure all python files, csv’s, and image files are in the same directory. This includes: Application.py, Attack.py, Kanto Pokemon Spreadsheet.csv, Main.py, Move.py, Poked.py, Pokemon Moves.csv, Pokemon.py, and Type Advantages.csv. 

Run the program by running Main.py. 

HOW THE PROGRAM WORKS
Begin the program by entering Pokemon names into the entry boxes at the top of the window. The user can press the “See All Pokemon” button to print a list of Pokemon to the text box in the middle of the window. 

This button is connected to a function that reads through the “Kanto Pokemon Spreadsheet.csv” file and extracts all the Pokemon names, which are then placed into a list called “pokedex.” It then prints this list to the text box.

After typing in both Pokemon, the user should press “Lock In.” This button checks the Pokemon entries for errors and enables the “Begin Battle” button. If any of the entries are not in the “pokedex”, it will ask the user to re-enter their choices and double-check for any spelling errors.  If both entries are valid, it will enable the “Begin Battle” button and prevent the user from changing their entries. 

Then the user should press the “Begin Battle” button. This button begins the battle and enables the user to input moves for one of the Pokemon. It decides which Pokemon to enable based on the Pokemon’s speed stat (Pokemon.battleSpeed) using an “if” statement. The Pokemon with the higher speed stat will be enabled first. 

After the user presses “Begin Battle,” the game loop begins. For whichever Pokemon has been enabled first, the user should type in a move from the provided move list into the respective entry field and press the “Select Move” button. If the user-selected move is not in the Pokemon’s moveset, nothing will happen when the user presses the button. If the user-selected move is in the Pokemon’s moveset, it will run the user-inputted string through the attack() function. For example, if the user had Charizard use “Fire Punch” on Blastoise, the attack function would read: attack(“Fire Punch”, Charizard, Blastoise). This attack function then returns a string indicating which move was used, how much HP the opposing Pokemon lost, and the move’s effective. It will then enable the move entry and button for the other Pokemon, while disabling the current Pokemon’s move entry field. 

The other “Select Move” button does the same thing as the first, just for the opposite Pokemon. This loop between the two selectMove() methods continues until one of the Pokemon faints, after which it will print “(Pokemon Name) fainted” to the text box. The program uses an if statement along with the isAlive() method for the Pokemon class to check if one of the Pokemon has fainted. If this method returns “True”, it will disable all buttons and entries EXCEPT for the reset button. 

If the user wants to play again, they should press the “Restart” button.  This button completely clears all data from the program. It resets the Pokemon objects and sprites, deletes all text from the window, and only enables the Pokemon entry boxes, the “See All Pokemon”  and “Lock In” buttons, just like at the beginning of the program.

OVERVIEW OF POKEMON BATTLE MECHANICS
Pokemon battles work on a turn-based system. One turn consists of one Pokemon attacking and then the other Pokemon attacking back. There are two different types of moves this program uses: those that deal damage, and those that alter stats. For damage-dealing moves, the damage is calculated using the damage formula: (((2 x Level + 10)/250) x (Attack/Defense) x Move Base Damage + 2) x Modifier). This program calculates all damage as if all Pokemon are level 50. 

The modifier for the damage depends on typing of the move and Pokemon. For example, Fire type moves are “super effective” against Grass type Pokemon. In this situation, the modifier for the damage would be 2 and the original damage would be doubled. Conversely, Grass type moves are “not very effective” against Fire type Pokemon, so the modifier for the damage is 0.5. Moves can also not affect other Pokemon. For example, Ground type moves are not effective against Flying type Pokemon, so the modifier for the damage is 0, making the damage 0. This program accounts for type effectiveness by reading through the “Type Advantages.csv” file. 

There are also stat-changing moves. For example, if a move lowers the opponent’s Attack stat, the damage of the opponent’s moves would decrease. If a move lowers the opponent’s Defense stat, the damage of your Pokemon’s moves would increase. Moves can also increase the user’s stats. Also, moves can increase any of the user Pokemon’s stats, such as attack or defense. In this program, for non-damaging moves, I use a code in the “Pokemon Moves.csv” file to indicate which stat to alter. For example “a+” means raise the user’s attack stage while “a-“ means lower the opponent’s attack stage.

At the beginning of a battle, all of a Pokemon’s stat stages are 0. Depending on different moves used, this stat stage will change, changing this stat for the duration of the battle. For example, if a Pokemon’s attack stage is +1, then the new in-battle attack (Pokemon.battleAttack) is multiplied by 3/2. Conversely, if a Pokemon’s attack stage is -1, then the new in-battle attack is multiple by 2/3. This process continues until the stat stage reaches +/- 6. This program takes these stat stages into account using a function called statMod() in the Attack.py file. 

This program tries to stay as true to the Pokemon games as possible, so all calculations of move damage, base stats, in-battle stats, and etc. are replicated from the actual Pokemon games. For more information about Pokemon battle mechanics, please visit: 
http://bulbapedia.bulbagarden.net/wiki/Damage#Damage_formula
http://bulbapedia.bulbagarden.net/wiki/Stats

Please note that there are several aspects of Pokemon battles that this program does not take into consideration, such as move accuracy, Pokemon nature, and move power points. 
