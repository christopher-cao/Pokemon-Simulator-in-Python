class Move(object):
    MOVES_DICTIONARY = {}
    def __init__(self, move):
        moveInfo = []
        # Only reading through the file if no information is stored in the Moves Dictionary
        if len(Move.MOVES_DICTIONARY) == 0:
            fin = open("Pokemon Moves.csv", 'r')
            for line in fin:
                line = line.strip()
                moveList = line.split(",")
                Move.MOVES_DICTIONARY[moveList[1]] = moveList  # The name of the move is the key while the rest of the
                # list is the value

            fin.close()

        # Finding the matching key in the dictionary, then assigning the list to a variable called moveInfo
        for key in Move.MOVES_DICTIONARY:
            if key.lower() == move.lower():
                moveInfo = Move.MOVES_DICTIONARY[key]


        # ATTRIBUTES
        # ID info
        self.moveInfo = moveInfo
        self.id = moveInfo[0]  # Move's number id
        self.name = moveInfo[1]  # Move's name

        # Description
        self.description = moveInfo[2]  # Move description
        self.type = moveInfo[3]  # Move type
        self.kind = moveInfo[4]  # Can be special, physical, or stat-changing

        # For in-battle calculations
        self.power = int(moveInfo[5])  # Move's base damage
        self.accuracy = moveInfo[6]
        self.pp = int(moveInfo[7])

    # METHODS
    # str method
    def __str__(self):
        msg = self.name + " " + str(self.power)
        return msg


    # GET Methods
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getType(self):
        return self.type

    def getKind(self):
        return self.kind

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getPP(self):
        return self.pp

    # SET Methods
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setPower(self, power):
        self.power = power

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def setPP(self, pp):
        self.pp = pp











