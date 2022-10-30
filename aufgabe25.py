from sudoku import Sudoku
import time
# Für diese Aufgabe habe ich eine Klasse Sudoku geschrieben.
#Die Klasse hat zwei Class-Methods, wobei getRandom() ein
#zufälliges gelöstes Sudoku ausgibt. (Aufgabe 25a) Um ein Sudoku zu lösen
#wird das Object instanziert. Das Sudoku kann dann als 2d-Liste
#mit dem Befehl .setUnsolved(2d-liste) gesetzt werden.
#Die Methode fillAtempt versucht dann, dass Sudoku zu lösen
#Bei der Klasse kann die Methode fillSafety() aufgerufen werden,
#Um Zahlen, die 100% richtig sein müssen im Sudoku einzutragen.
#--------------------------------------
#Die Klasse verfügt über einen Smart-Solve-Algorythmus, bei dem
#nach jeder eingetragenen Zahl die Safeties gesucht und gefunden werden.
#Die Laufzeit ist jedoch nicht markant besser und je nach Sudoku sogar schlechter.
randoSudoku = Sudoku.getRandom()
print("A random 9x9 Sudoku")
print(randoSudoku.toString())

sudoku = Sudoku()
nestedSudo = [
    [5,3,-1,-1,7,-1,-1,-1,-1],
    [6,-1,-1,1,9,5,-1,-1,-1],
    [-1,9,8,-1,-1,-1,-1,6,-1],
    [8,-1,-1,-1,6,-1,-1,-1,3],
    [4,-1,-1,8,-1,3,-1,-1,1],
    [7,-1,-1,-1,2,-1,-1,-1,6],
    [-1,6,-1,-1,-1,-1,2,8,-1],
    [-1,-1,-1,4,1,9,-1,-1,5],
    [-1,-1,-1,-1,8,-1,-1,7,9]
]
sudoku.setUnsolved(nestedSudo)
sudoku.fillSafety()
sudoku.fillAtempt()
print("The Sudoku from Exercise solved:")
print(sudoku.toString())

sudoku.setUnsolved(nestedSudo)
sudoku.fillSafety()
sudoku.smartAtempt()
print("The Sudoku from Exercise with smart solve:")
print(sudoku.toString())

def smartTime():
    sudok = Sudoku()
    sudok.setUnsolved(nestedSudo)
    start = time.time()
    for i in range(100):
        sudoku.smartAtempt()
        sudoku.restart()
    end = time.time()
    return end - start

def normalTime():
    sudok = Sudoku()
    sudok.setUnsolved(nestedSudo)
    start = time.time()
    for i in range(100):
        sudoku.fillAtempt()
        sudoku.restart()
    end = time.time()
    return end - start


#print(smartTime())
#print(normalTime())