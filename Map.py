import math
import random

class Map:

    def __init__(self, row, column):
                self.row = row
                self.column = column
                path = ""
    def getPath(self, startRow, startCol, destRow, destCol): # getPath method
        if (startRow < 0 or startRow > self.row or startCol < 0 or startCol > self.column or destRow < 0 or destRow > self.row or destCol < 0 or destCol > self.column):
            raise ValueError("IllegalArgumentException")
        elif (startRow >= destRow and startCol >= destCol): # goSouthWest Path START
            path = self.goSouthWest(startRow, startCol, destRow, destCol)
        elif (startRow >= destRow and startCol <= destCol): # goSouthEast Path START
            path = self.goSouthEast(startRow, startCol, destRow, destCol)
        elif (startRow <= destRow and startCol <= destCol):
            path = self.goNorthEast(startRow, startCol, destRow, destCol)
        elif (startRow <= destRow and startCol >= destCol):
            path = self.goNorthWest(startRow, startCol, destRow, destCol)
        return path
    def goSouthWest(self, startRow, startCol, destRow, destCol): # goSouthWest method
        colDiff = startCol - destCol
        rowDiff = startRow - destRow
        if((colDiff > rowDiff) and (startRow != destRow)):
            startRow -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((rowDiff > colDiff) and (startCol != destCol)):
            startCol -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((rowDiff > colDiff) and (startCol == destCol)):
            startRow -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((colDiff > rowDiff) and (startRow == destRow)):
            startCol -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((rowDiff == 0) and (colDiff == 0) and (destRow == 0) and (destCol == 0)):
            startCol += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        else:
            startRow -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "

        if (startCol != destCol or startRow != destRow):
            path = path + self.goSouthWest(startRow, startCol, destRow, destCol)
        return path

    def goSouthEast(self, startRow, startCol, destRow, destCol):
        colDiff = startCol - destCol
        rowDiff = startRow - destRow
        if((colDiff > rowDiff) and (startRow != destRow)):
            startRow -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((rowDiff > colDiff) and (startCol != destCol)):
            startCol -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((rowDiff > colDiff) and (startCol == destCol)):
            startRow -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((colDiff > rowDiff) and (startRow == destRow)):
            startCol -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((rowDiff == 0) and (colDiff == 0) and (destRow == 0) and (destCol == 0)):
            startCol += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        else:
            startRow -= 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "

        if (startCol == destCol and startRow == destRow):
            return path
        else:
            path = path + self.goSouthEast(startRow, startCol, destRow, destCol)

    def goNorthWest(self, startRow, startCol, destRow, destCol):
        colDiff = startCol - destCol
        rowDiff = startRow - destRow
        if ((colDiff > rowDiff) and (rowDiff != 0) and (colDiff > math.fabs(rowDiff))):
            startRow += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((colDiff > rowDiff) and (rowDiff == 0)):
            startCol += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif((colDiff == math.fabs(rowDiff)) and (rowDiff != 0 and colDiff != 0)):
            startCol += 1
            path = path + "(" + str(startRow) + "," + str(startCol) + ") "
        else:
            startCol += 1
            path = path + "(" + str(startRow) + "," + str(startCol) + ") "

        if (startCol == destCol and startRow == destRow):
            return path
        else:
            path = path + self.goNorthWest(startRow, startCol, destRow, destCol)

    def goNorthEast(self, startRow, startCol, destRow, destCol):
        colDiff = startCol - destCol
        rowDiff = startRow - destRow

        if (((math.fabs(rowDiff) > math.fabs(colDiff)) and (colDiff != 0)) or ((math.fabs(rowDiff) < math.fabs(colDiff)) and (rowDiff == 0))):
            startCol += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        elif(((math.fabs(rowDiff) > math.fabs(colDiff)) and (colDiff == 0)) or ((math.fabs(rowDiff) < math.fabs(colDiff)) and (rowDiff != 0))):
            startRow += 1
            path = "(" + str(startRow + 1) + "," + str(startCol) + ") "
        elif((colDiff == math.fabs(rowDiff)) and (rowDiff != 0 and colDiff != 0)):
            startCol += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "
        else:
            startCol += 1
            path = "(" + str(startRow) + "," + str(startCol) + ") "

        if (startCol == destCol and startRow == destRow):
            return path
        else:
            path = path + self.goNorthEast(startRow, startCol, destRow, destCol)
    def findPath(self, t, checker):
        if checker == False:
            global path
            path = []
            global s
            s=tuple(map(int,t.split(",")))
            path.append(s)
            self.findPath(s, True)
            y,x = path[len(path)-1]
            while not (x==0 or y==0 or y==self.row or x==self.column):
                self.findPath(path[len(path)-1], True)
                y,x = path[len(path)-1]

            print("Car got out of the city")
            return path
        else:
            j,i =t
            toss = random.randint(1,2)
            if toss == 1:
                t = (random.randint(j - 1, j + 1),i)
            else:
                t = (j,random.randint(i - 1, i + 1))
            if t not in path:
                path.append(t)
            else:
                path.clear()
                print("You were caught!")
                path.append(s)
                self.findPath(s, True)