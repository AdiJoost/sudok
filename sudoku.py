class Sudoku:
    NUMBERS = (1,2,3,4,5,6,7,8,9)

    def __init__(self):
        self.sudokuField = self.getEmpty()

    def getAvalible(self, ind):
        numbers = list(self.NUMBERS)
        for i in range (9):
            if(self.sudokuField[ind][i] != -1):
                numbers.remove(self.sudokuField[ind][i])
        return numbers

    def fill(self, nestedList):
        if(len(nestedList) != 9):
            raise ValueError
        for i in range(9):
            if (len(nestedList[i]) != 9):
                raise ValueError
        self.sudokuField = nestedList

    def getEmpty(self):
        myEmpty = []
        for i in range(9):
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