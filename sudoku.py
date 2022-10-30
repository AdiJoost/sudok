import time
import random

class Sudoku:
    #Schauen sie in der Methode fillCell für den
    #Backtrack-Algorythmus.
    #getRandom für den ersten Teil der Aufgabe
    NUMBERS = (1,2,3,4,5,6,7,8,9)

    def __init__(self, size=9):
        #is the Grid size
        self.size = 9
        #is the current state of the Sudoku
        self.sudokuField = self.getEmpty()
        #lowest possible number, /depricated...
        self.loci = self.getEmpty()
        #Unsolved is the unsolved Sudoku
        self.unsolved = self.getEmpty()
        
    
    
    def fillAtempt(self):
        print("Solving the Sudoku...")
        self.fillCell(0,0)

    def fillCell(self, x, y):
        if (self.unsolved[x][y] != -1):
            nexts = self.getNext((x,y), self.size)
            if (nexts[0] == 0 and nexts[1] == 0):
                return True
            return self.fillCell(*nexts)

        options = self.getOptions((x,y))
        random.shuffle(options)
        for option in options:
            self.erraseUp((x,y))
            self.insert(option,(x,y))
            nexts = self.getNext((x,y), self.size)
            if (nexts[0] == 0 and nexts[1] == 0):
                return True
            if self.fillCell(*nexts):
                return True
        return False

    def erraseUp(self, cords):
        for i in range (cords[1], self.size):
            self.sudokuField[cords[0]][i] = -1
        for i in range(cords[0] + 1, self.size):
            for j in range(self.size):
                self.sudokuField[i][j] = -1;
        self.correct()

    def erraseLociRaise(self, cords):
        for i in range (cords[1], self.size):
            self.loci[cords[0]][i] = -1
        for i in range(cords[0] + 1, self.size):
            for j in range(self.size):
                self.loci[i][j] = -1;
        print(self.loci)

    def lociRaise(self, number, cords):
        if self.unsolved[cords[0]][cords[1]] != -1:
            raise ValueError (f"loci does not exist for given cords: {cords}")
        self.loci[cords[0]][cords[1]] = number

    def insert(self, number, cords):
        if self.unsolved[cords[0]][cords[1]] != -1:
            raise ValueError (f"Insert in a set value: {cords}")
        self.sudokuField[cords[0]][cords[1]] = number

    def setUnsolved(self, nestedList):
        if(len(nestedList) != self.size):
            raise ValueError
        for i in range(9):
            if (len(nestedList[i]) != self.size):
                raise ValueError
        self.unsolved = nestedList
        self.restart()
    
    def restart(self):
        self.sudokuField = self.getEmpty()
        self.correct()
    
    def correct(self):
        #This function sets every Cell with a value from Unsolve to
        #the Sudokufield
        for i in range(self.size):
            for j in range(self.size):
                if (self.unsolved[i][j] != -1):
                    self.sudokuField[i][j] = self.unsolved[i][j]

    def fillSafety(self, setOnUnsolved=True):
        #finds all safe numbers and fills them in. Then repeads
        noMoreSafties = False
        safetiesFilled = 0
        while not noMoreSafties:
            safeties = self.findSafties()
            if (len(safeties)) == 0:
                noMoreSafties = True
            for safe in safeties:
                if setOnUnsolved:
                    self.unsolved[safe[0]][safe[1]] = safe[2][0]
                    safetiesFilled += 1
                else:
                    self.sudokuField[safe[0]][safe[1]] = safe[2][0]
                    print(f"inserting unsafe Number {safe}")
            self.correct()
        return safetiesFilled
    
    def findSafties(self):
        safeties = []
        for i in range(self.size):
            for j in range(self.size):
                if(self.unsolved[i][j] == -1):
                    possibleNumbers = self.getSafeNumbers((i,j))
                    if len(possibleNumbers) == 1:
                        safeties.append((i,j,possibleNumbers))
        return safeties

    def getSafeNumbers(self, cords: tuple) -> list:
        #This one is complicated to explain. If it gets a number
        #this number is the number in the field, as it is not 
        #possible to put this number anywhere else in the row
        #and column
        myList = []
        numbers = list(self.NUMBERS)
        for i in range(self.size):
            if i != cords[0]:
                myList.extend(self.getOptions((i, cords[1])))
        for i in range(self.size):
            if i !=cords[1]:
                myList.extend(self.getOptions((cords[0], i)))
        for i in range(cords[0] - (cords[0] %3), cords[0] - (cords[0] %3) + 3):
            for j in range(cords[1] - (cords[1]%3), cords[1] - (cords[1]%3)+3):
                if (cords[0] != i or cords[1] != j):
                    myList.extend(self.getOptions((i,j)))
        myList = list(set(myList))
        for number in myList:
            numbers.remove(number)
        return numbers
        
    def getOptions(self, cords: tuple):
        #gets all options for a given cell
        if (self.sudokuField[cords[0]][cords[1]]) != -1:
            return [self.sudokuField[cords[0]][cords[1]]]
        avalibleRow = self.getAvalibleInRow(cords[0])
        avalibleBlock = self.getAvalibleInBlock(cords)
        avalibleColumn = self.getAvalibleInColumn(cords[1])
        intersect = [value for value in avalibleBlock
                        if value in avalibleColumn and
                        value in avalibleRow]
        return intersect

    def getAvalibleInRow(self, ind):
        #gets all avalible Numbers in a Row
        numbers = list(self.NUMBERS)
        for i in range (self.size):
            if(self.sudokuField[ind][i] != -1):
                numbers.remove(self.sudokuField[ind][i])
        return numbers
    
    def getAvalibleInColumn(self, ind):
        #gets all avalible Numbers in a Row
        numbers = list(self.NUMBERS)
        for i in range (self.size):
            if(self.sudokuField[i][ind] != -1):
                numbers.remove(self.sudokuField[i][ind])
        return numbers
    
    def getAvalibleInBlock(self, block=(0,0)):
        numbers = list(self.NUMBERS)
        k = block[0] - (block[0] % 3)
        n = block[1] - (block[1] % 3)
        for i in range(k, k+3):
            for j in range(n, n+3):
                if(self.sudokuField[i][j] != -1):
                    numbers.remove(self.sudokuField[i][j])
        return numbers

    def fill(self, nestedList):
        if(len(nestedList) != self.size):
            raise ValueError
        for i in range(9):
            if (len(nestedList[i]) != self.size):
                raise ValueError
        self.sudokuField = nestedList

    def getEmpty(self):
        myEmpty = []
        for i in range(self.size):
            myEmpty.append([-1 for _ in range(9)])
        return myEmpty

    def toString(self):
        myString = ""
        counter = 1
        for row in self.sudokuField:
            myString += str(row[:3])
            myString += "|"
            myString += str(row[3:6])
            myString += "|"
            myString += str(row[6:9])
            if(counter % 3 == 0):
                myString +="\n----------------------------------------\n"
            else:
                myString += "\n"
            counter += 1
            
        return myString

    @classmethod
    def getNext(cls, cords, size):
        x = cords[0]
        y = cords[1] + 1 if (cords[1] + 1 < size) else 0
        if y == 0:
            x = x + 1 if (x + 1 < size) else 0
        return (x, y)

    @classmethod
    def getRandom(cls, size=9):
        sudok = Sudoku(size)
        sudok.fillAtempt()
        return sudok